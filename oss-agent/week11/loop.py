"""loop.py — 에이전트 동작 루프 (11주차)

빈칸 세 곳을 채우면 7주차 tools.py 를 도구로 쓰는 에이전트가 된다.
빈칸에 도착하면 안내를 출력하고 멈춘다. 오류가 아니라 '여기까지 왔다'는 표시.
"""
import json
import requests
import tools
from secret import GEMINI_API_KEY

# ---------- 설정 ----------
URL = ("https://generativelanguage.googleapis.com/"
       "v1beta/openai/chat/completions")
MODEL = "gemini-3.5-flash-lite"
MAX_TURNS = 5          # 반복 상한. 이 바퀴 수를 넘기면 멈춘다

# ---------- 도구 목록: 모델에게 보여 줄 설명 ----------
TOOLS = [
    {"type": "function",
     "function": {
         "name": "get_boxoffice_rank_1",
         "description": "그 날짜의 박스오피스 1위 영화 제목을 알려준다.",
         "parameters": {
             "type": "object",
             "properties": {
                 "date": {"type": "string",
                          "description": "8자리 날짜. 예: 20260824"}},
             "required": ["date"]}}},
    {"type": "function",
     "function": {
         "name": "get_movie_audience",
         "description": "그 날짜에 특정 영화를 본 관객 수를 알려준다.",
         "parameters": {
             "type": "object",
             "properties": {
                 "date": {"type": "string",
                          "description": "8자리 날짜. 예: 20260824"},
                 "title": {"type": "string",
                           "description": "영화 제목"}},
             "required": ["date", "title"]}}},
]

# ---------- 이름으로 실제 함수를 찾는 사전 ----------
FUNCTIONS = {
    "get_boxoffice_rank_1": tools.get_boxoffice_rank_1,
    "get_movie_audience": tools.get_movie_audience,
}


def ask_model(messages):
    """지금까지의 대화 전체와 도구 목록을 보내고, 모델의 답 메시지를 받는다."""
    response = requests.post(
        URL,
        headers={"Authorization": f"Bearer {GEMINI_API_KEY}"},
        json={"model": MODEL, "messages": messages, "tools": TOOLS},
        timeout=60,
    )
    if response.status_code != 200:
        raise SystemExit(f"요청 실패 (상태 코드 {response.status_code})\n"
                         f"{response.text[:500]}")
    return response.json()["choices"][0]["message"]


def stop_at_blank(number, where, hint, data=None):
    """빈칸에 도착하면 채울 줄과 안내를 출력하고 멈춘다."""
    print(f"\n[빈칸 {number}] 여기까지 진행됨 → loop.py {where}번째 줄을 채울 것")
    print(hint)
    if data is not None:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    raise SystemExit


def run(question):
    messages = [{"role": "user", "content": question}]

    for turn in range(1, MAX_TURNS + 1):
        message = ask_model(messages)
        messages.append(message)            # 받은 메시지는 받은 그대로 넣는다
        print(f"[{turn}바퀴] 대화 길이: {len(messages)}")

        if not message.get("tool_calls"):   # 도구 호출이 없으면 최종 답
            return message.get("content")

        for call in message["tool_calls"]:
            # [빈칸 1] 응답에서 도구 이름과 인자 꺼내기
            #   call 안에서 도구 이름(name)과 인자(args)를 꺼낸다
            #   인자는 글자(JSON 문자열)로 오므로 json.loads 로 딕셔너리로 바꾼다
            name = call["function"]["name"]
            args = json.loads(call["function"]["arguments"])
            if name is None or args is None:
                stop_at_blank(1, "88, 89", '아래 { … } 전체가 변수 call 임. call["칸 이름"] 으로 한 겹씩 꺼낼 것.', call)
            print(f"  도구 호출: {name} {args}")

            # [빈칸 2] 이름으로 함수를 찾기
            #   FUNCTIONS 사전에서 name 에 해당하는 함수를 꺼내 func 에 담는다
            func = None
            if func is None:
                stop_at_blank(2, "96", f"FUNCTIONS 사전에서 '{name}' 함수를 꺼내 func 에 담을 것.")
            result = func(**args)
            print(f"  도구 결과: {result}")

            # [빈칸 3] 결과를 대화에 다시 넣기
            #   role 은 "tool", 어느 호출의 결과인지(tool_call_id),
            #   도구 이름(name), 결과(content)
            tool_message = None
            if tool_message is None:
                stop_at_blank(3, "105", "결과를 대화에 넣을 메시지를 만들 것. "
                                           "넣지 않으면 모델은 결과를 모름.")
            messages.append(tool_message)

    return f"{MAX_TURNS}바퀴를 돌아도 끝나지 않아 멈춤."


if __name__ == "__main__":
    question = ("2026년 11월 8일 박스오피스 2위 영화는 뭐야?")
    print("질문:", question)
    print("최종 답:", run(question))
