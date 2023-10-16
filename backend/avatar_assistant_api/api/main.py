from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import logging

from api.generator.generator import get_openai_response, get_speech, get_wav2lip_url

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


@app.post("/get_response/")
async def get_message(request: MessageRequest):
    processed_message = request.message.lower()
    openai_response = await get_openai_response(processed_message)
    await get_speech(openai_response)
    wav2lip_response = await get_wav2lip_url()
    return {"script_response": openai_response, "url_response": wav2lip_response}
