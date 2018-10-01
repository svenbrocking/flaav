from data.msgs import Msg
import random


def create_msg(content: str) -> object:
    msg = Msg()
    msg.content = content

    msg.save()

    return Msg


def get_msg():
    # num_msgs = Msg.objects.count()
    num_msgs = Msg.objects(verified=True).count()
    n = random.randint(0, num_msgs)
    msg = Msg.objects(verified=True)[n]

    return msg.content
