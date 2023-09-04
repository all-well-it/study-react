from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from redis import StrictRedis
import os
import logging
from logging import config

config.fileConfig("logging.conf")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = StrictRedis(os.getenv('REDIS_HOST'), charset="utf-8")
graphs = {}


@app.get("/")
async def root():
    return {"message": "healthy"}


@app.post("/save")
async def save(x: dict):
    logging.info(x)
    redis.json().set('my_key', '.', {'value': x.get("value")})
    redis.save()
    logging.info(f'saved: {x.get("value")}')
    return {"message": "saved"}


@app.get("/read")
async def read():
    value = redis.json().get('my_key')
    logging.info(f'read {value}')
    return {"message": value}


@app.api_route("/{path_name:path}", methods=["GET", "POST"])
async def catch_all(request: Request, path_name: str):
    print(f'ERROR BAD REQUEST: {path_name}')
    raise HTTPException(status_code=404)
