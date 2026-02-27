import json, re, os

BLOG_DIR = os.path.dirname(os.path.abspath(__file__))

# Post mapping: (file_id, post_number, short_title_for_next_link)
POSTS = [
    ("1-1", 33, "벡터란 무엇인가"),
    ("1-2", 34, "벡터의 덧셈과 뺄셈"),
    ("1-3", 35, "스칼라 곱(Scalar Multiplication)"),
    ("1-4", 36, "벡터의 크기와 단위벡터"),
    ("2-1", 37, "내적(Dot Product)"),
    ("2-2", 38, "벡터 사영(Vector Projection)"),
    ("2-3", 39, "외적(Cross Product)"),
    ("3-1", 40, "행렬이란?"),
    ("3-2", 41, "행렬 연산"),
    ("3-3", 42, "역행렬과 행렬식"),
    ("4-1", 43, "선형변환이란?"),
    ("4-2", 44, "2D 선형변환"),
    ("4-3", 45, "3D 선형변환"),
    ("4-4", 46, "변환의 합성"),
    ("5-1", 47, "부분공간과 생성(Span)"),
    ("5-2", 48, "선형 독립과 기저"),
    ("5-3", 49, "차원(Dimension)"),
    ("5-4", 50, "영공간과 열공간"),
    ("6-1", 51, "고유값과 고유벡터란?"),
    ("6-2", 52, "특성방정식"),
    ("6-3", 53, "대각화(Diagonalization)"),
    ("6-4", 54, "고유값의 기하학적 의미"),
    ("7-1", 55, "직교 벡터와 직교 행렬"),
    ("7-2", 56, "그람-슈미트 과정"),
    ("7-3", 57, "최소제곱법(Least Squares)"),
    ("8-1", 58, "특이값 분해(SVD) 정의"),
    ("8-2", 59, "SVD의 기하학적 의미"),
    ("8-3", 60, "SVD의 응용"),
]

BASE_URL = "https://gunbungmath.tistory.com"

# Only process 2-1 (index 4) through 8-3 (index 27)
START_IDX = 4  # 2-1

def get_filename(file_id, post_num):
    return os.path.join(BLOG_DIR, f"tistory_{file_id}_{post_num}.html")

def fix_file(idx):
    file_id, post_num, short_title = POSTS[idx]
    filepath = get_filename(file_id, post_num)

    if not os.path.exists(filepath):
        print(f"  SKIP (not found): {filepath}")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    changes = []

    # === 1. Fix JSON-LD ===
    json_match = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', content, re.DOTALL)
    if json_match:
        try:
            ld = json.loads(json_match.group(1))
            modified_ld = False

            for item in ld.get("@graph", []):
                # Fix Article
                if item.get("@type") == "Article":
                    # Fix publisher URL
                    pub = item.get("publisher", {})
                    if pub.get("url", "").startswith("https://example"):
                        pub["url"] = BASE_URL
                        modified_ld = True
                        changes.append("publisher URL")

                    # Add image field if missing
                    if "image" not in item:
                        # Find first img src in content
                        img_match = re.search(r'<img[^>]+src="(https://cdn\.jsdelivr[^"]+)"', content)
                        if img_match:
                            item["image"] = img_match.group(1)
                            modified_ld = True
                            changes.append("image field")

                    # Fix articleSection naming
                    section = item.get("articleSection", "")
                    if "특이값 분해(SVD)" in section:
                        item["articleSection"] = "특이값 분해 (Chapter 8)"
                        modified_ld = True
                        changes.append("articleSection")

                # Fix BreadcrumbList
                if item.get("@type") == "BreadcrumbList":
                    items_list = item.get("itemListElement", [])
                    needs_fix = False

                    # Check if breadcrumbs need fixing
                    for li in items_list:
                        if "example.com" in li.get("item", ""):
                            needs_fix = True
                            break
                    if len(items_list) != 3:
                        needs_fix = True

                    if needs_fix:
                        # Get headline for breadcrumb name
                        headline = ""
                        for it2 in ld.get("@graph", []):
                            if it2.get("@type") == "Article":
                                headline = it2.get("headline", "")
                                break
                        # Extract short name like "2.1 내적"
                        bc_name = headline.split(" — ")[0] if " — " in headline else headline.split("?")[0] + ("?" if "?" in headline else "")
                        if not bc_name:
                            bc_name = file_id.replace("-", ".")

                        item["itemListElement"] = [
                            {"@type": "ListItem", "position": 1, "name": "홈", "item": f"{BASE_URL}/"},
                            {"@type": "ListItem", "position": 2, "name": "선형대수학", "item": f"{BASE_URL}/category/선형대수학"},
                            {"@type": "ListItem", "position": 3, "name": bc_name, "item": f"{BASE_URL}/{post_num}"}
                        ]
                        modified_ld = True
                        changes.append("breadcrumbs")

            if modified_ld:
                new_json = json.dumps(ld, ensure_ascii=False, indent=2)
                old_script = json_match.group(0)
                new_script = f'<script type="application/ld+json">\n{new_json}\n</script>'
                content = content.replace(old_script, new_script)
        except json.JSONDecodeError as e:
            print(f"  JSON error in {file_id}: {e}")

    # === 2. Add width/height to img tags ===
    def add_img_attrs(m):
        tag = m.group(0)
        if 'width=' not in tag:
            tag = tag.replace('style="display:block', 'width="480" height="270" style="display:block')
            return tag
        return m.group(0)

    new_content = re.sub(r'<img\s[^>]+>', add_img_attrs, content)
    if new_content != content:
        content = new_content
        changes.append("img width/height")

    # === 3. Add internal links ===
    # Previous post link in intro
    if idx > 0:
        prev_id, prev_num, prev_title = POSTS[idx - 1]
        prev_url = f"{BASE_URL}/{prev_num}"
        # Check if previous link already exists
        if f"/{prev_num}" not in content and f"/{prev_num}\"" not in content:
            # Don't force add prev link - some posts reference older posts naturally
            pass

    # Next post link at end
    if idx < len(POSTS) - 1:
        next_id, next_num, next_title = POSTS[idx + 1]
        next_url = f"{BASE_URL}/{next_num}"

        # Find the last <p> that contains "다음 글"
        last_p_pattern = r'(<p data-ke-size="size16">다음 글에서는\s*.*?</p>)\s*$'
        last_p_match = re.search(last_p_pattern, content, re.DOTALL)

        if last_p_match:
            old_last_p = last_p_match.group(1)
            # Check if it already has the correct link
            if f"/{next_num}" not in old_last_p:
                new_last_p = f'<p data-ke-size="size16">다음 글에서는 <a href="{next_url}"><b>{next_title}</b></a>을 알아본다.</p>'
                content = content.replace(old_last_p, new_last_p)
                changes.append("next link")
        else:
            # No "다음 글" paragraph found - check for last </table> or last </p>
            # For 8-3 (last post), no next link needed
            if idx < len(POSTS) - 1:
                # Try to find end of content and add next link
                # Look for the last closing tag before end
                end_match = re.search(r'(</table>|</p>)\s*$', content.strip())
                if end_match:
                    insert_point = content.rstrip()
                    new_last_p = f'\n\n<p data-ke-size="size16">다음 글에서는 <a href="{next_url}"><b>{next_title}</b></a>을 알아본다.</p>'
                    content = insert_point + new_last_p + '\n'
                    changes.append("next link (added)")

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [{file_id}_{post_num}] Fixed: {', '.join(changes)}")
    else:
        print(f"  [{file_id}_{post_num}] No changes needed")

print("=== Fixing blog HTML files (2-1 through 8-3) ===\n")
for i in range(START_IDX, len(POSTS)):
    fix_file(i)

print("\nDone!")
