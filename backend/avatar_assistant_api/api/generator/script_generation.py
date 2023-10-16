import openai

from api.cache.redis_helper import RedisHelper


class OpenAIChat:
    def __init__(self, AppSettings):
        self.model = AppSettings.openai_model
        self.max_token = AppSettings.max_token
        self.temperature = AppSettings.temperature
        openai.api_key = AppSettings.OPENAI_API_KEY

    def get_response_script(self, session_id: str, input_message: str) -> str:
        redis_helper = RedisHelper()

        # Check if a response for this session_id already exists in Redis
        prev_response = redis_helper.get(session_id)

        messages = [
            {
                "role": "system",
                "content": """You are a customer service representative of Cymbal.
                            Here is Cymbal policy: How many days do I have to return my purchase?
                            We offer free returns and exchanges within 30 days of your delivery, 
                            with exceptions as described in our Returns Policy. 
                            Certain items are designated as final sale and not eligible for returns or exchanges. 
                            All on-sale purchases are final.""",
            },
            {"role": "user", "content": input_message},
        ]

        # Append the previous response to the messages if it exists
        if prev_response:
            messages.append({"role": "assistant", "content": prev_response})

        response = openai.ChatCompletion.create(
            model=self.model,
            max_tokens=self.max_token,
            temperature=self.temperature,
            messages=messages,
        )
        response = response["choices"][0]["message"]["content"]

        # Store the latest response in Redis
        redis_helper.set(session_id, response)

        # If a previous response exists, print the latest response (optional, based on your requirements)
        if prev_response:
            redis_helper.print_latest_content(session_id)

        return response
