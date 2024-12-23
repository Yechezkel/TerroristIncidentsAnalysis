import redis
import os
from dotenv import load_dotenv


load_dotenv()

def get_redis_client():
    try:
        client = redis.StrictRedis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), decode_responses=True)
        return client
    except Exception as e:
        print(f"Couldn't connect to redis, exception: {e}")
        return None



if __name__ == "__main__":
    client = get_redis_client()
    keys = client.keys('*')
    for key in keys:
        print(f"{key}: {client.get(key)}")
