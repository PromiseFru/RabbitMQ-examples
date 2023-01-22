#!/usr/bin/env python

import pika
import sys

rabbitmq_user="megamind"
rabbitmq_password="asshole"

credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="localhost",
    credentials=credentials
))

channel = connection.channel()
channel.queue_declare(queue="basic", durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
    exchange="",
    routing_key="basic",
    body=message,
    properties=pika.BasicProperties(
        delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
    )
)

print("[x] Message successfilly sent!")

connection.close()