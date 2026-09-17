# 학습 문서 안내

실행용 코드는 짧고 명확하게 유지하고, 상세 학습 설명은 이 폴더에 분리했습니다.

## 클릭형 학습 페이지

Live Server 실행 후 <http://127.0.0.1:5500/docs/code-guide.html>을 열면 설명과 용어를 클릭해 실제 홈페이지의 관련 섹션으로 이동할 수 있습니다.

- [클릭형 코드 학습 가이드](code-guide.html)
- [CSS 변수·값·홈페이지 위치](CSS_VARIABLES.md)

- [index.html 줄별 해설](ANNOTATED_INDEX.md)
- [style.css 줄별 해설](ANNOTATED_STYLE.md)
- [script.js 줄별 해설](ANNOTATED_SCRIPT.md)
- [웹 개발 용어사전](GLOSSARY.md)

줄별 해설은 빈 줄을 포함해 원본의 모든 줄 번호와 대응합니다. 원본 파일을 수정한 뒤 다음 명령으로 다시 생성할 수 있습니다.


```powershell
python .\tools\generate_annotated_docs.py
```

생성 도구는 실행용 HTML·CSS·JavaScript를 수정하지 않고 다음 학습 문서만 갱신합니다.

- `ANNOTATED_INDEX.md`, `ANNOTATED_STYLE.md`, `ANNOTATED_SCRIPT.md`
- `annotated-index.html`, `annotated-style.html`, `annotated-script.html`
- `CSS_VARIABLES.md`, `css-variables.html`
- `glossary.html`

`code-guide.html`, `guide.css`, `GLOSSARY.md`는 사람이 직접 관리하는 학습 페이지·스타일·용어 원문입니다.
