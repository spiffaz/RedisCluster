FROM python:3.9-slim

WORKDIR /app

COPY log_to_redis.py .

RUN pip install redis

CMD ["python", "log_to_redis.py"]
