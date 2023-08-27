FROM python:latest
WORKDIR /app
COPY requirements.txt ./
COPY main.py ./
COPY .env ./

RUN pip install -r requirements.txt
CMD ['python', './main.py']