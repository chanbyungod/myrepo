import requests
import json

url = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
       "boxoffice/searchDailyBoxOfficeList.json")
params = {"key": "", "targetDt": "20260824"}

response = requests.get(url, params=params, timeout=10)
print(response.status_code)

print(response.text)


data = response.json()
result = data['boxOfficeResult']
print(result.keys)

movies = result['dailyBoxOfficeList']
first = movies[0]
print(first['rank'])
print(first['movieNm'])
print(first['audiCnt'])

movies = result['dailyBoxOfficeList']

for movie in movies[:5]:
    rank = movie['rank']
    name = movie['movieNm']
    audi = int(movie['audiCnt'])
    print(f"{rank}위: {name} ({audi:,}명)")


