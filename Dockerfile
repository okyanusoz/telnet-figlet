FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 23

CMD ["python", "main.py"]
