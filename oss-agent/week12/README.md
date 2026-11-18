# boxoffice — KOBIS 박스오피스 조회 스킬

## 하는 일
영화진흥위원회 KOBIS 박스오피스 1~3위의 영화 제목을 조회해줍니다.

## 들어 있는 파일
- .claude/skills/boxoffice/SKILL.md
- .claude/skills/boxoffice/scripts/boxoffice.py
- .claude/skills/boxoffice/LICENSE

## 필요한 것
필요한 패키지 : os, sys, requests
필요한 파일 : top3.py, LICENSE, SKILL.md

## 설치
(직접 쓸 것: boxoffice 폴더를 어디에 두고, Claude Code 에서 무엇을 하나)

## 바깥으로 요청하는 곳
"https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
            "boxoffice/searchDailyBoxOfficeList.json"

## 키
KOBIS에서 본인의 api키를 발급 후 secret.py에 저장

## 권한
폴더 내 파일을 조회할 수 있는 권한을 요구합니다.

## 라이선스
MIT-LISENSE / 스킬 파일/boxoffice 폴더 안에 있습니다.