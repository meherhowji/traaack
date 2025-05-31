from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/echo")
async def echo(request: Request):
    data = await request.json()
    return data
