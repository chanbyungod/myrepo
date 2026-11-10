"""check.py — 키와 연결 확인 (도구 없이 한 문장만 주고받음)"""
import requests
from secret import GEMINI_API_KEY

URL = ("https://generativelanguage.googleapis.com/"
       "v1beta/openai/chat/completions")
MODEL = "gemini-3.5-flash-lite"

response = requests.post(
    URL,
    headers={"Authorization": f"Bearer {GEMINI_API_KEY}"},
    json={"model": MODEL,
          "messages": [{"role": "user", "content": "한 문장으로 인사해 줘."}]},
    timeout=60,
)
print("상태 코드:", response.status_code)
if response.status_code == 200:
    print("답:", response.json()["choices"][0]["message"]["content"])
else:
    print(response.text[:500])
