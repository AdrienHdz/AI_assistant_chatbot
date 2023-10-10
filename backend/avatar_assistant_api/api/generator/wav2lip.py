import replicate


class Wav2LipClientRunner:
    def __init__(self, AppSettings):
        self.input_video_path = AppSettings.input_video_path
        self.input_audio_path = AppSettings.input_audio_path
        self.replicate_model_id = AppSettings.replicate_model_id
        self.replicate_api_key = AppSettings.REPLICATE_API_TOKEN
        self.replicate_client = replicate.Client(api_token=self.replicate_api_key)

    def get_generated_wav2lip(self) -> str:
        url = self.replicate_client.run(
            self.replicate_model_id,
            input={
                "face": open(self.input_video_path, "rb"),
                "audio": open(self.input_audio_path, "rb"),
            },
        )
        return url
