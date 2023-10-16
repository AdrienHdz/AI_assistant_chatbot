from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import logging

from api.generator.generator import get_openai_response, get_speech, get_wav2lip_url
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("log_file.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class MessageRequest(BaseModel):
    message: str


@app.on_event("startup")
async def on_startup():
    redis = RedisBackend("redis://redis:6379")
    FastAPICache.init(backend=redis, prefix="fastapi-cache")


@cache(expire=600)
@app.post("/get_response/")
async def get_message(message_request: MessageRequest):
    processed_message = message_request.message.lower()
    openai_response = await get_openai_response(processed_message)
    await get_speech(openai_response)
    wav2lip_response = await get_wav2lip_url()
    return {"script_response": openai_response, "url_response": wav2lip_response}
