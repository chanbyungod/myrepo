"""boxoffice 스킬의 스크립트. week12 폴더의 tools.py 함수를 명령줄에서 부른다.

쓰는 법 (week12 폴더에서 실행):
    python .claude/skills/boxoffice/scripts/boxoffice.py rank 20261114
    python .claude/skills/boxoffice/scripts/boxoffice.py audience 20261114 "영화 제목"

키는 이 스킬 폴더에 두지 않는다. week12 폴더의 secret.py 를 tools.py 가 읽는다.
"""
import os
import sys

sys.path.insert(0, os.getcwd())   # 지금 폴더(week12)의 tools.py 를 찾게 함
import tools


def stop_at_blank(number, message):
    print(f"[빈칸 {number}] 여기까지 진행됨 → {message}")
    sys.exit(1)


args = sys.argv[1:]               # 파일 이름 뒤에 적은 낱말들의 목록
if len(args) < 2:
    print("쓰는 법: boxoffice.py rank 날짜 / boxoffice.py audience 날짜 영화제목")
    sys.exit(1)

# [빈칸 1] args 에서 할 일(rank 또는 audience)과 날짜를 꺼내기
#          args 는 리스트. 첫 번째 칸이 할 일, 두 번째 칸이 날짜
command = args[0]
date = args[1]
if command is None or date is None:
    stop_at_blank(1, f"28, 29번째 줄을 채울 것. 지금 args = {args}")

# [빈칸 2] 할 일에 맞는 tools.py 함수를 불러 결과를 result 에 담기
#          rank 면 1위 제목, audience 면 세 번째 칸의 영화 제목으로 관객 수
if command == "rank":
    result = tools.get_boxoffice_rank_1(date)
elif command == "audience" and len(args) >= 3:
    result = tools.get_movie_audience(date, args[2])
else:
    result = "쓰는 법: boxoffice.py rank 날짜 / boxoffice.py audience 날짜 영화제목"
if result is None:
    stop_at_blank(2, f"36번째 줄(rank) 또는 38번째 줄(audience)을 채울 것. command = {command}")

print(result)
