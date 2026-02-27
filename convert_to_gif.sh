#!/bin/bash
FFMPEG="/c/Users/chohy/anaconda3/envs/math-animations/Library/bin/ffmpeg.exe"
MP4_DIR="/c/Users/chohy/project/math-animations/media/videos"
GIF_DIR="/c/Users/chohy/project/math-animations/media/gifs"

mkdir -p "$GIF_DIR"

find "$MP4_DIR" -name "*.mp4" -not -path "*/partial_movie_files/*" -not -path "*/test/*" | sort | while read mp4; do
  name=$(basename "$mp4" .mp4)
  gif="${GIF_DIR}/${name}.gif"
  palette="${GIF_DIR}/${name}_palette.png"

  echo "Converting: $name ..."

  # Step 1: palettegen (단일 이미지, -update 1 필요)
  "$FFMPEG" -y -i "$mp4" \
    -vf "fps=12,scale=480:-1:flags=lanczos,palettegen" \
    -frames:v 1 -update 1 "$palette" 2>/dev/null

  if [ ! -f "$palette" ]; then
    echo "  ✗ FAILED (palette): $name"
    continue
  fi

  # Step 2: paletteuse (-filter_complex 로 2입력 처리)
  "$FFMPEG" -y -i "$mp4" -i "$palette" \
    -filter_complex "fps=12,scale=480:-1:flags=lanczos[v];[v][1:v]paletteuse" \
    "$gif" 2>/dev/null

  rm -f "$palette"

  if [ -f "$gif" ]; then
    size=$(wc -c < "$gif")
    kb=$((size / 1024))
    echo "  ✓ ${name}.gif  (${kb}KB)"
  else
    echo "  ✗ FAILED (gif): $name"
  fi
done

echo ""
echo "=== 완료 ==="
echo "GIF 파일 수: $(ls "$GIF_DIR"/*.gif 2>/dev/null | wc -l)"
du -sh "$GIF_DIR" 2>/dev/null
