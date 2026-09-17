# script.js 줄별 해설

원본 파일: [`js/script.js`](../js/script.js)

> 실행 파일을 건드리지 않는 학습용 줄별 해설입니다. 빈 줄도 포함하며, 원본 수정 후 생성 도구를 다시 실행하면 줄 번호가 갱신됩니다.

| 줄 | 코드 | 설명(클릭하면 관련 홈페이지 섹션으로 이동) |
|---:|---|---|
| 1 | <code>&quot;use strict&quot;;</code> | [실수를 줄이기 위해 엄격 모드로 JavaScript를 실행합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 2 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 3 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 4 | <code>   1. 애플리케이션 설정과 상태</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 5 | <code>   화면에 영향을 주는 값을 한 객체에서 관리해</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 6 | <code>   &quot;이벤트 → 상태 변경 → 렌더링&quot; 흐름을 명확히 합니다.</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 7 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 8 | <code>const GITHUB_USERNAME = &quot;bidulgiya999&quot;;</code> | [값 또는 객체 참조를 `GITHUB_USERNAME`에 저장합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 9 | <code>const GITHUB_API_URL = `https://api.github.com/users/${GITHUB_USERNAME}/repos?sort=updated&amp;per_page=100`;</code> | [값 또는 객체 참조를 `GITHUB_API_URL`에 저장합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 10 | <code>const FORM_ENDPOINT = &quot;https://formsubmit.co/ajax/jae94bro@gmail.com&quot;;</code> | [값 또는 객체 참조를 `FORM_ENDPOINT`에 저장합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 11 | <code>const SCROLL_TOP_THRESHOLD = 300;</code> | [값 또는 객체 참조를 `SCROLL_TOP_THRESHOLD`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 12 | <code>const HEADER_SCROLL_THRESHOLD = 60;</code> | [값 또는 객체 참조를 `HEADER_SCROLL_THRESHOLD`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 13 | <code>const OBSERVER_THRESHOLD = 0.2;</code> | [값 또는 객체 참조를 `OBSERVER_THRESHOLD`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 14 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 15 | <code>// 학습 문서의 링크가 가리킬 수 있는 홈페이지 요소를 허용 목록으로 제한합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 16 | <code>// 예: index.html?focus=hero-visual#hero → Hero 오른쪽 이미지 강조</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: 첫 화면 오른쪽 MRI 히트맵 이미지](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero-visual#hero) |
| 17 | <code>const GUIDE_TARGETS = {</code> | [값 또는 객체 참조를 `GUIDE_TARGETS`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 18 | <code>  header: { selector: &quot;#site-header&quot;, label: &quot;상단 헤더와 내비게이션&quot; },</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: 상단 고정 헤더와 메뉴](https://bidulgiya999.github.io/codyssey_B1-1/?focus=header#hero) |
| 19 | <code>  hero: { selector: &quot;#hero&quot;, label: &quot;첫 화면(Hero) 전체&quot; },</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 20 | <code>  &quot;hero-copy&quot;: { selector: &quot;.hero-copy&quot;, label: &quot;첫 화면 왼쪽 소개 문구&quot; },</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면 왼쪽 소개 문구와 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero-copy#hero) |
| 21 | <code>  &quot;hero-visual&quot;: { selector: &quot;.hero-visual&quot;, label: &quot;첫 화면 오른쪽 MRI 히트맵 이미지&quot; },</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면 오른쪽 MRI 히트맵 이미지](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero-visual#hero) |
| 22 | <code>  about: { selector: &quot;#about&quot;, label: &quot;About 전체 영역&quot; },</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: About 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=about#about) |
| 23 | <code>  profile: { selector: &quot;.profile-frame&quot;, label: &quot;About의 프로필 사진&quot; },</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: About 왼쪽 프로필 사진](https://bidulgiya999.github.io/codyssey_B1-1/?focus=profile#about) |
| 24 | <code>  skills: { selector: &quot;#skills&quot;, label: &quot;Skills 전체 영역&quot; },</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Skills 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=skills#skills) |
| 25 | <code>  &quot;skill-cards&quot;: { selector: &quot;.skills-grid&quot;, label: &quot;기술 스택 카드 모음&quot; },</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 기술 스택 카드 모음](https://bidulgiya999.github.io/codyssey_B1-1/?focus=skill-cards#skills) |
| 26 | <code>  projects: { selector: &quot;#projects&quot;, label: &quot;GitHub Projects 전체 영역&quot; },</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 27 | <code>  &quot;project-filters&quot;: { selector: &quot;#project-filters&quot;, label: &quot;프로젝트 언어 필터&quot; },</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 28 | <code>  &quot;project-cards&quot;: { selector: &quot;#projects-grid&quot;, label: &quot;GitHub 프로젝트 카드 목록&quot; },</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 29 | <code>  contact: { selector: &quot;#contact&quot;, label: &quot;Contact 전체 영역&quot; },</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 30 | <code>  &quot;contact-form&quot;: { selector: &quot;#contact-form&quot;, label: &quot;이름·이메일·메시지 입력 폼&quot; },</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 31 | <code>  footer: { selector: &quot;.site-footer&quot;, label: &quot;페이지 하단 Footer&quot; },</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: 페이지 하단 Footer](https://bidulgiya999.github.io/codyssey_B1-1/?focus=footer#contact) |
| 32 | <code>  &quot;scroll-top&quot;: { selector: &quot;#scroll-top&quot;, label: &quot;맨 위로 이동 버튼&quot; },</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 오른쪽 아래 맨 위로 이동 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=scroll-top#hero) |
| 33 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 34 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 35 | <code>// 브라우저가 저장소 접근을 막더라도 사이트가 중단되지 않도록 안전하게 값을 읽습니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 36 | <code>const getStoredTheme = () =&gt; {</code> | [재사용할 화살표 함수를 `getStoredTheme` 이름으로 선언합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 37 | <code>  try {</code> | [오류 가능성이 있는 작업을 시도하는 블록입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 38 | <code>    return localStorage.getItem(&quot;portfolio-theme&quot;);</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 39 | <code>  } catch {</code> | [발생한 오류를 받아 사용자 친화적으로 처리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 40 | <code>    return null;</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 41 | <code>  }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 42 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 43 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 44 | <code>const systemPrefersDark = window.matchMedia(&quot;(prefers-color-scheme: dark)&quot;).matches;</code> | [값 또는 객체 참조를 `systemPrefersDark`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 45 | <code>const storedTheme = getStoredTheme();</code> | [값 또는 객체 참조를 `storedTheme`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 46 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 47 | <code>const state = {</code> | [값 또는 객체 참조를 `state`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 48 | <code>  theme: storedTheme === &quot;dark&quot; &#124;&#124; storedTheme === &quot;light&quot;</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 49 | <code>    ? storedTheme</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 50 | <code>    : systemPrefersDark</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 51 | <code>      ? &quot;dark&quot;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 52 | <code>      : &quot;light&quot;,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 53 | <code>  menuOpen: false,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 54 | <code>  projects: {</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 55 | <code>    status: &quot;idle&quot;,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 56 | <code>    items: [],</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 57 | <code>    error: &quot;&quot;,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 58 | <code>    activeLanguage: &quot;all&quot;,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 59 | <code>  },</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 60 | <code>  form: {</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 61 | <code>    values: { name: &quot;&quot;, email: &quot;&quot;, message: &quot;&quot; },</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 62 | <code>    errors: {},</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 63 | <code>    touched: new Set(),</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 64 | <code>    status: &quot;idle&quot;,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 65 | <code>  },</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 66 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 67 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 68 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 69 | <code>   2. DOM 선택</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 70 | <code>   querySelector와 querySelectorAll로 필요한 요소를 한 번만 찾습니다.</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 71 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 72 | <code>const siteHeader = document.querySelector(&quot;#site-header&quot;);</code> | [DOM 요소를 찾아 `siteHeader`에 저장합니다. — 위치: 상단 고정 헤더와 메뉴](https://bidulgiya999.github.io/codyssey_B1-1/?focus=header#hero) |
| 73 | <code>const themeToggle = document.querySelector(&quot;#theme-toggle&quot;);</code> | [DOM 요소를 찾아 `themeToggle`에 저장합니다. — 위치: 상단 고정 헤더와 메뉴](https://bidulgiya999.github.io/codyssey_B1-1/?focus=header#hero) |
| 74 | <code>const themeIcon = document.querySelector(&quot;#theme-icon&quot;);</code> | [DOM 요소를 찾아 `themeIcon`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 75 | <code>const themeLabel = document.querySelector(&quot;#theme-label&quot;);</code> | [DOM 요소를 찾아 `themeLabel`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 76 | <code>const menuToggle = document.querySelector(&quot;#menu-toggle&quot;);</code> | [DOM 요소를 찾아 `menuToggle`에 저장합니다. — 위치: 상단 고정 헤더와 메뉴](https://bidulgiya999.github.io/codyssey_B1-1/?focus=header#hero) |
| 77 | <code>const navMenu = document.querySelector(&quot;#nav-menu&quot;);</code> | [DOM 요소를 찾아 `navMenu`에 저장합니다. — 위치: 상단 고정 헤더와 메뉴](https://bidulgiya999.github.io/codyssey_B1-1/?focus=header#hero) |
| 78 | <code>const navLinks = document.querySelectorAll(&#x27;a[href^=&quot;#&quot;]&#x27;);</code> | [DOM 요소를 찾아 `navLinks`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 79 | <code>const scrollTopButton = document.querySelector(&quot;#scroll-top&quot;);</code> | [DOM 요소를 찾아 `scrollTopButton`에 저장합니다. — 위치: 오른쪽 아래 맨 위로 이동 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=scroll-top#hero) |
| 80 | <code>const revealElements = document.querySelectorAll(&quot;.reveal&quot;);</code> | [DOM 요소를 찾아 `revealElements`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 81 | <code>const projectsGrid = document.querySelector(&quot;#projects-grid&quot;);</code> | [DOM 요소를 찾아 `projectsGrid`에 저장합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 82 | <code>const projectFilters = document.querySelector(&quot;#project-filters&quot;);</code> | [DOM 요소를 찾아 `projectFilters`에 저장합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 83 | <code>const contactForm = document.querySelector(&quot;#contact-form&quot;);</code> | [DOM 요소를 찾아 `contactForm`에 저장합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 84 | <code>const formStatus = document.querySelector(&quot;#form-status&quot;);</code> | [DOM 요소를 찾아 `formStatus`에 저장합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 85 | <code>const formUrlField = document.querySelector(&quot;#form-url&quot;);</code> | [DOM 요소를 찾아 `formUrlField`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 86 | <code>const formFields = document.querySelectorAll(&quot;#contact-form [data-validate]&quot;);</code> | [DOM 요소를 찾아 `formFields`에 저장합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 87 | <code>const submitButton = document.querySelector(&quot;.submit-button&quot;);</code> | [DOM 요소를 찾아 `submitButton`에 저장합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 88 | <code>const currentYear = document.querySelector(&quot;#current-year&quot;);</code> | [DOM 요소를 찾아 `currentYear`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 89 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 90 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 91 | <code>   3. 테마 상태 → 문서 렌더링</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 92 | <code>   localStorage에는 기기별 사용자 선택만 저장합니다.</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 93 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 94 | <code>const saveTheme = (theme) =&gt; {</code> | [재사용할 화살표 함수를 `saveTheme` 이름으로 선언합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 95 | <code>  try {</code> | [오류 가능성이 있는 작업을 시도하는 블록입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 96 | <code>    localStorage.setItem(&quot;portfolio-theme&quot;, theme);</code> | [새로고침 후에도 남는 브라우저 저장소를 사용합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 97 | <code>  } catch {</code> | [발생한 오류를 받아 사용자 친화적으로 처리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 98 | <code>    // 저장소가 차단된 환경에서도 테마 전환 자체는 계속 동작합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 99 | <code>  }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 100 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 101 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 102 | <code>// 상태 객체의 테마 값을 실제 화면과 스크린 리더용 설명에 함께 반영합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 103 | <code>const renderTheme = () =&gt; {</code> | [재사용할 화살표 함수를 `renderTheme` 이름으로 선언합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 104 | <code>  const isDark = state.theme === &quot;dark&quot;;</code> | [값 또는 객체 참조를 `isDark`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 105 | <code>  document.documentElement.dataset.theme = state.theme;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 106 | <code>  themeIcon.textContent = isDark ? &quot;☀&quot; : &quot;◐&quot;;</code> | [HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 107 | <code>  themeLabel.textContent = isDark ? &quot;라이트 모드&quot; : &quot;다크 모드&quot;;</code> | [HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 108 | <code>  themeToggle.setAttribute(&quot;aria-label&quot;, isDark ? &quot;라이트 모드로 전환&quot; : &quot;다크 모드로 전환&quot;);</code> | [HTML 또는 ARIA 속성 값을 갱신합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 109 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 110 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 111 | <code>themeToggle.addEventListener(&quot;click&quot;, () =&gt; {</code> | [`click` 이벤트가 발생할 때 실행할 함수를 연결합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 112 | <code>  state.theme = state.theme === &quot;dark&quot; ? &quot;light&quot; : &quot;dark&quot;;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 113 | <code>  saveTheme(state.theme);</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 114 | <code>  renderTheme();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 115 | <code>});</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 116 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 117 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 118 | <code>   4. 모바일 메뉴와 부드러운 스크롤</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 119 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 120 | <code>// 메뉴의 열림 상태를 class와 ARIA 속성에 동시에 반영합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 121 | <code>const renderMenu = () =&gt; {</code> | [재사용할 화살표 함수를 `renderMenu` 이름으로 선언합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 122 | <code>  navMenu.classList.toggle(&quot;active&quot;, state.menuOpen);</code> | [CSS 클래스를 변경해 화면 상태를 바꿉니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 123 | <code>  menuToggle.classList.toggle(&quot;active&quot;, state.menuOpen);</code> | [CSS 클래스를 변경해 화면 상태를 바꿉니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 124 | <code>  document.body.classList.toggle(&quot;menu-open&quot;, state.menuOpen);</code> | [CSS 클래스를 변경해 화면 상태를 바꿉니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 125 | <code>  menuToggle.setAttribute(&quot;aria-expanded&quot;, String(state.menuOpen));</code> | [HTML 또는 ARIA 속성 값을 갱신합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 126 | <code>  menuToggle.setAttribute(&quot;aria-label&quot;, state.menuOpen ? &quot;메뉴 닫기&quot; : &quot;메뉴 열기&quot;);</code> | [HTML 또는 ARIA 속성 값을 갱신합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 127 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 128 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 129 | <code>const closeMenu = () =&gt; {</code> | [재사용할 화살표 함수를 `closeMenu` 이름으로 선언합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 130 | <code>  state.menuOpen = false;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 131 | <code>  navMenu.classList.remove(&quot;active&quot;);</code> | [CSS 클래스를 변경해 화면 상태를 바꿉니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 132 | <code>  menuToggle.classList.remove(&quot;active&quot;);</code> | [CSS 클래스를 변경해 화면 상태를 바꿉니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 133 | <code>  document.body.classList.remove(&quot;menu-open&quot;);</code> | [CSS 클래스를 변경해 화면 상태를 바꿉니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 134 | <code>  menuToggle.setAttribute(&quot;aria-expanded&quot;, &quot;false&quot;);</code> | [HTML 또는 ARIA 속성 값을 갱신합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 135 | <code>  menuToggle.setAttribute(&quot;aria-label&quot;, &quot;메뉴 열기&quot;);</code> | [HTML 또는 ARIA 속성 값을 갱신합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 136 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 137 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 138 | <code>menuToggle.addEventListener(&quot;click&quot;, () =&gt; {</code> | [`click` 이벤트가 발생할 때 실행할 함수를 연결합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 139 | <code>  state.menuOpen = !state.menuOpen;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 140 | <code>  renderMenu();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 141 | <code>});</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 142 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 143 | <code>navLinks.forEach((link) =&gt; {</code> | [각 항목에 같은 작업을 반복합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 144 | <code>  link.addEventListener(&quot;click&quot;, (event) =&gt; {</code> | [`click` 이벤트가 발생할 때 실행할 함수를 연결합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 145 | <code>    const targetId = link.getAttribute(&quot;href&quot;);</code> | [값 또는 객체 참조를 `targetId`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 146 | <code>    const target = document.querySelector(targetId);</code> | [DOM 요소를 찾아 `target`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 147 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 148 | <code>    if (!target) return;</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 149 | <code>    event.preventDefault();</code> | [브라우저 기본 동작을 막고 JavaScript가 직접 처리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 150 | <code>    closeMenu();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 151 | <code>    target.scrollIntoView({ behavior: &quot;smooth&quot;, block: &quot;start&quot; });</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 152 | <code>  });</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 153 | <code>});</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 154 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 155 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 156 | <code>   5. 스크롤 이벤트 → 헤더와 스크롤 탑 버튼 렌더링</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 157 | <code>   requestAnimationFrame으로 과도한 화면 갱신을 줄입니다.</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 158 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 159 | <code>let scrollTicking = false;</code> | [값 또는 객체 참조를 `scrollTicking`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 160 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 161 | <code>// 스크롤 위치에 따라 헤더 강조와 TOP 버튼 노출 여부만 갱신합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 162 | <code>const renderScrollState = () =&gt; {</code> | [재사용할 화살표 함수를 `renderScrollState` 이름으로 선언합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 163 | <code>  const scrollPosition = window.scrollY;</code> | [값 또는 객체 참조를 `scrollPosition`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 164 | <code>  siteHeader.classList.toggle(&quot;scrolled&quot;, scrollPosition &gt;= HEADER_SCROLL_THRESHOLD);</code> | [CSS 클래스를 변경해 화면 상태를 바꿉니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 165 | <code>  scrollTopButton.classList.toggle(&quot;visible&quot;, scrollPosition &gt;= SCROLL_TOP_THRESHOLD);</code> | [CSS 클래스를 변경해 화면 상태를 바꿉니다. — 위치: 오른쪽 아래 맨 위로 이동 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=scroll-top#hero) |
| 166 | <code>  scrollTicking = false;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 167 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 168 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 169 | <code>window.addEventListener(&quot;scroll&quot;, () =&gt; {</code> | [`scroll` 이벤트가 발생할 때 실행할 함수를 연결합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 170 | <code>  if (!scrollTicking) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 171 | <code>    window.requestAnimationFrame(renderScrollState);</code> | [다음 화면 갱신 시점에 작업을 예약합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 172 | <code>    scrollTicking = true;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 173 | <code>  }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 174 | <code>});</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 175 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 176 | <code>// 새로고침할 때 URL에 섹션 주소(#projects 등)가 있어도 버튼 상태를 바로 맞춥니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 177 | <code>renderScrollState();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 178 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 179 | <code>scrollTopButton.addEventListener(&quot;click&quot;, () =&gt; {</code> | [`click` 이벤트가 발생할 때 실행할 함수를 연결합니다. — 위치: 오른쪽 아래 맨 위로 이동 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=scroll-top#hero) |
| 180 | <code>  window.scrollTo({ top: 0, behavior: &quot;smooth&quot; });</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 오른쪽 아래 맨 위로 이동 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=scroll-top#hero) |
| 181 | <code>});</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 182 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 183 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 184 | <code>   6. Intersection Observer 스크롤 애니메이션</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 185 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 186 | <code>const reduceMotion = window.matchMedia(&quot;(prefers-reduced-motion: reduce)&quot;).matches;</code> | [값 또는 객체 참조를 `reduceMotion`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 187 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 188 | <code>if (reduceMotion &#124;&#124; !(&quot;IntersectionObserver&quot; in window)) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 189 | <code>  revealElements.forEach((element) =&gt; element.classList.add(&quot;visible&quot;));</code> | [각 항목에 같은 작업을 반복합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 190 | <code>} else {</code> | [앞 조건이 거짓일 때 실행할 대체 분기입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 191 | <code>  const revealObserver = new IntersectionObserver(</code> | [값 또는 객체 참조를 `revealObserver`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 192 | <code>    (entries, observer) =&gt; {</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 193 | <code>      entries.forEach((entry) =&gt; {</code> | [각 항목에 같은 작업을 반복합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 194 | <code>        if (entry.isIntersecting) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 195 | <code>          entry.target.classList.add(&quot;visible&quot;);</code> | [CSS 클래스를 변경해 화면 상태를 바꿉니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 196 | <code>          observer.unobserve(entry.target);</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 197 | <code>        }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 198 | <code>      });</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 199 | <code>    },</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 200 | <code>    { threshold: OBSERVER_THRESHOLD },</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 201 | <code>  );</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 202 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 203 | <code>  revealElements.forEach((element) =&gt; revealObserver.observe(element));</code> | [각 항목에 같은 작업을 반복합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 204 | <code>}</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 205 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 206 | <code>// 학습 문서에서 넘어온 링크라면 정확한 대상까지 이동한 뒤 잠시 강조합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 207 | <code>const highlightGuideTarget = () =&gt; {</code> | [재사용할 화살표 함수를 `highlightGuideTarget` 이름으로 선언합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 208 | <code>  const targetKey = new URLSearchParams(window.location.search).get(&quot;focus&quot;);</code> | [값 또는 객체 참조를 `targetKey`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 209 | <code>  const targetInfo = GUIDE_TARGETS[targetKey];</code> | [값 또는 객체 참조를 `targetInfo`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 210 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 211 | <code>  if (!targetInfo) return;</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 212 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 213 | <code>  const target = document.querySelector(targetInfo.selector);</code> | [DOM 요소를 찾아 `target`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 214 | <code>  if (!target) return;</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 215 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 216 | <code>  const wasVisible = target.classList.contains(&quot;visible&quot;);</code> | [값 또는 객체 참조를 `wasVisible`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 217 | <code>  const needsPositioning = window.getComputedStyle(target).position === &quot;static&quot;;</code> | [값 또는 객체 참조를 `needsPositioning`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 218 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 219 | <code>  if (needsPositioning) target.classList.add(&quot;guide-highlight-positioned&quot;);</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 220 | <code>  if (targetKey === &quot;scroll-top&quot;) target.classList.add(&quot;visible&quot;);</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: 오른쪽 아래 맨 위로 이동 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=scroll-top#hero) |
| 221 | <code>  target.classList.add(&quot;guide-highlight&quot;);</code> | [CSS 클래스를 변경해 화면 상태를 바꿉니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 222 | <code>  target.dataset.guideHighlight = `학습 가이드 위치 · ${targetInfo.label}`;</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 223 | <code>  target.scrollIntoView({ behavior: reduceMotion ? &quot;auto&quot; : &quot;smooth&quot;, block: &quot;center&quot; });</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 224 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 225 | <code>  window.setTimeout(() =&gt; {</code> | [일정 시간이 지난 후 실행할 타이머를 등록합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 226 | <code>    target.classList.remove(&quot;guide-highlight&quot;);</code> | [CSS 클래스를 변경해 화면 상태를 바꿉니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 227 | <code>    target.classList.remove(&quot;guide-highlight-positioned&quot;);</code> | [CSS 클래스를 변경해 화면 상태를 바꿉니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 228 | <code>    if (targetKey === &quot;scroll-top&quot; &amp;&amp; !wasVisible) target.classList.remove(&quot;visible&quot;);</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: 오른쪽 아래 맨 위로 이동 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=scroll-top#hero) |
| 229 | <code>    delete target.dataset.guideHighlight;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 230 | <code>  }, 5000);</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 231 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 232 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 233 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 234 | <code>   7. GitHub API 상태 → Projects UI 렌더링</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 235 | <code>   외부 문자열은 innerHTML에 넣기 전에 escapeHtml로 이스케이프합니다.</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 236 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 237 | <code>// GitHub에서 받은 문자열이 HTML로 해석되지 않도록 특수문자를 치환합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 238 | <code>const escapeHtml = (value) =&gt; String(value)</code> | [재사용할 화살표 함수를 `escapeHtml` 이름으로 선언합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 239 | <code>  .replaceAll(&quot;&amp;&quot;, &quot;&amp;amp;&quot;)</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 240 | <code>  .replaceAll(&quot;&lt;&quot;, &quot;&amp;lt;&quot;)</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 241 | <code>  .replaceAll(&quot;&gt;&quot;, &quot;&amp;gt;&quot;)</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 242 | <code>  .replaceAll(&#x27;&quot;&#x27;, &quot;&amp;quot;&quot;)</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 243 | <code>  .replaceAll(&quot;&#x27;&quot;, &quot;&amp;#039;&quot;);</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 244 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 245 | <code>const formatDate = (dateString) =&gt; new Intl.DateTimeFormat(&quot;ko-KR&quot;, {</code> | [재사용할 화살표 함수를 `formatDate` 이름으로 선언합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 246 | <code>  year: &quot;numeric&quot;,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 247 | <code>  month: &quot;short&quot;,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 248 | <code>  day: &quot;numeric&quot;,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 249 | <code>}).format(new Date(dateString));</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 250 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 251 | <code>// 저장소의 대표 언어를 중복 없이 모아 동적 필터 버튼을 만듭니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 252 | <code>const renderProjectFilters = () =&gt; {</code> | [재사용할 화살표 함수를 `renderProjectFilters` 이름으로 선언합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 253 | <code>  const languages = [...new Set(</code> | [값 또는 객체 참조를 `languages`에 저장합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 254 | <code>    state.projects.items</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 255 | <code>      .map(({ language }) =&gt; language)</code> | [각 배열 항목을 변환해 새 배열을 만듭니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 256 | <code>      .filter(Boolean),</code> | [조건을 통과한 항목만 새 배열로 모읍니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 257 | <code>  )].sort((first, second) =&gt; first.localeCompare(second));</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 258 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 259 | <code>  projectFilters.hidden = languages.length === 0;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 260 | <code>  if (languages.length === 0) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 261 | <code>    projectFilters.innerHTML = &quot;&quot;;</code> | [문자열로 만든 HTML 구조를 화면에 렌더링합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 262 | <code>    return;</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 263 | <code>  }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 264 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 265 | <code>  const filterNames = [&quot;all&quot;, ...languages];</code> | [값 또는 객체 참조를 `filterNames`에 저장합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 266 | <code>  projectFilters.innerHTML = filterNames.map((language) =&gt; {</code> | [각 배열 항목을 변환해 새 배열을 만듭니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 267 | <code>    const isActive = state.projects.activeLanguage === language;</code> | [값 또는 객체 참조를 `isActive`에 저장합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 268 | <code>    const label = language === &quot;all&quot; ? &quot;전체&quot; : escapeHtml(language);</code> | [값 또는 객체 참조를 `label`에 저장합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 269 | <code>    return `</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 270 | <code>      &lt;button</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 271 | <code>        class=&quot;filter-button${isActive ? &quot; active&quot; : &quot;&quot;}&quot;</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 272 | <code>        type=&quot;button&quot;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 273 | <code>        data-language=&quot;${escapeHtml(language)}&quot;</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 274 | <code>        aria-pressed=&quot;${isActive}&quot;</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 275 | <code>      &gt;${label}&lt;/button&gt;</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 276 | <code>    `;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 277 | <code>  }).join(&quot;&quot;);</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 278 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 279 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 280 | <code>// API 응답 한 건을 화면에 표시할 프로젝트 카드 HTML로 변환합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 281 | <code>const createProjectCard = (project) =&gt; {</code> | [재사용할 화살표 함수를 `createProjectCard` 이름으로 선언합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 282 | <code>  const {</code> | [값 또는 객체 참조를 `변수`에 저장합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 283 | <code>    name,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 284 | <code>    description,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 285 | <code>    htmlUrl,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 286 | <code>    language,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 287 | <code>    stars,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 288 | <code>    forks,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 289 | <code>    updatedAt,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 290 | <code>  } = project;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 291 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 292 | <code>  return `</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 293 | <code>    &lt;article class=&quot;project-card&quot;&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 294 | <code>      &lt;div class=&quot;project-card-header&quot;&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 295 | <code>        &lt;h3&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 296 | <code>          &lt;a class=&quot;repo-link&quot; href=&quot;${htmlUrl}&quot; target=&quot;_blank&quot; rel=&quot;noopener noreferrer&quot;&gt;</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 297 | <code>            ${escapeHtml(name)}</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 298 | <code>          &lt;/a&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 299 | <code>        &lt;/h3&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 300 | <code>        &lt;span aria-hidden=&quot;true&quot;&gt;↗&lt;/span&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 301 | <code>      &lt;/div&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 302 | <code>      &lt;p class=&quot;project-description&quot;&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 303 | <code>        ${escapeHtml(description &#124;&#124; &quot;프로젝트 설명이 아직 없습니다.&quot;)}</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 304 | <code>      &lt;/p&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 305 | <code>      &lt;div class=&quot;project-meta&quot; aria-label=&quot;저장소 정보&quot;&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 306 | <code>        &lt;span&gt;&lt;i class=&quot;language-dot&quot; aria-hidden=&quot;true&quot;&gt;&lt;/i&gt;${escapeHtml(language &#124;&#124; &quot;기타&quot;)}&lt;/span&gt;</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 307 | <code>        &lt;span&gt;★ ${stars}&lt;/span&gt;</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 308 | <code>        &lt;span&gt;⑂ ${forks}&lt;/span&gt;</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 309 | <code>        &lt;span&gt;업데이트 ${escapeHtml(formatDate(updatedAt))}&lt;/span&gt;</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 310 | <code>      &lt;/div&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 311 | <code>    &lt;/article&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 312 | <code>  `;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 313 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 314 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 315 | <code>// loading/error/empty/success 상태마다 서로 다른 화면을 그립니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 316 | <code>const renderProjects = () =&gt; {</code> | [재사용할 화살표 함수를 `renderProjects` 이름으로 선언합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 317 | <code>  const { status, items, error, activeLanguage } = state.projects;</code> | [값 또는 객체 참조를 `변수`에 저장합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 318 | <code>  projectsGrid.setAttribute(&quot;aria-busy&quot;, String(status === &quot;loading&quot;));</code> | [HTML 또는 ARIA 속성 값을 갱신합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 319 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 320 | <code>  if (status === &quot;loading&quot;) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 321 | <code>    projectFilters.hidden = true;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 322 | <code>    projectsGrid.innerHTML = `</code> | [문자열로 만든 HTML 구조를 화면에 렌더링합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 323 | <code>      &lt;div class=&quot;project-state&quot;&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 324 | <code>        &lt;span class=&quot;spinner&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 325 | <code>        &lt;p&gt;프로젝트를 불러오는 중입니다.&lt;/p&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 326 | <code>      &lt;/div&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 327 | <code>    `;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 328 | <code>    return;</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 329 | <code>  }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 330 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 331 | <code>  if (status === &quot;error&quot;) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 332 | <code>    projectFilters.hidden = true;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 333 | <code>    projectsGrid.innerHTML = `</code> | [문자열로 만든 HTML 구조를 화면에 렌더링합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 334 | <code>      &lt;div class=&quot;project-state&quot;&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 335 | <code>        &lt;strong&gt;프로젝트를 불러올 수 없습니다.&lt;/strong&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 336 | <code>        &lt;p&gt;${escapeHtml(error)}&lt;/p&gt;</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 337 | <code>        &lt;button class=&quot;button button-primary&quot; id=&quot;retry-projects&quot; type=&quot;button&quot;&gt;다시 시도&lt;/button&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 338 | <code>      &lt;/div&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 339 | <code>    `;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 340 | <code>    document.querySelector(&quot;#retry-projects&quot;).addEventListener(&quot;click&quot;, loadProjects);</code> | [`click` 이벤트가 발생할 때 실행할 함수를 연결합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 341 | <code>    return;</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 342 | <code>  }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 343 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 344 | <code>  if (status === &quot;success&quot; &amp;&amp; items.length === 0) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 345 | <code>    projectFilters.hidden = true;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 346 | <code>    projectsGrid.innerHTML = `</code> | [문자열로 만든 HTML 구조를 화면에 렌더링합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 347 | <code>      &lt;div class=&quot;project-state&quot;&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 348 | <code>        &lt;strong&gt;표시할 프로젝트가 없습니다.&lt;/strong&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 349 | <code>        &lt;p&gt;공개 저장소가 생성되면 이곳에 자동으로 표시됩니다.&lt;/p&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 350 | <code>      &lt;/div&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 351 | <code>    `;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 352 | <code>    return;</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 353 | <code>  }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 354 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 355 | <code>  renderProjectFilters();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 356 | <code>  const filteredProjects = activeLanguage === &quot;all&quot;</code> | [값 또는 객체 참조를 `filteredProjects`에 저장합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 357 | <code>    ? items</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 358 | <code>    : items.filter(({ language }) =&gt; language === activeLanguage);</code> | [조건을 통과한 항목만 새 배열로 모읍니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 359 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 360 | <code>  if (filteredProjects.length === 0) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 361 | <code>    projectsGrid.innerHTML = `</code> | [문자열로 만든 HTML 구조를 화면에 렌더링합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 362 | <code>      &lt;div class=&quot;project-state&quot;&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 363 | <code>        &lt;strong&gt;이 언어로 만든 프로젝트가 없습니다.&lt;/strong&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 364 | <code>        &lt;p&gt;다른 필터를 선택해주세요.&lt;/p&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 365 | <code>      &lt;/div&gt;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 366 | <code>    `;</code> | [템플릿 리터럴로 동적 HTML 일부를 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 367 | <code>    return;</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 368 | <code>  }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 369 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 370 | <code>  projectsGrid.innerHTML = filteredProjects.map(createProjectCard).join(&quot;&quot;);</code> | [각 배열 항목을 변환해 새 배열을 만듭니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 371 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 372 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 373 | <code>// 요청이 10초를 넘으면 중단하고, 필요한 값만 화면용 객체로 정리합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 374 | <code>async function loadProjects() {</code> | [`await`를 사용할 수 있는 비동기 함수를 선언합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 375 | <code>  state.projects.status = &quot;loading&quot;;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 376 | <code>  state.projects.error = &quot;&quot;;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 377 | <code>  renderProjects();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 378 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 379 | <code>  const controller = new AbortController();</code> | [값 또는 객체 참조를 `controller`에 저장합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 380 | <code>  const timeoutId = window.setTimeout(() =&gt; controller.abort(), 10000);</code> | [재사용할 화살표 함수를 `timeoutId` 이름으로 선언합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 381 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 382 | <code>  try {</code> | [오류 가능성이 있는 작업을 시도하는 블록입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 383 | <code>    const response = await fetch(GITHUB_API_URL, {</code> | [값 또는 객체 참조를 `response`에 저장합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 384 | <code>      headers: { Accept: &quot;application/vnd.github+json&quot; },</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 385 | <code>      signal: controller.signal,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 386 | <code>    });</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 387 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 388 | <code>    if (!response.ok) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 389 | <code>      if (response.status === 403) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 390 | <code>        throw new Error(&quot;GitHub API 요청 한도에 도달했습니다. 잠시 후 다시 시도해주세요.&quot;);</code> | [설명과 함께 오류를 발생시켜 catch 블록으로 전달합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 391 | <code>      }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 392 | <code>      if (response.status === 404) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 393 | <code>        throw new Error(&quot;GitHub 사용자를 찾을 수 없습니다.&quot;);</code> | [설명과 함께 오류를 발생시켜 catch 블록으로 전달합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 394 | <code>      }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 395 | <code>      throw new Error(`GitHub API 응답 오류가 발생했습니다. (${response.status})`);</code> | [설명과 함께 오류를 발생시켜 catch 블록으로 전달합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 396 | <code>    }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 397 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 398 | <code>    const repositories = await response.json();</code> | [값 또는 객체 참조를 `repositories`에 저장합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 399 | <code>    state.projects.items = repositories.slice(0, 6).map((repository) =&gt; {</code> | [각 배열 항목을 변환해 새 배열을 만듭니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 400 | <code>      const {</code> | [값 또는 객체 참조를 `변수`에 저장합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 401 | <code>        name,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 402 | <code>        description,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 403 | <code>        html_url: htmlUrl,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 404 | <code>        language,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 405 | <code>        stargazers_count: stars,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 406 | <code>        forks_count: forks,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 407 | <code>        updated_at: updatedAt,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 408 | <code>      } = repository;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 409 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 410 | <code>      const safeUrl = typeof htmlUrl === &quot;string&quot; &amp;&amp; htmlUrl.startsWith(&quot;https://github.com/&quot;)</code> | [값 또는 객체 참조를 `safeUrl`에 저장합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 411 | <code>        ? htmlUrl</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 412 | <code>        : `https://github.com/${GITHUB_USERNAME}`;</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 413 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 414 | <code>      return {</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 415 | <code>        name,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 416 | <code>        description,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 417 | <code>        htmlUrl: safeUrl,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 418 | <code>        language,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 419 | <code>        stars,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 420 | <code>        forks,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 421 | <code>        updatedAt,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 422 | <code>      };</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 423 | <code>    });</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 424 | <code>    state.projects.status = &quot;success&quot;;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 425 | <code>    state.projects.activeLanguage = &quot;all&quot;;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 426 | <code>  } catch (error) {</code> | [발생한 오류를 받아 사용자 친화적으로 처리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 427 | <code>    state.projects.status = &quot;error&quot;;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 428 | <code>    state.projects.error = error.name === &quot;AbortError&quot;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 429 | <code>      ? &quot;요청 시간이 초과되었습니다. 네트워크 연결을 확인해주세요.&quot;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 430 | <code>      : error.message;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 431 | <code>  } finally {</code> | [성공·실패와 관계없이 마지막 정리 작업을 실행합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 432 | <code>    window.clearTimeout(timeoutId);</code> | [등록했던 타이머를 해제합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 433 | <code>    renderProjects();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 434 | <code>  }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 435 | <code>}</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 436 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 437 | <code>// 부모 요소에서 클릭을 한 번만 감지하는 이벤트 위임 방식입니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 438 | <code>projectFilters.addEventListener(&quot;click&quot;, (event) =&gt; {</code> | [`click` 이벤트가 발생할 때 실행할 함수를 연결합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 439 | <code>  const button = event.target.closest(&quot;[data-language]&quot;);</code> | [값 또는 객체 참조를 `button`에 저장합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 440 | <code>  if (!button) return;</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 441 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 442 | <code>  state.projects.activeLanguage = button.dataset.language;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: 프로젝트 언어 필터 버튼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-filters#projects) |
| 443 | <code>  renderProjects();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 444 | <code>});</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 445 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 446 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 447 | <code>   8. 폼 입력 상태 → 필드별 오류와 성공 메시지 렌더링</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 448 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 449 | <code>// 필드별 검증 규칙을 한 객체에 모아 입력 및 제출 시 동일하게 재사용합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |
| 450 | <code>const validators = {</code> | [값 또는 객체 참조를 `validators`에 저장합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 451 | <code>  name: (value) =&gt; {</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 452 | <code>    if (!value.trim()) return &quot;이름을 입력해주세요.&quot;;</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 453 | <code>    if (value.trim().length &lt; 2) return &quot;이름은 두 글자 이상 입력해주세요.&quot;;</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 454 | <code>    return &quot;&quot;;</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 455 | <code>  },</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 456 | <code>  email: (value) =&gt; {</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 457 | <code>    if (!value.trim()) return &quot;이메일을 입력해주세요.&quot;;</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 458 | <code>    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;</code> | [값 또는 객체 참조를 `emailPattern`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 459 | <code>    return emailPattern.test(value.trim()) ? &quot;&quot; : &quot;올바른 이메일 형식을 입력해주세요.&quot;;</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 460 | <code>  },</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 461 | <code>  message: (value) =&gt; {</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 462 | <code>    if (!value.trim()) return &quot;메시지를 입력해주세요.&quot;;</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 463 | <code>    if (value.trim().length &lt; 10) return &quot;메시지는 10자 이상 입력해주세요.&quot;;</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 464 | <code>    return &quot;&quot;;</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 465 | <code>  },</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 466 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 467 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 468 | <code>// 검증 결과를 상태에 저장해 화면 렌더링과 데이터 처리를 분리합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 469 | <code>const validateField = (fieldName) =&gt; {</code> | [재사용할 화살표 함수를 `validateField` 이름으로 선언합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 470 | <code>  const error = validators[fieldName](state.form.values[fieldName]);</code> | [값 또는 객체 참조를 `error`에 저장합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 471 | <code>  state.form.errors[fieldName] = error;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 472 | <code>  return error;</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 473 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 474 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 475 | <code>// 사용자가 한 번이라도 입력한 필드에만 오류를 표시합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 476 | <code>const renderFieldValidation = (fieldName) =&gt; {</code> | [재사용할 화살표 함수를 `renderFieldValidation` 이름으로 선언합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 477 | <code>  const field = document.querySelector(`#${fieldName}`);</code> | [DOM 요소를 찾아 `field`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 478 | <code>  const errorElement = document.querySelector(`#${fieldName}-error`);</code> | [DOM 요소를 찾아 `errorElement`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 479 | <code>  const shouldShow = state.form.touched.has(fieldName);</code> | [값 또는 객체 참조를 `shouldShow`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 480 | <code>  const error = shouldShow ? state.form.errors[fieldName] : &quot;&quot;;</code> | [값 또는 객체 참조를 `error`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 481 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 482 | <code>  field.setAttribute(&quot;aria-invalid&quot;, String(Boolean(error)));</code> | [HTML 또는 ARIA 속성 값을 갱신합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 483 | <code>  errorElement.textContent = error;</code> | [HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 484 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 485 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 486 | <code>// 전송 중에는 중복 제출을 막고 버튼 문구로 진행 상태를 안내합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 487 | <code>const renderSubmitState = () =&gt; {</code> | [재사용할 화살표 함수를 `renderSubmitState` 이름으로 선언합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 488 | <code>  const isSubmitting = state.form.status === &quot;submitting&quot;;</code> | [값 또는 객체 참조를 `isSubmitting`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 489 | <code>  submitButton.disabled = isSubmitting;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 490 | <code>  submitButton.textContent = isSubmitting ? &quot;전송 중...&quot; : &quot;메시지 보내기&quot;;</code> | [HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 491 | <code>};</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 492 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 493 | <code>// FormSubmit이 로컬 파일로 오인하지 않도록 현재 HTTP 페이지 주소를 명시합니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 494 | <code>const getCurrentFormUrl = () =&gt; new URL(window.location.pathname, window.location.origin).href;</code> | [재사용할 화살표 함수를 `getCurrentFormUrl` 이름으로 선언합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 495 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 496 | <code>formFields.forEach((field) =&gt; {</code> | [각 항목에 같은 작업을 반복합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 497 | <code>  field.addEventListener(&quot;input&quot;, (event) =&gt; {</code> | [`input` 이벤트가 발생할 때 실행할 함수를 연결합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 498 | <code>    const { name, value } = event.target;</code> | [값 또는 객체 참조를 `변수`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 499 | <code>    state.form.values[name] = value;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 500 | <code>    state.form.touched.add(name);</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 501 | <code>    validateField(name);</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 502 | <code>    renderFieldValidation(name);</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 503 | <code>    formStatus.textContent = &quot;&quot;;</code> | [HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 504 | <code>    formStatus.dataset.status = &quot;&quot;;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 505 | <code>  });</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 506 | <code>});</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 507 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 508 | <code>contactForm.addEventListener(&quot;submit&quot;, async (event) =&gt; {</code> | [`submit` 이벤트가 발생할 때 실행할 함수를 연결합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 509 | <code>  event.preventDefault();</code> | [브라우저 기본 동작을 막고 JavaScript가 직접 처리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 510 | <code>  if (state.form.status === &quot;submitting&quot;) return;</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 511 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 512 | <code>  const fieldNames = Object.keys(state.form.values);</code> | [값 또는 객체 참조를 `fieldNames`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 513 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 514 | <code>  fieldNames.forEach((fieldName) =&gt; {</code> | [각 항목에 같은 작업을 반복합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 515 | <code>    // 브라우저 자동 완성으로 input 이벤트가 생략된 경우에도 현재 값을 다시 읽습니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 516 | <code>    state.form.values[fieldName] = contactForm.elements[fieldName].value;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 517 | <code>    state.form.touched.add(fieldName);</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 518 | <code>    validateField(fieldName);</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 519 | <code>    renderFieldValidation(fieldName);</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 520 | <code>  });</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 521 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 522 | <code>  const firstInvalidField = fieldNames.find((fieldName) =&gt; state.form.errors[fieldName]);</code> | [재사용할 화살표 함수를 `firstInvalidField` 이름으로 선언합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 523 | <code>  if (firstInvalidField) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 524 | <code>    formStatus.textContent = &quot;입력 내용을 다시 확인해주세요.&quot;;</code> | [HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 525 | <code>    formStatus.dataset.status = &quot;error&quot;;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 526 | <code>    document.querySelector(`#${firstInvalidField}`).focus();</code> | [템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 527 | <code>    return;</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 528 | <code>  }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 529 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 530 | <code>  state.form.status = &quot;submitting&quot;;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 531 | <code>  formStatus.textContent = &quot;&quot;;</code> | [HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 532 | <code>  formStatus.dataset.status = &quot;&quot;;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 533 | <code>  renderSubmitState();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 534 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 535 | <code>  const controller = new AbortController();</code> | [값 또는 객체 참조를 `controller`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 536 | <code>  const timeoutId = window.setTimeout(() =&gt; controller.abort(), 10000);</code> | [재사용할 화살표 함수를 `timeoutId` 이름으로 선언합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 537 | <code>  const payload = Object.fromEntries(new FormData(contactForm).entries());</code> | [값 또는 객체 참조를 `payload`에 저장합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 538 | <code>  payload._url = getCurrentFormUrl();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 539 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 540 | <code>  try {</code> | [오류 가능성이 있는 작업을 시도하는 블록입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 541 | <code>    const response = await fetch(FORM_ENDPOINT, {</code> | [값 또는 객체 참조를 `response`에 저장합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 542 | <code>      method: &quot;POST&quot;,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 543 | <code>      headers: {</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 544 | <code>        Accept: &quot;application/json&quot;,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 545 | <code>        &quot;Content-Type&quot;: &quot;application/json&quot;,</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 546 | <code>      },</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 547 | <code>      body: JSON.stringify(payload),</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 548 | <code>      signal: controller.signal,</code> | [객체 안에서 속성 이름과 값을 정의합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 549 | <code>    });</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 550 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 551 | <code>    const result = await response.json().catch(() =&gt; ({}));</code> | [재사용할 화살표 함수를 `result` 이름으로 선언합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 552 | <code>    const serviceRejected = result.success === false &#124;&#124; result.success === &quot;false&quot;;</code> | [값 또는 객체 참조를 `serviceRejected`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 553 | <code>    const serviceMessage = typeof result.message === &quot;string&quot; ? result.message : &quot;&quot;;</code> | [값 또는 객체 참조를 `serviceMessage`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 554 | <code>    const needsActivation = serviceRejected &amp;&amp; /activat/i.test(serviceMessage);</code> | [값 또는 객체 참조를 `needsActivation`에 저장합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 555 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 556 | <code>    // 첫 요청은 전송 실패가 아니라 수신 이메일 소유권 확인 단계입니다.</code> | [코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 557 | <code>    if (needsActivation) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 558 | <code>      formStatus.textContent = &quot;FormSubmit 활성화 메일을 보냈습니다. Gmail에서 Activate Form을 누른 뒤 다시 전송해주세요.&quot;;</code> | [HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 559 | <code>      formStatus.dataset.status = &quot;pending&quot;;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 560 | <code>      return;</code> | [현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 561 | <code>    }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 562 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 563 | <code>    if (!response.ok &#124;&#124; serviceRejected) {</code> | [조건이 참일 때만 다음 코드 블록을 실행합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 564 | <code>      throw new Error(serviceMessage &#124;&#124; `메일 전송 서비스 응답 오류가 발생했습니다. (${response.status})`);</code> | [설명과 함께 오류를 발생시켜 catch 블록으로 전달합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 565 | <code>    }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 566 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 567 | <code>    formStatus.textContent = &quot;메시지를 전송했습니다. 첫 사용이라면 수신함의 FormSubmit 인증 메일을 승인해주세요.&quot;;</code> | [HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 568 | <code>    formStatus.dataset.status = &quot;success&quot;;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 569 | <code>    contactForm.reset();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 이름·이메일·메시지 입력 폼](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact-form#contact) |
| 570 | <code>    state.form.values = { name: &quot;&quot;, email: &quot;&quot;, message: &quot;&quot; };</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 571 | <code>    state.form.errors = {};</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 572 | <code>    state.form.touched.clear();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 573 | <code>    fieldNames.forEach(renderFieldValidation);</code> | [각 항목에 같은 작업을 반복합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 574 | <code>  } catch (error) {</code> | [발생한 오류를 받아 사용자 친화적으로 처리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 575 | <code>    const isLocalFileError = /web server&#124;HTML files/i.test(error.message);</code> | [값 또는 객체 참조를 `isLocalFileError`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 576 | <code>    const message = error.name === &quot;AbortError&quot;</code> | [값 또는 객체 참조를 `message`에 저장합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 577 | <code>      ? &quot;전송 시간이 초과되었습니다. 네트워크 연결을 확인한 뒤 다시 시도해주세요.&quot;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 578 | <code>      : isLocalFileError</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 579 | <code>        ? &quot;HTML 파일을 직접 열지 말고 VS Code Live Server 주소에서 실행해주세요.&quot;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 580 | <code>        : &quot;메시지를 전송하지 못했습니다. 잠시 후 다시 시도하거나 이메일 주소로 직접 연락해주세요.&quot;;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 581 | <code>    console.error(&quot;문의 폼 전송 오류:&quot;, error);</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 582 | <code>    formStatus.textContent = message;</code> | [HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 583 | <code>    formStatus.dataset.status = &quot;error&quot;;</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 584 | <code>  } finally {</code> | [성공·실패와 관계없이 마지막 정리 작업을 실행합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 585 | <code>    window.clearTimeout(timeoutId);</code> | [등록했던 타이머를 해제합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 586 | <code>    state.form.status = &quot;idle&quot;;</code> | [상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 587 | <code>    renderSubmitState();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 588 | <code>  }</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 589 | <code>});</code> | [현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 590 | <em>(빈 줄)</em> | [로직 단위를 구분하는 빈 줄입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 591 | <code>/* ================================================================</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 592 | <code>   9. 초기 렌더링</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 593 | <code>   ================================================================ */</code> | [브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 594 | <code>currentYear.textContent = new Date().getFullYear();</code> | [HTML로 해석되지 않는 텍스트를 안전하게 변경합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 595 | <code>renderTheme();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 596 | <code>renderMenu();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 597 | <code>renderScrollState();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: 첫 화면(Hero) 전체](https://bidulgiya999.github.io/codyssey_B1-1/?focus=hero#hero) |
| 598 | <code>renderSubmitState();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 599 | <code>formUrlField.value = getCurrentFormUrl();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: Contact 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=contact#contact) |
| 600 | <code>loadProjects();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub 프로젝트 카드 목록](https://bidulgiya999.github.io/codyssey_B1-1/?focus=project-cards#projects) |
| 601 | <code>highlightGuideTarget();</code> | [앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다. — 위치: GitHub Projects 전체 영역](https://bidulgiya999.github.io/codyssey_B1-1/?focus=projects#projects) |

총 601줄을 설명했습니다.
