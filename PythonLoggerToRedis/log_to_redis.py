import redis
import time
import os

redis_host = os.getenv("REDIS_HOST", "localhost")

def main():
    client = redis.Redis(host=redis_host, port=6379, db=0)

    while True:
        log_message = "Logging something to Redis at " + time.strftime("%Y-%m-%d %H:%M:%S")
        client.rpush("log_messages", log_message)
        print(f"Logged: {log_message}")
        time.sleep(60)

if __name__ == "__main__":
    main()
