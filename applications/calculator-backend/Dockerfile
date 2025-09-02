FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY application /app/application

CMD ["python", "application/main.py"]
