import openai


class OpenAIChat:
    def __init__(self, AppSettings):
        self.model = AppSettings.openai_model
        self.max_token = AppSettings.max_token
        self.temperature = 1
        openai.api_key = AppSettings.OPENAI_API_KEY

    def get_response_script(self, input_message: str) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            max_tokens=self.max_token,
            temperature=self.temperature,
            messages=[
                {
                    "role": "system",
                    "content": """You are a customer service representative of Cymbal.
                                                 Here is Cymbal policy: How many days do I have to return my purchase?
                                                 We offer free returns and exchanges within 30 days of your delivery, with exceptions as described in our Returns Policy. Certain items are designated as final sale and not eligible for returns or exchanges. All on-sale purchases are final.""",
                },
                {"role": "user", "content": input_message},
            ],
        )
        response = response["choices"][0]["message"]["content"]
        return response
