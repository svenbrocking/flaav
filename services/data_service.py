from data.msgs import Msg
import random


def create_msg(content: str):
    msg = Msg()
    msg.content = content

    msg.save()

    return Msg


def get_msg():
    num_msgs = Msg.objects.count()
    n = random.randint(1, num_msgs + 1)
    msg = Msg.objects[n]

    return msg.content
