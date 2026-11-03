# week09

## 무엇을 하는 코드인가

`tools_nodoc.py`의 `get_boxoffice_rank_1(date)`는 영화진흥위원회(KOBIS) 오픈 API에서 지정한 날짜의 일별 박스오피스를 조회하고, 1위 영화 제목을 돌려줍니다.

## 설치

```bash
pip install requests
```

KOBIS 오픈 API 키가 필요합니다. 같은 폴더에 `secret.py`를 만들고 키를 넣어 주세요.

```python
API_KEY = "발급받은_키"
```

## 실행

`week09` 폴더에서 실행합니다. 날짜는 `YYYYMMDD` 형식의 문자열로 넘깁니다.

```bash
python -c "from tools_nodoc import get_boxoffice_rank_1; print(get_boxoffice_rank_1('20261027'))"
```
