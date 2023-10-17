from redis import Redis


class RedisHelper:
    def __init__(self, host: str, port: int):
        self.client = Redis(host=host, port=port)

    def get(self, key):
        value = self.client.get(key)
        return value.decode("utf-8") if value else None

    def set(self, key, value):
        self.client.set(key, value)

    def get_all_keys(self):
        return self.client.keys("*")

    def print_latest_content(self, session_id):
        value = self.get(session_id)
        if value:
            print(session_id, value)
