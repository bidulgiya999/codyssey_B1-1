# style.css 줄별 해설

원본 파일: [`css/style.css`](../css/style.css)

> 실행 파일을 건드리지 않는 학습용 줄별 해설입니다. 빈 줄도 포함하며, 원본 수정 후 생성 도구를 다시 실행하면 줄 번호가 갱신됩니다.

| 줄 | 코드 | 설명 |
|---:|---|---|
| 1 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 2 | <code>   1. 디자인 토큰</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 3 | <code>   색상·간격·그림자를 변수로 관리해 테마 변경과 유지보수를 단순화합니다.</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 4 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 5 | <code>:root {</code> | `:root` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 6 | <code>  color-scheme: light;</code> | `color-scheme` 스타일을 `light` 값으로 설정합니다. |
| 7 | <code>  --color-bg: #f5f8f9;</code> | CSS 변수 `--color-bg`에 `#f5f8f9` 값을 저장합니다. |
| 8 | <code>  --color-surface: #ffffff;</code> | CSS 변수 `--color-surface`에 `#ffffff` 값을 저장합니다. |
| 9 | <code>  --color-surface-muted: #eaf0f1;</code> | CSS 변수 `--color-surface-muted`에 `#eaf0f1` 값을 저장합니다. |
| 10 | <code>  --color-text: #10202c;</code> | CSS 변수 `--color-text`에 `#10202c` 값을 저장합니다. |
| 11 | <code>  --color-text-muted: #5e6f78;</code> | CSS 변수 `--color-text-muted`에 `#5e6f78` 값을 저장합니다. |
| 12 | <code>  --color-line: #cad6da;</code> | CSS 변수 `--color-line`에 `#cad6da` 값을 저장합니다. |
| 13 | <code>  --color-accent: #007f73;</code> | CSS 변수 `--color-accent`에 `#007f73` 값을 저장합니다. |
| 14 | <code>  --color-accent-strong: #00665d;</code> | CSS 변수 `--color-accent-strong`에 `#00665d` 값을 저장합니다. |
| 15 | <code>  --color-highlight: #d88a00;</code> | CSS 변수 `--color-highlight`에 `#d88a00` 값을 저장합니다. |
| 16 | <code>  --color-dark: #0d1b2a;</code> | CSS 변수 `--color-dark`에 `#0d1b2a` 값을 저장합니다. |
| 17 | <code>  --color-dark-muted: #13283b;</code> | CSS 변수 `--color-dark-muted`에 `#13283b` 값을 저장합니다. |
| 18 | <code>  --color-on-dark: #eef7f7;</code> | CSS 변수 `--color-on-dark`에 `#eef7f7` 값을 저장합니다. |
| 19 | <code>  --color-error: #b42318;</code> | CSS 변수 `--color-error`에 `#b42318` 값을 저장합니다. |
| 20 | <code>  --color-success: #087a55;</code> | CSS 변수 `--color-success`에 `#087a55` 값을 저장합니다. |
| 21 | <code>  --font-sans: &quot;Pretendard&quot;, &quot;Noto Sans KR&quot;, &quot;Segoe UI&quot;, sans-serif;</code> | CSS 변수 `--font-sans`에 `"Pretendard", "Noto Sans KR", "Segoe UI", sans-serif` 값을 저장합니다. |
| 22 | <code>  --font-mono: &quot;Cascadia Code&quot;, &quot;Consolas&quot;, monospace;</code> | CSS 변수 `--font-mono`에 `"Cascadia Code", "Consolas", monospace` 값을 저장합니다. |
| 23 | <code>  --space-1: 0.5rem;</code> | CSS 변수 `--space-1`에 `0.5rem` 값을 저장합니다. |
| 24 | <code>  --space-2: 1rem;</code> | CSS 변수 `--space-2`에 `1rem` 값을 저장합니다. |
| 25 | <code>  --space-3: 1.5rem;</code> | CSS 변수 `--space-3`에 `1.5rem` 값을 저장합니다. |
| 26 | <code>  --space-4: 2rem;</code> | CSS 변수 `--space-4`에 `2rem` 값을 저장합니다. |
| 27 | <code>  --space-5: 3rem;</code> | CSS 변수 `--space-5`에 `3rem` 값을 저장합니다. |
| 28 | <code>  --space-6: 5rem;</code> | CSS 변수 `--space-6`에 `5rem` 값을 저장합니다. |
| 29 | <code>  --radius-sm: 0.5rem;</code> | CSS 변수 `--radius-sm`에 `0.5rem` 값을 저장합니다. |
| 30 | <code>  --radius-md: 1rem;</code> | CSS 변수 `--radius-md`에 `1rem` 값을 저장합니다. |
| 31 | <code>  --radius-lg: 1.5rem;</code> | CSS 변수 `--radius-lg`에 `1.5rem` 값을 저장합니다. |
| 32 | <code>  --shadow-card: 0 1.25rem 3rem rgba(13, 27, 42, 0.1);</code> | CSS 변수 `--shadow-card`에 `0 1.25rem 3rem rgba(13, 27, 42, 0.1)` 값을 저장합니다. |
| 33 | <code>  --header-height: 4.5rem;</code> | CSS 변수 `--header-height`에 `4.5rem` 값을 저장합니다. |
| 34 | <code>  --transition: 180ms ease;</code> | CSS 변수 `--transition`에 `180ms ease` 값을 저장합니다. |
| 35 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 36 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 37 | <code>[data-theme=&quot;dark&quot;] {</code> | `[data-theme="dark"]` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 38 | <code>  color-scheme: dark;</code> | `color-scheme` 스타일을 `dark` 값으로 설정합니다. |
| 39 | <code>  --color-bg: #09131e;</code> | CSS 변수 `--color-bg`에 `#09131e` 값을 저장합니다. |
| 40 | <code>  --color-surface: #102131;</code> | CSS 변수 `--color-surface`에 `#102131` 값을 저장합니다. |
| 41 | <code>  --color-surface-muted: #152a3c;</code> | CSS 변수 `--color-surface-muted`에 `#152a3c` 값을 저장합니다. |
| 42 | <code>  --color-text: #eff8f7;</code> | CSS 변수 `--color-text`에 `#eff8f7` 값을 저장합니다. |
| 43 | <code>  --color-text-muted: #a9bdc4;</code> | CSS 변수 `--color-text-muted`에 `#a9bdc4` 값을 저장합니다. |
| 44 | <code>  --color-line: #2c4655;</code> | CSS 변수 `--color-line`에 `#2c4655` 값을 저장합니다. |
| 45 | <code>  --color-accent: #47dac5;</code> | CSS 변수 `--color-accent`에 `#47dac5` 값을 저장합니다. |
| 46 | <code>  --color-accent-strong: #72ebd9;</code> | CSS 변수 `--color-accent-strong`에 `#72ebd9` 값을 저장합니다. |
| 47 | <code>  --color-highlight: #ffc65c;</code> | CSS 변수 `--color-highlight`에 `#ffc65c` 값을 저장합니다. |
| 48 | <code>  --color-dark: #050c13;</code> | CSS 변수 `--color-dark`에 `#050c13` 값을 저장합니다. |
| 49 | <code>  --color-dark-muted: #0d1c29;</code> | CSS 변수 `--color-dark-muted`에 `#0d1c29` 값을 저장합니다. |
| 50 | <code>  --color-on-dark: #eff8f7;</code> | CSS 변수 `--color-on-dark`에 `#eff8f7` 값을 저장합니다. |
| 51 | <code>  --color-error: #ff8d85;</code> | CSS 변수 `--color-error`에 `#ff8d85` 값을 저장합니다. |
| 52 | <code>  --color-success: #6ee7b7;</code> | CSS 변수 `--color-success`에 `#6ee7b7` 값을 저장합니다. |
| 53 | <code>  --shadow-card: 0 1.25rem 3rem rgba(0, 0, 0, 0.35);</code> | CSS 변수 `--shadow-card`에 `0 1.25rem 3rem rgba(0, 0, 0, 0.35)` 값을 저장합니다. |
| 54 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 55 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 56 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 57 | <code>   2. 기본 스타일과 접근성</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 58 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 59 | <code>*,</code> | CSS 구역의 목적을 설명하는 주석입니다. |
| 60 | <code>*::before,</code> | CSS 구역의 목적을 설명하는 주석입니다. |
| 61 | <code>*::after {</code> | CSS 구역의 목적을 설명하는 주석입니다. |
| 62 | <code>  box-sizing: border-box;</code> | 크기 계산 방식을 `border-box` 값으로 설정합니다. |
| 63 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 64 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 65 | <code>html {</code> | `html` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 66 | <code>  scroll-behavior: smooth;</code> | 스크롤 움직임을 `smooth` 값으로 설정합니다. |
| 67 | <code>  scroll-padding-top: calc(var(--header-height) + 1rem);</code> | 앵커 이동 위쪽 여유을 `calc(var(--header-height) + 1rem)` 값으로 설정합니다. |
| 68 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 69 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 70 | <code>body {</code> | `body` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 71 | <code>  margin: 0;</code> | 바깥 여백을 `0` 값으로 설정합니다. |
| 72 | <code>  overflow-x: hidden;</code> | 가로 넘침 처리을 `hidden` 값으로 설정합니다. |
| 73 | <code>  background: var(--color-bg);</code> | 배경을 `var(--color-bg)` 값으로 설정합니다. |
| 74 | <code>  color: var(--color-text);</code> | 글자색을 `var(--color-text)` 값으로 설정합니다. |
| 75 | <code>  font-family: var(--font-sans);</code> | 글꼴을 `var(--font-sans)` 값으로 설정합니다. |
| 76 | <code>  font-size: 1rem;</code> | 글자 크기을 `1rem` 값으로 설정합니다. |
| 77 | <code>  line-height: 1.7;</code> | 줄 높이을 `1.7` 값으로 설정합니다. |
| 78 | <code>  transition:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 79 | <code>    background-color var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 80 | <code>    color var(--transition);</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 81 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 82 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 83 | <code>body.menu-open {</code> | `body.menu-open` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 84 | <code>  overflow: hidden;</code> | 넘친 내용 처리을 `hidden` 값으로 설정합니다. |
| 85 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 86 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 87 | <code>img {</code> | `img` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 88 | <code>  display: block;</code> | 레이아웃 방식을 `block` 값으로 설정합니다. |
| 89 | <code>  max-width: 100%;</code> | 최대 너비을 `100%` 값으로 설정합니다. |
| 90 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 91 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 92 | <code>a {</code> | `a` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 93 | <code>  color: inherit;</code> | 글자색을 `inherit` 값으로 설정합니다. |
| 94 | <code>  text-decoration: none;</code> | 텍스트 장식을 `none` 값으로 설정합니다. |
| 95 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 96 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 97 | <code>button,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 98 | <code>input,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 99 | <code>textarea {</code> | `textarea` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 100 | <code>  font: inherit;</code> | `font` 스타일을 `inherit` 값으로 설정합니다. |
| 101 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 102 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 103 | <code>button,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 104 | <code>a {</code> | `a` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 105 | <code>  -webkit-tap-highlight-color: transparent;</code> | `-webkit-tap-highlight-color` 스타일을 `transparent` 값으로 설정합니다. |
| 106 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 107 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 108 | <code>:focus-visible {</code> | `:focus-visible` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 109 | <code>  outline: 0.2rem solid var(--color-highlight);</code> | 외곽선을 `0.2rem solid var(--color-highlight)` 값으로 설정합니다. |
| 110 | <code>  outline-offset: 0.2rem;</code> | `outline-offset` 스타일을 `0.2rem` 값으로 설정합니다. |
| 111 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 112 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 113 | <code>.skip-link {</code> | `.skip-link` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 114 | <code>  position: fixed;</code> | 배치 기준을 `fixed` 값으로 설정합니다. |
| 115 | <code>  top: 0.5rem;</code> | 위쪽 위치을 `0.5rem` 값으로 설정합니다. |
| 116 | <code>  left: 0.5rem;</code> | 왼쪽 위치을 `0.5rem` 값으로 설정합니다. |
| 117 | <code>  z-index: 1000;</code> | 겹침 순서을 `1000` 값으로 설정합니다. |
| 118 | <code>  padding: 0.75rem 1rem;</code> | 안쪽 여백을 `0.75rem 1rem` 값으로 설정합니다. |
| 119 | <code>  transform: translateY(-150%);</code> | 이동·회전·크기 변형을 `translateY(-150%)` 값으로 설정합니다. |
| 120 | <code>  border-radius: var(--radius-sm);</code> | 모서리 둥글기을 `var(--radius-sm)` 값으로 설정합니다. |
| 121 | <code>  background: var(--color-text);</code> | 배경을 `var(--color-text)` 값으로 설정합니다. |
| 122 | <code>  color: var(--color-bg);</code> | 글자색을 `var(--color-bg)` 값으로 설정합니다. |
| 123 | <code>  font-weight: 700;</code> | 글자 굵기을 `700` 값으로 설정합니다. |
| 124 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 125 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 126 | <code>.skip-link:focus {</code> | `.skip-link:focus` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 127 | <code>  transform: translateY(0);</code> | 이동·회전·크기 변형을 `translateY(0)` 값으로 설정합니다. |
| 128 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 129 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 130 | <code>.container {</code> | `.container` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 131 | <code>  width: min(100% - 2rem, 72rem);</code> | 너비을 `min(100% - 2rem, 72rem)` 값으로 설정합니다. |
| 132 | <code>  margin-inline: auto;</code> | 좌우 바깥 여백을 `auto` 값으로 설정합니다. |
| 133 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 134 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 135 | <code>.section {</code> | `.section` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 136 | <code>  position: relative;</code> | 배치 기준을 `relative` 값으로 설정합니다. |
| 137 | <code>  padding-block: var(--space-6);</code> | 위아래 안쪽 여백을 `var(--space-6)` 값으로 설정합니다. |
| 138 | <code>  scroll-margin-top: var(--header-height);</code> | `scroll-margin-top` 스타일을 `var(--header-height)` 값으로 설정합니다. |
| 139 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 140 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 141 | <code>.section-muted {</code> | `.section-muted` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 142 | <code>  background: var(--color-surface-muted);</code> | 배경을 `var(--color-surface-muted)` 값으로 설정합니다. |
| 143 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 144 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 145 | <code>.section-dark {</code> | `.section-dark` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 146 | <code>  background: var(--color-dark);</code> | 배경을 `var(--color-dark)` 값으로 설정합니다. |
| 147 | <code>  color: var(--color-on-dark);</code> | 글자색을 `var(--color-on-dark)` 값으로 설정합니다. |
| 148 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 149 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 150 | <code>.section-kicker,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 151 | <code>.eyebrow {</code> | `.eyebrow` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 152 | <code>  margin: 0 0 var(--space-1);</code> | 바깥 여백을 `0 0 var(--space-1)` 값으로 설정합니다. |
| 153 | <code>  color: var(--color-accent);</code> | 글자색을 `var(--color-accent)` 값으로 설정합니다. |
| 154 | <code>  font-family: var(--font-mono);</code> | 글꼴을 `var(--font-mono)` 값으로 설정합니다. |
| 155 | <code>  font-size: 0.875rem;</code> | 글자 크기을 `0.875rem` 값으로 설정합니다. |
| 156 | <code>  font-weight: 700;</code> | 글자 굵기을 `700` 값으로 설정합니다. |
| 157 | <code>  letter-spacing: 0.12em;</code> | 글자 간격을 `0.12em` 값으로 설정합니다. |
| 158 | <code>  text-transform: uppercase;</code> | 대소문자 표시을 `uppercase` 값으로 설정합니다. |
| 159 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 160 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 161 | <code>.section-dark .section-kicker {</code> | `.section-dark .section-kicker` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 162 | <code>  color: #69e6d4;</code> | 글자색을 `#69e6d4` 값으로 설정합니다. |
| 163 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 164 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 165 | <code>h1,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 166 | <code>h2,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 167 | <code>h3,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 168 | <code>p {</code> | `p` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 169 | <code>  margin-top: 0;</code> | 위 바깥 여백을 `0` 값으로 설정합니다. |
| 170 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 171 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 172 | <code>h1,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 173 | <code>h2,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 174 | <code>h3 {</code> | `h3` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 175 | <code>  line-height: 1.2;</code> | 줄 높이을 `1.2` 값으로 설정합니다. |
| 176 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 177 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 178 | <code>h1 {</code> | `h1` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 179 | <code>  margin-bottom: var(--space-3);</code> | 아래 바깥 여백을 `var(--space-3)` 값으로 설정합니다. |
| 180 | <code>  font-size: clamp(2.75rem, 12vw, 5.75rem);</code> | 글자 크기을 `clamp(2.75rem, 12vw, 5.75rem)` 값으로 설정합니다. |
| 181 | <code>  letter-spacing: -0.055em;</code> | 글자 간격을 `-0.055em` 값으로 설정합니다. |
| 182 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 183 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 184 | <code>h1 span {</code> | `h1 span` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 185 | <code>  color: var(--color-accent);</code> | 글자색을 `var(--color-accent)` 값으로 설정합니다. |
| 186 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 187 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 188 | <code>h2 {</code> | `h2` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 189 | <code>  margin-bottom: var(--space-2);</code> | 아래 바깥 여백을 `var(--space-2)` 값으로 설정합니다. |
| 190 | <code>  font-size: clamp(2rem, 7vw, 3.5rem);</code> | 글자 크기을 `clamp(2rem, 7vw, 3.5rem)` 값으로 설정합니다. |
| 191 | <code>  letter-spacing: -0.04em;</code> | 글자 간격을 `-0.04em` 값으로 설정합니다. |
| 192 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 193 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 194 | <code>h3 {</code> | `h3` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 195 | <code>  font-size: 1.35rem;</code> | 글자 크기을 `1.35rem` 값으로 설정합니다. |
| 196 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 197 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 198 | <code>.section-heading {</code> | `.section-heading` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 199 | <code>  max-width: 44rem;</code> | 최대 너비을 `44rem` 값으로 설정합니다. |
| 200 | <code>  margin-bottom: var(--space-4);</code> | 아래 바깥 여백을 `var(--space-4)` 값으로 설정합니다. |
| 201 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 202 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 203 | <code>.section-heading &gt; p:last-child,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 204 | <code>.projects-heading p,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 205 | <code>.about-copy p,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 206 | <code>.contact-copy p {</code> | `.contact-copy p` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 207 | <code>  color: var(--color-text-muted);</code> | 글자색을 `var(--color-text-muted)` 값으로 설정합니다. |
| 208 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 209 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 210 | <code>.button {</code> | `.button` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 211 | <code>  display: inline-flex;</code> | 레이아웃 방식을 `inline-flex` 값으로 설정합니다. |
| 212 | <code>  min-height: 3rem;</code> | 최소 높이을 `3rem` 값으로 설정합니다. |
| 213 | <code>  align-items: center;</code> | 교차축의 정렬을 `center` 값으로 설정합니다. |
| 214 | <code>  justify-content: center;</code> | 주축 정렬을 `center` 값으로 설정합니다. |
| 215 | <code>  padding: 0.75rem 1.25rem;</code> | 안쪽 여백을 `0.75rem 1.25rem` 값으로 설정합니다. |
| 216 | <code>  border: 0.1rem solid transparent;</code> | 테두리을 `0.1rem solid transparent` 값으로 설정합니다. |
| 217 | <code>  border-radius: 999px;</code> | 모서리 둥글기을 `999px` 값으로 설정합니다. |
| 218 | <code>  cursor: pointer;</code> | 마우스 커서을 `pointer` 값으로 설정합니다. |
| 219 | <code>  font-weight: 800;</code> | 글자 굵기을 `800` 값으로 설정합니다. |
| 220 | <code>  transition:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 221 | <code>    transform var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 222 | <code>    background-color var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 223 | <code>    border-color var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 224 | <code>    color var(--transition);</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 225 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 226 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 227 | <code>.button:hover {</code> | `.button:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 228 | <code>  transform: translateY(-0.15rem);</code> | 이동·회전·크기 변형을 `translateY(-0.15rem)` 값으로 설정합니다. |
| 229 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 230 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 231 | <code>.button-primary {</code> | `.button-primary` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 232 | <code>  background: var(--color-accent);</code> | 배경을 `var(--color-accent)` 값으로 설정합니다. |
| 233 | <code>  color: #ffffff;</code> | 글자색을 `#ffffff` 값으로 설정합니다. |
| 234 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 235 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 236 | <code>.button-primary:hover {</code> | `.button-primary:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 237 | <code>  background: var(--color-accent-strong);</code> | 배경을 `var(--color-accent-strong)` 값으로 설정합니다. |
| 238 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 239 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 240 | <code>.button-secondary {</code> | `.button-secondary` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 241 | <code>  border-color: var(--color-line);</code> | `border-color` 스타일을 `var(--color-line)` 값으로 설정합니다. |
| 242 | <code>  background: transparent;</code> | 배경을 `transparent` 값으로 설정합니다. |
| 243 | <code>  color: var(--color-text);</code> | 글자색을 `var(--color-text)` 값으로 설정합니다. |
| 244 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 245 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 246 | <code>.button-secondary:hover {</code> | `.button-secondary:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 247 | <code>  border-color: var(--color-accent);</code> | `border-color` 스타일을 `var(--color-accent)` 값으로 설정합니다. |
| 248 | <code>  color: var(--color-accent);</code> | 글자색을 `var(--color-accent)` 값으로 설정합니다. |
| 249 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 250 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 251 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 252 | <code>   3. 헤더와 내비게이션 — 모바일 우선</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 253 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 254 | <code>.site-header {</code> | `.site-header` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 255 | <code>  position: fixed;</code> | 배치 기준을 `fixed` 값으로 설정합니다. |
| 256 | <code>  top: 0;</code> | 위쪽 위치을 `0` 값으로 설정합니다. |
| 257 | <code>  right: 0;</code> | 오른쪽 위치을 `0` 값으로 설정합니다. |
| 258 | <code>  left: 0;</code> | 왼쪽 위치을 `0` 값으로 설정합니다. |
| 259 | <code>  z-index: 100;</code> | 겹침 순서을 `100` 값으로 설정합니다. |
| 260 | <code>  min-height: var(--header-height);</code> | 최소 높이을 `var(--header-height)` 값으로 설정합니다. |
| 261 | <code>  border-bottom: 0.0625rem solid transparent;</code> | `border-bottom` 스타일을 `0.0625rem solid transparent` 값으로 설정합니다. |
| 262 | <code>  transition:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 263 | <code>    background-color var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 264 | <code>    border-color var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 265 | <code>    box-shadow var(--transition);</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 266 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 267 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 268 | <code>.site-header.scrolled {</code> | `.site-header.scrolled` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 269 | <code>  border-color: var(--color-line);</code> | `border-color` 스타일을 `var(--color-line)` 값으로 설정합니다. |
| 270 | <code>  background: color-mix(in srgb, var(--color-bg) 90%, transparent);</code> | 배경을 `color-mix(in srgb, var(--color-bg) 90%, transparent)` 값으로 설정합니다. |
| 271 | <code>  box-shadow: 0 0.5rem 1.5rem rgba(13, 27, 42, 0.08);</code> | 그림자을 `0 0.5rem 1.5rem rgba(13, 27, 42, 0.08)` 값으로 설정합니다. |
| 272 | <code>  backdrop-filter: blur(0.75rem);</code> | `backdrop-filter` 스타일을 `blur(0.75rem)` 값으로 설정합니다. |
| 273 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 274 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 275 | <code>.nav {</code> | `.nav` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 276 | <code>  min-height: var(--header-height);</code> | 최소 높이을 `var(--header-height)` 값으로 설정합니다. |
| 277 | <code>  display: flex;</code> | 레이아웃 방식을 `flex` 값으로 설정합니다. |
| 278 | <code>  align-items: center;</code> | 교차축의 정렬을 `center` 값으로 설정합니다. |
| 279 | <code>  justify-content: space-between;</code> | 주축 정렬을 `space-between` 값으로 설정합니다. |
| 280 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 281 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 282 | <code>.logo {</code> | `.logo` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 283 | <code>  display: inline-flex;</code> | 레이아웃 방식을 `inline-flex` 값으로 설정합니다. |
| 284 | <code>  align-items: center;</code> | 교차축의 정렬을 `center` 값으로 설정합니다. |
| 285 | <code>  gap: 0.65rem;</code> | 항목 사이 간격을 `0.65rem` 값으로 설정합니다. |
| 286 | <code>  font-weight: 900;</code> | 글자 굵기을 `900` 값으로 설정합니다. |
| 287 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 288 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 289 | <code>.logo-mark {</code> | `.logo-mark` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 290 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 291 | <code>  width: 2.35rem;</code> | 너비을 `2.35rem` 값으로 설정합니다. |
| 292 | <code>  aspect-ratio: 1;</code> | `aspect-ratio` 스타일을 `1` 값으로 설정합니다. |
| 293 | <code>  place-items: center;</code> | Grid 양방향 정렬을 `center` 값으로 설정합니다. |
| 294 | <code>  border: 0.125rem solid var(--color-accent);</code> | 테두리을 `0.125rem solid var(--color-accent)` 값으로 설정합니다. |
| 295 | <code>  color: var(--color-accent);</code> | 글자색을 `var(--color-accent)` 값으로 설정합니다. |
| 296 | <code>  font-family: var(--font-mono);</code> | 글꼴을 `var(--font-mono)` 값으로 설정합니다. |
| 297 | <code>  font-size: 0.75rem;</code> | 글자 크기을 `0.75rem` 값으로 설정합니다. |
| 298 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 299 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 300 | <code>.nav-actions {</code> | `.nav-actions` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 301 | <code>  display: flex;</code> | 레이아웃 방식을 `flex` 값으로 설정합니다. |
| 302 | <code>  align-items: center;</code> | 교차축의 정렬을 `center` 값으로 설정합니다. |
| 303 | <code>  gap: 0.5rem;</code> | 항목 사이 간격을 `0.5rem` 값으로 설정합니다. |
| 304 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 305 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 306 | <code>.theme-toggle,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 307 | <code>.menu-toggle {</code> | `.menu-toggle` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 308 | <code>  min-height: 2.75rem;</code> | 최소 높이을 `2.75rem` 값으로 설정합니다. |
| 309 | <code>  border: 0.0625rem solid var(--color-line);</code> | 테두리을 `0.0625rem solid var(--color-line)` 값으로 설정합니다. |
| 310 | <code>  border-radius: 999px;</code> | 모서리 둥글기을 `999px` 값으로 설정합니다. |
| 311 | <code>  background: var(--color-surface);</code> | 배경을 `var(--color-surface)` 값으로 설정합니다. |
| 312 | <code>  color: var(--color-text);</code> | 글자색을 `var(--color-text)` 값으로 설정합니다. |
| 313 | <code>  cursor: pointer;</code> | 마우스 커서을 `pointer` 값으로 설정합니다. |
| 314 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 315 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 316 | <code>.theme-toggle {</code> | `.theme-toggle` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 317 | <code>  display: inline-flex;</code> | 레이아웃 방식을 `inline-flex` 값으로 설정합니다. |
| 318 | <code>  align-items: center;</code> | 교차축의 정렬을 `center` 값으로 설정합니다. |
| 319 | <code>  gap: 0.45rem;</code> | 항목 사이 간격을 `0.45rem` 값으로 설정합니다. |
| 320 | <code>  padding-inline: 0.85rem;</code> | 좌우 안쪽 여백을 `0.85rem` 값으로 설정합니다. |
| 321 | <code>  font-size: 0.875rem;</code> | 글자 크기을 `0.875rem` 값으로 설정합니다. |
| 322 | <code>  font-weight: 700;</code> | 글자 굵기을 `700` 값으로 설정합니다. |
| 323 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 324 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 325 | <code>.theme-label {</code> | `.theme-label` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 326 | <code>  display: none;</code> | 레이아웃 방식을 `none` 값으로 설정합니다. |
| 327 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 328 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 329 | <code>.menu-toggle {</code> | `.menu-toggle` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 330 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 331 | <code>  width: 2.75rem;</code> | 너비을 `2.75rem` 값으로 설정합니다. |
| 332 | <code>  place-content: center;</code> | `place-content` 스타일을 `center` 값으로 설정합니다. |
| 333 | <code>  gap: 0.28rem;</code> | 항목 사이 간격을 `0.28rem` 값으로 설정합니다. |
| 334 | <code>  padding: 0;</code> | 안쪽 여백을 `0` 값으로 설정합니다. |
| 335 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 336 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 337 | <code>.menu-toggle span {</code> | `.menu-toggle span` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 338 | <code>  width: 1.15rem;</code> | 너비을 `1.15rem` 값으로 설정합니다. |
| 339 | <code>  height: 0.125rem;</code> | 높이을 `0.125rem` 값으로 설정합니다. |
| 340 | <code>  background: currentColor;</code> | 배경을 `currentColor` 값으로 설정합니다. |
| 341 | <code>  transition:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 342 | <code>    transform var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 343 | <code>    opacity var(--transition);</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 344 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 345 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 346 | <code>.menu-toggle.active span:nth-child(1) {</code> | `.menu-toggle.active span:nth-child(1)` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 347 | <code>  transform: translateY(0.405rem) rotate(45deg);</code> | 이동·회전·크기 변형을 `translateY(0.405rem) rotate(45deg)` 값으로 설정합니다. |
| 348 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 349 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 350 | <code>.menu-toggle.active span:nth-child(2) {</code> | `.menu-toggle.active span:nth-child(2)` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 351 | <code>  opacity: 0;</code> | 투명도을 `0` 값으로 설정합니다. |
| 352 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 353 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 354 | <code>.menu-toggle.active span:nth-child(3) {</code> | `.menu-toggle.active span:nth-child(3)` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 355 | <code>  transform: translateY(-0.405rem) rotate(-45deg);</code> | 이동·회전·크기 변형을 `translateY(-0.405rem) rotate(-45deg)` 값으로 설정합니다. |
| 356 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 357 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 358 | <code>.nav-menu {</code> | `.nav-menu` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 359 | <code>  position: fixed;</code> | 배치 기준을 `fixed` 값으로 설정합니다. |
| 360 | <code>  inset: var(--header-height) 0 auto;</code> | 네 방향 위치을 `var(--header-height) 0 auto` 값으로 설정합니다. |
| 361 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 362 | <code>  max-height: 0;</code> | `max-height` 스타일을 `0` 값으로 설정합니다. |
| 363 | <code>  margin: 0;</code> | 바깥 여백을 `0` 값으로 설정합니다. |
| 364 | <code>  overflow: hidden;</code> | 넘친 내용 처리을 `hidden` 값으로 설정합니다. |
| 365 | <code>  padding: 0 1rem;</code> | 안쪽 여백을 `0 1rem` 값으로 설정합니다. |
| 366 | <code>  background: var(--color-surface);</code> | 배경을 `var(--color-surface)` 값으로 설정합니다. |
| 367 | <code>  box-shadow: var(--shadow-card);</code> | 그림자을 `var(--shadow-card)` 값으로 설정합니다. |
| 368 | <code>  list-style: none;</code> | 목록 기호을 `none` 값으로 설정합니다. |
| 369 | <code>  opacity: 0;</code> | 투명도을 `0` 값으로 설정합니다. |
| 370 | <code>  transition:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 371 | <code>    max-height 250ms ease,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 372 | <code>    padding 250ms ease,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 373 | <code>    opacity var(--transition);</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 374 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 375 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 376 | <code>.nav-menu.active {</code> | `.nav-menu.active` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 377 | <code>  max-height: 24rem;</code> | `max-height` 스타일을 `24rem` 값으로 설정합니다. |
| 378 | <code>  padding-block: 1rem;</code> | 위아래 안쪽 여백을 `1rem` 값으로 설정합니다. |
| 379 | <code>  opacity: 1;</code> | 투명도을 `1` 값으로 설정합니다. |
| 380 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 381 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 382 | <code>.nav-menu a {</code> | `.nav-menu a` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 383 | <code>  display: block;</code> | 레이아웃 방식을 `block` 값으로 설정합니다. |
| 384 | <code>  padding: 0.85rem 0.75rem;</code> | 안쪽 여백을 `0.85rem 0.75rem` 값으로 설정합니다. |
| 385 | <code>  border-bottom: 0.0625rem solid var(--color-line);</code> | `border-bottom` 스타일을 `0.0625rem solid var(--color-line)` 값으로 설정합니다. |
| 386 | <code>  font-weight: 750;</code> | 글자 굵기을 `750` 값으로 설정합니다. |
| 387 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 388 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 389 | <code>.nav-menu a:hover {</code> | `.nav-menu a:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 390 | <code>  color: var(--color-accent);</code> | 글자색을 `var(--color-accent)` 값으로 설정합니다. |
| 391 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 392 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 393 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 394 | <code>   4. Hero와 컴퓨터 비전 모티프</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 395 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 396 | <code>.hero {</code> | `.hero` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 397 | <code>  min-height: 100svh;</code> | 최소 높이을 `100svh` 값으로 설정합니다. |
| 398 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 399 | <code>  align-items: center;</code> | 교차축의 정렬을 `center` 값으로 설정합니다. |
| 400 | <code>  padding-top: calc(var(--header-height) + var(--space-5));</code> | `padding-top` 스타일을 `calc(var(--header-height) + var(--space-5))` 값으로 설정합니다. |
| 401 | <code>  background-image:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 402 | <code>    linear-gradient(var(--color-line) 0.0625rem, transparent 0.0625rem),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 403 | <code>    linear-gradient(90deg, var(--color-line) 0.0625rem, transparent 0.0625rem);</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 404 | <code>  background-size: 2.5rem 2.5rem;</code> | `background-size` 스타일을 `2.5rem 2.5rem` 값으로 설정합니다. |
| 405 | <code>  background-position: center;</code> | `background-position` 스타일을 `center` 값으로 설정합니다. |
| 406 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 407 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 408 | <code>.hero::before {</code> | `.hero::before` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 409 | <code>  position: absolute;</code> | 배치 기준을 `absolute` 값으로 설정합니다. |
| 410 | <code>  inset: 0;</code> | 네 방향 위치을 `0` 값으로 설정합니다. |
| 411 | <code>  background: linear-gradient(100deg, var(--color-bg) 20%, transparent 75%);</code> | 배경을 `linear-gradient(100deg, var(--color-bg) 20%, transparent 75%)` 값으로 설정합니다. |
| 412 | <code>  content: &quot;&quot;;</code> | 가상 요소 내용을 `""` 값으로 설정합니다. |
| 413 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 414 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 415 | <code>.hero-grid {</code> | `.hero-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 416 | <code>  position: relative;</code> | 배치 기준을 `relative` 값으로 설정합니다. |
| 417 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 418 | <code>  gap: var(--space-5);</code> | 항목 사이 간격을 `var(--space-5)` 값으로 설정합니다. |
| 419 | <code>  align-items: center;</code> | 교차축의 정렬을 `center` 값으로 설정합니다. |
| 420 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 421 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 422 | <code>.hero-description {</code> | `.hero-description` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 423 | <code>  max-width: 37rem;</code> | 최대 너비을 `37rem` 값으로 설정합니다. |
| 424 | <code>  margin-bottom: var(--space-4);</code> | 아래 바깥 여백을 `var(--space-4)` 값으로 설정합니다. |
| 425 | <code>  color: var(--color-text-muted);</code> | 글자색을 `var(--color-text-muted)` 값으로 설정합니다. |
| 426 | <code>  font-size: clamp(1.05rem, 3vw, 1.25rem);</code> | 글자 크기을 `clamp(1.05rem, 3vw, 1.25rem)` 값으로 설정합니다. |
| 427 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 428 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 429 | <code>.hero-cta {</code> | `.hero-cta` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 430 | <code>  display: flex;</code> | 레이아웃 방식을 `flex` 값으로 설정합니다. |
| 431 | <code>  flex-wrap: wrap;</code> | Flex 줄바꿈을 `wrap` 값으로 설정합니다. |
| 432 | <code>  gap: 0.75rem;</code> | 항목 사이 간격을 `0.75rem` 값으로 설정합니다. |
| 433 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 434 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 435 | <code>.vision-panel {</code> | `.vision-panel` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 436 | <code>  width: min(100%, 26rem);</code> | 너비을 `min(100%, 26rem)` 값으로 설정합니다. |
| 437 | <code>  justify-self: center;</code> | 개별 항목 정렬을 `center` 값으로 설정합니다. |
| 438 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 439 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 440 | <code>.vision-frame {</code> | `.vision-frame` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 441 | <code>  position: relative;</code> | 배치 기준을 `relative` 값으로 설정합니다. |
| 442 | <code>  aspect-ratio: 1;</code> | `aspect-ratio` 스타일을 `1` 값으로 설정합니다. |
| 443 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 444 | <code>  place-items: center;</code> | Grid 양방향 정렬을 `center` 값으로 설정합니다. |
| 445 | <code>  border: 0.125rem solid var(--color-accent);</code> | 테두리을 `0.125rem solid var(--color-accent)` 값으로 설정합니다. |
| 446 | <code>  background: color-mix(in srgb, var(--color-surface) 88%, transparent);</code> | 배경을 `color-mix(in srgb, var(--color-surface) 88%, transparent)` 값으로 설정합니다. |
| 447 | <code>  box-shadow:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 448 | <code>    1rem 1rem 0 color-mix(in srgb, var(--color-accent) 20%, transparent),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 449 | <code>    var(--shadow-card);</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 450 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 451 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 452 | <code>.vision-frame::before,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 453 | <code>.vision-frame::after {</code> | `.vision-frame::after` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 454 | <code>  position: absolute;</code> | 배치 기준을 `absolute` 값으로 설정합니다. |
| 455 | <code>  width: 25%;</code> | 너비을 `25%` 값으로 설정합니다. |
| 456 | <code>  height: 25%;</code> | 높이을 `25%` 값으로 설정합니다. |
| 457 | <code>  content: &quot;&quot;;</code> | 가상 요소 내용을 `""` 값으로 설정합니다. |
| 458 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 459 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 460 | <code>.vision-frame::before {</code> | `.vision-frame::before` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 461 | <code>  top: -0.5rem;</code> | 위쪽 위치을 `-0.5rem` 값으로 설정합니다. |
| 462 | <code>  left: -0.5rem;</code> | 왼쪽 위치을 `-0.5rem` 값으로 설정합니다. |
| 463 | <code>  border-top: 0.4rem solid var(--color-highlight);</code> | `border-top` 스타일을 `0.4rem solid var(--color-highlight)` 값으로 설정합니다. |
| 464 | <code>  border-left: 0.4rem solid var(--color-highlight);</code> | `border-left` 스타일을 `0.4rem solid var(--color-highlight)` 값으로 설정합니다. |
| 465 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 466 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 467 | <code>.vision-frame::after {</code> | `.vision-frame::after` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 468 | <code>  right: -0.5rem;</code> | 오른쪽 위치을 `-0.5rem` 값으로 설정합니다. |
| 469 | <code>  bottom: -0.5rem;</code> | 아래쪽 위치을 `-0.5rem` 값으로 설정합니다. |
| 470 | <code>  border-right: 0.4rem solid var(--color-highlight);</code> | `border-right` 스타일을 `0.4rem solid var(--color-highlight)` 값으로 설정합니다. |
| 471 | <code>  border-bottom: 0.4rem solid var(--color-highlight);</code> | `border-bottom` 스타일을 `0.4rem solid var(--color-highlight)` 값으로 설정합니다. |
| 472 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 473 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 474 | <code>.focus-label {</code> | `.focus-label` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 475 | <code>  position: absolute;</code> | 배치 기준을 `absolute` 값으로 설정합니다. |
| 476 | <code>  top: -2rem;</code> | 위쪽 위치을 `-2rem` 값으로 설정합니다. |
| 477 | <code>  left: -0.125rem;</code> | 왼쪽 위치을 `-0.125rem` 값으로 설정합니다. |
| 478 | <code>  padding: 0.25rem 0.5rem;</code> | 안쪽 여백을 `0.25rem 0.5rem` 값으로 설정합니다. |
| 479 | <code>  background: var(--color-accent);</code> | 배경을 `var(--color-accent)` 값으로 설정합니다. |
| 480 | <code>  color: #ffffff;</code> | 글자색을 `#ffffff` 값으로 설정합니다. |
| 481 | <code>  font-family: var(--font-mono);</code> | 글꼴을 `var(--font-mono)` 값으로 설정합니다. |
| 482 | <code>  font-size: 0.75rem;</code> | 글자 크기을 `0.75rem` 값으로 설정합니다. |
| 483 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 484 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 485 | <code>.vision-content {</code> | `.vision-content` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 486 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 487 | <code>  justify-items: center;</code> | Grid 항목 정렬을 `center` 값으로 설정합니다. |
| 488 | <code>  gap: 0.35rem;</code> | 항목 사이 간격을 `0.35rem` 값으로 설정합니다. |
| 489 | <code>  font-family: var(--font-mono);</code> | 글꼴을 `var(--font-mono)` 값으로 설정합니다. |
| 490 | <code>  text-align: center;</code> | 텍스트 정렬을 `center` 값으로 설정합니다. |
| 491 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 492 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 493 | <code>.vision-content strong {</code> | `.vision-content strong` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 494 | <code>  font-size: clamp(3.5rem, 18vw, 6rem);</code> | 글자 크기을 `clamp(3.5rem, 18vw, 6rem)` 값으로 설정합니다. |
| 495 | <code>  line-height: 1;</code> | 줄 높이을 `1` 값으로 설정합니다. |
| 496 | <code>  letter-spacing: -0.1em;</code> | 글자 간격을 `-0.1em` 값으로 설정합니다. |
| 497 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 498 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 499 | <code>.vision-content &gt; span:last-child {</code> | `.vision-content > span:last-child` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 500 | <code>  font-size: 0.75rem;</code> | 글자 크기을 `0.75rem` 값으로 설정합니다. |
| 501 | <code>  letter-spacing: 0.08em;</code> | 글자 간격을 `0.08em` 값으로 설정합니다. |
| 502 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 503 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 504 | <code>.vision-index {</code> | `.vision-index` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 505 | <code>  color: var(--color-highlight);</code> | 글자색을 `var(--color-highlight)` 값으로 설정합니다. |
| 506 | <code>  font-size: 1rem;</code> | 글자 크기을 `1rem` 값으로 설정합니다. |
| 507 | <code>  font-weight: 800;</code> | 글자 굵기을 `800` 값으로 설정합니다. |
| 508 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 509 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 510 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 511 | <code>   5. About와 Skills</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 512 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 513 | <code>.about-grid,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 514 | <code>.contact-grid {</code> | `.contact-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 515 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 516 | <code>  gap: var(--space-4);</code> | 항목 사이 간격을 `var(--space-4)` 값으로 설정합니다. |
| 517 | <code>  align-items: center;</code> | 교차축의 정렬을 `center` 값으로 설정합니다. |
| 518 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 519 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 520 | <code>.profile-frame {</code> | `.profile-frame` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 521 | <code>  position: relative;</code> | 배치 기준을 `relative` 값으로 설정합니다. |
| 522 | <code>  max-width: 28rem;</code> | 최대 너비을 `28rem` 값으로 설정합니다. |
| 523 | <code>  padding: 0.75rem;</code> | 안쪽 여백을 `0.75rem` 값으로 설정합니다. |
| 524 | <code>  border: 0.0625rem solid var(--color-line);</code> | 테두리을 `0.0625rem solid var(--color-line)` 값으로 설정합니다. |
| 525 | <code>  background: var(--color-surface);</code> | 배경을 `var(--color-surface)` 값으로 설정합니다. |
| 526 | <code>  box-shadow: var(--shadow-card);</code> | 그림자을 `var(--shadow-card)` 값으로 설정합니다. |
| 527 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 528 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 529 | <code>.profile-frame img {</code> | `.profile-frame img` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 530 | <code>  width: 100%;</code> | 너비을 `100%` 값으로 설정합니다. |
| 531 | <code>  aspect-ratio: 1;</code> | `aspect-ratio` 스타일을 `1` 값으로 설정합니다. |
| 532 | <code>  object-fit: cover;</code> | 이미지 채움 방식을 `cover` 값으로 설정합니다. |
| 533 | <code>  object-position: center;</code> | `object-position` 스타일을 `center` 값으로 설정합니다. |
| 534 | <code>  filter: saturate(0.9) contrast(1.04);</code> | 시각 필터을 `saturate(0.9) contrast(1.04)` 값으로 설정합니다. |
| 535 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 536 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 537 | <code>.profile-caption {</code> | `.profile-caption` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 538 | <code>  display: block;</code> | 레이아웃 방식을 `block` 값으로 설정합니다. |
| 539 | <code>  padding-top: 0.65rem;</code> | `padding-top` 스타일을 `0.65rem` 값으로 설정합니다. |
| 540 | <code>  color: var(--color-text-muted);</code> | 글자색을 `var(--color-text-muted)` 값으로 설정합니다. |
| 541 | <code>  font-family: var(--font-mono);</code> | 글꼴을 `var(--font-mono)` 값으로 설정합니다. |
| 542 | <code>  font-size: 0.75rem;</code> | 글자 크기을 `0.75rem` 값으로 설정합니다. |
| 543 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 544 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 545 | <code>.about-facts {</code> | `.about-facts` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 546 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 547 | <code>  gap: 0.75rem;</code> | 항목 사이 간격을 `0.75rem` 값으로 설정합니다. |
| 548 | <code>  margin: var(--space-4) 0 0;</code> | 바깥 여백을 `var(--space-4) 0 0` 값으로 설정합니다. |
| 549 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 550 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 551 | <code>.about-facts div {</code> | `.about-facts div` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 552 | <code>  padding: 1rem;</code> | 안쪽 여백을 `1rem` 값으로 설정합니다. |
| 553 | <code>  border-left: 0.2rem solid var(--color-accent);</code> | `border-left` 스타일을 `0.2rem solid var(--color-accent)` 값으로 설정합니다. |
| 554 | <code>  background: var(--color-surface);</code> | 배경을 `var(--color-surface)` 값으로 설정합니다. |
| 555 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 556 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 557 | <code>.about-facts dt {</code> | `.about-facts dt` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 558 | <code>  color: var(--color-text-muted);</code> | 글자색을 `var(--color-text-muted)` 값으로 설정합니다. |
| 559 | <code>  font-size: 0.875rem;</code> | 글자 크기을 `0.875rem` 값으로 설정합니다. |
| 560 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 561 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 562 | <code>.about-facts dd {</code> | `.about-facts dd` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 563 | <code>  margin: 0.2rem 0 0;</code> | 바깥 여백을 `0.2rem 0 0` 값으로 설정합니다. |
| 564 | <code>  font-weight: 800;</code> | 글자 굵기을 `800` 값으로 설정합니다. |
| 565 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 566 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 567 | <code>.skills-grid {</code> | `.skills-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 568 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 569 | <code>  gap: var(--space-2);</code> | 항목 사이 간격을 `var(--space-2)` 값으로 설정합니다. |
| 570 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 571 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 572 | <code>.skill-card {</code> | `.skill-card` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 573 | <code>  position: relative;</code> | 배치 기준을 `relative` 값으로 설정합니다. |
| 574 | <code>  min-height: 19rem;</code> | 최소 높이을 `19rem` 값으로 설정합니다. |
| 575 | <code>  padding: var(--space-4);</code> | 안쪽 여백을 `var(--space-4)` 값으로 설정합니다. |
| 576 | <code>  overflow: hidden;</code> | 넘친 내용 처리을 `hidden` 값으로 설정합니다. |
| 577 | <code>  border: 0.0625rem solid var(--color-line);</code> | 테두리을 `0.0625rem solid var(--color-line)` 값으로 설정합니다. |
| 578 | <code>  border-radius: var(--radius-md);</code> | 모서리 둥글기을 `var(--radius-md)` 값으로 설정합니다. |
| 579 | <code>  background: var(--color-surface);</code> | 배경을 `var(--color-surface)` 값으로 설정합니다. |
| 580 | <code>  box-shadow: 0 0.75rem 1.5rem rgba(13, 27, 42, 0.05);</code> | 그림자을 `0 0.75rem 1.5rem rgba(13, 27, 42, 0.05)` 값으로 설정합니다. |
| 581 | <code>  transition:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 582 | <code>    transform var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 583 | <code>    box-shadow var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 584 | <code>    border-color var(--transition);</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 585 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 586 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 587 | <code>.skill-card:hover {</code> | `.skill-card:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 588 | <code>  transform: translateY(-0.4rem);</code> | 이동·회전·크기 변형을 `translateY(-0.4rem)` 값으로 설정합니다. |
| 589 | <code>  border-color: var(--color-accent);</code> | `border-color` 스타일을 `var(--color-accent)` 값으로 설정합니다. |
| 590 | <code>  box-shadow: var(--shadow-card);</code> | 그림자을 `var(--shadow-card)` 값으로 설정합니다. |
| 591 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 592 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 593 | <code>.card-number {</code> | `.card-number` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 594 | <code>  color: var(--color-accent);</code> | 글자색을 `var(--color-accent)` 값으로 설정합니다. |
| 595 | <code>  font-family: var(--font-mono);</code> | 글꼴을 `var(--font-mono)` 값으로 설정합니다. |
| 596 | <code>  font-weight: 800;</code> | 글자 굵기을 `800` 값으로 설정합니다. |
| 597 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 598 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 599 | <code>.skill-card h3 {</code> | `.skill-card h3` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 600 | <code>  margin-block: var(--space-3);</code> | 위아래 바깥 여백을 `var(--space-3)` 값으로 설정합니다. |
| 601 | <code>  font-size: 1.5rem;</code> | 글자 크기을 `1.5rem` 값으로 설정합니다. |
| 602 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 603 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 604 | <code>.skill-card p {</code> | `.skill-card p` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 605 | <code>  margin: var(--space-3) 0 0;</code> | 바깥 여백을 `var(--space-3) 0 0` 값으로 설정합니다. |
| 606 | <code>  color: var(--color-text-muted);</code> | 글자색을 `var(--color-text-muted)` 값으로 설정합니다. |
| 607 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 608 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 609 | <code>.tag-list {</code> | `.tag-list` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 610 | <code>  display: flex;</code> | 레이아웃 방식을 `flex` 값으로 설정합니다. |
| 611 | <code>  flex-wrap: wrap;</code> | Flex 줄바꿈을 `wrap` 값으로 설정합니다. |
| 612 | <code>  gap: 0.5rem;</code> | 항목 사이 간격을 `0.5rem` 값으로 설정합니다. |
| 613 | <code>  margin: 0;</code> | 바깥 여백을 `0` 값으로 설정합니다. |
| 614 | <code>  padding: 0;</code> | 안쪽 여백을 `0` 값으로 설정합니다. |
| 615 | <code>  list-style: none;</code> | 목록 기호을 `none` 값으로 설정합니다. |
| 616 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 617 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 618 | <code>.tag-list li {</code> | `.tag-list li` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 619 | <code>  padding: 0.4rem 0.7rem;</code> | 안쪽 여백을 `0.4rem 0.7rem` 값으로 설정합니다. |
| 620 | <code>  border-radius: 999px;</code> | 모서리 둥글기을 `999px` 값으로 설정합니다. |
| 621 | <code>  background: var(--color-surface-muted);</code> | 배경을 `var(--color-surface-muted)` 값으로 설정합니다. |
| 622 | <code>  font-family: var(--font-mono);</code> | 글꼴을 `var(--font-mono)` 값으로 설정합니다. |
| 623 | <code>  font-size: 0.82rem;</code> | 글자 크기을 `0.82rem` 값으로 설정합니다. |
| 624 | <code>  font-weight: 700;</code> | 글자 굵기을 `700` 값으로 설정합니다. |
| 625 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 626 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 627 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 628 | <code>   6. GitHub Projects — Grid와 상태별 UI</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 629 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 630 | <code>.projects-heading {</code> | `.projects-heading` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 631 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 632 | <code>  gap: var(--space-2);</code> | 항목 사이 간격을 `var(--space-2)` 값으로 설정합니다. |
| 633 | <code>  margin-bottom: var(--space-4);</code> | 아래 바깥 여백을 `var(--space-4)` 값으로 설정합니다. |
| 634 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 635 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 636 | <code>.projects-heading p {</code> | `.projects-heading p` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 637 | <code>  color: #a9bdc4;</code> | 글자색을 `#a9bdc4` 값으로 설정합니다. |
| 638 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 639 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 640 | <code>.text-link {</code> | `.text-link` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 641 | <code>  width: fit-content;</code> | 너비을 `fit-content` 값으로 설정합니다. |
| 642 | <code>  color: #69e6d4;</code> | 글자색을 `#69e6d4` 값으로 설정합니다. |
| 643 | <code>  font-weight: 800;</code> | 글자 굵기을 `800` 값으로 설정합니다. |
| 644 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 645 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 646 | <code>.text-link:hover {</code> | `.text-link:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 647 | <code>  text-decoration: underline;</code> | 텍스트 장식을 `underline` 값으로 설정합니다. |
| 648 | <code>  text-underline-offset: 0.3rem;</code> | 밑줄 거리을 `0.3rem` 값으로 설정합니다. |
| 649 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 650 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 651 | <code>.project-filters {</code> | `.project-filters` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 652 | <code>  display: flex;</code> | 레이아웃 방식을 `flex` 값으로 설정합니다. |
| 653 | <code>  flex-wrap: wrap;</code> | Flex 줄바꿈을 `wrap` 값으로 설정합니다. |
| 654 | <code>  gap: 0.5rem;</code> | 항목 사이 간격을 `0.5rem` 값으로 설정합니다. |
| 655 | <code>  margin-bottom: var(--space-3);</code> | 아래 바깥 여백을 `var(--space-3)` 값으로 설정합니다. |
| 656 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 657 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 658 | <code>.project-filters[hidden] {</code> | `.project-filters[hidden]` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 659 | <code>  display: none;</code> | 레이아웃 방식을 `none` 값으로 설정합니다. |
| 660 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 661 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 662 | <code>.filter-button {</code> | `.filter-button` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 663 | <code>  padding: 0.5rem 0.9rem;</code> | 안쪽 여백을 `0.5rem 0.9rem` 값으로 설정합니다. |
| 664 | <code>  border: 0.0625rem solid #385064;</code> | 테두리을 `0.0625rem solid #385064` 값으로 설정합니다. |
| 665 | <code>  border-radius: 999px;</code> | 모서리 둥글기을 `999px` 값으로 설정합니다. |
| 666 | <code>  background: transparent;</code> | 배경을 `transparent` 값으로 설정합니다. |
| 667 | <code>  color: #c8d8dd;</code> | 글자색을 `#c8d8dd` 값으로 설정합니다. |
| 668 | <code>  cursor: pointer;</code> | 마우스 커서을 `pointer` 값으로 설정합니다. |
| 669 | <code>  font-size: 0.875rem;</code> | 글자 크기을 `0.875rem` 값으로 설정합니다. |
| 670 | <code>  font-weight: 750;</code> | 글자 굵기을 `750` 값으로 설정합니다. |
| 671 | <code>  transition:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 672 | <code>    background-color var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 673 | <code>    color var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 674 | <code>    border-color var(--transition);</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 675 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 676 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 677 | <code>.filter-button:hover,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 678 | <code>.filter-button.active {</code> | `.filter-button.active` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 679 | <code>  border-color: #69e6d4;</code> | `border-color` 스타일을 `#69e6d4` 값으로 설정합니다. |
| 680 | <code>  background: #69e6d4;</code> | 배경을 `#69e6d4` 값으로 설정합니다. |
| 681 | <code>  color: #08131d;</code> | 글자색을 `#08131d` 값으로 설정합니다. |
| 682 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 683 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 684 | <code>.projects-grid {</code> | `.projects-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 685 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 686 | <code>  grid-template-columns: minmax(0, 1fr);</code> | Grid 열 구성을 `minmax(0, 1fr)` 값으로 설정합니다. |
| 687 | <code>  gap: var(--space-2);</code> | 항목 사이 간격을 `var(--space-2)` 값으로 설정합니다. |
| 688 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 689 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 690 | <code>.project-card {</code> | `.project-card` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 691 | <code>  display: flex;</code> | 레이아웃 방식을 `flex` 값으로 설정합니다. |
| 692 | <code>  min-height: 18rem;</code> | 최소 높이을 `18rem` 값으로 설정합니다. |
| 693 | <code>  flex-direction: column;</code> | Flex 진행 방향을 `column` 값으로 설정합니다. |
| 694 | <code>  padding: var(--space-3);</code> | 안쪽 여백을 `var(--space-3)` 값으로 설정합니다. |
| 695 | <code>  border: 0.0625rem solid #2b4254;</code> | 테두리을 `0.0625rem solid #2b4254` 값으로 설정합니다. |
| 696 | <code>  border-radius: var(--radius-md);</code> | 모서리 둥글기을 `var(--radius-md)` 값으로 설정합니다. |
| 697 | <code>  background: var(--color-dark-muted);</code> | 배경을 `var(--color-dark-muted)` 값으로 설정합니다. |
| 698 | <code>  box-shadow: 0 1rem 2rem rgba(0, 0, 0, 0.15);</code> | 그림자을 `0 1rem 2rem rgba(0, 0, 0, 0.15)` 값으로 설정합니다. |
| 699 | <code>  transition:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 700 | <code>    transform var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 701 | <code>    border-color var(--transition);</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 702 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 703 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 704 | <code>.project-card:hover {</code> | `.project-card:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 705 | <code>  transform: translateY(-0.35rem);</code> | 이동·회전·크기 변형을 `translateY(-0.35rem)` 값으로 설정합니다. |
| 706 | <code>  border-color: #69e6d4;</code> | `border-color` 스타일을 `#69e6d4` 값으로 설정합니다. |
| 707 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 708 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 709 | <code>.project-card-header {</code> | `.project-card-header` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 710 | <code>  display: flex;</code> | 레이아웃 방식을 `flex` 값으로 설정합니다. |
| 711 | <code>  align-items: start;</code> | 교차축의 정렬을 `start` 값으로 설정합니다. |
| 712 | <code>  justify-content: space-between;</code> | 주축 정렬을 `space-between` 값으로 설정합니다. |
| 713 | <code>  gap: 1rem;</code> | 항목 사이 간격을 `1rem` 값으로 설정합니다. |
| 714 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 715 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 716 | <code>.project-card h3 {</code> | `.project-card h3` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 717 | <code>  overflow-wrap: anywhere;</code> | `overflow-wrap` 스타일을 `anywhere` 값으로 설정합니다. |
| 718 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 719 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 720 | <code>.repo-link {</code> | `.repo-link` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 721 | <code>  color: #69e6d4;</code> | 글자색을 `#69e6d4` 값으로 설정합니다. |
| 722 | <code>  font-family: var(--font-mono);</code> | 글꼴을 `var(--font-mono)` 값으로 설정합니다. |
| 723 | <code>  font-size: 1.1rem;</code> | 글자 크기을 `1.1rem` 값으로 설정합니다. |
| 724 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 725 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 726 | <code>.repo-link:hover {</code> | `.repo-link:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 727 | <code>  text-decoration: underline;</code> | 텍스트 장식을 `underline` 값으로 설정합니다. |
| 728 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 729 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 730 | <code>.project-description {</code> | `.project-description` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 731 | <code>  flex: 1;</code> | Flex 항목 크기을 `1` 값으로 설정합니다. |
| 732 | <code>  color: #b8c9cf;</code> | 글자색을 `#b8c9cf` 값으로 설정합니다. |
| 733 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 734 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 735 | <code>.project-meta {</code> | `.project-meta` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 736 | <code>  display: flex;</code> | 레이아웃 방식을 `flex` 값으로 설정합니다. |
| 737 | <code>  flex-wrap: wrap;</code> | Flex 줄바꿈을 `wrap` 값으로 설정합니다. |
| 738 | <code>  gap: 0.75rem;</code> | 항목 사이 간격을 `0.75rem` 값으로 설정합니다. |
| 739 | <code>  margin: var(--space-3) 0 0;</code> | 바깥 여백을 `var(--space-3) 0 0` 값으로 설정합니다. |
| 740 | <code>  padding: var(--space-2) 0 0;</code> | 안쪽 여백을 `var(--space-2) 0 0` 값으로 설정합니다. |
| 741 | <code>  border-top: 0.0625rem solid #2b4254;</code> | `border-top` 스타일을 `0.0625rem solid #2b4254` 값으로 설정합니다. |
| 742 | <code>  color: #a9bdc4;</code> | 글자색을 `#a9bdc4` 값으로 설정합니다. |
| 743 | <code>  font-size: 0.82rem;</code> | 글자 크기을 `0.82rem` 값으로 설정합니다. |
| 744 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 745 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 746 | <code>.language-dot {</code> | `.language-dot` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 747 | <code>  display: inline-block;</code> | 레이아웃 방식을 `inline-block` 값으로 설정합니다. |
| 748 | <code>  width: 0.65rem;</code> | 너비을 `0.65rem` 값으로 설정합니다. |
| 749 | <code>  aspect-ratio: 1;</code> | `aspect-ratio` 스타일을 `1` 값으로 설정합니다. |
| 750 | <code>  margin-right: 0.35rem;</code> | `margin-right` 스타일을 `0.35rem` 값으로 설정합니다. |
| 751 | <code>  border-radius: 50%;</code> | 모서리 둥글기을 `50%` 값으로 설정합니다. |
| 752 | <code>  background: #69e6d4;</code> | 배경을 `#69e6d4` 값으로 설정합니다. |
| 753 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 754 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 755 | <code>.project-state,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 756 | <code>.noscript-message {</code> | `.noscript-message` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 757 | <code>  grid-column: 1 / -1;</code> | Grid 열 범위을 `1 / -1` 값으로 설정합니다. |
| 758 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 759 | <code>  min-height: 16rem;</code> | 최소 높이을 `16rem` 값으로 설정합니다. |
| 760 | <code>  place-items: center;</code> | Grid 양방향 정렬을 `center` 값으로 설정합니다. |
| 761 | <code>  align-content: center;</code> | `align-content` 스타일을 `center` 값으로 설정합니다. |
| 762 | <code>  gap: 0.75rem;</code> | 항목 사이 간격을 `0.75rem` 값으로 설정합니다. |
| 763 | <code>  padding: var(--space-4);</code> | 안쪽 여백을 `var(--space-4)` 값으로 설정합니다. |
| 764 | <code>  border: 0.0625rem dashed #385064;</code> | 테두리을 `0.0625rem dashed #385064` 값으로 설정합니다. |
| 765 | <code>  border-radius: var(--radius-md);</code> | 모서리 둥글기을 `var(--radius-md)` 값으로 설정합니다. |
| 766 | <code>  color: #c8d8dd;</code> | 글자색을 `#c8d8dd` 값으로 설정합니다. |
| 767 | <code>  text-align: center;</code> | 텍스트 정렬을 `center` 값으로 설정합니다. |
| 768 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 769 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 770 | <code>.project-state p {</code> | `.project-state p` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 771 | <code>  margin: 0;</code> | 바깥 여백을 `0` 값으로 설정합니다. |
| 772 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 773 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 774 | <code>.spinner {</code> | `.spinner` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 775 | <code>  width: 2.4rem;</code> | 너비을 `2.4rem` 값으로 설정합니다. |
| 776 | <code>  aspect-ratio: 1;</code> | `aspect-ratio` 스타일을 `1` 값으로 설정합니다. |
| 777 | <code>  border: 0.2rem solid #385064;</code> | 테두리을 `0.2rem solid #385064` 값으로 설정합니다. |
| 778 | <code>  border-top-color: #69e6d4;</code> | `border-top-color` 스타일을 `#69e6d4` 값으로 설정합니다. |
| 779 | <code>  border-radius: 50%;</code> | 모서리 둥글기을 `50%` 값으로 설정합니다. |
| 780 | <code>  animation: spin 700ms linear infinite;</code> | `animation` 스타일을 `spin 700ms linear infinite` 값으로 설정합니다. |
| 781 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 782 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 783 | <code>@keyframes spin {</code> | `@keyframes spin` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 784 | <code>  to {</code> | `to` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 785 | <code>    transform: rotate(360deg);</code> | 이동·회전·크기 변형을 `rotate(360deg)` 값으로 설정합니다. |
| 786 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 787 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 788 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 789 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 790 | <code>   7. Contact Form</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 791 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 792 | <code>.contact-copy {</code> | `.contact-copy` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 793 | <code>  align-self: start;</code> | `align-self` 스타일을 `start` 값으로 설정합니다. |
| 794 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 795 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 796 | <code>.contact-email {</code> | `.contact-email` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 797 | <code>  display: inline-block;</code> | 레이아웃 방식을 `inline-block` 값으로 설정합니다. |
| 798 | <code>  margin-top: var(--space-2);</code> | 위 바깥 여백을 `var(--space-2)` 값으로 설정합니다. |
| 799 | <code>  color: var(--color-accent);</code> | 글자색을 `var(--color-accent)` 값으로 설정합니다. |
| 800 | <code>  font-family: var(--font-mono);</code> | 글꼴을 `var(--font-mono)` 값으로 설정합니다. |
| 801 | <code>  font-weight: 800;</code> | 글자 굵기을 `800` 값으로 설정합니다. |
| 802 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 803 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 804 | <code>.contact-email:hover {</code> | `.contact-email:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 805 | <code>  text-decoration: underline;</code> | 텍스트 장식을 `underline` 값으로 설정합니다. |
| 806 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 807 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 808 | <code>.contact-form {</code> | `.contact-form` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 809 | <code>  position: relative;</code> | 배치 기준을 `relative` 값으로 설정합니다. |
| 810 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 811 | <code>  gap: var(--space-2);</code> | 항목 사이 간격을 `var(--space-2)` 값으로 설정합니다. |
| 812 | <code>  padding: var(--space-3);</code> | 안쪽 여백을 `var(--space-3)` 값으로 설정합니다. |
| 813 | <code>  border: 0.0625rem solid var(--color-line);</code> | 테두리을 `0.0625rem solid var(--color-line)` 값으로 설정합니다. |
| 814 | <code>  border-radius: var(--radius-lg);</code> | 모서리 둥글기을 `var(--radius-lg)` 값으로 설정합니다. |
| 815 | <code>  background: var(--color-surface);</code> | 배경을 `var(--color-surface)` 값으로 설정합니다. |
| 816 | <code>  box-shadow: var(--shadow-card);</code> | 그림자을 `var(--shadow-card)` 값으로 설정합니다. |
| 817 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 818 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 819 | <code>/* 사람에게는 보이지 않고 자동 입력 프로그램만 채우게 유도하는 스팸 방지 필드입니다. */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 820 | <code>.honeypot {</code> | `.honeypot` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 821 | <code>  position: absolute;</code> | 배치 기준을 `absolute` 값으로 설정합니다. |
| 822 | <code>  left: -10000px;</code> | 왼쪽 위치을 `-10000px` 값으로 설정합니다. |
| 823 | <code>  width: 1px;</code> | 너비을 `1px` 값으로 설정합니다. |
| 824 | <code>  height: 1px;</code> | 높이을 `1px` 값으로 설정합니다. |
| 825 | <code>  overflow: hidden;</code> | 넘친 내용 처리을 `hidden` 값으로 설정합니다. |
| 826 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 827 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 828 | <code>.form-field {</code> | `.form-field` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 829 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 830 | <code>  gap: 0.4rem;</code> | 항목 사이 간격을 `0.4rem` 값으로 설정합니다. |
| 831 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 832 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 833 | <code>.form-field label {</code> | `.form-field label` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 834 | <code>  font-weight: 800;</code> | 글자 굵기을 `800` 값으로 설정합니다. |
| 835 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 836 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 837 | <code>.form-field input,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 838 | <code>.form-field textarea {</code> | `.form-field textarea` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 839 | <code>  width: 100%;</code> | 너비을 `100%` 값으로 설정합니다. |
| 840 | <code>  border: 0.1rem solid var(--color-line);</code> | 테두리을 `0.1rem solid var(--color-line)` 값으로 설정합니다. |
| 841 | <code>  border-radius: var(--radius-sm);</code> | 모서리 둥글기을 `var(--radius-sm)` 값으로 설정합니다. |
| 842 | <code>  background: var(--color-bg);</code> | 배경을 `var(--color-bg)` 값으로 설정합니다. |
| 843 | <code>  color: var(--color-text);</code> | 글자색을 `var(--color-text)` 값으로 설정합니다. |
| 844 | <code>  padding: 0.8rem 0.9rem;</code> | 안쪽 여백을 `0.8rem 0.9rem` 값으로 설정합니다. |
| 845 | <code>  transition:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 846 | <code>    border-color var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 847 | <code>    box-shadow var(--transition);</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 848 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 849 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 850 | <code>.form-field input:focus,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 851 | <code>.form-field textarea:focus {</code> | `.form-field textarea:focus` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 852 | <code>  border-color: var(--color-accent);</code> | `border-color` 스타일을 `var(--color-accent)` 값으로 설정합니다. |
| 853 | <code>  box-shadow: 0 0 0 0.2rem color-mix(in srgb, var(--color-accent) 18%, transparent);</code> | 그림자을 `0 0 0 0.2rem color-mix(in srgb, var(--color-accent) 18%, transparent)` 값으로 설정합니다. |
| 854 | <code>  outline: none;</code> | 외곽선을 `none` 값으로 설정합니다. |
| 855 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 856 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 857 | <code>.form-field input[aria-invalid=&quot;true&quot;],</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 858 | <code>.form-field textarea[aria-invalid=&quot;true&quot;] {</code> | `.form-field textarea[aria-invalid="true"]` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 859 | <code>  border-color: var(--color-error);</code> | `border-color` 스타일을 `var(--color-error)` 값으로 설정합니다. |
| 860 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 861 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 862 | <code>.field-error {</code> | `.field-error` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 863 | <code>  min-height: 1.35rem;</code> | 최소 높이을 `1.35rem` 값으로 설정합니다. |
| 864 | <code>  color: var(--color-error);</code> | 글자색을 `var(--color-error)` 값으로 설정합니다. |
| 865 | <code>  font-size: 0.875rem;</code> | 글자 크기을 `0.875rem` 값으로 설정합니다. |
| 866 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 867 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 868 | <code>.submit-button {</code> | `.submit-button` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 869 | <code>  width: 100%;</code> | 너비을 `100%` 값으로 설정합니다. |
| 870 | <code>  border: 0;</code> | 테두리을 `0` 값으로 설정합니다. |
| 871 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 872 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 873 | <code>.submit-button:disabled {</code> | `.submit-button:disabled` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 874 | <code>  cursor: wait;</code> | 마우스 커서을 `wait` 값으로 설정합니다. |
| 875 | <code>  opacity: 0.65;</code> | 투명도을 `0.65` 값으로 설정합니다. |
| 876 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 877 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 878 | <code>.form-status {</code> | `.form-status` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 879 | <code>  min-height: 1.5rem;</code> | 최소 높이을 `1.5rem` 값으로 설정합니다. |
| 880 | <code>  margin: 0;</code> | 바깥 여백을 `0` 값으로 설정합니다. |
| 881 | <code>  color: var(--color-success);</code> | 글자색을 `var(--color-success)` 값으로 설정합니다. |
| 882 | <code>  font-weight: 750;</code> | 글자 굵기을 `750` 값으로 설정합니다. |
| 883 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 884 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 885 | <code>.form-status[data-status=&quot;error&quot;] {</code> | `.form-status[data-status="error"]` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 886 | <code>  color: var(--color-error);</code> | 글자색을 `var(--color-error)` 값으로 설정합니다. |
| 887 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 888 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 889 | <code>.form-status[data-status=&quot;pending&quot;] {</code> | `.form-status[data-status="pending"]` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 890 | <code>  color: var(--color-highlight);</code> | 글자색을 `var(--color-highlight)` 값으로 설정합니다. |
| 891 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 892 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 893 | <code>.form-notice {</code> | `.form-notice` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 894 | <code>  margin: 0;</code> | 바깥 여백을 `0` 값으로 설정합니다. |
| 895 | <code>  color: var(--color-text-muted);</code> | 글자색을 `var(--color-text-muted)` 값으로 설정합니다. |
| 896 | <code>  font-size: 0.8rem;</code> | 글자 크기을 `0.8rem` 값으로 설정합니다. |
| 897 | <code>  line-height: 1.6;</code> | 줄 높이을 `1.6` 값으로 설정합니다. |
| 898 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 899 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 900 | <code>.form-notice a {</code> | `.form-notice a` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 901 | <code>  color: var(--color-accent);</code> | 글자색을 `var(--color-accent)` 값으로 설정합니다. |
| 902 | <code>  text-decoration: underline;</code> | 텍스트 장식을 `underline` 값으로 설정합니다. |
| 903 | <code>  text-underline-offset: 0.2em;</code> | 밑줄 거리을 `0.2em` 값으로 설정합니다. |
| 904 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 905 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 906 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 907 | <code>   8. Footer, 스크롤 탑, 스크롤 애니메이션</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 908 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 909 | <code>.site-footer {</code> | `.site-footer` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 910 | <code>  padding-block: var(--space-3);</code> | 위아래 안쪽 여백을 `var(--space-3)` 값으로 설정합니다. |
| 911 | <code>  border-top: 0.0625rem solid var(--color-line);</code> | `border-top` 스타일을 `0.0625rem solid var(--color-line)` 값으로 설정합니다. |
| 912 | <code>  background: var(--color-surface);</code> | 배경을 `var(--color-surface)` 값으로 설정합니다. |
| 913 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 914 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 915 | <code>.footer-content {</code> | `.footer-content` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 916 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 917 | <code>  gap: var(--space-2);</code> | 항목 사이 간격을 `var(--space-2)` 값으로 설정합니다. |
| 918 | <code>  color: var(--color-text-muted);</code> | 글자색을 `var(--color-text-muted)` 값으로 설정합니다. |
| 919 | <code>  font-size: 0.875rem;</code> | 글자 크기을 `0.875rem` 값으로 설정합니다. |
| 920 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 921 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 922 | <code>.footer-content p {</code> | `.footer-content p` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 923 | <code>  margin: 0;</code> | 바깥 여백을 `0` 값으로 설정합니다. |
| 924 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 925 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 926 | <code>.footer-links {</code> | `.footer-links` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 927 | <code>  display: flex;</code> | 레이아웃 방식을 `flex` 값으로 설정합니다. |
| 928 | <code>  gap: var(--space-2);</code> | 항목 사이 간격을 `var(--space-2)` 값으로 설정합니다. |
| 929 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 930 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 931 | <code>.footer-links a:hover {</code> | `.footer-links a:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 932 | <code>  color: var(--color-accent);</code> | 글자색을 `var(--color-accent)` 값으로 설정합니다. |
| 933 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 934 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 935 | <code>.scroll-top {</code> | `.scroll-top` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 936 | <code>  position: fixed;</code> | 배치 기준을 `fixed` 값으로 설정합니다. |
| 937 | <code>  right: 1rem;</code> | 오른쪽 위치을 `1rem` 값으로 설정합니다. |
| 938 | <code>  bottom: 1rem;</code> | 아래쪽 위치을 `1rem` 값으로 설정합니다. |
| 939 | <code>  z-index: 80;</code> | 겹침 순서을 `80` 값으로 설정합니다. |
| 940 | <code>  display: grid;</code> | 레이아웃 방식을 `grid` 값으로 설정합니다. |
| 941 | <code>  min-width: 3.75rem;</code> | 최소 너비을 `3.75rem` 값으로 설정합니다. |
| 942 | <code>  min-height: 2.75rem;</code> | 최소 높이을 `2.75rem` 값으로 설정합니다. |
| 943 | <code>  padding: 0.5rem 0.75rem;</code> | 안쪽 여백을 `0.5rem 0.75rem` 값으로 설정합니다. |
| 944 | <code>  place-items: center;</code> | Grid 양방향 정렬을 `center` 값으로 설정합니다. |
| 945 | <code>  transform: translateY(1rem);</code> | 이동·회전·크기 변형을 `translateY(1rem)` 값으로 설정합니다. |
| 946 | <code>  border: 0;</code> | 테두리을 `0` 값으로 설정합니다. |
| 947 | <code>  border-radius: 0.5rem;</code> | 모서리 둥글기을 `0.5rem` 값으로 설정합니다. |
| 948 | <code>  background: var(--color-accent);</code> | 배경을 `var(--color-accent)` 값으로 설정합니다. |
| 949 | <code>  color: #ffffff;</code> | 글자색을 `#ffffff` 값으로 설정합니다. |
| 950 | <code>  font-family: var(--font-mono);</code> | 글꼴을 `var(--font-mono)` 값으로 설정합니다. |
| 951 | <code>  font-size: 0.75rem;</code> | 글자 크기을 `0.75rem` 값으로 설정합니다. |
| 952 | <code>  font-weight: 800;</code> | 글자 굵기을 `800` 값으로 설정합니다. |
| 953 | <code>  letter-spacing: 0.08em;</code> | 글자 간격을 `0.08em` 값으로 설정합니다. |
| 954 | <code>  box-shadow: var(--shadow-card);</code> | 그림자을 `var(--shadow-card)` 값으로 설정합니다. |
| 955 | <code>  cursor: pointer;</code> | 마우스 커서을 `pointer` 값으로 설정합니다. |
| 956 | <code>  opacity: 0;</code> | 투명도을 `0` 값으로 설정합니다. |
| 957 | <code>  pointer-events: none;</code> | 포인터 입력 허용 여부을 `none` 값으로 설정합니다. |
| 958 | <code>  transition:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 959 | <code>    opacity var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 960 | <code>    transform var(--transition),</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 961 | <code>    background-color var(--transition);</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 962 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 963 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 964 | <code>.scroll-top.visible {</code> | `.scroll-top.visible` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 965 | <code>  transform: translateY(0);</code> | 이동·회전·크기 변형을 `translateY(0)` 값으로 설정합니다. |
| 966 | <code>  opacity: 1;</code> | 투명도을 `1` 값으로 설정합니다. |
| 967 | <code>  pointer-events: auto;</code> | 포인터 입력 허용 여부을 `auto` 값으로 설정합니다. |
| 968 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 969 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 970 | <code>.scroll-top:hover {</code> | `.scroll-top:hover` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 971 | <code>  background: var(--color-accent-strong);</code> | 배경을 `var(--color-accent-strong)` 값으로 설정합니다. |
| 972 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 973 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 974 | <code>.reveal {</code> | `.reveal` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 975 | <code>  transform: translateY(1.75rem);</code> | 이동·회전·크기 변형을 `translateY(1.75rem)` 값으로 설정합니다. |
| 976 | <code>  opacity: 0;</code> | 투명도을 `0` 값으로 설정합니다. |
| 977 | <code>  transition:</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 978 | <code>    transform 600ms ease,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 979 | <code>    opacity 600ms ease;</code> | 앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다. |
| 980 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 981 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 982 | <code>.reveal.visible {</code> | `.reveal.visible` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 983 | <code>  transform: translateY(0);</code> | 이동·회전·크기 변형을 `translateY(0)` 값으로 설정합니다. |
| 984 | <code>  opacity: 1;</code> | 투명도을 `1` 값으로 설정합니다. |
| 985 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 986 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 987 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 988 | <code>   9. 태블릿: 768px 이상</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 989 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 990 | <code>@media (min-width: 48rem) {</code> | 화면 크기 또는 접근성 설정 조건에 따라 적용할 스타일을 시작합니다. |
| 991 | <code>  .theme-label {</code> | `.theme-label` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 992 | <code>    display: inline;</code> | 레이아웃 방식을 `inline` 값으로 설정합니다. |
| 993 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 994 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 995 | <code>  .menu-toggle {</code> | `.menu-toggle` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 996 | <code>    display: none;</code> | 레이아웃 방식을 `none` 값으로 설정합니다. |
| 997 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 998 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 999 | <code>  .nav-actions {</code> | `.nav-actions` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1000 | <code>    order: 3;</code> | `order` 스타일을 `3` 값으로 설정합니다. |
| 1001 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1002 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1003 | <code>  .nav-menu {</code> | `.nav-menu` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1004 | <code>    position: static;</code> | 배치 기준을 `static` 값으로 설정합니다. |
| 1005 | <code>    display: flex;</code> | 레이아웃 방식을 `flex` 값으로 설정합니다. |
| 1006 | <code>    max-height: none;</code> | `max-height` 스타일을 `none` 값으로 설정합니다. |
| 1007 | <code>    margin-left: auto;</code> | `margin-left` 스타일을 `auto` 값으로 설정합니다. |
| 1008 | <code>    padding: 0;</code> | 안쪽 여백을 `0` 값으로 설정합니다. |
| 1009 | <code>    overflow: visible;</code> | 넘친 내용 처리을 `visible` 값으로 설정합니다. |
| 1010 | <code>    background: transparent;</code> | 배경을 `transparent` 값으로 설정합니다. |
| 1011 | <code>    box-shadow: none;</code> | 그림자을 `none` 값으로 설정합니다. |
| 1012 | <code>    opacity: 1;</code> | 투명도을 `1` 값으로 설정합니다. |
| 1013 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1014 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1015 | <code>  .nav-menu a {</code> | `.nav-menu a` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1016 | <code>    padding: 0.75rem;</code> | 안쪽 여백을 `0.75rem` 값으로 설정합니다. |
| 1017 | <code>    border: 0;</code> | 테두리을 `0` 값으로 설정합니다. |
| 1018 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1019 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1020 | <code>  .hero-grid {</code> | `.hero-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1021 | <code>    grid-template-columns: minmax(0, 1.2fr) minmax(18rem, 0.8fr);</code> | Grid 열 구성을 `minmax(0, 1.2fr) minmax(18rem, 0.8fr)` 값으로 설정합니다. |
| 1022 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1023 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1024 | <code>  .about-grid,</code> | 다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다. |
| 1025 | <code>  .contact-grid {</code> | `.contact-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1026 | <code>    grid-template-columns: minmax(16rem, 0.8fr) minmax(0, 1.2fr);</code> | Grid 열 구성을 `minmax(16rem, 0.8fr) minmax(0, 1.2fr)` 값으로 설정합니다. |
| 1027 | <code>    gap: var(--space-6);</code> | 항목 사이 간격을 `var(--space-6)` 값으로 설정합니다. |
| 1028 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1029 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1030 | <code>  .skills-grid {</code> | `.skills-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1031 | <code>    grid-template-columns: repeat(3, minmax(0, 1fr));</code> | Grid 열 구성을 `repeat(3, minmax(0, 1fr))` 값으로 설정합니다. |
| 1032 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1033 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1034 | <code>  .projects-heading {</code> | `.projects-heading` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1035 | <code>    grid-template-columns: 1fr auto;</code> | Grid 열 구성을 `1fr auto` 값으로 설정합니다. |
| 1036 | <code>    align-items: end;</code> | 교차축의 정렬을 `end` 값으로 설정합니다. |
| 1037 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1038 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1039 | <code>  .projects-grid {</code> | `.projects-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1040 | <code>    grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr));</code> | Grid 열 구성을 `repeat(auto-fit, minmax(17rem, 1fr))` 값으로 설정합니다. |
| 1041 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1042 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1043 | <code>  .footer-content {</code> | `.footer-content` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1044 | <code>    grid-template-columns: 1fr auto;</code> | Grid 열 구성을 `1fr auto` 값으로 설정합니다. |
| 1045 | <code>    align-items: center;</code> | 교차축의 정렬을 `center` 값으로 설정합니다. |
| 1046 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1047 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1048 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1049 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 1050 | <code>   10. 데스크톱: 1024px 이상</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 1051 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 1052 | <code>@media (min-width: 64rem) {</code> | 화면 크기 또는 접근성 설정 조건에 따라 적용할 스타일을 시작합니다. |
| 1053 | <code>  .container {</code> | `.container` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1054 | <code>    width: min(100% - 4rem, 72rem);</code> | 너비을 `min(100% - 4rem, 72rem)` 값으로 설정합니다. |
| 1055 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1056 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1057 | <code>  .section {</code> | `.section` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1058 | <code>    padding-block: 7rem;</code> | 위아래 안쪽 여백을 `7rem` 값으로 설정합니다. |
| 1059 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1060 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1061 | <code>  .hero-grid {</code> | `.hero-grid` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1062 | <code>    gap: 7rem;</code> | 항목 사이 간격을 `7rem` 값으로 설정합니다. |
| 1063 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1064 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1065 | <code>  .contact-form {</code> | `.contact-form` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1066 | <code>    padding: var(--space-4);</code> | 안쪽 여백을 `var(--space-4)` 값으로 설정합니다. |
| 1067 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1068 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1069 | <code>  .scroll-top {</code> | `.scroll-top` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1070 | <code>    right: 2rem;</code> | 오른쪽 위치을 `2rem` 값으로 설정합니다. |
| 1071 | <code>    bottom: 2rem;</code> | 아래쪽 위치을 `2rem` 값으로 설정합니다. |
| 1072 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1073 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1074 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1075 | <code>/* 사용자가 동작 감소를 요청하면 애니메이션과 부드러운 이동을 제거합니다. */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 1076 | <code>@media (prefers-reduced-motion: reduce) {</code> | 화면 크기 또는 접근성 설정 조건에 따라 적용할 스타일을 시작합니다. |
| 1077 | <code>  *,</code> | CSS 구역의 목적을 설명하는 주석입니다. |
| 1078 | <code>  *::before,</code> | CSS 구역의 목적을 설명하는 주석입니다. |
| 1079 | <code>  *::after {</code> | CSS 구역의 목적을 설명하는 주석입니다. |
| 1080 | <code>    scroll-behavior: auto !important;</code> | 스크롤 움직임을 `auto !important` 값으로 설정합니다. |
| 1081 | <code>    animation-duration: 0.01ms !important;</code> | `animation-duration` 스타일을 `0.01ms !important` 값으로 설정합니다. |
| 1082 | <code>    animation-iteration-count: 1 !important;</code> | `animation-iteration-count` 스타일을 `1 !important` 값으로 설정합니다. |
| 1083 | <code>    transition-duration: 0.01ms !important;</code> | `transition-duration` 스타일을 `0.01ms !important` 값으로 설정합니다. |
| 1084 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1085 | <em>(빈 줄)</em> | 스타일 규칙을 구분하는 빈 줄입니다. |
| 1086 | <code>  .reveal {</code> | `.reveal` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다. |
| 1087 | <code>    transform: none;</code> | 이동·회전·크기 변형을 `none` 값으로 설정합니다. |
| 1088 | <code>    opacity: 1;</code> | 투명도을 `1` 값으로 설정합니다. |
| 1089 | <code>  }</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |
| 1090 | <code>}</code> | 현재 선택자 또는 미디어 쿼리의 범위를 닫습니다. |

총 1,090줄을 설명했습니다.
