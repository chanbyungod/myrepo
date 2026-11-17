"""tools.py — 박스오피스 정보를 가져오는 도구 모음 (7주차 예시 답안)

쓰는 곳: 11주차 에이전트 루프, 12주차 스킬, 14주차 공개
필요한 것: requests, secret.py 의 API_KEY
"""
import requests
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
            "boxoffice/searchDailyBoxOfficeList.json")


def _get_movies(date):
    """KOBIS 에 요청해 그 날짜의 영화 목록을 받는다. 실패하면 안내 문장을 돌려준다."""
    params = {"key": API_KEY, "targetDt": date}
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.RequestException:
        return "네트워크에 연결하지 못했습니다."
    if response.status_code != 200:
        return f"요청이 실패했습니다. 상태 코드: {response.status_code}"
    data = response.json()
    if "faultInfo" in data:
        return "요청이 거절되었습니다: " + data["faultInfo"]["message"]
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]
    if len(movies) == 0:
        return f"{date} 에는 집계된 자료가 없습니다."
    return movies


def get_boxoffice_rank_1(date):
    """
    그 날짜의 박스오피스 1위 영화 제목을 알려준다.

    받는 것: date (문자열) — 8자리 날짜. 예: "20260824"
    돌려주는 것: (문자열) 1위 영화 제목. 예: "오디세이"
    """
    movies = _get_movies(date)
    if isinstance(movies, str):
        return movies
    return movies[0]["movieNm"]


def get_movie_audience(date, title):
    """
    그 날짜에 특정 영화를 본 관객 수를 알려준다.

    받는 것: date (문자열) — 8자리 날짜, title (문자열) — 영화 제목
    돌려주는 것: (문자열) 관객 수. 예: "186,587명"
    """
    movies = _get_movies(date)
    if isinstance(movies, str):
        return movies
    for movie in movies:
        if movie["movieNm"] == title:
            return f"{int(movie['audiCnt']):,}명"
    return f"'{title}' 은(는) {date} 순위에 없습니다."
