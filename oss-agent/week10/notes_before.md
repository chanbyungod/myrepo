# week09/tools.py 함수 정리

`week09/tools.py`는 영화진흥위원회(KOBIS) 오픈 API로 박스오피스 정보를 가져오는 도구 모음이다. 현재 함수는 **1개**다.

## `get_boxoffice_rank_1(date)`

특정 날짜의 일별 박스오피스 1위 영화 제목을 돌려준다.

| 구분 | 타입 | 설명 | 예시 |
| --- | --- | --- | --- |
| 입력 `date` | 문자열 | 8자리 날짜 | `"20260824"` |
| 반환값 | 문자열 | 1위 영화 제목 | `"오디세이"` |

### 동작 순서

1. `API_KEY`와 `date`로 요청 파라미터(`key`, `targetDt`)를 만든다.
2. `BASE_URL`에 GET 요청을 보낸다. 타임아웃은 10초다.
3. 응답 JSON에서 `boxOfficeResult` → `dailyBoxOfficeList` 목록을 꺼낸다.
4. 목록 첫 번째 영화의 `movieNm`(제목)을 반환한다.

## 함수 외 구성 요소

- `BASE_URL`: KOBIS 일별 박스오피스 조회 API 주소
- `API_KEY`: `secret` 모듈에서 가져오는 API 키
- `requests`: HTTP 요청에 사용하는 외부 라이브러리
