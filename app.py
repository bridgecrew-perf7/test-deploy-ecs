
from fastapi import FastAPI

app = FastAPI()

@app.get("/sum")
async def sun(a: int, b: int):
    return a+b

@app.get("/fer")
async def fer():
    return "hola"
