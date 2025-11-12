FROM python:3.11-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000
VOLUME /models

CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "8000" ]