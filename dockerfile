FROM python:3.12-slim

WORKDIR /app

COPY factorial.py .

ENTRYPOINT ["python", "factorial.py"]
