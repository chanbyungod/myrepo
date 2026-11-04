작성: Claude Code / 확인: 이찬병

# week09/tools.py 함수 설명

## 파일 개요

- 박스오피스 정보를 가져오는 도구 모음임이오
- 영화진흥위원회(KOBIS) 일별 박스오피스 API를 호출함이오
- API 키는 secret.py의 `API_KEY`에서 가져옴이오
- 정의된 함수는 `get_boxoffice_rank_1` 하나뿐임이오

## get_boxoffice_rank_1(date)

- 역할: 해당 날짜의 박스오피스 1위 영화 제목을 알려줌이오
- 받는 값: `date` (문자열), 8자리 날짜임이오. 예: `"20260824"`
- 돌려주는 값: 1위 영화 제목 (문자열)임이오. 예: `"오디세이"`
- 동작 순서
  - `key`와 `targetDt`를 인자로 담아 API에 GET 요청을 보냄이오 (제한 시간 10초)
  - 응답 JSON에서 `boxOfficeResult` → `dailyBoxOfficeList` 목록을 꺼냄이오
  - 목록 첫 항목의 `movieNm`을 돌려줌이오
