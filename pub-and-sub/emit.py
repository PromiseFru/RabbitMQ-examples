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

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
    exchange="logs",
    routing_key="",
    body=message,
    properties=pika.BasicProperties(
        delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
    )
)

print("[x] Message successfilly sent!")

connection.close()