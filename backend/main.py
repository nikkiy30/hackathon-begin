# def main():
#     print("Hello from backend!")


# if __name__ == "__main__":
#     main()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI起動成功！uvのおかげで爆速セットアップ完了です！"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}