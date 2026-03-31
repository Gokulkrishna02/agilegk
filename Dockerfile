FROM python:3.11-slim
WORKDIR /app
COPY Add.py .
RUN pip install flask
CMD ["python", "Add.py"]
