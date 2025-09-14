FROM python:3.11-slim

WORKDIR /backend

ENV PYTHONPATH=/backend

RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
# COPY backend/ ./backend

COPY . .

EXPOSE 8000
