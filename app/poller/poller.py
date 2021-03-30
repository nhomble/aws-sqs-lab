#!/usr/bin/env python3

import time
import boto3
import os

endpoint = os.environ.get("APP_ENDPOINT", "http://localhost:4566")
queue_name = os.environ.get("APP_SQS_NAME", "hello")

print(f"Starting... {endpoint} {queue_name}")
sqs = boto3.resource('sqs',
    endpoint_url=endpoint,
    region_name='us-east-1',
    aws_access_key_id="foo",
    aws_secret_access_key="bar",
    aws_session_token="baz")

print("Created client...")
queue = sqs.get_queue_by_name(QueueName=queue_name)

print("Polling...")
while True:
    print("Another poll...")
    for message in queue.receive_messages():
        print(f"polled message={message.body}")
    time.sleep(10)
