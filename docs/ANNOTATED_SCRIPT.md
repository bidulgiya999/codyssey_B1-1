# script.js 줄별 해설

원본 파일: [`js/script.js`](../js/script.js)

> 실행 파일을 건드리지 않는 학습용 줄별 해설입니다. 빈 줄도 포함하며, 원본 수정 후 생성 도구를 다시 실행하면 줄 번호가 갱신됩니다.

| 줄 | 코드 | 설명 |
|---:|---|---|
| 1 | <code>&quot;use strict&quot;;</code> | 실수를 줄이기 위해 엄격 모드로 JavaScript를 실행합니다. |
| 2 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 3 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 4 | <code>   1. 애플리케이션 설정과 상태</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 5 | <code>   화면에 영향을 주는 값을 한 객체에서 관리해</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 6 | <code>   &quot;이벤트 → 상태 변경 → 렌더링&quot; 흐름을 명확히 합니다.</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 7 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 8 | <code>const GITHUB_USERNAME = &quot;bidulgiya999&quot;;</code> | 값 또는 객체 참조를 `GITHUB_USERNAME`에 저장합니다. |
| 9 | <code>const GITHUB_API_URL = `https://api.github.com/users/${GITHUB_USERNAME}/repos?sort=updated&amp;per_page=100`;</code> | 값 또는 객체 참조를 `GITHUB_API_URL`에 저장합니다. |
| 10 | <code>const FORM_ENDPOINT = &quot;https://formsubmit.co/ajax/jae94bro@gmail.com&quot;;</code> | 값 또는 객체 참조를 `FORM_ENDPOINT`에 저장합니다. |
| 11 | <code>const SCROLL_TOP_THRESHOLD = 300;</code> | 값 또는 객체 참조를 `SCROLL_TOP_THRESHOLD`에 저장합니다. |
| 12 | <code>const HEADER_SCROLL_THRESHOLD = 60;</code> | 값 또는 객체 참조를 `HEADER_SCROLL_THRESHOLD`에 저장합니다. |
| 13 | <code>const OBSERVER_THRESHOLD = 0.2;</code> | 값 또는 객체 참조를 `OBSERVER_THRESHOLD`에 저장합니다. |
| 14 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 15 | <code>// 브라우저가 저장소 접근을 막더라도 사이트가 중단되지 않도록 안전하게 값을 읽습니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 16 | <code>const getStoredTheme = () =&gt; {</code> | 재사용할 화살표 함수를 `getStoredTheme` 이름으로 선언합니다. |
| 17 | <code>  try {</code> | 오류 가능성이 있는 작업을 시도하는 블록입니다. |
| 18 | <code>    return localStorage.getItem(&quot;portfolio-theme&quot;);</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 19 | <code>  } catch {</code> | 발생한 오류를 받아 사용자 친화적으로 처리합니다. |
| 20 | <code>    return null;</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 21 | <code>  }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 22 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 23 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 24 | <code>const systemPrefersDark = window.matchMedia(&quot;(prefers-color-scheme: dark)&quot;).matches;</code> | 값 또는 객체 참조를 `systemPrefersDark`에 저장합니다. |
| 25 | <code>const storedTheme = getStoredTheme();</code> | 값 또는 객체 참조를 `storedTheme`에 저장합니다. |
| 26 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 27 | <code>const state = {</code> | 값 또는 객체 참조를 `state`에 저장합니다. |
| 28 | <code>  theme: storedTheme === &quot;dark&quot; &#124;&#124; storedTheme === &quot;light&quot;</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 29 | <code>    ? storedTheme</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 30 | <code>    : systemPrefersDark</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 31 | <code>      ? &quot;dark&quot;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 32 | <code>      : &quot;light&quot;,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 33 | <code>  menuOpen: false,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 34 | <code>  projects: {</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 35 | <code>    status: &quot;idle&quot;,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 36 | <code>    items: [],</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 37 | <code>    error: &quot;&quot;,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 38 | <code>    activeLanguage: &quot;all&quot;,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 39 | <code>  },</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 40 | <code>  form: {</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 41 | <code>    values: { name: &quot;&quot;, email: &quot;&quot;, message: &quot;&quot; },</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 42 | <code>    errors: {},</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 43 | <code>    touched: new Set(),</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 44 | <code>    status: &quot;idle&quot;,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 45 | <code>  },</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 46 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 47 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 48 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 49 | <code>   2. DOM 선택</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 50 | <code>   querySelector와 querySelectorAll로 필요한 요소를 한 번만 찾습니다.</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 51 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 52 | <code>const siteHeader = document.querySelector(&quot;#site-header&quot;);</code> | DOM 요소를 찾아 `siteHeader`에 저장합니다. |
| 53 | <code>const themeToggle = document.querySelector(&quot;#theme-toggle&quot;);</code> | DOM 요소를 찾아 `themeToggle`에 저장합니다. |
| 54 | <code>const themeIcon = document.querySelector(&quot;#theme-icon&quot;);</code> | DOM 요소를 찾아 `themeIcon`에 저장합니다. |
| 55 | <code>const themeLabel = document.querySelector(&quot;#theme-label&quot;);</code> | DOM 요소를 찾아 `themeLabel`에 저장합니다. |
| 56 | <code>const menuToggle = document.querySelector(&quot;#menu-toggle&quot;);</code> | DOM 요소를 찾아 `menuToggle`에 저장합니다. |
| 57 | <code>const navMenu = document.querySelector(&quot;#nav-menu&quot;);</code> | DOM 요소를 찾아 `navMenu`에 저장합니다. |
| 58 | <code>const navLinks = document.querySelectorAll(&#x27;a[href^=&quot;#&quot;]&#x27;);</code> | DOM 요소를 찾아 `navLinks`에 저장합니다. |
| 59 | <code>const scrollTopButton = document.querySelector(&quot;#scroll-top&quot;);</code> | DOM 요소를 찾아 `scrollTopButton`에 저장합니다. |
| 60 | <code>const revealElements = document.querySelectorAll(&quot;.reveal&quot;);</code> | DOM 요소를 찾아 `revealElements`에 저장합니다. |
| 61 | <code>const projectsGrid = document.querySelector(&quot;#projects-grid&quot;);</code> | DOM 요소를 찾아 `projectsGrid`에 저장합니다. |
| 62 | <code>const projectFilters = document.querySelector(&quot;#project-filters&quot;);</code> | DOM 요소를 찾아 `projectFilters`에 저장합니다. |
| 63 | <code>const contactForm = document.querySelector(&quot;#contact-form&quot;);</code> | DOM 요소를 찾아 `contactForm`에 저장합니다. |
| 64 | <code>const formStatus = document.querySelector(&quot;#form-status&quot;);</code> | DOM 요소를 찾아 `formStatus`에 저장합니다. |
| 65 | <code>const formUrlField = document.querySelector(&quot;#form-url&quot;);</code> | DOM 요소를 찾아 `formUrlField`에 저장합니다. |
| 66 | <code>const formFields = document.querySelectorAll(&quot;#contact-form [data-validate]&quot;);</code> | DOM 요소를 찾아 `formFields`에 저장합니다. |
| 67 | <code>const submitButton = document.querySelector(&quot;.submit-button&quot;);</code> | DOM 요소를 찾아 `submitButton`에 저장합니다. |
| 68 | <code>const currentYear = document.querySelector(&quot;#current-year&quot;);</code> | DOM 요소를 찾아 `currentYear`에 저장합니다. |
| 69 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 70 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 71 | <code>   3. 테마 상태 → 문서 렌더링</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 72 | <code>   localStorage에는 기기별 사용자 선택만 저장합니다.</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 73 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 74 | <code>const saveTheme = (theme) =&gt; {</code> | 재사용할 화살표 함수를 `saveTheme` 이름으로 선언합니다. |
| 75 | <code>  try {</code> | 오류 가능성이 있는 작업을 시도하는 블록입니다. |
| 76 | <code>    localStorage.setItem(&quot;portfolio-theme&quot;, theme);</code> | 새로고침 후에도 남는 브라우저 저장소를 사용합니다. |
| 77 | <code>  } catch {</code> | 발생한 오류를 받아 사용자 친화적으로 처리합니다. |
| 78 | <code>    // 저장소가 차단된 환경에서도 테마 전환 자체는 계속 동작합니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 79 | <code>  }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 80 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 81 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 82 | <code>// 상태 객체의 테마 값을 실제 화면과 스크린 리더용 설명에 함께 반영합니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 83 | <code>const renderTheme = () =&gt; {</code> | 재사용할 화살표 함수를 `renderTheme` 이름으로 선언합니다. |
| 84 | <code>  const isDark = state.theme === &quot;dark&quot;;</code> | 값 또는 객체 참조를 `isDark`에 저장합니다. |
| 85 | <code>  document.documentElement.dataset.theme = state.theme;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 86 | <code>  themeIcon.textContent = isDark ? &quot;☀&quot; : &quot;◐&quot;;</code> | HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. |
| 87 | <code>  themeLabel.textContent = isDark ? &quot;라이트 모드&quot; : &quot;다크 모드&quot;;</code> | HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. |
| 88 | <code>  themeToggle.setAttribute(&quot;aria-label&quot;, isDark ? &quot;라이트 모드로 전환&quot; : &quot;다크 모드로 전환&quot;);</code> | HTML 또는 ARIA 속성 값을 갱신합니다. |
| 89 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 90 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 91 | <code>themeToggle.addEventListener(&quot;click&quot;, () =&gt; {</code> | `click` 이벤트가 발생할 때 실행할 함수를 연결합니다. |
| 92 | <code>  state.theme = state.theme === &quot;dark&quot; ? &quot;light&quot; : &quot;dark&quot;;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 93 | <code>  saveTheme(state.theme);</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 94 | <code>  renderTheme();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 95 | <code>});</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 96 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 97 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 98 | <code>   4. 모바일 메뉴와 부드러운 스크롤</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 99 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 100 | <code>// 메뉴의 열림 상태를 class와 ARIA 속성에 동시에 반영합니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 101 | <code>const renderMenu = () =&gt; {</code> | 재사용할 화살표 함수를 `renderMenu` 이름으로 선언합니다. |
| 102 | <code>  navMenu.classList.toggle(&quot;active&quot;, state.menuOpen);</code> | CSS 클래스를 변경해 화면 상태를 바꿉니다. |
| 103 | <code>  menuToggle.classList.toggle(&quot;active&quot;, state.menuOpen);</code> | CSS 클래스를 변경해 화면 상태를 바꿉니다. |
| 104 | <code>  document.body.classList.toggle(&quot;menu-open&quot;, state.menuOpen);</code> | CSS 클래스를 변경해 화면 상태를 바꿉니다. |
| 105 | <code>  menuToggle.setAttribute(&quot;aria-expanded&quot;, String(state.menuOpen));</code> | HTML 또는 ARIA 속성 값을 갱신합니다. |
| 106 | <code>  menuToggle.setAttribute(&quot;aria-label&quot;, state.menuOpen ? &quot;메뉴 닫기&quot; : &quot;메뉴 열기&quot;);</code> | HTML 또는 ARIA 속성 값을 갱신합니다. |
| 107 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 108 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 109 | <code>const closeMenu = () =&gt; {</code> | 재사용할 화살표 함수를 `closeMenu` 이름으로 선언합니다. |
| 110 | <code>  state.menuOpen = false;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 111 | <code>  navMenu.classList.remove(&quot;active&quot;);</code> | CSS 클래스를 변경해 화면 상태를 바꿉니다. |
| 112 | <code>  menuToggle.classList.remove(&quot;active&quot;);</code> | CSS 클래스를 변경해 화면 상태를 바꿉니다. |
| 113 | <code>  document.body.classList.remove(&quot;menu-open&quot;);</code> | CSS 클래스를 변경해 화면 상태를 바꿉니다. |
| 114 | <code>  menuToggle.setAttribute(&quot;aria-expanded&quot;, &quot;false&quot;);</code> | HTML 또는 ARIA 속성 값을 갱신합니다. |
| 115 | <code>  menuToggle.setAttribute(&quot;aria-label&quot;, &quot;메뉴 열기&quot;);</code> | HTML 또는 ARIA 속성 값을 갱신합니다. |
| 116 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 117 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 118 | <code>menuToggle.addEventListener(&quot;click&quot;, () =&gt; {</code> | `click` 이벤트가 발생할 때 실행할 함수를 연결합니다. |
| 119 | <code>  state.menuOpen = !state.menuOpen;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 120 | <code>  renderMenu();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 121 | <code>});</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 122 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 123 | <code>navLinks.forEach((link) =&gt; {</code> | 각 항목에 같은 작업을 반복합니다. |
| 124 | <code>  link.addEventListener(&quot;click&quot;, (event) =&gt; {</code> | `click` 이벤트가 발생할 때 실행할 함수를 연결합니다. |
| 125 | <code>    const targetId = link.getAttribute(&quot;href&quot;);</code> | 값 또는 객체 참조를 `targetId`에 저장합니다. |
| 126 | <code>    const target = document.querySelector(targetId);</code> | DOM 요소를 찾아 `target`에 저장합니다. |
| 127 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 128 | <code>    if (!target) return;</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 129 | <code>    event.preventDefault();</code> | 브라우저 기본 동작을 막고 JavaScript가 직접 처리합니다. |
| 130 | <code>    closeMenu();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 131 | <code>    target.scrollIntoView({ behavior: &quot;smooth&quot;, block: &quot;start&quot; });</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 132 | <code>  });</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 133 | <code>});</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 134 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 135 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 136 | <code>   5. 스크롤 이벤트 → 헤더와 스크롤 탑 버튼 렌더링</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 137 | <code>   requestAnimationFrame으로 과도한 화면 갱신을 줄입니다.</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 138 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 139 | <code>let scrollTicking = false;</code> | 값 또는 객체 참조를 `scrollTicking`에 저장합니다. |
| 140 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 141 | <code>// 스크롤 위치에 따라 헤더 강조와 TOP 버튼 노출 여부만 갱신합니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 142 | <code>const renderScrollState = () =&gt; {</code> | 재사용할 화살표 함수를 `renderScrollState` 이름으로 선언합니다. |
| 143 | <code>  const scrollPosition = window.scrollY;</code> | 값 또는 객체 참조를 `scrollPosition`에 저장합니다. |
| 144 | <code>  siteHeader.classList.toggle(&quot;scrolled&quot;, scrollPosition &gt;= HEADER_SCROLL_THRESHOLD);</code> | CSS 클래스를 변경해 화면 상태를 바꿉니다. |
| 145 | <code>  scrollTopButton.classList.toggle(&quot;visible&quot;, scrollPosition &gt;= SCROLL_TOP_THRESHOLD);</code> | CSS 클래스를 변경해 화면 상태를 바꿉니다. |
| 146 | <code>  scrollTicking = false;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 147 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 148 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 149 | <code>window.addEventListener(&quot;scroll&quot;, () =&gt; {</code> | `scroll` 이벤트가 발생할 때 실행할 함수를 연결합니다. |
| 150 | <code>  if (!scrollTicking) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 151 | <code>    window.requestAnimationFrame(renderScrollState);</code> | 다음 화면 갱신 시점에 작업을 예약합니다. |
| 152 | <code>    scrollTicking = true;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 153 | <code>  }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 154 | <code>});</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 155 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 156 | <code>// 새로고침할 때 URL에 섹션 주소(#projects 등)가 있어도 버튼 상태를 바로 맞춥니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 157 | <code>renderScrollState();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 158 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 159 | <code>scrollTopButton.addEventListener(&quot;click&quot;, () =&gt; {</code> | `click` 이벤트가 발생할 때 실행할 함수를 연결합니다. |
| 160 | <code>  window.scrollTo({ top: 0, behavior: &quot;smooth&quot; });</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 161 | <code>});</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 162 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 163 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 164 | <code>   6. Intersection Observer 스크롤 애니메이션</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 165 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 166 | <code>const reduceMotion = window.matchMedia(&quot;(prefers-reduced-motion: reduce)&quot;).matches;</code> | 값 또는 객체 참조를 `reduceMotion`에 저장합니다. |
| 167 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 168 | <code>if (reduceMotion &#124;&#124; !(&quot;IntersectionObserver&quot; in window)) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 169 | <code>  revealElements.forEach((element) =&gt; element.classList.add(&quot;visible&quot;));</code> | 각 항목에 같은 작업을 반복합니다. |
| 170 | <code>} else {</code> | 앞 조건이 거짓일 때 실행할 대체 분기입니다. |
| 171 | <code>  const revealObserver = new IntersectionObserver(</code> | 값 또는 객체 참조를 `revealObserver`에 저장합니다. |
| 172 | <code>    (entries, observer) =&gt; {</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 173 | <code>      entries.forEach((entry) =&gt; {</code> | 각 항목에 같은 작업을 반복합니다. |
| 174 | <code>        if (entry.isIntersecting) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 175 | <code>          entry.target.classList.add(&quot;visible&quot;);</code> | CSS 클래스를 변경해 화면 상태를 바꿉니다. |
| 176 | <code>          observer.unobserve(entry.target);</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 177 | <code>        }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 178 | <code>      });</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 179 | <code>    },</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 180 | <code>    { threshold: OBSERVER_THRESHOLD },</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 181 | <code>  );</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 182 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 183 | <code>  revealElements.forEach((element) =&gt; revealObserver.observe(element));</code> | 각 항목에 같은 작업을 반복합니다. |
| 184 | <code>}</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 185 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 186 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 187 | <code>   7. GitHub API 상태 → Projects UI 렌더링</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 188 | <code>   외부 문자열은 innerHTML에 넣기 전에 escapeHtml로 이스케이프합니다.</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 189 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 190 | <code>// GitHub에서 받은 문자열이 HTML로 해석되지 않도록 특수문자를 치환합니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 191 | <code>const escapeHtml = (value) =&gt; String(value)</code> | 재사용할 화살표 함수를 `escapeHtml` 이름으로 선언합니다. |
| 192 | <code>  .replaceAll(&quot;&amp;&quot;, &quot;&amp;amp;&quot;)</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 193 | <code>  .replaceAll(&quot;&lt;&quot;, &quot;&amp;lt;&quot;)</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 194 | <code>  .replaceAll(&quot;&gt;&quot;, &quot;&amp;gt;&quot;)</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 195 | <code>  .replaceAll(&#x27;&quot;&#x27;, &quot;&amp;quot;&quot;)</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 196 | <code>  .replaceAll(&quot;&#x27;&quot;, &quot;&amp;#039;&quot;);</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 197 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 198 | <code>const formatDate = (dateString) =&gt; new Intl.DateTimeFormat(&quot;ko-KR&quot;, {</code> | 재사용할 화살표 함수를 `formatDate` 이름으로 선언합니다. |
| 199 | <code>  year: &quot;numeric&quot;,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 200 | <code>  month: &quot;short&quot;,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 201 | <code>  day: &quot;numeric&quot;,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 202 | <code>}).format(new Date(dateString));</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 203 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 204 | <code>// 저장소의 대표 언어를 중복 없이 모아 동적 필터 버튼을 만듭니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 205 | <code>const renderProjectFilters = () =&gt; {</code> | 재사용할 화살표 함수를 `renderProjectFilters` 이름으로 선언합니다. |
| 206 | <code>  const languages = [...new Set(</code> | 값 또는 객체 참조를 `languages`에 저장합니다. |
| 207 | <code>    state.projects.items</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 208 | <code>      .map(({ language }) =&gt; language)</code> | 각 배열 항목을 변환해 새 배열을 만듭니다. |
| 209 | <code>      .filter(Boolean),</code> | 조건을 통과한 항목만 새 배열로 모읍니다. |
| 210 | <code>  )].sort((first, second) =&gt; first.localeCompare(second));</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 211 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 212 | <code>  projectFilters.hidden = languages.length === 0;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 213 | <code>  if (languages.length === 0) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 214 | <code>    projectFilters.innerHTML = &quot;&quot;;</code> | 문자열로 만든 HTML 구조를 화면에 렌더링합니다. |
| 215 | <code>    return;</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 216 | <code>  }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 217 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 218 | <code>  const filterNames = [&quot;all&quot;, ...languages];</code> | 값 또는 객체 참조를 `filterNames`에 저장합니다. |
| 219 | <code>  projectFilters.innerHTML = filterNames.map((language) =&gt; {</code> | 각 배열 항목을 변환해 새 배열을 만듭니다. |
| 220 | <code>    const isActive = state.projects.activeLanguage === language;</code> | 값 또는 객체 참조를 `isActive`에 저장합니다. |
| 221 | <code>    const label = language === &quot;all&quot; ? &quot;전체&quot; : escapeHtml(language);</code> | 값 또는 객체 참조를 `label`에 저장합니다. |
| 222 | <code>    return `</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 223 | <code>      &lt;button</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 224 | <code>        class=&quot;filter-button${isActive ? &quot; active&quot; : &quot;&quot;}&quot;</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 225 | <code>        type=&quot;button&quot;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 226 | <code>        data-language=&quot;${escapeHtml(language)}&quot;</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 227 | <code>        aria-pressed=&quot;${isActive}&quot;</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 228 | <code>      &gt;${label}&lt;/button&gt;</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 229 | <code>    `;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 230 | <code>  }).join(&quot;&quot;);</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 231 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 232 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 233 | <code>// API 응답 한 건을 화면에 표시할 프로젝트 카드 HTML로 변환합니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 234 | <code>const createProjectCard = (project) =&gt; {</code> | 재사용할 화살표 함수를 `createProjectCard` 이름으로 선언합니다. |
| 235 | <code>  const {</code> | 값 또는 객체 참조를 `변수`에 저장합니다. |
| 236 | <code>    name,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 237 | <code>    description,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 238 | <code>    htmlUrl,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 239 | <code>    language,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 240 | <code>    stars,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 241 | <code>    forks,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 242 | <code>    updatedAt,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 243 | <code>  } = project;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 244 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 245 | <code>  return `</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 246 | <code>    &lt;article class=&quot;project-card&quot;&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 247 | <code>      &lt;div class=&quot;project-card-header&quot;&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 248 | <code>        &lt;h3&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 249 | <code>          &lt;a class=&quot;repo-link&quot; href=&quot;${htmlUrl}&quot; target=&quot;_blank&quot; rel=&quot;noopener noreferrer&quot;&gt;</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 250 | <code>            ${escapeHtml(name)}</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 251 | <code>          &lt;/a&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 252 | <code>        &lt;/h3&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 253 | <code>        &lt;span aria-hidden=&quot;true&quot;&gt;↗&lt;/span&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 254 | <code>      &lt;/div&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 255 | <code>      &lt;p class=&quot;project-description&quot;&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 256 | <code>        ${escapeHtml(description &#124;&#124; &quot;프로젝트 설명이 아직 없습니다.&quot;)}</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 257 | <code>      &lt;/p&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 258 | <code>      &lt;div class=&quot;project-meta&quot; aria-label=&quot;저장소 정보&quot;&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 259 | <code>        &lt;span&gt;&lt;i class=&quot;language-dot&quot; aria-hidden=&quot;true&quot;&gt;&lt;/i&gt;${escapeHtml(language &#124;&#124; &quot;기타&quot;)}&lt;/span&gt;</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 260 | <code>        &lt;span&gt;★ ${stars}&lt;/span&gt;</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 261 | <code>        &lt;span&gt;⑂ ${forks}&lt;/span&gt;</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 262 | <code>        &lt;span&gt;업데이트 ${escapeHtml(formatDate(updatedAt))}&lt;/span&gt;</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 263 | <code>      &lt;/div&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 264 | <code>    &lt;/article&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 265 | <code>  `;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 266 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 267 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 268 | <code>// loading/error/empty/success 상태마다 서로 다른 화면을 그립니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 269 | <code>const renderProjects = () =&gt; {</code> | 재사용할 화살표 함수를 `renderProjects` 이름으로 선언합니다. |
| 270 | <code>  const { status, items, error, activeLanguage } = state.projects;</code> | 값 또는 객체 참조를 `변수`에 저장합니다. |
| 271 | <code>  projectsGrid.setAttribute(&quot;aria-busy&quot;, String(status === &quot;loading&quot;));</code> | HTML 또는 ARIA 속성 값을 갱신합니다. |
| 272 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 273 | <code>  if (status === &quot;loading&quot;) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 274 | <code>    projectFilters.hidden = true;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 275 | <code>    projectsGrid.innerHTML = `</code> | 문자열로 만든 HTML 구조를 화면에 렌더링합니다. |
| 276 | <code>      &lt;div class=&quot;project-state&quot;&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 277 | <code>        &lt;span class=&quot;spinner&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 278 | <code>        &lt;p&gt;프로젝트를 불러오는 중입니다.&lt;/p&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 279 | <code>      &lt;/div&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 280 | <code>    `;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 281 | <code>    return;</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 282 | <code>  }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 283 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 284 | <code>  if (status === &quot;error&quot;) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 285 | <code>    projectFilters.hidden = true;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 286 | <code>    projectsGrid.innerHTML = `</code> | 문자열로 만든 HTML 구조를 화면에 렌더링합니다. |
| 287 | <code>      &lt;div class=&quot;project-state&quot;&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 288 | <code>        &lt;strong&gt;프로젝트를 불러올 수 없습니다.&lt;/strong&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 289 | <code>        &lt;p&gt;${escapeHtml(error)}&lt;/p&gt;</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 290 | <code>        &lt;button class=&quot;button button-primary&quot; id=&quot;retry-projects&quot; type=&quot;button&quot;&gt;다시 시도&lt;/button&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 291 | <code>      &lt;/div&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 292 | <code>    `;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 293 | <code>    document.querySelector(&quot;#retry-projects&quot;).addEventListener(&quot;click&quot;, loadProjects);</code> | `click` 이벤트가 발생할 때 실행할 함수를 연결합니다. |
| 294 | <code>    return;</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 295 | <code>  }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 296 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 297 | <code>  if (status === &quot;success&quot; &amp;&amp; items.length === 0) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 298 | <code>    projectFilters.hidden = true;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 299 | <code>    projectsGrid.innerHTML = `</code> | 문자열로 만든 HTML 구조를 화면에 렌더링합니다. |
| 300 | <code>      &lt;div class=&quot;project-state&quot;&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 301 | <code>        &lt;strong&gt;표시할 프로젝트가 없습니다.&lt;/strong&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 302 | <code>        &lt;p&gt;공개 저장소가 생성되면 이곳에 자동으로 표시됩니다.&lt;/p&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 303 | <code>      &lt;/div&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 304 | <code>    `;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 305 | <code>    return;</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 306 | <code>  }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 307 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 308 | <code>  renderProjectFilters();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 309 | <code>  const filteredProjects = activeLanguage === &quot;all&quot;</code> | 값 또는 객체 참조를 `filteredProjects`에 저장합니다. |
| 310 | <code>    ? items</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 311 | <code>    : items.filter(({ language }) =&gt; language === activeLanguage);</code> | 조건을 통과한 항목만 새 배열로 모읍니다. |
| 312 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 313 | <code>  if (filteredProjects.length === 0) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 314 | <code>    projectsGrid.innerHTML = `</code> | 문자열로 만든 HTML 구조를 화면에 렌더링합니다. |
| 315 | <code>      &lt;div class=&quot;project-state&quot;&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 316 | <code>        &lt;strong&gt;이 언어로 만든 프로젝트가 없습니다.&lt;/strong&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 317 | <code>        &lt;p&gt;다른 필터를 선택해주세요.&lt;/p&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 318 | <code>      &lt;/div&gt;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 319 | <code>    `;</code> | 템플릿 리터럴로 동적 HTML 일부를 구성합니다. |
| 320 | <code>    return;</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 321 | <code>  }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 322 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 323 | <code>  projectsGrid.innerHTML = filteredProjects.map(createProjectCard).join(&quot;&quot;);</code> | 각 배열 항목을 변환해 새 배열을 만듭니다. |
| 324 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 325 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 326 | <code>// 요청이 10초를 넘으면 중단하고, 필요한 값만 화면용 객체로 정리합니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 327 | <code>async function loadProjects() {</code> | `await`를 사용할 수 있는 비동기 함수를 선언합니다. |
| 328 | <code>  state.projects.status = &quot;loading&quot;;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 329 | <code>  state.projects.error = &quot;&quot;;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 330 | <code>  renderProjects();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 331 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 332 | <code>  const controller = new AbortController();</code> | 값 또는 객체 참조를 `controller`에 저장합니다. |
| 333 | <code>  const timeoutId = window.setTimeout(() =&gt; controller.abort(), 10000);</code> | 재사용할 화살표 함수를 `timeoutId` 이름으로 선언합니다. |
| 334 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 335 | <code>  try {</code> | 오류 가능성이 있는 작업을 시도하는 블록입니다. |
| 336 | <code>    const response = await fetch(GITHUB_API_URL, {</code> | 값 또는 객체 참조를 `response`에 저장합니다. |
| 337 | <code>      headers: { Accept: &quot;application/vnd.github+json&quot; },</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 338 | <code>      signal: controller.signal,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 339 | <code>    });</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 340 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 341 | <code>    if (!response.ok) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 342 | <code>      if (response.status === 403) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 343 | <code>        throw new Error(&quot;GitHub API 요청 한도에 도달했습니다. 잠시 후 다시 시도해주세요.&quot;);</code> | 설명과 함께 오류를 발생시켜 catch 블록으로 전달합니다. |
| 344 | <code>      }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 345 | <code>      if (response.status === 404) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 346 | <code>        throw new Error(&quot;GitHub 사용자를 찾을 수 없습니다.&quot;);</code> | 설명과 함께 오류를 발생시켜 catch 블록으로 전달합니다. |
| 347 | <code>      }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 348 | <code>      throw new Error(`GitHub API 응답 오류가 발생했습니다. (${response.status})`);</code> | 설명과 함께 오류를 발생시켜 catch 블록으로 전달합니다. |
| 349 | <code>    }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 350 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 351 | <code>    const repositories = await response.json();</code> | 값 또는 객체 참조를 `repositories`에 저장합니다. |
| 352 | <code>    state.projects.items = repositories.slice(0, 6).map((repository) =&gt; {</code> | 각 배열 항목을 변환해 새 배열을 만듭니다. |
| 353 | <code>      const {</code> | 값 또는 객체 참조를 `변수`에 저장합니다. |
| 354 | <code>        name,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 355 | <code>        description,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 356 | <code>        html_url: htmlUrl,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 357 | <code>        language,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 358 | <code>        stargazers_count: stars,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 359 | <code>        forks_count: forks,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 360 | <code>        updated_at: updatedAt,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 361 | <code>      } = repository;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 362 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 363 | <code>      const safeUrl = typeof htmlUrl === &quot;string&quot; &amp;&amp; htmlUrl.startsWith(&quot;https://github.com/&quot;)</code> | 값 또는 객체 참조를 `safeUrl`에 저장합니다. |
| 364 | <code>        ? htmlUrl</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 365 | <code>        : `https://github.com/${GITHUB_USERNAME}`;</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 366 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 367 | <code>      return {</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 368 | <code>        name,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 369 | <code>        description,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 370 | <code>        htmlUrl: safeUrl,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 371 | <code>        language,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 372 | <code>        stars,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 373 | <code>        forks,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 374 | <code>        updatedAt,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 375 | <code>      };</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 376 | <code>    });</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 377 | <code>    state.projects.status = &quot;success&quot;;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 378 | <code>    state.projects.activeLanguage = &quot;all&quot;;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 379 | <code>  } catch (error) {</code> | 발생한 오류를 받아 사용자 친화적으로 처리합니다. |
| 380 | <code>    state.projects.status = &quot;error&quot;;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 381 | <code>    state.projects.error = error.name === &quot;AbortError&quot;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 382 | <code>      ? &quot;요청 시간이 초과되었습니다. 네트워크 연결을 확인해주세요.&quot;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 383 | <code>      : error.message;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 384 | <code>  } finally {</code> | 성공·실패와 관계없이 마지막 정리 작업을 실행합니다. |
| 385 | <code>    window.clearTimeout(timeoutId);</code> | 등록했던 타이머를 해제합니다. |
| 386 | <code>    renderProjects();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 387 | <code>  }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 388 | <code>}</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 389 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 390 | <code>// 부모 요소에서 클릭을 한 번만 감지하는 이벤트 위임 방식입니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 391 | <code>projectFilters.addEventListener(&quot;click&quot;, (event) =&gt; {</code> | `click` 이벤트가 발생할 때 실행할 함수를 연결합니다. |
| 392 | <code>  const button = event.target.closest(&quot;[data-language]&quot;);</code> | 값 또는 객체 참조를 `button`에 저장합니다. |
| 393 | <code>  if (!button) return;</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 394 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 395 | <code>  state.projects.activeLanguage = button.dataset.language;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 396 | <code>  renderProjects();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 397 | <code>});</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 398 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 399 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 400 | <code>   8. 폼 입력 상태 → 필드별 오류와 성공 메시지 렌더링</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 401 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 402 | <code>// 필드별 검증 규칙을 한 객체에 모아 입력 및 제출 시 동일하게 재사용합니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 403 | <code>const validators = {</code> | 값 또는 객체 참조를 `validators`에 저장합니다. |
| 404 | <code>  name: (value) =&gt; {</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 405 | <code>    if (!value.trim()) return &quot;이름을 입력해주세요.&quot;;</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 406 | <code>    if (value.trim().length &lt; 2) return &quot;이름은 두 글자 이상 입력해주세요.&quot;;</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 407 | <code>    return &quot;&quot;;</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 408 | <code>  },</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 409 | <code>  email: (value) =&gt; {</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 410 | <code>    if (!value.trim()) return &quot;이메일을 입력해주세요.&quot;;</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 411 | <code>    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;</code> | 값 또는 객체 참조를 `emailPattern`에 저장합니다. |
| 412 | <code>    return emailPattern.test(value.trim()) ? &quot;&quot; : &quot;올바른 이메일 형식을 입력해주세요.&quot;;</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 413 | <code>  },</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 414 | <code>  message: (value) =&gt; {</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 415 | <code>    if (!value.trim()) return &quot;메시지를 입력해주세요.&quot;;</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 416 | <code>    if (value.trim().length &lt; 10) return &quot;메시지는 10자 이상 입력해주세요.&quot;;</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 417 | <code>    return &quot;&quot;;</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 418 | <code>  },</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 419 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 420 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 421 | <code>// 검증 결과를 상태에 저장해 화면 렌더링과 데이터 처리를 분리합니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 422 | <code>const validateField = (fieldName) =&gt; {</code> | 재사용할 화살표 함수를 `validateField` 이름으로 선언합니다. |
| 423 | <code>  const error = validators[fieldName](state.form.values[fieldName]);</code> | 값 또는 객체 참조를 `error`에 저장합니다. |
| 424 | <code>  state.form.errors[fieldName] = error;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 425 | <code>  return error;</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 426 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 427 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 428 | <code>// 사용자가 한 번이라도 입력한 필드에만 오류를 표시합니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 429 | <code>const renderFieldValidation = (fieldName) =&gt; {</code> | 재사용할 화살표 함수를 `renderFieldValidation` 이름으로 선언합니다. |
| 430 | <code>  const field = document.querySelector(`#${fieldName}`);</code> | DOM 요소를 찾아 `field`에 저장합니다. |
| 431 | <code>  const errorElement = document.querySelector(`#${fieldName}-error`);</code> | DOM 요소를 찾아 `errorElement`에 저장합니다. |
| 432 | <code>  const shouldShow = state.form.touched.has(fieldName);</code> | 값 또는 객체 참조를 `shouldShow`에 저장합니다. |
| 433 | <code>  const error = shouldShow ? state.form.errors[fieldName] : &quot;&quot;;</code> | 값 또는 객체 참조를 `error`에 저장합니다. |
| 434 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 435 | <code>  field.setAttribute(&quot;aria-invalid&quot;, String(Boolean(error)));</code> | HTML 또는 ARIA 속성 값을 갱신합니다. |
| 436 | <code>  errorElement.textContent = error;</code> | HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. |
| 437 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 438 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 439 | <code>// 전송 중에는 중복 제출을 막고 버튼 문구로 진행 상태를 안내합니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 440 | <code>const renderSubmitState = () =&gt; {</code> | 재사용할 화살표 함수를 `renderSubmitState` 이름으로 선언합니다. |
| 441 | <code>  const isSubmitting = state.form.status === &quot;submitting&quot;;</code> | 값 또는 객체 참조를 `isSubmitting`에 저장합니다. |
| 442 | <code>  submitButton.disabled = isSubmitting;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 443 | <code>  submitButton.textContent = isSubmitting ? &quot;전송 중...&quot; : &quot;메시지 보내기&quot;;</code> | HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. |
| 444 | <code>};</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 445 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 446 | <code>// FormSubmit이 로컬 파일로 오인하지 않도록 현재 HTTP 페이지 주소를 명시합니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 447 | <code>const getCurrentFormUrl = () =&gt; new URL(window.location.pathname, window.location.origin).href;</code> | 재사용할 화살표 함수를 `getCurrentFormUrl` 이름으로 선언합니다. |
| 448 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 449 | <code>formFields.forEach((field) =&gt; {</code> | 각 항목에 같은 작업을 반복합니다. |
| 450 | <code>  field.addEventListener(&quot;input&quot;, (event) =&gt; {</code> | `input` 이벤트가 발생할 때 실행할 함수를 연결합니다. |
| 451 | <code>    const { name, value } = event.target;</code> | 값 또는 객체 참조를 `변수`에 저장합니다. |
| 452 | <code>    state.form.values[name] = value;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 453 | <code>    state.form.touched.add(name);</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 454 | <code>    validateField(name);</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 455 | <code>    renderFieldValidation(name);</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 456 | <code>    formStatus.textContent = &quot;&quot;;</code> | HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. |
| 457 | <code>    formStatus.dataset.status = &quot;&quot;;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 458 | <code>  });</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 459 | <code>});</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 460 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 461 | <code>contactForm.addEventListener(&quot;submit&quot;, async (event) =&gt; {</code> | `submit` 이벤트가 발생할 때 실행할 함수를 연결합니다. |
| 462 | <code>  event.preventDefault();</code> | 브라우저 기본 동작을 막고 JavaScript가 직접 처리합니다. |
| 463 | <code>  if (state.form.status === &quot;submitting&quot;) return;</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 464 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 465 | <code>  const fieldNames = Object.keys(state.form.values);</code> | 값 또는 객체 참조를 `fieldNames`에 저장합니다. |
| 466 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 467 | <code>  fieldNames.forEach((fieldName) =&gt; {</code> | 각 항목에 같은 작업을 반복합니다. |
| 468 | <code>    // 브라우저 자동 완성으로 input 이벤트가 생략된 경우에도 현재 값을 다시 읽습니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 469 | <code>    state.form.values[fieldName] = contactForm.elements[fieldName].value;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 470 | <code>    state.form.touched.add(fieldName);</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 471 | <code>    validateField(fieldName);</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 472 | <code>    renderFieldValidation(fieldName);</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 473 | <code>  });</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 474 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 475 | <code>  const firstInvalidField = fieldNames.find((fieldName) =&gt; state.form.errors[fieldName]);</code> | 재사용할 화살표 함수를 `firstInvalidField` 이름으로 선언합니다. |
| 476 | <code>  if (firstInvalidField) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 477 | <code>    formStatus.textContent = &quot;입력 내용을 다시 확인해주세요.&quot;;</code> | HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. |
| 478 | <code>    formStatus.dataset.status = &quot;error&quot;;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 479 | <code>    document.querySelector(`#${firstInvalidField}`).focus();</code> | 템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. |
| 480 | <code>    return;</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 481 | <code>  }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 482 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 483 | <code>  state.form.status = &quot;submitting&quot;;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 484 | <code>  formStatus.textContent = &quot;&quot;;</code> | HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. |
| 485 | <code>  formStatus.dataset.status = &quot;&quot;;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 486 | <code>  renderSubmitState();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 487 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 488 | <code>  const controller = new AbortController();</code> | 값 또는 객체 참조를 `controller`에 저장합니다. |
| 489 | <code>  const timeoutId = window.setTimeout(() =&gt; controller.abort(), 10000);</code> | 재사용할 화살표 함수를 `timeoutId` 이름으로 선언합니다. |
| 490 | <code>  const payload = Object.fromEntries(new FormData(contactForm).entries());</code> | 값 또는 객체 참조를 `payload`에 저장합니다. |
| 491 | <code>  payload._url = getCurrentFormUrl();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 492 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 493 | <code>  try {</code> | 오류 가능성이 있는 작업을 시도하는 블록입니다. |
| 494 | <code>    const response = await fetch(FORM_ENDPOINT, {</code> | 값 또는 객체 참조를 `response`에 저장합니다. |
| 495 | <code>      method: &quot;POST&quot;,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 496 | <code>      headers: {</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 497 | <code>        Accept: &quot;application/json&quot;,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 498 | <code>        &quot;Content-Type&quot;: &quot;application/json&quot;,</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 499 | <code>      },</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 500 | <code>      body: JSON.stringify(payload),</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 501 | <code>      signal: controller.signal,</code> | 객체 안에서 속성 이름과 값을 정의합니다. |
| 502 | <code>    });</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 503 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 504 | <code>    const result = await response.json().catch(() =&gt; ({}));</code> | 재사용할 화살표 함수를 `result` 이름으로 선언합니다. |
| 505 | <code>    const serviceRejected = result.success === false &#124;&#124; result.success === &quot;false&quot;;</code> | 값 또는 객체 참조를 `serviceRejected`에 저장합니다. |
| 506 | <code>    const serviceMessage = typeof result.message === &quot;string&quot; ? result.message : &quot;&quot;;</code> | 값 또는 객체 참조를 `serviceMessage`에 저장합니다. |
| 507 | <code>    const needsActivation = serviceRejected &amp;&amp; /activat/i.test(serviceMessage);</code> | 값 또는 객체 참조를 `needsActivation`에 저장합니다. |
| 508 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 509 | <code>    // 첫 요청은 전송 실패가 아니라 수신 이메일 소유권 확인 단계입니다.</code> | 코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. |
| 510 | <code>    if (needsActivation) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 511 | <code>      formStatus.textContent = &quot;FormSubmit 활성화 메일을 보냈습니다. Gmail에서 Activate Form을 누른 뒤 다시 전송해주세요.&quot;;</code> | HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. |
| 512 | <code>      formStatus.dataset.status = &quot;pending&quot;;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 513 | <code>      return;</code> | 현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. |
| 514 | <code>    }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 515 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 516 | <code>    if (!response.ok &#124;&#124; serviceRejected) {</code> | 조건이 참일 때만 다음 코드 블록을 실행합니다. |
| 517 | <code>      throw new Error(serviceMessage &#124;&#124; `메일 전송 서비스 응답 오류가 발생했습니다. (${response.status})`);</code> | 설명과 함께 오류를 발생시켜 catch 블록으로 전달합니다. |
| 518 | <code>    }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 519 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 520 | <code>    formStatus.textContent = &quot;메시지를 전송했습니다. 첫 사용이라면 수신함의 FormSubmit 인증 메일을 승인해주세요.&quot;;</code> | HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. |
| 521 | <code>    formStatus.dataset.status = &quot;success&quot;;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 522 | <code>    contactForm.reset();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 523 | <code>    state.form.values = { name: &quot;&quot;, email: &quot;&quot;, message: &quot;&quot; };</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 524 | <code>    state.form.errors = {};</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 525 | <code>    state.form.touched.clear();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 526 | <code>    fieldNames.forEach(renderFieldValidation);</code> | 각 항목에 같은 작업을 반복합니다. |
| 527 | <code>  } catch (error) {</code> | 발생한 오류를 받아 사용자 친화적으로 처리합니다. |
| 528 | <code>    const isLocalFileError = /web server&#124;HTML files/i.test(error.message);</code> | 값 또는 객체 참조를 `isLocalFileError`에 저장합니다. |
| 529 | <code>    const message = error.name === &quot;AbortError&quot;</code> | 값 또는 객체 참조를 `message`에 저장합니다. |
| 530 | <code>      ? &quot;전송 시간이 초과되었습니다. 네트워크 연결을 확인한 뒤 다시 시도해주세요.&quot;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 531 | <code>      : isLocalFileError</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 532 | <code>        ? &quot;HTML 파일을 직접 열지 말고 VS Code Live Server 주소에서 실행해주세요.&quot;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 533 | <code>        : &quot;메시지를 전송하지 못했습니다. 잠시 후 다시 시도하거나 이메일 주소로 직접 연락해주세요.&quot;;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 534 | <code>    console.error(&quot;문의 폼 전송 오류:&quot;, error);</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 535 | <code>    formStatus.textContent = message;</code> | HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. |
| 536 | <code>    formStatus.dataset.status = &quot;error&quot;;</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 537 | <code>  } finally {</code> | 성공·실패와 관계없이 마지막 정리 작업을 실행합니다. |
| 538 | <code>    window.clearTimeout(timeoutId);</code> | 등록했던 타이머를 해제합니다. |
| 539 | <code>    state.form.status = &quot;idle&quot;;</code> | 상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. |
| 540 | <code>    renderSubmitState();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 541 | <code>  }</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 542 | <code>});</code> | 현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. |
| 543 | <em>(빈 줄)</em> | 로직 단위를 구분하는 빈 줄입니다. |
| 544 | <code>/* ================================================================</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 545 | <code>   9. 초기 렌더링</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 546 | <code>   ================================================================ */</code> | 브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. |
| 547 | <code>currentYear.textContent = new Date().getFullYear();</code> | HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. |
| 548 | <code>renderTheme();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 549 | <code>renderMenu();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 550 | <code>renderScrollState();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 551 | <code>renderSubmitState();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 552 | <code>formUrlField.value = getCurrentFormUrl();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |
| 553 | <code>loadProjects();</code> | 앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. |

총 553줄을 설명했습니다.
