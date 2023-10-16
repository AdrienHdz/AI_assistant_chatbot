from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import logging
from uuid import uuid4

from api.generator.generator import get_openai_response, get_speech, get_wav2lip_url
from api.cache.cache import ROUTE_CACHING
from api.models.response_message import MessageRequest

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


@app.post("/get_response/")
@ROUTE_CACHING(ttl="3h", prefix="httproute")
async def get_message(message_request: MessageRequest):
    processed_message = message_request.message.lower()

    session_id = message_request.session_id or str(uuid4())

    openai_response = await get_openai_response(session_id, processed_message)

    await get_speech(openai_response)
    wav2lip_response = await get_wav2lip_url()

    return {
        "script_response": openai_response,
        "url_response": wav2lip_response,
        "session_id": session_id,
    }
