FROM python:3.8-slim-buster
RUN mkdir -p /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD python main.py
