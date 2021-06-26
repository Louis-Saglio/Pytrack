FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install black

COPY . .

ENTRYPOINT ["python", "/app/entrypoint.py"]