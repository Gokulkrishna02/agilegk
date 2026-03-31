FROM python:3.11-slim
WORKDIR /app
COPY Add.py .
CMD ["python", "Add.py"]