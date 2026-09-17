# style.css 줄별 해설

원본 파일: [`css/style.css`](../css/style.css)

> 실행 파일을 건드리지 않는 학습용 줄별 해설입니다. 빈 줄도 포함하며, 원본 수정 후 생성 도구를 다시 실행하면 줄 번호가 갱신됩니다.

| 줄 | 코드 | 설명(클릭하면 관련 홈페이지 섹션으로 이동) |
|---:|---|---|
| 1 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 2 | <code>   1. 디자인 토큰</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 3 | <code>   색상·간격·그림자를 변수로 관리해 테마 변경과 유지보수를 단순화합니다.</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 4 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 5 | <code>:root {</code> | [`:root` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 6 | <code>  color-scheme: light;</code> | [`color-scheme` 스타일을 `light` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 7 | <code>  --color-bg: #f5f8f9;</code> | [CSS 변수 `--color-bg`은 페이지 전체의 가장 바깥 배경색입니다. 현재 값은 `#f5f8f9`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 8 | <code>  --color-surface: #ffffff;</code> | [CSS 변수 `--color-surface`은 카드·폼처럼 배경 위에 올라오는 표면색입니다. 현재 값은 `#ffffff`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 9 | <code>  --color-surface-muted: #eaf0f1;</code> | [CSS 변수 `--color-surface-muted`은 About처럼 구역을 은은하게 구분하는 배경색입니다. 현재 값은 `#eaf0f1`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 10 | <code>  --color-text: #10202c;</code> | [CSS 변수 `--color-text`은 일반 제목과 본문에 사용하는 기본 글자색입니다. 현재 값은 `#10202c`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 11 | <code>  --color-text-muted: #5e6f78;</code> | [CSS 변수 `--color-text-muted`은 설명·보조 문구에 사용하는 약한 글자색입니다. 현재 값은 `#5e6f78`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 12 | <code>  --color-line: #cad6da;</code> | [CSS 변수 `--color-line`은 카드와 입력칸 경계선 색상입니다. 현재 값은 `#cad6da`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 13 | <code>  --color-accent: #007f73;</code> | [CSS 변수 `--color-accent`은 버튼·링크·강조선에 사용하는 대표 강조색입니다. 현재 값은 `#007f73`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 14 | <code>  --color-accent-strong: #00665d;</code> | [CSS 변수 `--color-accent-strong`은 강조 요소의 hover 상태에 사용하는 진한 색입니다. 현재 값은 `#00665d`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 15 | <code>  --color-highlight: #d88a00;</code> | [CSS 변수 `--color-highlight`은 비전 프레임과 번호에 사용하는 보조 강조색입니다. 현재 값은 `#d88a00`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 16 | <code>  --color-dark: #0d1b2a;</code> | [CSS 변수 `--color-dark`은 Projects와 Footer의 가장 어두운 배경색입니다. 현재 값은 `#0d1b2a`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 17 | <code>  --color-dark-muted: #13283b;</code> | [CSS 변수 `--color-dark-muted`은 어두운 영역의 카드에 사용하는 한 단계 밝은 배경색입니다. 현재 값은 `#13283b`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 18 | <code>  --color-on-dark: #eef7f7;</code> | [CSS 변수 `--color-on-dark`은 어두운 배경 위에서 읽히는 밝은 글자색입니다. 현재 값은 `#eef7f7`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 19 | <code>  --color-error: #b42318;</code> | [CSS 변수 `--color-error`은 폼 입력 오류와 실패 메시지 색상입니다. 현재 값은 `#b42318`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 20 | <code>  --color-success: #087a55;</code> | [CSS 변수 `--color-success`은 폼 전송 성공 메시지 색상입니다. 현재 값은 `#087a55`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 21 | <code>  --font-sans: &quot;Pretendard&quot;, &quot;Noto Sans KR&quot;, &quot;Segoe UI&quot;, sans-serif;</code> | [CSS 변수 `--font-sans`은 본문과 제목에 사용하는 고딕 계열 글꼴 묶음입니다. 현재 값은 `"Pretendard", "Noto Sans KR", "Segoe UI", sans-serif`입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 22 | <code>  --font-mono: &quot;Cascadia Code&quot;, &quot;Consolas&quot;, monospace;</code> | [CSS 변수 `--font-mono`은 라벨·번호에 사용하는 고정폭 글꼴 묶음입니다. 현재 값은 `"Cascadia Code", "Consolas", monospace`입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 23 | <code>  --space-1: 0.5rem;</code> | [CSS 변수 `--space-1`은 가장 작은 0.5rem 간격 단위입니다. 현재 값은 `0.5rem`입니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 24 | <code>  --space-2: 1rem;</code> | [CSS 변수 `--space-2`은 기본 1rem 간격 단위입니다. 현재 값은 `1rem`입니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 25 | <code>  --space-3: 1.5rem;</code> | [CSS 변수 `--space-3`은 중간 1.5rem 간격 단위입니다. 현재 값은 `1.5rem`입니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 26 | <code>  --space-4: 2rem;</code> | [CSS 변수 `--space-4`은 큰 2rem 간격 단위입니다. 현재 값은 `2rem`입니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 27 | <code>  --space-5: 3rem;</code> | [CSS 변수 `--space-5`은 섹션 내부용 3rem 간격 단위입니다. 현재 값은 `3rem`입니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 28 | <code>  --space-6: 5rem;</code> | [CSS 변수 `--space-6`은 섹션 사이용 5rem 간격 단위입니다. 현재 값은 `5rem`입니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 29 | <code>  --radius-sm: 0.5rem;</code> | [CSS 변수 `--radius-sm`은 버튼 등에 사용하는 작은 모서리 둥글기입니다. 현재 값은 `0.5rem`입니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 30 | <code>  --radius-md: 1rem;</code> | [CSS 변수 `--radius-md`은 카드에 사용하는 중간 모서리 둥글기입니다. 현재 값은 `1rem`입니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 31 | <code>  --radius-lg: 1.5rem;</code> | [CSS 변수 `--radius-lg`은 큰 카드와 폼에 사용하는 큰 모서리 둥글기입니다. 현재 값은 `1.5rem`입니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 32 | <code>  --shadow-card: 0 1.25rem 3rem rgba(13, 27, 42, 0.1);</code> | [CSS 변수 `--shadow-card`은 카드가 배경에서 떠 보이게 하는 공통 그림자입니다. 현재 값은 `0 1.25rem 3rem rgba(13, 27, 42, 0.1)`입니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `rgba()`의 마지막 값은 투명도입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 33 | <code>  --header-height: 4.5rem;</code> | [CSS 변수 `--header-height`은 고정 헤더 높이와 앵커 여백 계산에 쓰는 값입니다. 현재 값은 `4.5rem`입니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 34 | <code>  --transition: 180ms ease;</code> | [CSS 변수 `--transition`은 hover·테마 변화에 사용하는 공통 전환 시간과 속도입니다. 현재 값은 `180ms ease`입니다. `ms`는 1/1000초 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 35 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 36 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 37 | <code>[data-theme=&quot;dark&quot;] {</code> | [`[data-theme="dark"]` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 38 | <code>  color-scheme: dark;</code> | [`color-scheme` 스타일을 `dark` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 39 | <code>  --color-bg: #09131e;</code> | [CSS 변수 `--color-bg`은 페이지 전체의 가장 바깥 배경색입니다. 현재 값은 `#09131e`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 40 | <code>  --color-surface: #102131;</code> | [CSS 변수 `--color-surface`은 카드·폼처럼 배경 위에 올라오는 표면색입니다. 현재 값은 `#102131`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 41 | <code>  --color-surface-muted: #152a3c;</code> | [CSS 변수 `--color-surface-muted`은 About처럼 구역을 은은하게 구분하는 배경색입니다. 현재 값은 `#152a3c`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 42 | <code>  --color-text: #eff8f7;</code> | [CSS 변수 `--color-text`은 일반 제목과 본문에 사용하는 기본 글자색입니다. 현재 값은 `#eff8f7`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 43 | <code>  --color-text-muted: #a9bdc4;</code> | [CSS 변수 `--color-text-muted`은 설명·보조 문구에 사용하는 약한 글자색입니다. 현재 값은 `#a9bdc4`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 44 | <code>  --color-line: #2c4655;</code> | [CSS 변수 `--color-line`은 카드와 입력칸 경계선 색상입니다. 현재 값은 `#2c4655`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 45 | <code>  --color-accent: #47dac5;</code> | [CSS 변수 `--color-accent`은 버튼·링크·강조선에 사용하는 대표 강조색입니다. 현재 값은 `#47dac5`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 46 | <code>  --color-accent-strong: #72ebd9;</code> | [CSS 변수 `--color-accent-strong`은 강조 요소의 hover 상태에 사용하는 진한 색입니다. 현재 값은 `#72ebd9`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 47 | <code>  --color-highlight: #ffc65c;</code> | [CSS 변수 `--color-highlight`은 비전 프레임과 번호에 사용하는 보조 강조색입니다. 현재 값은 `#ffc65c`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 48 | <code>  --color-dark: #050c13;</code> | [CSS 변수 `--color-dark`은 Projects와 Footer의 가장 어두운 배경색입니다. 현재 값은 `#050c13`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 49 | <code>  --color-dark-muted: #0d1c29;</code> | [CSS 변수 `--color-dark-muted`은 어두운 영역의 카드에 사용하는 한 단계 밝은 배경색입니다. 현재 값은 `#0d1c29`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 50 | <code>  --color-on-dark: #eff8f7;</code> | [CSS 변수 `--color-on-dark`은 어두운 배경 위에서 읽히는 밝은 글자색입니다. 현재 값은 `#eff8f7`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 51 | <code>  --color-error: #ff8d85;</code> | [CSS 변수 `--color-error`은 폼 입력 오류와 실패 메시지 색상입니다. 현재 값은 `#ff8d85`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 52 | <code>  --color-success: #6ee7b7;</code> | [CSS 변수 `--color-success`은 폼 전송 성공 메시지 색상입니다. 현재 값은 `#6ee7b7`입니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 53 | <code>  --shadow-card: 0 1.25rem 3rem rgba(0, 0, 0, 0.35);</code> | [CSS 변수 `--shadow-card`은 카드가 배경에서 떠 보이게 하는 공통 그림자입니다. 현재 값은 `0 1.25rem 3rem rgba(0, 0, 0, 0.35)`입니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `rgba()`의 마지막 값은 투명도입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 54 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 55 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 56 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 57 | <code>   2. 기본 스타일과 접근성</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 58 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 59 | <code>*,</code> | [CSS 구역의 목적을 설명하는 주석입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 60 | <code>*::before,</code> | [CSS 구역의 목적을 설명하는 주석입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 61 | <code>*::after {</code> | [CSS 구역의 목적을 설명하는 주석입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 62 | <code>  box-sizing: border-box;</code> | [크기 계산 방식을 `border-box` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 63 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 64 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 65 | <code>html {</code> | [`html` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 66 | <code>  scroll-behavior: smooth;</code> | [스크롤 움직임을 `smooth` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 67 | <code>  scroll-padding-top: calc(var(--header-height) + 1rem);</code> | [앵커 이동 위쪽 여유을 `calc(var(--header-height) + 1rem)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 68 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 69 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 70 | <code>body {</code> | [`body` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 71 | <code>  margin: 0;</code> | [바깥 여백을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 72 | <code>  overflow-x: hidden;</code> | [가로 넘침 처리을 `hidden` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 73 | <code>  background: var(--color-bg);</code> | [배경을 `var(--color-bg)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 74 | <code>  color: var(--color-text);</code> | [글자색을 `var(--color-text)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 75 | <code>  font-family: var(--font-sans);</code> | [글꼴을 `var(--font-sans)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 76 | <code>  font-size: 1rem;</code> | [글자 크기을 `1rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 77 | <code>  line-height: 1.7;</code> | [줄 높이을 `1.7` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 78 | <code>  transition:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 79 | <code>    background-color var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 80 | <code>    color var(--transition);</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 81 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 82 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 83 | <code>body.menu-open {</code> | [`body.menu-open` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 84 | <code>  overflow: hidden;</code> | [넘친 내용 처리을 `hidden` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 85 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 86 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 87 | <code>img {</code> | [`img` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 88 | <code>  display: block;</code> | [레이아웃 방식을 `block` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 89 | <code>  max-width: 100%;</code> | [최대 너비을 `100%` 값으로 설정합니다. `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 90 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 91 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 92 | <code>a {</code> | [`a` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 93 | <code>  color: inherit;</code> | [글자색을 `inherit` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 94 | <code>  text-decoration: none;</code> | [텍스트 장식을 `none` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 95 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 96 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 97 | <code>button,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 98 | <code>input,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 99 | <code>textarea {</code> | [`textarea` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 100 | <code>  font: inherit;</code> | [`font` 스타일을 `inherit` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 101 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 102 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 103 | <code>button,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 104 | <code>a {</code> | [`a` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 105 | <code>  -webkit-tap-highlight-color: transparent;</code> | [`-webkit-tap-highlight-color` 스타일을 `transparent` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 106 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 107 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 108 | <code>:focus-visible {</code> | [`:focus-visible` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 109 | <code>  outline: 0.2rem solid var(--color-highlight);</code> | [외곽선을 `0.2rem solid var(--color-highlight)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 110 | <code>  outline-offset: 0.2rem;</code> | [`outline-offset` 스타일을 `0.2rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 111 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 112 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 113 | <code>.skip-link {</code> | [`.skip-link` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 114 | <code>  position: fixed;</code> | [배치 기준을 `fixed` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 115 | <code>  top: 0.5rem;</code> | [위쪽 위치을 `0.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 116 | <code>  left: 0.5rem;</code> | [왼쪽 위치을 `0.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 117 | <code>  z-index: 1000;</code> | [겹침 순서을 `1000` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 118 | <code>  padding: 0.75rem 1rem;</code> | [안쪽 여백을 `0.75rem 1rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 119 | <code>  transform: translateY(-150%);</code> | [이동·회전·크기 변형을 `translateY(-150%)` 값으로 설정합니다. `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 120 | <code>  border-radius: var(--radius-sm);</code> | [모서리 둥글기을 `var(--radius-sm)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 121 | <code>  background: var(--color-text);</code> | [배경을 `var(--color-text)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 122 | <code>  color: var(--color-bg);</code> | [글자색을 `var(--color-bg)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 123 | <code>  font-weight: 700;</code> | [글자 굵기을 `700` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 124 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 125 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 126 | <code>.skip-link:focus {</code> | [`.skip-link:focus` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 127 | <code>  transform: translateY(0);</code> | [이동·회전·크기 변형을 `translateY(0)` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 128 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 129 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 130 | <code>.container {</code> | [`.container` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 131 | <code>  width: min(100% - 2rem, 72rem);</code> | [너비을 `min(100% - 2rem, 72rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 132 | <code>  margin-inline: auto;</code> | [좌우 바깥 여백을 `auto` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 133 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 134 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 135 | <code>.section {</code> | [`.section` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 136 | <code>  position: relative;</code> | [배치 기준을 `relative` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 137 | <code>  padding-block: var(--space-6);</code> | [위아래 안쪽 여백을 `var(--space-6)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 138 | <code>  scroll-margin-top: var(--header-height);</code> | [`scroll-margin-top` 스타일을 `var(--header-height)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 139 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 140 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 141 | <code>.section-muted {</code> | [`.section-muted` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 142 | <code>  background: var(--color-surface-muted);</code> | [배경을 `var(--color-surface-muted)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 143 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 144 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 145 | <code>.section-dark {</code> | [`.section-dark` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 146 | <code>  background: var(--color-dark);</code> | [배경을 `var(--color-dark)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 147 | <code>  color: var(--color-on-dark);</code> | [글자색을 `var(--color-on-dark)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 148 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 149 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 150 | <code>.section-kicker,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 151 | <code>.eyebrow {</code> | [`.eyebrow` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 152 | <code>  margin: 0 0 var(--space-1);</code> | [바깥 여백을 `0 0 var(--space-1)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 153 | <code>  color: var(--color-accent);</code> | [글자색을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 154 | <code>  font-family: var(--font-mono);</code> | [글꼴을 `var(--font-mono)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 155 | <code>  font-size: 0.875rem;</code> | [글자 크기을 `0.875rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 156 | <code>  font-weight: 700;</code> | [글자 굵기을 `700` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 157 | <code>  letter-spacing: 0.12em;</code> | [글자 간격을 `0.12em` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 158 | <code>  text-transform: uppercase;</code> | [대소문자 표시을 `uppercase` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 159 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 160 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 161 | <code>.section-dark .section-kicker {</code> | [`.section-dark .section-kicker` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 162 | <code>  color: #69e6d4;</code> | [글자색을 `#69e6d4` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 163 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 164 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 165 | <code>h1,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 166 | <code>h2,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 167 | <code>h3,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 168 | <code>p {</code> | [`p` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 169 | <code>  margin-top: 0;</code> | [위 바깥 여백을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 170 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 171 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 172 | <code>h1,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 173 | <code>h2,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 174 | <code>h3 {</code> | [`h3` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 175 | <code>  line-height: 1.2;</code> | [줄 높이을 `1.2` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 176 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 177 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 178 | <code>h1 {</code> | [`h1` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 179 | <code>  margin-bottom: var(--space-3);</code> | [아래 바깥 여백을 `var(--space-3)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 180 | <code>  font-size: clamp(2.75rem, 12vw, 5.75rem);</code> | [글자 크기을 `clamp(2.75rem, 12vw, 5.75rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `vw`는 화면 너비의 1%를 기준으로 합니다 `clamp()`는 최소·선호·최대값 사이에서 반응형 값을 선택합니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 181 | <code>  letter-spacing: -0.055em;</code> | [글자 간격을 `-0.055em` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 182 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 183 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 184 | <code>h1 span {</code> | [`h1 span` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 185 | <code>  color: var(--color-accent);</code> | [글자색을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 186 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 187 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 188 | <code>h2 {</code> | [`h2` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 189 | <code>  margin-bottom: var(--space-2);</code> | [아래 바깥 여백을 `var(--space-2)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 190 | <code>  font-size: clamp(2rem, 7vw, 3.5rem);</code> | [글자 크기을 `clamp(2rem, 7vw, 3.5rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `vw`는 화면 너비의 1%를 기준으로 합니다 `clamp()`는 최소·선호·최대값 사이에서 반응형 값을 선택합니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 191 | <code>  letter-spacing: -0.04em;</code> | [글자 간격을 `-0.04em` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 192 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 193 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 194 | <code>h3 {</code> | [`h3` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 195 | <code>  font-size: 1.35rem;</code> | [글자 크기을 `1.35rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 196 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 197 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 198 | <code>.section-heading {</code> | [`.section-heading` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 199 | <code>  max-width: 44rem;</code> | [최대 너비을 `44rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 200 | <code>  margin-bottom: var(--space-4);</code> | [아래 바깥 여백을 `var(--space-4)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 201 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 202 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 203 | <code>.section-heading &gt; p:last-child,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 204 | <code>.projects-heading p,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 205 | <code>.about-copy p,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 206 | <code>.contact-copy p {</code> | [`.contact-copy p` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 207 | <code>  color: var(--color-text-muted);</code> | [글자색을 `var(--color-text-muted)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 208 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 209 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 210 | <code>.button {</code> | [`.button` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 211 | <code>  display: inline-flex;</code> | [레이아웃 방식을 `inline-flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 212 | <code>  min-height: 3rem;</code> | [최소 높이을 `3rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 213 | <code>  align-items: center;</code> | [교차축의 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 214 | <code>  justify-content: center;</code> | [주축 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 215 | <code>  padding: 0.75rem 1.25rem;</code> | [안쪽 여백을 `0.75rem 1.25rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 216 | <code>  border: 0.1rem solid transparent;</code> | [테두리을 `0.1rem solid transparent` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 217 | <code>  border-radius: 999px;</code> | [모서리 둥글기을 `999px` 값으로 설정합니다. `px`는 CSS 픽셀 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 218 | <code>  cursor: pointer;</code> | [마우스 커서을 `pointer` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 219 | <code>  font-weight: 800;</code> | [글자 굵기을 `800` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 220 | <code>  transition:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 221 | <code>    transform var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 222 | <code>    background-color var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 223 | <code>    border-color var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 224 | <code>    color var(--transition);</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 225 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 226 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 227 | <code>.button:hover {</code> | [`.button:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 228 | <code>  transform: translateY(-0.15rem);</code> | [이동·회전·크기 변형을 `translateY(-0.15rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 229 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 230 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 231 | <code>.button-primary {</code> | [`.button-primary` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 232 | <code>  background: var(--color-accent);</code> | [배경을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 233 | <code>  color: #ffffff;</code> | [글자색을 `#ffffff` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 234 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 235 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 236 | <code>.button-primary:hover {</code> | [`.button-primary:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 237 | <code>  background: var(--color-accent-strong);</code> | [배경을 `var(--color-accent-strong)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 238 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 239 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 240 | <code>.button-secondary {</code> | [`.button-secondary` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 241 | <code>  border-color: var(--color-line);</code> | [`border-color` 스타일을 `var(--color-line)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 242 | <code>  background: transparent;</code> | [배경을 `transparent` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 243 | <code>  color: var(--color-text);</code> | [글자색을 `var(--color-text)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 244 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 245 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 246 | <code>.button-secondary:hover {</code> | [`.button-secondary:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 247 | <code>  border-color: var(--color-accent);</code> | [`border-color` 스타일을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 248 | <code>  color: var(--color-accent);</code> | [글자색을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 249 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 250 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 251 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 252 | <code>   3. 헤더와 내비게이션 — 모바일 우선</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 253 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 254 | <code>.site-header {</code> | [`.site-header` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 255 | <code>  position: fixed;</code> | [배치 기준을 `fixed` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 256 | <code>  top: 0;</code> | [위쪽 위치을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 257 | <code>  right: 0;</code> | [오른쪽 위치을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 258 | <code>  left: 0;</code> | [왼쪽 위치을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 259 | <code>  z-index: 100;</code> | [겹침 순서을 `100` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 260 | <code>  min-height: var(--header-height);</code> | [최소 높이을 `var(--header-height)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 261 | <code>  border-bottom: 0.0625rem solid transparent;</code> | [`border-bottom` 스타일을 `0.0625rem solid transparent` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 262 | <code>  transition:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 263 | <code>    background-color var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 264 | <code>    border-color var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 265 | <code>    box-shadow var(--transition);</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 266 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 267 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 268 | <code>.site-header.scrolled {</code> | [`.site-header.scrolled` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 269 | <code>  border-color: var(--color-line);</code> | [`border-color` 스타일을 `var(--color-line)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 270 | <code>  background: color-mix(in srgb, var(--color-bg) 90%, transparent);</code> | [배경을 `color-mix(in srgb, var(--color-bg) 90%, transparent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `%`는 기준 요소에 대한 비율입니다 `color-mix()`는 두 색상을 지정 비율로 섞습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 271 | <code>  box-shadow: 0 0.5rem 1.5rem rgba(13, 27, 42, 0.08);</code> | [그림자을 `0 0.5rem 1.5rem rgba(13, 27, 42, 0.08)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `rgba()`의 마지막 값은 투명도입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 272 | <code>  backdrop-filter: blur(0.75rem);</code> | [`backdrop-filter` 스타일을 `blur(0.75rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 273 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 274 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 275 | <code>.nav {</code> | [`.nav` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 276 | <code>  min-height: var(--header-height);</code> | [최소 높이을 `var(--header-height)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 277 | <code>  display: flex;</code> | [레이아웃 방식을 `flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 278 | <code>  align-items: center;</code> | [교차축의 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 279 | <code>  justify-content: space-between;</code> | [주축 정렬을 `space-between` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 280 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 281 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 282 | <code>.logo {</code> | [`.logo` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 283 | <code>  display: inline-flex;</code> | [레이아웃 방식을 `inline-flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 284 | <code>  align-items: center;</code> | [교차축의 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 285 | <code>  gap: 0.65rem;</code> | [항목 사이 간격을 `0.65rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 286 | <code>  font-weight: 900;</code> | [글자 굵기을 `900` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 287 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 288 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 289 | <code>.logo-mark {</code> | [`.logo-mark` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 290 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 291 | <code>  width: 2.35rem;</code> | [너비을 `2.35rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 292 | <code>  aspect-ratio: 1;</code> | [`aspect-ratio` 스타일을 `1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 293 | <code>  place-items: center;</code> | [Grid 양방향 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 294 | <code>  border: 0.125rem solid var(--color-accent);</code> | [테두리을 `0.125rem solid var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 295 | <code>  color: var(--color-accent);</code> | [글자색을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 296 | <code>  font-family: var(--font-mono);</code> | [글꼴을 `var(--font-mono)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 297 | <code>  font-size: 0.75rem;</code> | [글자 크기을 `0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 298 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 299 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 300 | <code>.nav-actions {</code> | [`.nav-actions` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 301 | <code>  display: flex;</code> | [레이아웃 방식을 `flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 302 | <code>  align-items: center;</code> | [교차축의 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 303 | <code>  gap: 0.5rem;</code> | [항목 사이 간격을 `0.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 304 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 305 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 306 | <code>.theme-toggle,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 307 | <code>.menu-toggle {</code> | [`.menu-toggle` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 308 | <code>  min-height: 2.75rem;</code> | [최소 높이을 `2.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 309 | <code>  border: 0.0625rem solid var(--color-line);</code> | [테두리을 `0.0625rem solid var(--color-line)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 310 | <code>  border-radius: 999px;</code> | [모서리 둥글기을 `999px` 값으로 설정합니다. `px`는 CSS 픽셀 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 311 | <code>  background: var(--color-surface);</code> | [배경을 `var(--color-surface)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 312 | <code>  color: var(--color-text);</code> | [글자색을 `var(--color-text)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 313 | <code>  cursor: pointer;</code> | [마우스 커서을 `pointer` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 314 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 315 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 316 | <code>.theme-toggle {</code> | [`.theme-toggle` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 317 | <code>  display: inline-flex;</code> | [레이아웃 방식을 `inline-flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 318 | <code>  align-items: center;</code> | [교차축의 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 319 | <code>  gap: 0.45rem;</code> | [항목 사이 간격을 `0.45rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 320 | <code>  padding-inline: 0.85rem;</code> | [좌우 안쪽 여백을 `0.85rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 321 | <code>  font-size: 0.875rem;</code> | [글자 크기을 `0.875rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 322 | <code>  font-weight: 700;</code> | [글자 굵기을 `700` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 323 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 324 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 325 | <code>.theme-label {</code> | [`.theme-label` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 326 | <code>  display: none;</code> | [레이아웃 방식을 `none` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 327 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 328 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 329 | <code>.menu-toggle {</code> | [`.menu-toggle` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 330 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 331 | <code>  width: 2.75rem;</code> | [너비을 `2.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 332 | <code>  place-content: center;</code> | [`place-content` 스타일을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 333 | <code>  gap: 0.28rem;</code> | [항목 사이 간격을 `0.28rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 334 | <code>  padding: 0;</code> | [안쪽 여백을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 335 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 336 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 337 | <code>.menu-toggle span {</code> | [`.menu-toggle span` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 338 | <code>  width: 1.15rem;</code> | [너비을 `1.15rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 339 | <code>  height: 0.125rem;</code> | [높이을 `0.125rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 340 | <code>  background: currentColor;</code> | [배경을 `currentColor` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 341 | <code>  transition:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 342 | <code>    transform var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 343 | <code>    opacity var(--transition);</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 344 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 345 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 346 | <code>.menu-toggle.active span:nth-child(1) {</code> | [`.menu-toggle.active span:nth-child(1)` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 347 | <code>  transform: translateY(0.405rem) rotate(45deg);</code> | [이동·회전·크기 변형을 `translateY(0.405rem) rotate(45deg)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 348 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 349 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 350 | <code>.menu-toggle.active span:nth-child(2) {</code> | [`.menu-toggle.active span:nth-child(2)` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 351 | <code>  opacity: 0;</code> | [투명도을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 352 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 353 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 354 | <code>.menu-toggle.active span:nth-child(3) {</code> | [`.menu-toggle.active span:nth-child(3)` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 355 | <code>  transform: translateY(-0.405rem) rotate(-45deg);</code> | [이동·회전·크기 변형을 `translateY(-0.405rem) rotate(-45deg)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 356 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 357 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 358 | <code>.nav-menu {</code> | [`.nav-menu` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 359 | <code>  position: fixed;</code> | [배치 기준을 `fixed` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 360 | <code>  inset: var(--header-height) 0 auto;</code> | [네 방향 위치을 `var(--header-height) 0 auto` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 361 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 362 | <code>  max-height: 0;</code> | [`max-height` 스타일을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 363 | <code>  margin: 0;</code> | [바깥 여백을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 364 | <code>  overflow: hidden;</code> | [넘친 내용 처리을 `hidden` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 365 | <code>  padding: 0 1rem;</code> | [안쪽 여백을 `0 1rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 366 | <code>  background: var(--color-surface);</code> | [배경을 `var(--color-surface)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 367 | <code>  box-shadow: var(--shadow-card);</code> | [그림자을 `var(--shadow-card)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 368 | <code>  list-style: none;</code> | [목록 기호을 `none` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 369 | <code>  opacity: 0;</code> | [투명도을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 370 | <code>  transition:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 371 | <code>    max-height 250ms ease,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 372 | <code>    padding 250ms ease,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 373 | <code>    opacity var(--transition);</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 374 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 375 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 376 | <code>.nav-menu.active {</code> | [`.nav-menu.active` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 377 | <code>  max-height: 24rem;</code> | [`max-height` 스타일을 `24rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 378 | <code>  padding-block: 1rem;</code> | [위아래 안쪽 여백을 `1rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 379 | <code>  opacity: 1;</code> | [투명도을 `1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 380 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 381 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 382 | <code>.nav-menu a {</code> | [`.nav-menu a` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 383 | <code>  display: block;</code> | [레이아웃 방식을 `block` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 384 | <code>  padding: 0.85rem 0.75rem;</code> | [안쪽 여백을 `0.85rem 0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 385 | <code>  border-bottom: 0.0625rem solid var(--color-line);</code> | [`border-bottom` 스타일을 `0.0625rem solid var(--color-line)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 386 | <code>  font-weight: 750;</code> | [글자 굵기을 `750` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 387 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 388 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 389 | <code>.nav-menu a:hover {</code> | [`.nav-menu a:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 390 | <code>  color: var(--color-accent);</code> | [글자색을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 391 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 392 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 393 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 394 | <code>   4. Hero와 컴퓨터 비전 모티프</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 395 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 396 | <code>.hero {</code> | [`.hero` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 397 | <code>  min-height: 100svh;</code> | [최소 높이을 `100svh` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 398 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 399 | <code>  align-items: center;</code> | [교차축의 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 400 | <code>  padding-top: calc(var(--header-height) + var(--space-5));</code> | [`padding-top` 스타일을 `calc(var(--header-height) + var(--space-5))` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 401 | <code>  background-image:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 402 | <code>    linear-gradient(var(--color-line) 0.0625rem, transparent 0.0625rem),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 403 | <code>    linear-gradient(90deg, var(--color-line) 0.0625rem, transparent 0.0625rem);</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 404 | <code>  background-size: 2.5rem 2.5rem;</code> | [`background-size` 스타일을 `2.5rem 2.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 405 | <code>  background-position: center;</code> | [`background-position` 스타일을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 406 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 407 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 408 | <code>.hero::before {</code> | [`.hero::before` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 409 | <code>  position: absolute;</code> | [배치 기준을 `absolute` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 410 | <code>  inset: 0;</code> | [네 방향 위치을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 411 | <code>  background: linear-gradient(100deg, var(--color-bg) 20%, transparent 75%);</code> | [배경을 `linear-gradient(100deg, var(--color-bg) 20%, transparent 75%)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 412 | <code>  content: &quot;&quot;;</code> | [가상 요소 내용을 `""` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 413 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 414 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 415 | <code>.hero-grid {</code> | [`.hero-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 416 | <code>  position: relative;</code> | [배치 기준을 `relative` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 417 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 418 | <code>  gap: var(--space-5);</code> | [항목 사이 간격을 `var(--space-5)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 419 | <code>  align-items: center;</code> | [교차축의 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 420 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 421 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 422 | <code>.hero-description {</code> | [`.hero-description` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 423 | <code>  max-width: 37rem;</code> | [최대 너비을 `37rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 424 | <code>  margin-bottom: var(--space-4);</code> | [아래 바깥 여백을 `var(--space-4)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 425 | <code>  color: var(--color-text-muted);</code> | [글자색을 `var(--color-text-muted)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 426 | <code>  font-size: clamp(1.05rem, 3vw, 1.25rem);</code> | [글자 크기을 `clamp(1.05rem, 3vw, 1.25rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `vw`는 화면 너비의 1%를 기준으로 합니다 `clamp()`는 최소·선호·최대값 사이에서 반응형 값을 선택합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 427 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 428 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 429 | <code>.hero-cta {</code> | [`.hero-cta` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 430 | <code>  display: flex;</code> | [레이아웃 방식을 `flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 431 | <code>  flex-wrap: wrap;</code> | [Flex 줄바꿈을 `wrap` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 432 | <code>  gap: 0.75rem;</code> | [항목 사이 간격을 `0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 433 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 434 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 435 | <code>.vision-panel {</code> | [`.vision-panel` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 436 | <code>  width: min(100%, 26rem);</code> | [너비을 `min(100%, 26rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 437 | <code>  justify-self: center;</code> | [개별 항목 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 438 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 439 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 440 | <code>.vision-frame {</code> | [`.vision-frame` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 441 | <code>  position: relative;</code> | [배치 기준을 `relative` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 442 | <code>  aspect-ratio: 1;</code> | [`aspect-ratio` 스타일을 `1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 443 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 444 | <code>  place-items: center;</code> | [Grid 양방향 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 445 | <code>  border: 0.125rem solid var(--color-accent);</code> | [테두리을 `0.125rem solid var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 446 | <code>  background: color-mix(in srgb, var(--color-surface) 88%, transparent);</code> | [배경을 `color-mix(in srgb, var(--color-surface) 88%, transparent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `%`는 기준 요소에 대한 비율입니다 `color-mix()`는 두 색상을 지정 비율로 섞습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 447 | <code>  box-shadow:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 448 | <code>    1rem 1rem 0 color-mix(in srgb, var(--color-accent) 20%, transparent),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 449 | <code>    var(--shadow-card);</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 450 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 451 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 452 | <code>.vision-frame::before,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 453 | <code>.vision-frame::after {</code> | [`.vision-frame::after` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 454 | <code>  position: absolute;</code> | [배치 기준을 `absolute` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 455 | <code>  width: 25%;</code> | [너비을 `25%` 값으로 설정합니다. `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 456 | <code>  height: 25%;</code> | [높이을 `25%` 값으로 설정합니다. `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 457 | <code>  content: &quot;&quot;;</code> | [가상 요소 내용을 `""` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 458 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 459 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 460 | <code>.vision-frame::before {</code> | [`.vision-frame::before` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 461 | <code>  top: -0.5rem;</code> | [위쪽 위치을 `-0.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 462 | <code>  left: -0.5rem;</code> | [왼쪽 위치을 `-0.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 463 | <code>  border-top: 0.4rem solid var(--color-highlight);</code> | [`border-top` 스타일을 `0.4rem solid var(--color-highlight)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 464 | <code>  border-left: 0.4rem solid var(--color-highlight);</code> | [`border-left` 스타일을 `0.4rem solid var(--color-highlight)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 465 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 466 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 467 | <code>.vision-frame::after {</code> | [`.vision-frame::after` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 468 | <code>  right: -0.5rem;</code> | [오른쪽 위치을 `-0.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 469 | <code>  bottom: -0.5rem;</code> | [아래쪽 위치을 `-0.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 470 | <code>  border-right: 0.4rem solid var(--color-highlight);</code> | [`border-right` 스타일을 `0.4rem solid var(--color-highlight)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 471 | <code>  border-bottom: 0.4rem solid var(--color-highlight);</code> | [`border-bottom` 스타일을 `0.4rem solid var(--color-highlight)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 472 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 473 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 474 | <code>.focus-label {</code> | [`.focus-label` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 475 | <code>  position: absolute;</code> | [배치 기준을 `absolute` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 476 | <code>  top: -2rem;</code> | [위쪽 위치을 `-2rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 477 | <code>  left: -0.125rem;</code> | [왼쪽 위치을 `-0.125rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 478 | <code>  padding: 0.25rem 0.5rem;</code> | [안쪽 여백을 `0.25rem 0.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 479 | <code>  background: var(--color-accent);</code> | [배경을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 480 | <code>  color: #ffffff;</code> | [글자색을 `#ffffff` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 481 | <code>  font-family: var(--font-mono);</code> | [글꼴을 `var(--font-mono)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 482 | <code>  font-size: 0.75rem;</code> | [글자 크기을 `0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 483 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 484 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 485 | <code>.vision-content {</code> | [`.vision-content` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 486 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 487 | <code>  justify-items: center;</code> | [Grid 항목 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 488 | <code>  gap: 0.35rem;</code> | [항목 사이 간격을 `0.35rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 489 | <code>  font-family: var(--font-mono);</code> | [글꼴을 `var(--font-mono)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 490 | <code>  text-align: center;</code> | [텍스트 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 491 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 492 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 493 | <code>.vision-content strong {</code> | [`.vision-content strong` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 494 | <code>  font-size: clamp(3.5rem, 18vw, 6rem);</code> | [글자 크기을 `clamp(3.5rem, 18vw, 6rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `vw`는 화면 너비의 1%를 기준으로 합니다 `clamp()`는 최소·선호·최대값 사이에서 반응형 값을 선택합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 495 | <code>  line-height: 1;</code> | [줄 높이을 `1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 496 | <code>  letter-spacing: -0.1em;</code> | [글자 간격을 `-0.1em` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 497 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 498 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 499 | <code>.vision-content &gt; span:last-child {</code> | [`.vision-content > span:last-child` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 500 | <code>  font-size: 0.75rem;</code> | [글자 크기을 `0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 501 | <code>  letter-spacing: 0.08em;</code> | [글자 간격을 `0.08em` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 502 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 503 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 504 | <code>.vision-index {</code> | [`.vision-index` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 505 | <code>  color: var(--color-highlight);</code> | [글자색을 `var(--color-highlight)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 506 | <code>  font-size: 1rem;</code> | [글자 크기을 `1rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 507 | <code>  font-weight: 800;</code> | [글자 굵기을 `800` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 508 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 509 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 510 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 511 | <code>   5. About와 Skills</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 512 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 513 | <code>.about-grid,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 514 | <code>.contact-grid {</code> | [`.contact-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 515 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 516 | <code>  gap: var(--space-4);</code> | [항목 사이 간격을 `var(--space-4)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 517 | <code>  align-items: center;</code> | [교차축의 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 518 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 519 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 520 | <code>.profile-frame {</code> | [`.profile-frame` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 521 | <code>  position: relative;</code> | [배치 기준을 `relative` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 522 | <code>  max-width: 28rem;</code> | [최대 너비을 `28rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 523 | <code>  padding: 0.75rem;</code> | [안쪽 여백을 `0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 524 | <code>  border: 0.0625rem solid var(--color-line);</code> | [테두리을 `0.0625rem solid var(--color-line)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 525 | <code>  background: var(--color-surface);</code> | [배경을 `var(--color-surface)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 526 | <code>  box-shadow: var(--shadow-card);</code> | [그림자을 `var(--shadow-card)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 527 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 528 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 529 | <code>.profile-frame img {</code> | [`.profile-frame img` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 530 | <code>  width: 100%;</code> | [너비을 `100%` 값으로 설정합니다. `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 531 | <code>  aspect-ratio: 1;</code> | [`aspect-ratio` 스타일을 `1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 532 | <code>  object-fit: cover;</code> | [이미지 채움 방식을 `cover` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 533 | <code>  object-position: center;</code> | [`object-position` 스타일을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 534 | <code>  filter: saturate(0.9) contrast(1.04);</code> | [시각 필터을 `saturate(0.9) contrast(1.04)` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 535 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 536 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 537 | <code>.profile-caption {</code> | [`.profile-caption` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 538 | <code>  display: block;</code> | [레이아웃 방식을 `block` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 539 | <code>  padding-top: 0.65rem;</code> | [`padding-top` 스타일을 `0.65rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 540 | <code>  color: var(--color-text-muted);</code> | [글자색을 `var(--color-text-muted)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 541 | <code>  font-family: var(--font-mono);</code> | [글꼴을 `var(--font-mono)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 542 | <code>  font-size: 0.75rem;</code> | [글자 크기을 `0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 543 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 544 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 545 | <code>.about-facts {</code> | [`.about-facts` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 546 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 547 | <code>  gap: 0.75rem;</code> | [항목 사이 간격을 `0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 548 | <code>  margin: var(--space-4) 0 0;</code> | [바깥 여백을 `var(--space-4) 0 0` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 549 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 550 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 551 | <code>.about-facts div {</code> | [`.about-facts div` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 552 | <code>  padding: 1rem;</code> | [안쪽 여백을 `1rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 553 | <code>  border-left: 0.2rem solid var(--color-accent);</code> | [`border-left` 스타일을 `0.2rem solid var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 554 | <code>  background: var(--color-surface);</code> | [배경을 `var(--color-surface)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 555 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 556 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 557 | <code>.about-facts dt {</code> | [`.about-facts dt` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 558 | <code>  color: var(--color-text-muted);</code> | [글자색을 `var(--color-text-muted)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 559 | <code>  font-size: 0.875rem;</code> | [글자 크기을 `0.875rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 560 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 561 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 562 | <code>.about-facts dd {</code> | [`.about-facts dd` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 563 | <code>  margin: 0.2rem 0 0;</code> | [바깥 여백을 `0.2rem 0 0` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 564 | <code>  font-weight: 800;</code> | [글자 굵기을 `800` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 565 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 566 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 567 | <code>.skills-grid {</code> | [`.skills-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 568 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 569 | <code>  gap: var(--space-2);</code> | [항목 사이 간격을 `var(--space-2)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 570 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 571 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 572 | <code>.skill-card {</code> | [`.skill-card` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 573 | <code>  position: relative;</code> | [배치 기준을 `relative` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 574 | <code>  min-height: 19rem;</code> | [최소 높이을 `19rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 575 | <code>  padding: var(--space-4);</code> | [안쪽 여백을 `var(--space-4)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 576 | <code>  overflow: hidden;</code> | [넘친 내용 처리을 `hidden` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 577 | <code>  border: 0.0625rem solid var(--color-line);</code> | [테두리을 `0.0625rem solid var(--color-line)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 578 | <code>  border-radius: var(--radius-md);</code> | [모서리 둥글기을 `var(--radius-md)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 579 | <code>  background: var(--color-surface);</code> | [배경을 `var(--color-surface)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 580 | <code>  box-shadow: 0 0.75rem 1.5rem rgba(13, 27, 42, 0.05);</code> | [그림자을 `0 0.75rem 1.5rem rgba(13, 27, 42, 0.05)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `rgba()`의 마지막 값은 투명도입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 581 | <code>  transition:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 582 | <code>    transform var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 583 | <code>    box-shadow var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 584 | <code>    border-color var(--transition);</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 585 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 586 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 587 | <code>.skill-card:hover {</code> | [`.skill-card:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 588 | <code>  transform: translateY(-0.4rem);</code> | [이동·회전·크기 변형을 `translateY(-0.4rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 589 | <code>  border-color: var(--color-accent);</code> | [`border-color` 스타일을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 590 | <code>  box-shadow: var(--shadow-card);</code> | [그림자을 `var(--shadow-card)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 591 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 592 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 593 | <code>.card-number {</code> | [`.card-number` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 594 | <code>  color: var(--color-accent);</code> | [글자색을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 595 | <code>  font-family: var(--font-mono);</code> | [글꼴을 `var(--font-mono)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 596 | <code>  font-weight: 800;</code> | [글자 굵기을 `800` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 597 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 598 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 599 | <code>.skill-card h3 {</code> | [`.skill-card h3` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 600 | <code>  margin-block: var(--space-3);</code> | [위아래 바깥 여백을 `var(--space-3)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 601 | <code>  font-size: 1.5rem;</code> | [글자 크기을 `1.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 602 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 603 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 604 | <code>.skill-card p {</code> | [`.skill-card p` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 605 | <code>  margin: var(--space-3) 0 0;</code> | [바깥 여백을 `var(--space-3) 0 0` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 606 | <code>  color: var(--color-text-muted);</code> | [글자색을 `var(--color-text-muted)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 607 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 608 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 609 | <code>.tag-list {</code> | [`.tag-list` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 610 | <code>  display: flex;</code> | [레이아웃 방식을 `flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 611 | <code>  flex-wrap: wrap;</code> | [Flex 줄바꿈을 `wrap` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 612 | <code>  gap: 0.5rem;</code> | [항목 사이 간격을 `0.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 613 | <code>  margin: 0;</code> | [바깥 여백을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 614 | <code>  padding: 0;</code> | [안쪽 여백을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 615 | <code>  list-style: none;</code> | [목록 기호을 `none` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 616 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 617 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 618 | <code>.tag-list li {</code> | [`.tag-list li` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 619 | <code>  padding: 0.4rem 0.7rem;</code> | [안쪽 여백을 `0.4rem 0.7rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 620 | <code>  border-radius: 999px;</code> | [모서리 둥글기을 `999px` 값으로 설정합니다. `px`는 CSS 픽셀 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 621 | <code>  background: var(--color-surface-muted);</code> | [배경을 `var(--color-surface-muted)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 622 | <code>  font-family: var(--font-mono);</code> | [글꼴을 `var(--font-mono)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 623 | <code>  font-size: 0.82rem;</code> | [글자 크기을 `0.82rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 624 | <code>  font-weight: 700;</code> | [글자 굵기을 `700` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 625 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 626 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 627 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 628 | <code>   6. GitHub Projects — Grid와 상태별 UI</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 629 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 630 | <code>.projects-heading {</code> | [`.projects-heading` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 631 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 632 | <code>  gap: var(--space-2);</code> | [항목 사이 간격을 `var(--space-2)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 633 | <code>  margin-bottom: var(--space-4);</code> | [아래 바깥 여백을 `var(--space-4)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 634 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 635 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 636 | <code>.projects-heading p {</code> | [`.projects-heading p` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 637 | <code>  color: #a9bdc4;</code> | [글자색을 `#a9bdc4` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 638 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 639 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 640 | <code>.text-link {</code> | [`.text-link` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 641 | <code>  width: fit-content;</code> | [너비을 `fit-content` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 642 | <code>  color: #69e6d4;</code> | [글자색을 `#69e6d4` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 643 | <code>  font-weight: 800;</code> | [글자 굵기을 `800` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 644 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 645 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 646 | <code>.text-link:hover {</code> | [`.text-link:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 647 | <code>  text-decoration: underline;</code> | [텍스트 장식을 `underline` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 648 | <code>  text-underline-offset: 0.3rem;</code> | [밑줄 거리을 `0.3rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 649 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 650 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 651 | <code>.project-filters {</code> | [`.project-filters` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 652 | <code>  display: flex;</code> | [레이아웃 방식을 `flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 653 | <code>  flex-wrap: wrap;</code> | [Flex 줄바꿈을 `wrap` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 654 | <code>  gap: 0.5rem;</code> | [항목 사이 간격을 `0.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 655 | <code>  margin-bottom: var(--space-3);</code> | [아래 바깥 여백을 `var(--space-3)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 656 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 657 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 658 | <code>.project-filters[hidden] {</code> | [`.project-filters[hidden]` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 659 | <code>  display: none;</code> | [레이아웃 방식을 `none` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 660 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 661 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 662 | <code>.filter-button {</code> | [`.filter-button` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 663 | <code>  padding: 0.5rem 0.9rem;</code> | [안쪽 여백을 `0.5rem 0.9rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 664 | <code>  border: 0.0625rem solid #385064;</code> | [테두리을 `0.0625rem solid #385064` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 665 | <code>  border-radius: 999px;</code> | [모서리 둥글기을 `999px` 값으로 설정합니다. `px`는 CSS 픽셀 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 666 | <code>  background: transparent;</code> | [배경을 `transparent` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 667 | <code>  color: #c8d8dd;</code> | [글자색을 `#c8d8dd` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 668 | <code>  cursor: pointer;</code> | [마우스 커서을 `pointer` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 669 | <code>  font-size: 0.875rem;</code> | [글자 크기을 `0.875rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 670 | <code>  font-weight: 750;</code> | [글자 굵기을 `750` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 671 | <code>  transition:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 672 | <code>    background-color var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 673 | <code>    color var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 674 | <code>    border-color var(--transition);</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 675 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 676 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 677 | <code>.filter-button:hover,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 678 | <code>.filter-button.active {</code> | [`.filter-button.active` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 679 | <code>  border-color: #69e6d4;</code> | [`border-color` 스타일을 `#69e6d4` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 680 | <code>  background: #69e6d4;</code> | [배경을 `#69e6d4` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 681 | <code>  color: #08131d;</code> | [글자색을 `#08131d` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 682 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 683 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 684 | <code>.projects-grid {</code> | [`.projects-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 685 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 686 | <code>  grid-template-columns: minmax(0, 1fr);</code> | [Grid 열 구성을 `minmax(0, 1fr)` 값으로 설정합니다. `fr`은 Grid의 남은 공간 비율입니다 `minmax()`는 Grid 크기의 최소값과 최대값을 정합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 687 | <code>  gap: var(--space-2);</code> | [항목 사이 간격을 `var(--space-2)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 688 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 689 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 690 | <code>.project-card {</code> | [`.project-card` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 691 | <code>  display: flex;</code> | [레이아웃 방식을 `flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 692 | <code>  min-height: 18rem;</code> | [최소 높이을 `18rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 693 | <code>  flex-direction: column;</code> | [Flex 진행 방향을 `column` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 694 | <code>  padding: var(--space-3);</code> | [안쪽 여백을 `var(--space-3)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 695 | <code>  border: 0.0625rem solid #2b4254;</code> | [테두리을 `0.0625rem solid #2b4254` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 696 | <code>  border-radius: var(--radius-md);</code> | [모서리 둥글기을 `var(--radius-md)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 697 | <code>  background: var(--color-dark-muted);</code> | [배경을 `var(--color-dark-muted)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 698 | <code>  box-shadow: 0 1rem 2rem rgba(0, 0, 0, 0.15);</code> | [그림자을 `0 1rem 2rem rgba(0, 0, 0, 0.15)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `rgba()`의 마지막 값은 투명도입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 699 | <code>  transition:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 700 | <code>    transform var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 701 | <code>    border-color var(--transition);</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 702 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 703 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 704 | <code>.project-card:hover {</code> | [`.project-card:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 705 | <code>  transform: translateY(-0.35rem);</code> | [이동·회전·크기 변형을 `translateY(-0.35rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 706 | <code>  border-color: #69e6d4;</code> | [`border-color` 스타일을 `#69e6d4` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 707 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 708 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 709 | <code>.project-card-header {</code> | [`.project-card-header` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 710 | <code>  display: flex;</code> | [레이아웃 방식을 `flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 711 | <code>  align-items: start;</code> | [교차축의 정렬을 `start` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 712 | <code>  justify-content: space-between;</code> | [주축 정렬을 `space-between` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 713 | <code>  gap: 1rem;</code> | [항목 사이 간격을 `1rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 714 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 715 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 716 | <code>.project-card h3 {</code> | [`.project-card h3` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 717 | <code>  overflow-wrap: anywhere;</code> | [`overflow-wrap` 스타일을 `anywhere` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 718 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 719 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 720 | <code>.repo-link {</code> | [`.repo-link` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 721 | <code>  color: #69e6d4;</code> | [글자색을 `#69e6d4` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 722 | <code>  font-family: var(--font-mono);</code> | [글꼴을 `var(--font-mono)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 723 | <code>  font-size: 1.1rem;</code> | [글자 크기을 `1.1rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 724 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 725 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 726 | <code>.repo-link:hover {</code> | [`.repo-link:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 727 | <code>  text-decoration: underline;</code> | [텍스트 장식을 `underline` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 728 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 729 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 730 | <code>.project-description {</code> | [`.project-description` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 731 | <code>  flex: 1;</code> | [Flex 항목 크기을 `1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 732 | <code>  color: #b8c9cf;</code> | [글자색을 `#b8c9cf` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 733 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 734 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 735 | <code>.project-meta {</code> | [`.project-meta` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 736 | <code>  display: flex;</code> | [레이아웃 방식을 `flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 737 | <code>  flex-wrap: wrap;</code> | [Flex 줄바꿈을 `wrap` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 738 | <code>  gap: 0.75rem;</code> | [항목 사이 간격을 `0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 739 | <code>  margin: var(--space-3) 0 0;</code> | [바깥 여백을 `var(--space-3) 0 0` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 740 | <code>  padding: var(--space-2) 0 0;</code> | [안쪽 여백을 `var(--space-2) 0 0` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 741 | <code>  border-top: 0.0625rem solid #2b4254;</code> | [`border-top` 스타일을 `0.0625rem solid #2b4254` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 742 | <code>  color: #a9bdc4;</code> | [글자색을 `#a9bdc4` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 743 | <code>  font-size: 0.82rem;</code> | [글자 크기을 `0.82rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 744 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 745 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 746 | <code>.language-dot {</code> | [`.language-dot` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 747 | <code>  display: inline-block;</code> | [레이아웃 방식을 `inline-block` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 748 | <code>  width: 0.65rem;</code> | [너비을 `0.65rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 749 | <code>  aspect-ratio: 1;</code> | [`aspect-ratio` 스타일을 `1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 750 | <code>  margin-right: 0.35rem;</code> | [`margin-right` 스타일을 `0.35rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 751 | <code>  border-radius: 50%;</code> | [모서리 둥글기을 `50%` 값으로 설정합니다. `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 752 | <code>  background: #69e6d4;</code> | [배경을 `#69e6d4` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 753 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 754 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 755 | <code>.project-state,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 756 | <code>.noscript-message {</code> | [`.noscript-message` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 757 | <code>  grid-column: 1 / -1;</code> | [Grid 열 범위을 `1 / -1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 758 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 759 | <code>  min-height: 16rem;</code> | [최소 높이을 `16rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 760 | <code>  place-items: center;</code> | [Grid 양방향 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 761 | <code>  align-content: center;</code> | [`align-content` 스타일을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 762 | <code>  gap: 0.75rem;</code> | [항목 사이 간격을 `0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 763 | <code>  padding: var(--space-4);</code> | [안쪽 여백을 `var(--space-4)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 764 | <code>  border: 0.0625rem dashed #385064;</code> | [테두리을 `0.0625rem dashed #385064` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 765 | <code>  border-radius: var(--radius-md);</code> | [모서리 둥글기을 `var(--radius-md)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 766 | <code>  color: #c8d8dd;</code> | [글자색을 `#c8d8dd` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 767 | <code>  text-align: center;</code> | [텍스트 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 768 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 769 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 770 | <code>.project-state p {</code> | [`.project-state p` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 771 | <code>  margin: 0;</code> | [바깥 여백을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 772 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 773 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 774 | <code>.spinner {</code> | [`.spinner` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 775 | <code>  width: 2.4rem;</code> | [너비을 `2.4rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 776 | <code>  aspect-ratio: 1;</code> | [`aspect-ratio` 스타일을 `1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 777 | <code>  border: 0.2rem solid #385064;</code> | [테두리을 `0.2rem solid #385064` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 778 | <code>  border-top-color: #69e6d4;</code> | [`border-top-color` 스타일을 `#69e6d4` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 779 | <code>  border-radius: 50%;</code> | [모서리 둥글기을 `50%` 값으로 설정합니다. `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 780 | <code>  animation: spin 700ms linear infinite;</code> | [`animation` 스타일을 `spin 700ms linear infinite` 값으로 설정합니다. `ms`는 1/1000초 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 781 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 782 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 783 | <code>@keyframes spin {</code> | [`@keyframes spin` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 784 | <code>  to {</code> | [`to` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 785 | <code>    transform: rotate(360deg);</code> | [이동·회전·크기 변형을 `rotate(360deg)` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 786 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 787 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 788 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 789 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 790 | <code>   7. Contact Form</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 791 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 792 | <code>.contact-copy {</code> | [`.contact-copy` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 793 | <code>  align-self: start;</code> | [`align-self` 스타일을 `start` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 794 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 795 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 796 | <code>.contact-email {</code> | [`.contact-email` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 797 | <code>  display: inline-block;</code> | [레이아웃 방식을 `inline-block` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 798 | <code>  margin-top: var(--space-2);</code> | [위 바깥 여백을 `var(--space-2)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 799 | <code>  color: var(--color-accent);</code> | [글자색을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 800 | <code>  font-family: var(--font-mono);</code> | [글꼴을 `var(--font-mono)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 801 | <code>  font-weight: 800;</code> | [글자 굵기을 `800` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 802 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 803 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 804 | <code>.contact-email:hover {</code> | [`.contact-email:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 805 | <code>  text-decoration: underline;</code> | [텍스트 장식을 `underline` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 806 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 807 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 808 | <code>.contact-form {</code> | [`.contact-form` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 809 | <code>  position: relative;</code> | [배치 기준을 `relative` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 810 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 811 | <code>  gap: var(--space-2);</code> | [항목 사이 간격을 `var(--space-2)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 812 | <code>  padding: var(--space-3);</code> | [안쪽 여백을 `var(--space-3)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 813 | <code>  border: 0.0625rem solid var(--color-line);</code> | [테두리을 `0.0625rem solid var(--color-line)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 814 | <code>  border-radius: var(--radius-lg);</code> | [모서리 둥글기을 `var(--radius-lg)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 815 | <code>  background: var(--color-surface);</code> | [배경을 `var(--color-surface)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 816 | <code>  box-shadow: var(--shadow-card);</code> | [그림자을 `var(--shadow-card)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 817 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 818 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 819 | <code>/* 사람에게는 보이지 않고 자동 입력 프로그램만 채우게 유도하는 스팸 방지 필드입니다. */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 820 | <code>.honeypot {</code> | [`.honeypot` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 821 | <code>  position: absolute;</code> | [배치 기준을 `absolute` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 822 | <code>  left: -10000px;</code> | [왼쪽 위치을 `-10000px` 값으로 설정합니다. `px`는 CSS 픽셀 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 823 | <code>  width: 1px;</code> | [너비을 `1px` 값으로 설정합니다. `px`는 CSS 픽셀 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 824 | <code>  height: 1px;</code> | [높이을 `1px` 값으로 설정합니다. `px`는 CSS 픽셀 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 825 | <code>  overflow: hidden;</code> | [넘친 내용 처리을 `hidden` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 826 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 827 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 828 | <code>.form-field {</code> | [`.form-field` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 829 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 830 | <code>  gap: 0.4rem;</code> | [항목 사이 간격을 `0.4rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 831 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 832 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 833 | <code>.form-field label {</code> | [`.form-field label` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 834 | <code>  font-weight: 800;</code> | [글자 굵기을 `800` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 835 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 836 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 837 | <code>.form-field input,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 838 | <code>.form-field textarea {</code> | [`.form-field textarea` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 839 | <code>  width: 100%;</code> | [너비을 `100%` 값으로 설정합니다. `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 840 | <code>  border: 0.1rem solid var(--color-line);</code> | [테두리을 `0.1rem solid var(--color-line)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 841 | <code>  border-radius: var(--radius-sm);</code> | [모서리 둥글기을 `var(--radius-sm)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 842 | <code>  background: var(--color-bg);</code> | [배경을 `var(--color-bg)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 843 | <code>  color: var(--color-text);</code> | [글자색을 `var(--color-text)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 844 | <code>  padding: 0.8rem 0.9rem;</code> | [안쪽 여백을 `0.8rem 0.9rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 845 | <code>  transition:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 846 | <code>    border-color var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 847 | <code>    box-shadow var(--transition);</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 848 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 849 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 850 | <code>.form-field input:focus,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 851 | <code>.form-field textarea:focus {</code> | [`.form-field textarea:focus` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 852 | <code>  border-color: var(--color-accent);</code> | [`border-color` 스타일을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 853 | <code>  box-shadow: 0 0 0 0.2rem color-mix(in srgb, var(--color-accent) 18%, transparent);</code> | [그림자을 `0 0 0 0.2rem color-mix(in srgb, var(--color-accent) 18%, transparent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `%`는 기준 요소에 대한 비율입니다 `color-mix()`는 두 색상을 지정 비율로 섞습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 854 | <code>  outline: none;</code> | [외곽선을 `none` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 855 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 856 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 857 | <code>.form-field input[aria-invalid=&quot;true&quot;],</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 858 | <code>.form-field textarea[aria-invalid=&quot;true&quot;] {</code> | [`.form-field textarea[aria-invalid="true"]` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 859 | <code>  border-color: var(--color-error);</code> | [`border-color` 스타일을 `var(--color-error)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 860 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 861 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 862 | <code>.field-error {</code> | [`.field-error` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 863 | <code>  min-height: 1.35rem;</code> | [최소 높이을 `1.35rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 864 | <code>  color: var(--color-error);</code> | [글자색을 `var(--color-error)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 865 | <code>  font-size: 0.875rem;</code> | [글자 크기을 `0.875rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 866 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 867 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 868 | <code>.submit-button {</code> | [`.submit-button` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 869 | <code>  width: 100%;</code> | [너비을 `100%` 값으로 설정합니다. `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 870 | <code>  border: 0;</code> | [테두리을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 871 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 872 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 873 | <code>.submit-button:disabled {</code> | [`.submit-button:disabled` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 874 | <code>  cursor: wait;</code> | [마우스 커서을 `wait` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 875 | <code>  opacity: 0.65;</code> | [투명도을 `0.65` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 876 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 877 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 878 | <code>.form-status {</code> | [`.form-status` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 879 | <code>  min-height: 1.5rem;</code> | [최소 높이을 `1.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 880 | <code>  margin: 0;</code> | [바깥 여백을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 881 | <code>  color: var(--color-success);</code> | [글자색을 `var(--color-success)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 882 | <code>  font-weight: 750;</code> | [글자 굵기을 `750` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 883 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 884 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 885 | <code>.form-status[data-status=&quot;error&quot;] {</code> | [`.form-status[data-status="error"]` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 886 | <code>  color: var(--color-error);</code> | [글자색을 `var(--color-error)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 887 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 888 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 889 | <code>.form-status[data-status=&quot;pending&quot;] {</code> | [`.form-status[data-status="pending"]` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 890 | <code>  color: var(--color-highlight);</code> | [글자색을 `var(--color-highlight)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 891 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 892 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 893 | <code>.form-notice {</code> | [`.form-notice` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 894 | <code>  margin: 0;</code> | [바깥 여백을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 895 | <code>  color: var(--color-text-muted);</code> | [글자색을 `var(--color-text-muted)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 896 | <code>  font-size: 0.8rem;</code> | [글자 크기을 `0.8rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 897 | <code>  line-height: 1.6;</code> | [줄 높이을 `1.6` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 898 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 899 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 900 | <code>.form-notice a {</code> | [`.form-notice a` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 901 | <code>  color: var(--color-accent);</code> | [글자색을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 902 | <code>  text-decoration: underline;</code> | [텍스트 장식을 `underline` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 903 | <code>  text-underline-offset: 0.2em;</code> | [밑줄 거리을 `0.2em` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 904 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 905 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 906 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 907 | <code>   8. Footer, 스크롤 탑, 스크롤 애니메이션</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 908 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 909 | <code>.site-footer {</code> | [`.site-footer` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 910 | <code>  padding-block: var(--space-3);</code> | [위아래 안쪽 여백을 `var(--space-3)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 911 | <code>  border-top: 0.0625rem solid var(--color-line);</code> | [`border-top` 스타일을 `0.0625rem solid var(--color-line)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다 `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 912 | <code>  background: var(--color-surface);</code> | [배경을 `var(--color-surface)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 913 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 914 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 915 | <code>.footer-content {</code> | [`.footer-content` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 916 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 917 | <code>  gap: var(--space-2);</code> | [항목 사이 간격을 `var(--space-2)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 918 | <code>  color: var(--color-text-muted);</code> | [글자색을 `var(--color-text-muted)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 919 | <code>  font-size: 0.875rem;</code> | [글자 크기을 `0.875rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 920 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 921 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 922 | <code>.footer-content p {</code> | [`.footer-content p` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 923 | <code>  margin: 0;</code> | [바깥 여백을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 924 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 925 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 926 | <code>.footer-links {</code> | [`.footer-links` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 927 | <code>  display: flex;</code> | [레이아웃 방식을 `flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 928 | <code>  gap: var(--space-2);</code> | [항목 사이 간격을 `var(--space-2)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 929 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 930 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 931 | <code>.footer-links a:hover {</code> | [`.footer-links a:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 932 | <code>  color: var(--color-accent);</code> | [글자색을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 933 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 934 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 935 | <code>.scroll-top {</code> | [`.scroll-top` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 936 | <code>  position: fixed;</code> | [배치 기준을 `fixed` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 937 | <code>  right: 1rem;</code> | [오른쪽 위치을 `1rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 938 | <code>  bottom: 1rem;</code> | [아래쪽 위치을 `1rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 939 | <code>  z-index: 80;</code> | [겹침 순서을 `80` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 940 | <code>  display: grid;</code> | [레이아웃 방식을 `grid` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 941 | <code>  min-width: 3.75rem;</code> | [최소 너비을 `3.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 942 | <code>  min-height: 2.75rem;</code> | [최소 높이을 `2.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 943 | <code>  padding: 0.5rem 0.75rem;</code> | [안쪽 여백을 `0.5rem 0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 944 | <code>  place-items: center;</code> | [Grid 양방향 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 945 | <code>  transform: translateY(1rem);</code> | [이동·회전·크기 변형을 `translateY(1rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 946 | <code>  border: 0;</code> | [테두리을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 947 | <code>  border-radius: 0.5rem;</code> | [모서리 둥글기을 `0.5rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 948 | <code>  background: var(--color-accent);</code> | [배경을 `var(--color-accent)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 949 | <code>  color: #ffffff;</code> | [글자색을 `#ffffff` 값으로 설정합니다. `#` 값은 RGB 색상을 16진수로 표현합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 950 | <code>  font-family: var(--font-mono);</code> | [글꼴을 `var(--font-mono)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 951 | <code>  font-size: 0.75rem;</code> | [글자 크기을 `0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 952 | <code>  font-weight: 800;</code> | [글자 굵기을 `800` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 953 | <code>  letter-spacing: 0.08em;</code> | [글자 간격을 `0.08em` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 954 | <code>  box-shadow: var(--shadow-card);</code> | [그림자을 `var(--shadow-card)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 955 | <code>  cursor: pointer;</code> | [마우스 커서을 `pointer` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 956 | <code>  opacity: 0;</code> | [투명도을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 957 | <code>  pointer-events: none;</code> | [포인터 입력 허용 여부을 `none` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 958 | <code>  transition:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 959 | <code>    opacity var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 960 | <code>    transform var(--transition),</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 961 | <code>    background-color var(--transition);</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 962 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 963 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 964 | <code>.scroll-top.visible {</code> | [`.scroll-top.visible` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 965 | <code>  transform: translateY(0);</code> | [이동·회전·크기 변형을 `translateY(0)` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 966 | <code>  opacity: 1;</code> | [투명도을 `1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 967 | <code>  pointer-events: auto;</code> | [포인터 입력 허용 여부을 `auto` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 968 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 969 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 970 | <code>.scroll-top:hover {</code> | [`.scroll-top:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 971 | <code>  background: var(--color-accent-strong);</code> | [배경을 `var(--color-accent-strong)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 972 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 973 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 974 | <code>.reveal {</code> | [`.reveal` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 975 | <code>  transform: translateY(1.75rem);</code> | [이동·회전·크기 변형을 `translateY(1.75rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 976 | <code>  opacity: 0;</code> | [투명도을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 977 | <code>  transition:</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 978 | <code>    transform 600ms ease,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 979 | <code>    opacity 600ms ease;</code> | [앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 980 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 981 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 982 | <code>.reveal.visible {</code> | [`.reveal.visible` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 983 | <code>  transform: translateY(0);</code> | [이동·회전·크기 변형을 `translateY(0)` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 984 | <code>  opacity: 1;</code> | [투명도을 `1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 985 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 986 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 987 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 988 | <code>   9. 태블릿: 768px 이상</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 989 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 990 | <code>@media (min-width: 48rem) {</code> | [화면 크기 또는 접근성 설정 조건에 따라 적용할 스타일을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 991 | <code>  .theme-label {</code> | [`.theme-label` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 992 | <code>    display: inline;</code> | [레이아웃 방식을 `inline` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 993 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 994 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 995 | <code>  .menu-toggle {</code> | [`.menu-toggle` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 996 | <code>    display: none;</code> | [레이아웃 방식을 `none` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 997 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 998 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 999 | <code>  .nav-actions {</code> | [`.nav-actions` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1000 | <code>    order: 3;</code> | [`order` 스타일을 `3` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1001 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1002 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1003 | <code>  .nav-menu {</code> | [`.nav-menu` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1004 | <code>    position: static;</code> | [배치 기준을 `static` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1005 | <code>    display: flex;</code> | [레이아웃 방식을 `flex` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1006 | <code>    max-height: none;</code> | [`max-height` 스타일을 `none` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1007 | <code>    margin-left: auto;</code> | [`margin-left` 스타일을 `auto` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1008 | <code>    padding: 0;</code> | [안쪽 여백을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1009 | <code>    overflow: visible;</code> | [넘친 내용 처리을 `visible` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1010 | <code>    background: transparent;</code> | [배경을 `transparent` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1011 | <code>    box-shadow: none;</code> | [그림자을 `none` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1012 | <code>    opacity: 1;</code> | [투명도을 `1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1013 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1014 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1015 | <code>  .nav-menu a {</code> | [`.nav-menu a` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1016 | <code>    padding: 0.75rem;</code> | [안쪽 여백을 `0.75rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1017 | <code>    border: 0;</code> | [테두리을 `0` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1018 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1019 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1020 | <code>  .hero-grid {</code> | [`.hero-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1021 | <code>    grid-template-columns: minmax(0, 1.2fr) minmax(18rem, 0.8fr);</code> | [Grid 열 구성을 `minmax(0, 1.2fr) minmax(18rem, 0.8fr)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `fr`은 Grid의 남은 공간 비율입니다 `minmax()`는 Grid 크기의 최소값과 최대값을 정합니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1022 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1023 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1024 | <code>  .about-grid,</code> | [다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 1025 | <code>  .contact-grid {</code> | [`.contact-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1026 | <code>    grid-template-columns: minmax(16rem, 0.8fr) minmax(0, 1.2fr);</code> | [Grid 열 구성을 `minmax(16rem, 0.8fr) minmax(0, 1.2fr)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `fr`은 Grid의 남은 공간 비율입니다 `minmax()`는 Grid 크기의 최소값과 최대값을 정합니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1027 | <code>    gap: var(--space-6);</code> | [항목 사이 간격을 `var(--space-6)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 1028 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 1029 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#about) |
| 1030 | <code>  .skills-grid {</code> | [`.skills-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 1031 | <code>    grid-template-columns: repeat(3, minmax(0, 1fr));</code> | [Grid 열 구성을 `repeat(3, minmax(0, 1fr))` 값으로 설정합니다. `fr`은 Grid의 남은 공간 비율입니다 `minmax()`는 Grid 크기의 최소값과 최대값을 정합니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 1032 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 1033 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 1034 | <code>  .projects-heading {</code> | [`.projects-heading` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 1035 | <code>    grid-template-columns: 1fr auto;</code> | [Grid 열 구성을 `1fr auto` 값으로 설정합니다. `fr`은 Grid의 남은 공간 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 1036 | <code>    align-items: end;</code> | [교차축의 정렬을 `end` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 1037 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 1038 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 1039 | <code>  .projects-grid {</code> | [`.projects-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 1040 | <code>    grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr));</code> | [Grid 열 구성을 `repeat(auto-fit, minmax(17rem, 1fr))` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `fr`은 Grid의 남은 공간 비율입니다 `minmax()`는 Grid 크기의 최소값과 최대값을 정합니다 `auto-fit`은 가능한 만큼 Grid 열을 자동 배치합니다](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 1041 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 1042 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#projects) |
| 1043 | <code>  .footer-content {</code> | [`.footer-content` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1044 | <code>    grid-template-columns: 1fr auto;</code> | [Grid 열 구성을 `1fr auto` 값으로 설정합니다. `fr`은 Grid의 남은 공간 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1045 | <code>    align-items: center;</code> | [교차축의 정렬을 `center` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1046 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1047 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1048 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1049 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1050 | <code>   10. 데스크톱: 1024px 이상</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1051 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1052 | <code>@media (min-width: 64rem) {</code> | [화면 크기 또는 접근성 설정 조건에 따라 적용할 스타일을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1053 | <code>  .container {</code> | [`.container` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1054 | <code>    width: min(100% - 4rem, 72rem);</code> | [너비을 `min(100% - 4rem, 72rem)` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다 `%`는 기준 요소에 대한 비율입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1055 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1056 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1057 | <code>  .section {</code> | [`.section` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1058 | <code>    padding-block: 7rem;</code> | [위아래 안쪽 여백을 `7rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1059 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1060 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1061 | <code>  .hero-grid {</code> | [`.hero-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1062 | <code>    gap: 7rem;</code> | [항목 사이 간격을 `7rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1063 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1064 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1065 | <code>  .contact-form {</code> | [`.contact-form` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1066 | <code>    padding: var(--space-4);</code> | [안쪽 여백을 `var(--space-4)` 값으로 설정합니다. `var()`는 앞에서 정의한 CSS 변수를 읽습니다](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 1067 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 1068 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#skills) |
| 1069 | <code>  .scroll-top {</code> | [`.scroll-top` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1070 | <code>    right: 2rem;</code> | [오른쪽 위치을 `2rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1071 | <code>    bottom: 2rem;</code> | [아래쪽 위치을 `2rem` 값으로 설정합니다. `rem`은 최상위 글자 크기 기준의 상대 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1072 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1073 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1074 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1075 | <code>/* 사용자가 동작 감소를 요청하면 애니메이션과 부드러운 이동을 제거합니다. */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1076 | <code>@media (prefers-reduced-motion: reduce) {</code> | [화면 크기 또는 접근성 설정 조건에 따라 적용할 스타일을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1077 | <code>  *,</code> | [CSS 구역의 목적을 설명하는 주석입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1078 | <code>  *::before,</code> | [CSS 구역의 목적을 설명하는 주석입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1079 | <code>  *::after {</code> | [CSS 구역의 목적을 설명하는 주석입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1080 | <code>    scroll-behavior: auto !important;</code> | [스크롤 움직임을 `auto !important` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1081 | <code>    animation-duration: 0.01ms !important;</code> | [`animation-duration` 스타일을 `0.01ms !important` 값으로 설정합니다. `ms`는 1/1000초 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1082 | <code>    animation-iteration-count: 1 !important;</code> | [`animation-iteration-count` 스타일을 `1 !important` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1083 | <code>    transition-duration: 0.01ms !important;</code> | [`transition-duration` 스타일을 `0.01ms !important` 값으로 설정합니다. `ms`는 1/1000초 단위입니다](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1084 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1085 | <em>(빈 줄)</em> | [스타일 규칙을 구분하는 빈 줄입니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1086 | <code>  .reveal {</code> | [`.reveal` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#hero) |
| 1087 | <code>    transform: none;</code> | [이동·회전·크기 변형을 `none` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1088 | <code>    opacity: 1;</code> | [투명도을 `1` 값으로 설정합니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1089 | <code>  }</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |
| 1090 | <code>}</code> | [현재 선택자 또는 미디어 쿼리의 범위를 닫습니다.](https://bidulgiya999.github.io/codyssey_B1-1/#contact) |

총 1,090줄을 설명했습니다.
