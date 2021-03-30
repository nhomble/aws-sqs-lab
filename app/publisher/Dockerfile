FROM python:3.7-alpine
WORKDIR /app

ENV APP_ENDPOINT=http://localhost:4566
ENV APP_SQS_NAME=hello

RUN apk add --no-cache gcc musl-dev linux-headers bash

COPY publisher.py publisher.py
COPY requirements.txt requirements.txt
COPY entrypoint.sh entrypoint.sh

RUN pip install -r requirements.txt

CMD ["bash", "/app/entrypoint.sh"]
