import requests


class TextToSpeech:
    def __init__(self, input_text: str, AppSettings):
        self.voice_id = AppSettings.elevenlabs_voice_id
        self.model_id = AppSettings.elevenlabs_model_id
        self.stability = AppSettings.stability
        self.similarity_boost = AppSettings.similarity_boost
        self.chunk_size = AppSettings.chunk_size
        self.elevenlabs_api_key = AppSettings.ELEVENLABS_API_KEY
        self.input_text = input_text

    def _get_headers(self) -> dict:
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.elevenlabs_api_key,
        }
        return headers

    def _get_data(self) -> dict:
        data = {
            "text": self.input_text,
            "model_id": self.model_id,
            "voice_settings": {
                "stability": self.stability,
                "similarity_boost": self.similarity_boost,
            },
        }
        return data

    def _get_url(self) -> str:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}/stream"
        return url

    def make_post_request(self):
        url = self._get_url()
        data = self._get_data()
        headers = self._get_headers()
        response = requests.post(url, json=data, headers=headers, stream=True)
        with open("generated_speech.mp3", "wb") as f:
            for chunk in response.iter_content(chunk_size=self.chunk_size):
                if chunk:
                    f.write(chunk)
