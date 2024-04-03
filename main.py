from fastapi import FastAPI

from upbit import Upbit

app = FastAPI()

# FastAPI 엔드포인트
@app.get("/accounts")
async def get_accounts():
    upbit = Upbit()
    accounts = await upbit.get_accounts()
    return accounts