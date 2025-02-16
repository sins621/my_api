FROM python:3.9-slim-buster  # Or your preferred Python version

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 2000  # Flask default port
EXPOSE 3000

CMD ["python", "server.py"] # Or your Flask application entry point
