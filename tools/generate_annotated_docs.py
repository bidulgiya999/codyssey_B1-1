"""원본 실행 파일을 유지하면서 줄 번호별 한국어 해설 문서를 생성합니다."""

from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

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
        return f"CSS 변수 `{custom.group(1)}`에 `{custom.group(2)}` 값을 저장합니다."
    decl = re.match(r"([\w-]+)\s*:\s*(.+);", s)
    if decl:
        prop, value = decl.groups()
        meaning = CSS_TERMS.get(prop, f"`{prop}` 스타일")
        return f"{meaning}을 `{value}` 값으로 설정합니다."
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


def make_doc(source: Path, title: str, note_func) -> str:
    lines = source.read_text(encoding="utf-8").splitlines()
    relative = source.relative_to(ROOT).as_posix()
    rows = [
        f"# {title}", "", f"원본 파일: [`{relative}`](../{relative})", "",
        "> 실행 파일을 건드리지 않는 학습용 줄별 해설입니다. 빈 줄도 포함하며, 원본 수정 후 생성 도구를 다시 실행하면 줄 번호가 갱신됩니다.",
        "", "| 줄 | 코드 | 설명 |", "|---:|---|---|",
    ]
    # 여러 줄 주석 내부의 일반 문장을 실제 콘텐츠로 오해하지 않도록 범위를 추적합니다.
    comment_start, comment_end = (
        ("<!--", "-->") if source.suffix == ".html" else ("/*", "*/")
    )
    inside_comment = False
    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        starts_comment = comment_start in stripped
        if starts_comment:
            inside_comment = True

        if inside_comment:
            note = "브라우저 동작에는 영향을 주지 않는 여러 줄 설명 주석의 일부입니다."
        else:
            note = note_func(line)

        rows.append(f"| {number} | {code_cell(line)} | {note} |")

        if inside_comment and comment_end in stripped:
            inside_comment = False
    rows += ["", f"총 {len(lines):,}줄을 설명했습니다.", ""]
    return "\n".join(rows)


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    targets = [
        (ROOT / "index.html", DOCS / "ANNOTATED_INDEX.md", "index.html 줄별 해설", html_note),
        (ROOT / "css/style.css", DOCS / "ANNOTATED_STYLE.md", "style.css 줄별 해설", css_note),
        (ROOT / "js/script.js", DOCS / "ANNOTATED_SCRIPT.md", "script.js 줄별 해설", js_note),
    ]
    for source, output, title, note_func in targets:
        output.write_text(make_doc(source, title, note_func), encoding="utf-8", newline="\n")
        print(f"generated: {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
