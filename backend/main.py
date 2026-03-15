# def main():
#     print("Hello from backend!")


# if __name__ == "__main__":
#     main()

import os
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

# APIキーの設定
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    system_instruction="あなたはプロの販売員です。悩みに合わせた商品を1つ提案して。回答は簡潔に。"
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI起動成功！uvのおかげで爆速セットアップ完了です！"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}