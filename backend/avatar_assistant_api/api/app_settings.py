from pydantic import BaseSettings


class AppSettings(BaseSettings):
    OPENAI_API_KEY: str
    REPLICATE_API_TOKEN: str
    ELEVENLABS_API_KEY: str

    ###OpenAi (response script)
    openai_model: str = "gpt-3.5-turbo"
    max_token: int = 100
    temperature: int = 1

    ###Elevenlabs (TextToSpeech)
    elevenlabs_voice_id: str = "XrExE9yKIg1WjnnlVkGX"
    elevenlabs_model_id: str = "eleven_multilingual_v1"
    stability: float = 0.5
    similarity_boost: float = 0.5
    chunk_size: int = 1024

    ###Replicate (Wav2Lip)
    input_video_path: str = "input_video.mp4"
    input_audio_path: str = "generated_speech.mp3"
    replicate_model_id: str = "devxpy/cog-wav2lip:8d65e3f4f4298520e079198b493c25adfc43c058ffec924f2aefc8010ed25eef"

    class Config:
        env_prefix = "APP_"
