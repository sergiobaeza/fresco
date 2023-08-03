FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

RUN apt update -y && apt upgrade -y

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "fresco.wsgi" ]
