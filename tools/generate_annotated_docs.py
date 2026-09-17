"""원본 실행 파일을 유지하면서 줄 번호별 한국어 해설 문서를 생성합니다."""

from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LIVE_SITE = "https://bidulgiya999.github.io/codyssey_B1-1/"

CSS_VARIABLES = {
    "--color-bg": ("페이지 전체의 가장 바깥 배경색", "hero"),
    "--color-surface": ("카드·폼처럼 배경 위에 올라오는 표면색", "contact"),
    "--color-surface-muted": ("About처럼 구역을 은은하게 구분하는 배경색", "about"),
    "--color-text": ("일반 제목과 본문에 사용하는 기본 글자색", "hero"),
    "--color-text-muted": ("설명·보조 문구에 사용하는 약한 글자색", "about"),
    "--color-line": ("카드와 입력칸 경계선 색상", "contact"),
    "--color-accent": ("버튼·링크·강조선에 사용하는 대표 강조색", "hero"),
    "--color-accent-strong": ("강조 요소의 hover 상태에 사용하는 진한 색", "hero"),
    "--color-highlight": ("비전 프레임과 번호에 사용하는 보조 강조색", "hero"),
    "--color-dark": ("Projects와 Footer의 가장 어두운 배경색", "projects"),
    "--color-dark-muted": ("어두운 영역의 카드에 사용하는 한 단계 밝은 배경색", "projects"),
    "--color-on-dark": ("어두운 배경 위에서 읽히는 밝은 글자색", "projects"),
    "--color-error": ("폼 입력 오류와 실패 메시지 색상", "contact"),
    "--color-success": ("폼 전송 성공 메시지 색상", "contact"),
    "--font-sans": ("본문과 제목에 사용하는 고딕 계열 글꼴 묶음", "hero"),
    "--font-mono": ("라벨·번호에 사용하는 고정폭 글꼴 묶음", "skills"),
    "--space-1": ("가장 작은 0.5rem 간격 단위", "skills"),
    "--space-2": ("기본 1rem 간격 단위", "skills"),
    "--space-3": ("중간 1.5rem 간격 단위", "skills"),
    "--space-4": ("큰 2rem 간격 단위", "skills"),
    "--space-5": ("섹션 내부용 3rem 간격 단위", "about"),
    "--space-6": ("섹션 사이용 5rem 간격 단위", "about"),
    "--radius-sm": ("버튼 등에 사용하는 작은 모서리 둥글기", "hero"),
    "--radius-md": ("카드에 사용하는 중간 모서리 둥글기", "skills"),
    "--radius-lg": ("큰 카드와 폼에 사용하는 큰 모서리 둥글기", "contact"),
    "--shadow-card": ("카드가 배경에서 떠 보이게 하는 공통 그림자", "skills"),
    "--header-height": ("고정 헤더 높이와 앵커 여백 계산에 쓰는 값", "hero"),
    "--transition": ("hover·테마 변화에 사용하는 공통 전환 시간과 속도", "hero"),
}

# 같은 섹션 안에서도 실제로 강조할 대표 요소를 변수별로 지정합니다.
CSS_VARIABLE_TARGETS = {
    "--color-bg": "hero",
    "--color-surface": "contact-form",
    "--color-surface-muted": "about",
    "--color-text": "hero-copy",
    "--color-text-muted": "hero-copy",
    "--color-line": "contact-form",
    "--color-accent": "hero-copy",
    "--color-accent-strong": "hero-copy",
    "--color-highlight": "hero-visual",
    "--color-dark": "projects",
    "--color-dark-muted": "project-cards",
    "--color-on-dark": "project-cards",
    "--color-error": "contact-form",
    "--color-success": "contact-form",
    "--font-sans": "hero-copy",
    "--font-mono": "skill-cards",
    "--space-1": "skill-cards",
    "--space-2": "skill-cards",
    "--space-3": "skill-cards",
    "--space-4": "contact-form",
    "--space-5": "about",
    "--space-6": "about",
    "--radius-sm": "hero-copy",
    "--radius-md": "skill-cards",
    "--radius-lg": "contact-form",
    "--shadow-card": "skill-cards",
    "--header-height": "header",
    "--transition": "header",
}

TARGET_LABELS = {
    "header": "상단 고정 헤더와 메뉴",
    "hero": "첫 화면(Hero) 전체",
    "hero-copy": "첫 화면 왼쪽 소개 문구와 버튼",
    "hero-visual": "첫 화면 오른쪽 MRI 히트맵 이미지",
    "about": "About 전체 영역",
    "profile": "About 왼쪽 프로필 사진",
    "skills": "Skills 전체 영역",
    "skill-cards": "기술 스택 카드 모음",
    "projects": "GitHub Projects 전체 영역",
    "project-filters": "프로젝트 언어 필터 버튼",
    "project-cards": "GitHub 프로젝트 카드 목록",
    "contact": "Contact 전체 영역",
    "contact-form": "이름·이메일·메시지 입력 폼",
    "footer": "페이지 하단 Footer",
    "scroll-top": "오른쪽 아래 맨 위로 이동 버튼",
}

SECTION_DEFAULT_TARGET = {
    "hero": "hero",
    "about": "about",
    "skills": "skills",
    "projects": "projects",
    "contact": "contact",
}

TARGET_SECTIONS = {
    "header": "hero", "hero": "hero", "hero-copy": "hero", "hero-visual": "hero",
    "about": "about", "profile": "about",
    "skills": "skills", "skill-cards": "skills",
    "projects": "projects", "project-filters": "projects", "project-cards": "projects",
    "contact": "contact", "contact-form": "contact", "footer": "contact", "scroll-top": "hero",
}

CSS_TERMS = {
    "align-items": "교차축의 정렬", "background": "배경", "border": "테두리",
    "border-radius": "모서리 둥글기", "bottom": "아래쪽 위치", "box-shadow": "그림자",
    "box-sizing": "크기 계산 방식", "color": "글자색", "content": "가상 요소 내용",
    "cursor": "마우스 커서", "display": "레이아웃 방식", "filter": "시각 필터",
    "flex": "Flex 항목 크기", "flex-direction": "Flex 진행 방향", "flex-wrap": "Flex 줄바꿈",
    "font-family": "글꼴", "font-size": "글자 크기", "font-weight": "글자 굵기",
    "gap": "항목 사이 간격", "grid-column": "Grid 열 범위",
    "grid-template-columns": "Grid 열 구성", "height": "높이", "inset": "네 방향 위치",
    "justify-content": "주축 정렬", "justify-items": "Grid 항목 정렬", "justify-self": "개별 항목 정렬",
    "left": "왼쪽 위치", "letter-spacing": "글자 간격", "line-height": "줄 높이",
    "list-style": "목록 기호", "margin": "바깥 여백", "margin-block": "위아래 바깥 여백",
    "margin-bottom": "아래 바깥 여백", "margin-inline": "좌우 바깥 여백", "margin-top": "위 바깥 여백",
    "max-width": "최대 너비", "min-height": "최소 높이", "min-width": "최소 너비",
    "object-fit": "이미지 채움 방식", "opacity": "투명도", "outline": "외곽선",
    "overflow": "넘친 내용 처리", "overflow-x": "가로 넘침 처리", "padding": "안쪽 여백",
    "padding-block": "위아래 안쪽 여백", "padding-inline": "좌우 안쪽 여백",
    "place-items": "Grid 양방향 정렬", "pointer-events": "포인터 입력 허용 여부",
    "position": "배치 기준", "right": "오른쪽 위치", "scroll-behavior": "스크롤 움직임",
    "scroll-padding-top": "앵커 이동 위쪽 여유", "text-align": "텍스트 정렬",
    "text-decoration": "텍스트 장식", "text-transform": "대소문자 표시", "text-underline-offset": "밑줄 거리",
    "top": "위쪽 위치", "transform": "이동·회전·크기 변형", "transform-origin": "변형 기준점",
    "transition": "상태 전환 효과", "visibility": "표시 여부", "white-space": "공백·줄바꿈 처리",
    "width": "너비", "z-index": "겹침 순서",
}


def code_cell(line: str) -> str:
    if not line:
        return "<em>(빈 줄)</em>"
    return f"<code>{escape(line).replace('|', '&#124;')}</code>"


def value_note(value: str) -> str:
    """CSS 값에 사용된 단위와 함수의 의미를 설명합니다."""
    notes = []
    checks = [
        ("var(" in value, "`var()`는 앞에서 정의한 CSS 변수를 읽습니다"),
        ("rem" in value, "`rem`은 최상위 글자 크기 기준의 상대 단위입니다"),
        (bool(re.search(r"\dpx", value)), "`px`는 CSS 픽셀 단위입니다"),
        ("%" in value, "`%`는 기준 요소에 대한 비율입니다"),
        ("vw" in value, "`vw`는 화면 너비의 1%를 기준으로 합니다"),
        ("fr" in value, "`fr`은 Grid의 남은 공간 비율입니다"),
        ("clamp(" in value, "`clamp()`는 최소·선호·최대값 사이에서 반응형 값을 선택합니다"),
        ("minmax(" in value, "`minmax()`는 Grid 크기의 최소값과 최대값을 정합니다"),
        ("auto-fit" in value, "`auto-fit`은 가능한 만큼 Grid 열을 자동 배치합니다"),
        ("color-mix(" in value, "`color-mix()`는 두 색상을 지정 비율로 섞습니다"),
        ("rgba(" in value, "`rgba()`의 마지막 값은 투명도입니다"),
        (bool(re.search(r"#[0-9a-fA-F]{3,8}", value)), "`#` 값은 RGB 색상을 16진수로 표현합니다"),
        ("ms" in value, "`ms`는 1/1000초 단위입니다"),
    ]
    notes.extend(note for matched, note in checks if matched)
    return " ".join(notes)


def html_note(line: str) -> str:
    s = line.strip()
    if not s:
        return "구조를 구분해 읽기 쉽게 만드는 빈 줄입니다."
    if s.startswith("<!--") or s.endswith("-->"):
        return "화면에는 표시되지 않는 HTML 설명 주석입니다."
    if s.startswith("<!doctype"):
        return "문서를 HTML5 표준 모드로 해석하도록 선언합니다."
    if s.startswith("</"):
        match = re.search(r"</([\w-]+)", s)
        return f"앞에서 연 `{match.group(1) if match else '요소'}` 영역을 닫습니다."
    tag_notes = {
        "html": "문서 최상위 요소이며 언어와 초기 테마 정보를 가집니다.",
        "head": "메타데이터와 외부 파일 연결을 묶습니다.",
        "body": "화면에 표시될 콘텐츠를 시작합니다.",
        "header": "사이트 상단과 주요 메뉴를 담는 시맨틱 영역입니다.",
        "nav": "주요 이동 링크를 묶는 시맨틱 내비게이션입니다.",
        "main": "페이지의 핵심 콘텐츠를 담는 시맨틱 영역입니다.",
        "section": "같은 주제의 콘텐츠를 하나의 구역으로 묶습니다.",
        "article": "독립적으로 이해할 수 있는 카드 콘텐츠입니다.",
        "footer": "저작권과 보조 링크를 담는 하단 영역입니다.",
        "form": "사용자 입력을 하나의 제출 단위로 묶습니다.",
        "label": "입력 요소의 이름을 제공하고 `for`로 입력과 연결합니다.",
        "input": "한 줄 입력값 또는 숨겨진 전송 설정을 담습니다.",
        "textarea": "여러 줄 메시지를 입력받습니다.",
        "button": "클릭 이벤트를 받을 버튼을 만듭니다.",
        "img": "이미지를 표시하고 `alt` 대체 설명을 제공합니다.",
        "a": "내부 섹션 또는 외부 주소로 이동하는 링크입니다.",
        "ul": "순서가 중요하지 않은 목록을 시작합니다.",
        "li": "목록의 한 항목입니다.",
        "div": "스타일 배치용 범용 블록 컨테이너입니다.",
        "span": "작은 텍스트나 UI 조각을 묶는 인라인 컨테이너입니다.",
        "p": "하나의 문단 또는 상태 문구입니다.",
    }
    match = re.match(r"<([\w-]+)", s)
    if match and match.group(1) in tag_notes:
        return tag_notes[match.group(1)]
    if match and re.fullmatch(r"h[1-6]", match.group(1)):
        return "콘텐츠 계층을 나타내는 제목 요소입니다. 숫자가 작을수록 상위 제목입니다."
    if s.startswith("<meta") or s.startswith("content="):
        return "문자 인코딩·화면 크기·검색 설명 등의 메타데이터를 설정합니다."
    if s.startswith("<title"):
        return "브라우저 탭에 표시할 페이지 제목을 정합니다."
    if s.startswith("<link"):
        return "CSS나 파비콘 같은 외부 자원을 문서에 연결합니다."
    if s.startswith("<script"):
        return "JavaScript를 연결하며 `defer`로 HTML 파싱 후 실행합니다."
    attrs = {
        "class=": "CSS와 JavaScript가 공통으로 찾을 클래스 이름을 지정합니다.",
        "id=": "앵커·label·DOM 선택에 사용할 고유 식별자를 지정합니다.",
        "aria-": "스크린 리더에 역할이나 상태를 전달하는 접근성 속성입니다.",
        "href=": "링크의 이동 목적지를 지정합니다.", "src=": "불러올 파일 경로를 지정합니다.",
        "alt=": "이미지의 의미를 전달하는 대체 텍스트입니다.", "name=": "폼 데이터의 필드 이름입니다.",
        "type=": "입력 또는 버튼의 종류를 지정합니다.", "value=": "입력 요소의 기본 전송값입니다.",
        "autocomplete=": "브라우저 자동 완성 데이터 종류를 알려줍니다.",
        "required": "비어 있으면 안 되는 필수 입력임을 알립니다.",
        "action=": "폼 데이터를 보낼 주소를 지정합니다.", "method=": "폼의 HTTP 전송 방식을 지정합니다.",
        "target=": "링크를 열 창을 지정합니다.", "rel=": "외부 링크와 현재 문서의 보안 관계를 설정합니다.",
    }
    for token, note in attrs.items():
        if s.startswith(token) or token in s:
            return note
    if s in {">", "/>"}:
        return "여러 줄로 작성한 시작 태그를 마무리합니다."
    if s.startswith("<"):
        return "앞뒤 줄과 함께 HTML 요소 또는 속성을 구성합니다."
    return "방문자에게 실제로 표시되는 텍스트 콘텐츠입니다."


def css_note(line: str) -> str:
    s = line.strip()
    if not s:
        return "스타일 규칙을 구분하는 빈 줄입니다."
    if s.startswith("/*") or s.startswith("*") or s.endswith("*/"):
        return "CSS 구역의 목적을 설명하는 주석입니다."
    if s.startswith("@media"):
        return "화면 크기 또는 접근성 설정 조건에 따라 적용할 스타일을 시작합니다."
    if s == "}":
        return "현재 선택자 또는 미디어 쿼리의 범위를 닫습니다."
    if s.endswith("{"):
        return f"`{s[:-1].strip()}` 선택자와 일치하는 요소의 스타일 규칙을 시작합니다."
    if s.endswith(","):
        return "다음 선택자와 동일한 스타일 선언을 공유하도록 이어 씁니다."
    custom = re.match(r"(--[\w-]+)\s*:\s*(.+);", s)
    if custom:
        name, value = custom.groups()
        meaning = CSS_VARIABLES.get(name, ("여러 스타일에서 재사용하는 디자인 값", "hero"))[0]
        detail = value_note(value)
        return f"CSS 변수 `{name}`은 {meaning}입니다. 현재 값은 `{value}`입니다. {detail}".strip()
    decl = re.match(r"([\w-]+)\s*:\s*(.+);", s)
    if decl:
        prop, value = decl.groups()
        meaning = CSS_TERMS.get(prop, f"`{prop}` 스타일")
        detail = value_note(value)
        return f"{meaning}을 `{value}` 값으로 설정합니다. {detail}".strip()
    return "앞뒤 줄과 함께 여러 줄 선택자 또는 속성 값을 구성합니다."


def js_note(line: str) -> str:
    s = line.strip()
    if not s:
        return "로직 단위를 구분하는 빈 줄입니다."
    if s.startswith(("/*", "*", "//")) or s.endswith("*/"):
        return "코드의 목적이나 처리 이유를 설명하는 JavaScript 주석입니다."
    if s == '"use strict";':
        return "실수를 줄이기 위해 엄격 모드로 JavaScript를 실행합니다."
    if "addEventListener" in s:
        match = re.search(r'addEventListener\("([^"]+)', s)
        return f"`{match.group(1) if match else '지정된'}` 이벤트가 발생할 때 실행할 함수를 연결합니다."
    if s.startswith("async function"):
        return "`await`를 사용할 수 있는 비동기 함수를 선언합니다."
    if s.startswith(("const ", "let ")):
        name = re.match(r"(?:const|let)\s+(\w+)", s)
        label = name.group(1) if name else "변수"
        if "querySelector" in s:
            return f"DOM 요소를 찾아 `{label}`에 저장합니다."
        if "=>" in s:
            return f"재사용할 화살표 함수를 `{label}` 이름으로 선언합니다."
        return f"값 또는 객체 참조를 `{label}`에 저장합니다."
    if s.startswith("if"):
        return "조건이 참일 때만 다음 코드 블록을 실행합니다."
    if s.startswith("} else"):
        return "앞 조건이 거짓일 때 실행할 대체 분기입니다."
    if s.startswith("try"):
        return "오류 가능성이 있는 작업을 시도하는 블록입니다."
    if "catch" in s and s.startswith(("}", "catch")):
        return "발생한 오류를 받아 사용자 친화적으로 처리합니다."
    if "finally" in s:
        return "성공·실패와 관계없이 마지막 정리 작업을 실행합니다."
    if s.startswith("return"):
        return "현재 함수 실행을 끝내고 결과를 호출한 곳으로 돌려줍니다."
    if "await fetch" in s:
        return "HTTP 요청 응답이 올 때까지 기다린 뒤 결과를 저장합니다."
    operations = {
        ".map(": "각 배열 항목을 변환해 새 배열을 만듭니다.",
        ".filter(": "조건을 통과한 항목만 새 배열로 모읍니다.",
        ".forEach(": "각 항목에 같은 작업을 반복합니다.",
        ".classList.": "CSS 클래스를 변경해 화면 상태를 바꿉니다.",
        ".setAttribute(": "HTML 또는 ARIA 속성 값을 갱신합니다.",
        ".textContent": "HTML로 해석되지 않는 텍스트를 안전하게 변경합니다.",
        ".innerHTML": "문자열로 만든 HTML 구조를 화면에 렌더링합니다.",
        "localStorage": "새로고침 후에도 남는 브라우저 저장소를 사용합니다.",
        "IntersectionObserver": "요소가 화면에 들어오는 시점을 관찰합니다.",
        "requestAnimationFrame": "다음 화면 갱신 시점에 작업을 예약합니다.",
        "AbortController": "시간 초과 시 네트워크 요청을 취소할 준비를 합니다.",
        "setTimeout": "일정 시간이 지난 후 실행할 타이머를 등록합니다.",
        "clearTimeout": "등록했던 타이머를 해제합니다.",
        "preventDefault": "브라우저 기본 동작을 막고 JavaScript가 직접 처리합니다.",
    }
    for token, note in operations.items():
        if token in s:
            return note
    if s.startswith("throw new Error"):
        return "설명과 함께 오류를 발생시켜 catch 블록으로 전달합니다."
    if "state." in s and "=" in s:
        return "상태 값을 변경해 다음 화면 렌더링 결과를 결정합니다."
    if "${" in s:
        return "템플릿 리터럴 안에 현재 JavaScript 값을 삽입합니다."
    if s.startswith(("<", "`")) or s.endswith("`"):
        return "템플릿 리터럴로 동적 HTML 일부를 구성합니다."
    if re.match(r"[\w]+\s*:", s):
        return "객체 안에서 속성 이름과 값을 정의합니다."
    if s in {"}", "};", "});", ");", "],", "},"}:
        return "현재 객체·함수·조건문 또는 메서드 호출을 마무리합니다."
    return "앞뒤 줄과 함께 함수 호출·조건·객체 또는 문자열을 구성합니다."


def detect_section(source: Path, line: str, current: str) -> str:
    """코드 한 줄과 가장 관련 있는 홈페이지 섹션을 판별합니다."""
    text = line.lower()
    if source.name == "style.css":
        for variable, (_, section) in CSS_VARIABLES.items():
            if variable in text:
                return section
        selector = text.strip().rstrip("{,").strip()
        if selector in {":root", "*", "html", "body", "img", "a", "button", "input", "textarea",
                        "h1", "h2", "h3", "p", ".container", ".section", ":focus-visible"}:
            return "hero"
        if selector.startswith(".section-heading"):
            return "skills"
        if selector.startswith(".section-dark"):
            return "projects"
    for section in ("hero", "about", "skills", "projects", "contact"):
        if f'id="{section}"' in text:
            return section
    groups = {
        "contact": ("contact", "form", "field", "validator", "submit", "honeypot", "email"),
        "projects": ("project", "github", "repo", "filter", "spinner", "language"),
        "skills": ("skill", "tag-list", "card-number"),
        "about": ("about", "profile"),
        "hero": ("hero", "vision", "header", "nav", "menu", "theme", "scroll", "reveal", "observer", "logo"),
    }
    for section, tokens in groups.items():
        if any(token in text for token in tokens):
            return section
    if "footer" in text:
        return "contact"
    return current


def detect_target(source: Path, line: str, section: str, current: str) -> str:
    """섹션보다 더 구체적으로, 화면에서 강조할 대표 요소를 판별합니다."""
    text = line.lower()

    if source.name == "style.css":
        for variable, target in CSS_VARIABLE_TARGETS.items():
            if variable in text:
                return target

    # JavaScript는 한 줄마다 처리 대상이 빠르게 바뀌므로 이전 줄의 세부 위치를
    # 무조건 이어받지 않습니다. HTML/CSS는 같은 요소·선택자가 여러 줄이므로 유지합니다.
    if source.name == "script.js":
        current = SECTION_DEFAULT_TARGET[section]
    elif source.name == "index.html" and current == "footer" and "scroll-top" not in text:
        return "footer"
    elif TARGET_SECTIONS.get(current) != section:
        current = SECTION_DEFAULT_TARGET[section]

    checks = [
        ("scroll-top", ("scroll-top", "scrolltopbutton", "window.scrollto")),
        ("footer", ("site-footer", "footer-content", "footer-links", "<footer", "</footer")),
        ("contact-form", ("contact-form", "form-field", "field-error", "form-status", "submit-button",
                          "validator", "honeypot", "formsubmit", "form_endpoint", "contactform", "formfields")),
        ("project-filters", ("project-filters", "projectfilters", "activelanguage", "filter-button")),
        ("project-cards", ("projects-grid", "projectsgrid", "project-card", "github_api", "loadprojects",
                           "renderprojects", "repo", "spinner")),
        ("skill-cards", ("skills-grid", "skill-card", "tag-list", "card-number")),
        ("profile", ("profile-frame", "profile-image", "profile-caption")),
        ("hero-visual", ("hero-visual", "hero-image", "mri", "heatmap", "vision-frame")),
        ("hero-copy", ("hero-copy", "hero-description", "hero-cta", "hero-title", "eyebrow")),
        ("header", ("site-header", "nav-menu", "nav-actions", "menu-toggle", "theme-toggle", "logo-mark")),
    ]
    for target, tokens in checks:
        if any(token in text for token in tokens):
            return target
    return current


def location_url(section: str, target: str, *, live: bool) -> str:
    """홈페이지 이동과 정확한 요소 강조에 사용할 안전한 URL을 만듭니다."""
    base = LIVE_SITE if live else "../index.html"
    resolved_section = TARGET_SECTIONS.get(target, section)
    return f"{base}?focus={target}#{resolved_section}"


def location_label(target: str) -> str:
    return TARGET_LABELS.get(target, "관련 홈페이지 영역")


def make_doc(source: Path, title: str, note_func) -> str:
    lines = source.read_text(encoding="utf-8").splitlines()
    relative = source.relative_to(ROOT).as_posix()
    rows = [
        f"# {title}", "", f"원본 파일: [`{relative}`](../{relative})", "",
        "> 실행 파일을 건드리지 않는 학습용 줄별 해설입니다. 빈 줄도 포함하며, 원본 수정 후 생성 도구를 다시 실행하면 줄 번호가 갱신됩니다.",
        "", "| 줄 | 코드 | 설명(클릭하면 관련 홈페이지 섹션으로 이동) |", "|---:|---|---|",
    ]
    # 여러 줄 주석 내부의 일반 문장을 실제 콘텐츠로 오해하지 않도록 범위를 추적합니다.
    comment_start, comment_end = (
        ("<!--", "-->") if source.suffix == ".html" else ("/*", "*/")
    )
    inside_comment = False
    current_section = "hero"
    current_target = "hero"
    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        starts_comment = comment_start in stripped
        if starts_comment:
            inside_comment = True

        if inside_comment:
            note = "브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다."
        else:
            note = note_func(line)

        previous_section = current_section
        current_section = detect_section(source, line, current_section)
        if previous_section != current_section:
            current_target = SECTION_DEFAULT_TARGET[current_section]
        current_target = detect_target(source, line, current_section, current_target)
        live_url = location_url(current_section, current_target, live=True)
        rows.append(
            f"| {number} | {code_cell(line)} | [{note} — 위치: {location_label(current_target)}]({live_url}) |"
        )

        if inside_comment and comment_end in stripped:
            inside_comment = False
    rows += ["", f"총 {len(lines):,}줄을 설명했습니다.", ""]
    return "\n".join(rows)


def make_html_doc(source: Path, title: str, note_func) -> str:
    """Live Server와 GitHub Pages에서 클릭 가능한 줄별 해설 HTML을 만듭니다."""
    lines = source.read_text(encoding="utf-8").splitlines()
    comment_start, comment_end = (("<!--", "-->") if source.suffix == ".html" else ("/*", "*/"))
    inside_comment = False
    current_section = "hero"
    current_target = "hero"
    table_rows = []
    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if comment_start in stripped:
            inside_comment = True
        note = (
            "브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다."
            if inside_comment else note_func(line)
        )
        previous_section = current_section
        current_section = detect_section(source, line, current_section)
        if previous_section != current_section:
            current_target = SECTION_DEFAULT_TARGET[current_section]
        current_target = detect_target(source, line, current_section, current_target)
        local_url = location_url(current_section, current_target, live=False)
        shown_code = escape(line) if line else "(빈 줄)"
        table_rows.append(
            f'<tr id="L{number}"><th>{number}</th><td><code>{shown_code}</code></td>'
            f'<td><a href="{local_url}" title="{escape(location_label(current_target))}에서 보기">{escape(note)}</a>'
            f'<small class="location-label">정확한 위치: {escape(location_label(current_target))}</small></td></tr>'
        )
        if inside_comment and comment_end in stripped:
            inside_comment = False
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)}</title><link rel="stylesheet" href="guide.css"></head>
<body><header class="guide-header"><a href="code-guide.html">← 학습 문서 홈</a><h1>{escape(title)}</h1>
<p>설명을 클릭하면 실제 홈페이지의 정확한 요소로 이동하고, 5초 동안 강조 표시됩니다.</p></header>
<main><div class="table-wrap"><table><thead><tr><th>줄</th><th>코드</th><th>설명·홈페이지 위치</th></tr></thead>
<tbody>{''.join(table_rows)}</tbody></table></div></main></body></html>'''


def make_css_variables() -> tuple[str, str]:
    """라이트·다크 테마의 CSS 변수와 적용 위치 문서를 만듭니다."""
    css = (ROOT / "css/style.css").read_text(encoding="utf-8")
    root_match = re.search(r":root\s*{(.*?)}", css, re.S)
    dark_match = re.search(r'\[data-theme="dark"\]\s*{(.*?)}', css, re.S)
    if not root_match or not dark_match:
        raise RuntimeError("CSS 변수 블록을 찾을 수 없습니다.")
    parse = lambda block: dict(re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", block))
    light, dark = parse(root_match.group(1)), parse(dark_match.group(1))
    md = [
        "# CSS 변수·값·홈페이지 위치", "",
        "변수 이름 또는 설명을 클릭하면 실제 홈페이지의 관련 섹션으로 이동합니다.", "",
        "| 변수 | 라이트 값 | 다크 값 | 의미·위치 |", "|---|---|---|---|",
    ]
    html_rows = []
    for name, value in light.items():
        meaning, section = CSS_VARIABLES.get(name, ("재사용하는 디자인 값", "hero"))
        target = CSS_VARIABLE_TARGETS.get(name, SECTION_DEFAULT_TARGET[section])
        dark_value = dark.get(name, "동일")
        detail = value_note(value)
        url = location_url(section, target, live=True)
        local_url = location_url(section, target, live=False)
        label = location_label(target)
        md.append(f"| [`{name}`]({url}) | `{value}` | `{dark_value}` | [{meaning}. {detail} 위치: {label}]({url}) |")
        html_rows.append(
            f'<tr><th><a href="{local_url}"><code>{name}</code></a></th>'
            f'<td><code>{escape(value)}</code></td><td><code>{escape(dark_value)}</code></td>'
            f'<td><a href="{local_url}">{escape(meaning)}. {escape(detail)}</a>'
            f'<small class="location-label">정확한 위치: {escape(label)}</small></td></tr>'
        )
    md += ["", "라이트 값은 `:root`, 다크 값은 `[data-theme=\"dark\"]`에서 정의됩니다.", ""]
    html_doc = f'''<!doctype html><html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CSS 변수·값·위치</title><link rel="stylesheet" href="guide.css"></head><body>
<header class="guide-header"><a href="code-guide.html">← 학습 문서 홈</a><h1>CSS 변수·값·홈페이지 위치</h1>
<p>변수 이름이나 설명을 클릭하면 실제 적용 예시가 있는 정확한 요소로 이동하고, 5초 동안 강조 표시됩니다.</p></header>
<main><div class="table-wrap"><table><thead><tr><th>변수</th><th>라이트</th><th>다크</th><th>의미·위치</th></tr></thead>
<tbody>{''.join(html_rows)}</tbody></table></div></main></body></html>'''
    return "\n".join(md), html_doc


def make_glossary_html() -> str:
    """Markdown 용어사전을 클릭 가능한 카드형 HTML로 변환합니다."""
    lines = (DOCS / "GLOSSARY.md").read_text(encoding="utf-8").splitlines()
    cards, term, body = [], "", []

    def flush() -> None:
        if not term:
            return
        section = detect_section(Path("glossary"), term, "hero")
        target = detect_target(Path("glossary"), term, section, SECTION_DEFAULT_TARGET[section])
        local_url = location_url(section, target, live=False)
        content = " ".join(escape(part) for part in body if part and not part.startswith("```"))
        cards.append(
            f'<article><h2><a href="{local_url}">{escape(term)}</a></h2>'
            f'<p>{content}</p><small class="location-label">정확한 위치: {escape(location_label(target))}</small></article>'
        )

    for line in lines:
        if line.startswith("### "):
            flush()
            term, body = line[4:], []
        elif term and not line.startswith("## "):
            body.append(line)
    flush()
    return f'''<!doctype html><html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>웹 개발 용어사전</title><link rel="stylesheet" href="guide.css"></head><body>
<header class="guide-header"><a href="code-guide.html">← 학습 문서 홈</a><h1>웹 개발 용어사전</h1>
<p>용어 제목을 클릭하면 해당 개념을 확인하기 좋은 정확한 요소로 이동하고, 5초 동안 강조 표시됩니다.</p></header>
<main class="term-grid">{''.join(cards)}</main></body></html>'''


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    targets = [
        (ROOT / "index.html", DOCS / "ANNOTATED_INDEX.md", DOCS / "annotated-index.html", "index.html 줄별 해설", html_note),
        (ROOT / "css/style.css", DOCS / "ANNOTATED_STYLE.md", DOCS / "annotated-style.html", "style.css 줄별 해설", css_note),
        (ROOT / "js/script.js", DOCS / "ANNOTATED_SCRIPT.md", DOCS / "annotated-script.html", "script.js 줄별 해설", js_note),
    ]
    for source, output, html_output, title, note_func in targets:
        output.write_text(make_doc(source, title, note_func), encoding="utf-8", newline="\n")
        html_output.write_text(make_html_doc(source, title, note_func), encoding="utf-8", newline="\n")
        print(f"generated: {output.relative_to(ROOT)}")
        print(f"generated: {html_output.relative_to(ROOT)}")
    variables_md, variables_html = make_css_variables()
    (DOCS / "CSS_VARIABLES.md").write_text(variables_md, encoding="utf-8", newline="\n")
    (DOCS / "css-variables.html").write_text(variables_html, encoding="utf-8", newline="\n")
    (DOCS / "glossary.html").write_text(make_glossary_html(), encoding="utf-8", newline="\n")
    print("generated: docs/CSS_VARIABLES.md")
    print("generated: docs/css-variables.html")
    print("generated: docs/glossary.html")


if __name__ == "__main__":
    main()
