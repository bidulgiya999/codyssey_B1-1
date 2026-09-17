# 학습 문서 안내

실행용 코드는 짧고 명확하게 유지하고, 상세 학습 설명은 이 폴더에 분리했습니다.

- [index.html 줄별 해설](ANNOTATED_INDEX.md)
- [style.css 줄별 해설](ANNOTATED_STYLE.md)
- [script.js 줄별 해설](ANNOTATED_SCRIPT.md)
- [웹 개발 용어사전](GLOSSARY.md)

줄별 해설은 빈 줄을 포함해 원본의 모든 줄 번호와 대응합니다. 원본 파일을 수정한 뒤 다음 명령으로 다시 생성할 수 있습니다.


```powershell
python .\tools\generate_annotated_docs.py
```

생성 도구는 실행용 HTML·CSS·JavaScript를 수정하지 않고 `docs/ANNOTATED_*.md` 문서만 갱신합니다.
