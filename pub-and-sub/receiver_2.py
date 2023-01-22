#!/usr/bin/env python

import pika
import os
import sys
import time 

def main():
    rabbitmq_user="megamind"
    rabbitmq_password="asshole"

    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host="localhost",
        credentials=credentials
    ))
    channel = connection.channel()

    queue_name = "receiver_2"

    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    channel.queue_declare(queue=queue_name, durable=True)
    channel.queue_bind(exchange='logs', queue=queue_name)

    def callback(ch, method, properties, body):
        print("[x] Message Received: %r" % body)
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=queue_name,
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