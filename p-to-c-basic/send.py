#!/usr/bin/env python

import pika

rabbitmq_user="admin"
rabbitmq_password="admin"

credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="localhost",
    credentials=credentials
))

channel = connection.channel()
channel.queue_declare(queue="basic")

channel.basic_publish(
    exchange="",
    routing_key="basic",
    body="This is a basic p-to-c communication!"
)

print("[x] Message successfilly sent!")

connection.close()