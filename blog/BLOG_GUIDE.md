# 티스토리 블로그 포스트 작성 가이드

## 블로그 정보

| 항목 | 값 |
|------|-----|
| URL | `https://gunbungmath.tistory.com` |
| 카테고리 | 선형대수학 |
| 작성자 | 선형대수 시각화 블로그 |
| 언어 | ko-KR |
| 수학 렌더링 | KaTeX (스킨에 이미 설정됨) |

## 글 번호 매핑

| 글 ID | 포스트 번호 | 제목 |
|--------|-------------|------|
| 1-1 | /33 | 벡터란 무엇인가 — 크기와 방향의 수학 |
| 1-2 | /34 | 벡터의 덧셈과 뺄셈 — 평행사변형 법칙과 Tip-to-Tail |
| 1-3 | /35 | 스칼라 곱 (Scalar Multiplication) — 크기와 방향을 조절하는 연산 |
| 1-4 | /36 | 벡터의 크기와 단위벡터 — 피타고라스 정리와 정규화 |
| 2-1 | /37 | 내적 (Dot Product) — 두 벡터가 얼마나 같은 방향인지 측정하기 |
| 2-2 | /38 | 벡터 사영 (Vector Projection) — 한 벡터를 다른 벡터 위에 투영하기 |
| 2-3 | /39 | 외적 (Cross Product) — 두 벡터로 수직 벡터 만들기 |
| 3-1 | /40 | 행렬이란? — 숫자의 직사각형 배열로 세상을 기술하다 |
| 3-2 | /41 | 행렬 연산 — 덧셈, 스칼라 곱, 그리고 행렬 곱셈 |
| 3-3 | /42 | 역행렬과 행렬식 — 행렬 방정식의 해를 구하는 핵심 도구 |
| 4-1 | /43 | 선형변환이란? — 행렬로 표현하는 공간의 변화 |
| 4-2 | /44 | 2D 선형변환 — 회전, 반사, 전단, 크기 조정 |
| 4-3 | /45 | 3D 선형변환 — x·y·z 축 회전과 동차좌표계 |
| 4-4 | /46 | 변환의 합성 — 행렬 곱과 순서의 중요성 |
| 5-1 | /47 | 부분공간과 생성(Span) — 벡터들이 만드는 공간 |
| 5-2 | /48 | 선형 독립과 기저 — 공간을 기술하는 최소한의 벡터 집합 |
| 5-3 | /49 | 차원(Dimension) — 공간의 자유도를 수로 표현하다 |
| 5-4 | /50 | 영공간과 열공간 — 랭크-영공간 정리와 해의 구조 |
| 6-1 | /51 | 고유값과 고유벡터란? — 정의와 기하학적 의미 |
| 6-2 | /52 | 특성방정식 — 고유값을 구하는 체계적인 방법 |
| 6-3 | /53 | 대각화 (Diagonalization) — A = PDP⁻¹와 행렬의 거듭제곱 |
| 6-4 | /54 | 고유값의 기하학적 의미 — 스펙트럴 정리와 스펙트럴 분해 |
| 7-1 | /55 | 직교 벡터와 직교 행렬 — 정의, 성질, 회전 행렬 |
| 7-2 | /56 | 그람-슈미트 과정 — 정규직교기저 만들기와 QR 분해 |
| 7-3 | /57 | 최소제곱법 (Least Squares) — 정규방정식과 직선 피팅 |
| 8-1 | /58 | 특이값 분해 (SVD) 정의 — A = UΣVᵀ와 특이값의 의미 |
| 8-2 | /59 | SVD의 기하학적 의미 — 회전-스트레치-회전 |
| 8-3 | /60 | SVD의 응용 — 저랭크 근사, 이미지 압축, PCA, 의사역행렬 |

> 새 글 추가 시 번호 이어서 할당

---

## HTML 파일 구조

모든 포스트는 `blog/tistory_X-Y_포스트번호.html` 파일로 저장하며, 아래 순서로 구성한다.

```
1. JSON-LD 구조화 데이터 (<script type="application/ld+json">)
2. 본문 HTML (도입 → 주요 섹션들 → 핵심 포인트 정리 → 다음 글 링크)
```

---

## 1. JSON-LD 구조화 데이터

모든 포스트 상단에 삽입한다. `Article` + `BreadcrumbList` 두 가지를 `@graph`로 묶는다.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "X.Y 제목 — 부제목",
      "description": "150자 내외의 설명 (검색 결과에 노출됨)",
      "datePublished": "2026-MM-DDT00:00:00+09:00",
      "dateModified": "2026-MM-DDT00:00:00+09:00",
      "author": { "@type": "Person", "name": "선형대수 시각화 블로그" },
      "publisher": { "@type": "Organization", "name": "선형대수 시각화 블로그", "url": "https://gunbungmath.tistory.com" },
      "inLanguage": "ko-KR",
      "articleSection": "챕터명 (Chapter N)",
      "keywords": ["키워드1", "키워드2", "키워드3", "선형대수"],
      "timeRequired": "PT8M",
      "image": "https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/X_Y_첫번째씬이름.gif"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "홈", "item": "https://gunbungmath.tistory.com/" },
        { "@type": "ListItem", "position": 2, "name": "선형대수학", "item": "https://gunbungmath.tistory.com/category/선형대수학" },
        { "@type": "ListItem", "position": 3, "name": "X.Y 글 제목", "item": "https://gunbungmath.tistory.com/포스트번호" }
      ]
    }
  ]
}
</script>
```

### JSON-LD 체크리스트

- [ ] `headline`: SEO 키워드 포함, "X.Y 주제 — 부제목" 형식
- [ ] `description`: 150자 내외, 핵심 키워드 포함
- [ ] `datePublished` / `dateModified`: 실제 발행일
- [ ] `articleSection`: 챕터 이름 (예: "벡터 (Chapter 1)")
- [ ] `keywords`: 5~7개, 한글+영문 혼합
- [ ] `timeRequired`: 예상 읽기 시간 (PT8M ~ PT12M)
- [ ] `image`: 첫 번째 GIF의 jsdelivr CDN URL
- [ ] `publisher.url`: `https://gunbungmath.tistory.com` (example.com 아님!)
- [ ] BreadcrumbList의 `item` URL: 실제 포스트 번호

---

## 2. 본문 HTML 구조

### 전체 흐름

```
도입 → hr → 주요 섹션 1 → hr → 주요 섹션 2 → ... → hr → 핵심 포인트 정리 → 다음 글 링크
```

### 도입

- 일상적인 비유로 시작 (GPS, 자전거, 길찾기 등)
- 이전 글 링크 자연스럽게 포함
- 이번 글에서 배울 내용 간략 소개

```html
<!-- ══ 도입 ══ -->
<h2 data-ke-size="size26">도입</h2>
<p data-ke-size="size16">일상적인 비유로 시작하는 도입부...</p>
<p data-ke-size="size16"><a href="https://gunbungmath.tistory.com/이전번호">이전 글</a>에서 배운 내용을 바탕으로...</p>

<hr data-ke-style="style1" />
```

### 주요 섹션

```html
<!-- ══ 섹션 제목 ══ -->
<h2 data-ke-size="size26">섹션 제목</h2>

<h3 data-ke-size="size23">소제목</h3>
<p data-ke-size="size16">본문 텍스트...</p>
```

### 핵심 포인트 정리 (마지막 섹션)

```html
<!-- ══ 핵심 포인트 정리 ══ -->
<h2 data-ke-size="size26">핵심 포인트 정리</h2>
<table data-ke-align="alignLeft">
<thead>
<tr>
<th>개념</th>
<th>설명</th>
</tr>
</thead>
<tbody>
<tr>
<td>개념명</td>
<td>$수식$ 또는 설명</td>
</tr>
</tbody>
</table>
```

### 다음 글 링크 (마지막 줄)

```html
<p data-ke-size="size16">다음 글에서는 <a href="https://gunbungmath.tistory.com/다음번호"><b>다음 주제명</b></a>을 알아본다.</p>
```

---

## 3. HTML 요소 규칙

### 태그 속성

| 요소 | 필수 속성 |
|------|-----------|
| `<h2>` | `data-ke-size="size26"` |
| `<h3>` | `data-ke-size="size23"` |
| `<p>` | `data-ke-size="size16"` |
| `<ul>` | `style="list-style-type: disc;" data-ke-list-type="disc"` |
| `<ol>` | `style="list-style-type: decimal;" data-ke-list-type="decimal"` |
| `<hr>` | `data-ke-style="style1"` |
| `<table>` | `data-ke-align="alignLeft"` |

### 수식

- 인라인: `$...$`
- 디스플레이: `$$...$$` (별도 줄에 작성)
- KaTeX가 스킨에서 자동 렌더링

### 강조

- 핵심 용어 첫 등장: `<b>용어명(영문)</b>`
- 이후 반복: 굵게 안 함

### 이미지

```html
<img src="https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/X_Y_씬이름.gif" alt="한국어 설명" width="480" height="270" style="display:block; margin:1.5rem auto;">
```

- **src**: jsdelivr CDN 경로 (GitHub repo: `rse112/math-animations`)
- **alt**: 한국어로 내용 설명 (SEO용)
- **width/height**: 반드시 `480` x `270` 명시 (CLS 방지)
- **style**: 가운데 정렬

### 내부 링크

- 도입부에 이전 글 링크 (자연스러운 문맥으로)
- 마지막에 다음 글 링크
- URL 형식: `https://gunbungmath.tistory.com/포스트번호`

---

## 4. SEO 체크리스트

### 글 발행 시

- [ ] JSON-LD 구조화 데이터 포함
- [ ] 이미지에 alt, width, height 속성 포함
- [ ] 내부 링크 (이전 글 ↔ 다음 글) 연결
- [ ] 본문 첫 1~2문장에 핵심 키워드 포함 (자동 meta description 역할)
- [ ] 해시태그 10개 내외 설정 (한글 + 영문 혼합)

### 글 발행 후

- [ ] Google Search Console > URL 검사 > 해당 URL 색인 요청
- [ ] 이전 글의 "다음 글" 링크가 새 글을 가리키는지 확인

### SEO 제목 형식

```
[핵심 키워드] 완벽 정리 — [부가 설명]
```

예시:
- "벡터 스칼라 곱 완벽 정리 — 크기 조절부터 선형결합까지"
- "벡터의 크기(Norm)와 단위벡터 완벽 정리 — 정규화까지 한번에"

### 해시태그 구성 (10개 내외)

- 한글 핵심 키워드 5~6개
- 영문 키워드 3~4개
- 항상 포함: `선형대수`

---

## 5. 스킨 설정 (이미 적용됨)

- `<head>`에 Google Search Console 인증 메타태그 삽입 완료
- `<head>`에 KaTeX CDN 스크립트 삽입 완료
- `<s_article_rep>` > `<s_permalink_article_rep>` 내 글 제목: `<h1>` (SEO용)
- 나머지 섹션(`s_page_rep`, `s_notice_rep` 등)은 `<h3>` 유지

---

## 6. articleSection 매핑

| Chapter | articleSection 값 |
|---------|-------------------|
| 1 (1-1 ~ 1-4) | 벡터 (Chapter 1) |
| 2 (2-1 ~ 2-3) | 내적과 외적 (Chapter 2) |
| 3 (3-1 ~ 3-3) | 행렬 (Chapter 3) |
| 4 (4-1 ~ 4-4) | 선형변환 (Chapter 4) |
| 5 (5-1 ~ 5-4) | 벡터 공간 (Chapter 5) |
| 6 (6-1 ~ 6-4) | 고유값과 고유벡터 (Chapter 6) |
| 7 (7-1 ~ 7-3) | 직교성 (Chapter 7) |
| 8 (8-1 ~ 8-3) | 특이값 분해 (Chapter 8) |
