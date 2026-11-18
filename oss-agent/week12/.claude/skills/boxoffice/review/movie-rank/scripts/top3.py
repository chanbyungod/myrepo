"""KOBIS 일별 박스오피스 상위 3편의 제목을 출력한다. 키는 프로젝트 폴더의 secret.py 에서 읽는다."""
import os
import sys

import requests

sys.path.insert(0, os.getcwd())
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
            "boxoffice/searchDailyBoxOfficeList.json")


def top3(date):
    response = requests.get(BASE_URL, params={"key": API_KEY, "targetDt": date}, timeout=10)
    if response.status_code != 200:
        return f"요청이 실패했습니다. 상태 코드: {response.status_code}"
    data = response.json()
    if "faultInfo" in data:
        return "요청이 거절되었습니다: " + data["faultInfo"]["message"]
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]
    if len(movies) == 0:
        return f"{date} 에는 집계된 자료가 없습니다."
    return "\n".join(f"{m['rank']}위 {m['movieNm']}" for m in movies[:3])


if __name__ == "__main__":
    print(top3(sys.argv[1]))
