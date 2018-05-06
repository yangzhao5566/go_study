# coding=utf-8

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='compute_queue')
print(' [*] Waiting for n')


def increase(n):
    return n + 1


# 定义接收到消息的处理方法
def request(ch, method, properties, body):
    print(" [.] increase(%s)" % (body,))
    response = increase(int(body))

    # 将计算结果发送回控制中心
    ch.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        body=str(response)
    )

channel.basic_qos(prefetch_count=1)

channel.basic_consume(request, queue='compute_queue')

channel.start_consuming()
