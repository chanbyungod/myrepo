---
name: movie-rank
description: 영화진흥위원회(KOBIS) 일별 박스오피스에서 특정 날짜의 1위부터 3위까지 영화 제목을 알려준다. 박스오피스 상위 몇 편을 물을 때 사용한다.
license: MIT (LICENSE 파일 참고)
---

# 박스오피스 상위 3편

## 쓰는 법

프로젝트 폴더에서 아래 명령을 실행한다. 날짜는 8자리로 쓴다.

`python .claude/skills/movie-rank/scripts/top3.py 날짜`

## 지킬 것

- 스크립트의 출력만 근거로 답한다.
- 자료가 없다는 안내가 나오면 그대로 전한다.
