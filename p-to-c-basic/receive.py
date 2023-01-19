#!/usr/bin/env python

import pika
import os
import sys

def main():
    rabbitmq_user="admin"
    rabbitmq_password="admin"

    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host="localhost",
        credentials=credentials
    ))
    channel = connection.channel()
    channel.queue_declare(queue="basic")

    def callback(ch, method, properties, body):
        print("[x] Message Received: %r" % body)

    channel.basic_consume(
        queue="basic",
        auto_ack=True,
        on_message_callback=callback
    )

    print('[*] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)