from api.generator.script_generation import OpenAIChat
from api.generator.text_to_speech import TextToSpeech
from api.generator.wav2lip import Wav2LipClientRunner
from api.app_settings import AppSettings


async def get_openai_response(input_message: str) -> str:
    response = OpenAIChat(AppSettings=AppSettings()).get_response_script(
        input_message=input_message
    )
    return response


async def get_speech(input_message: str):
    speech = TextToSpeech(input_text=input_message, AppSettings=AppSettings())
    speech.make_post_request()


async def get_wav2lip_url():
    video_url = Wav2LipClientRunner(AppSettings=AppSettings()).get_generated_wav2lip()
    return video_url
