#!/usr/bin/env python3

import time
import boto3
import os
from datetime import datetime

endpoint = os.environ.get("APP_ENDPOINT", "http://localhost:4566")
queue_name = os.environ.get("APP_SQS_NAME", "hello")

print(f"Starting... {endpoint} {queue_name}")
sqs = boto3.resource('sqs',
    endpoint_url=endpoint,
    region_name='us-east-1',
    aws_access_key_id="foo",
    aws_secret_access_key="bar",
    aws_session_token="baz")

queue = sqs.create_queue(QueueName=queue_name)

while True:
    queue.send_message(MessageBody=f"ping {datetime.now()}")
    time.sleep(15)
