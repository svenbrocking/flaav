from data.msgs import Msg
import random

# Save messages to the database
def create_msg(content: str) -> object:
    msg = Msg()
    msg.content = content

    msg.save()

    return Msg

# Get a random message from the database
def get_msg():
    verified_msgs = Msg.objects(verified=True)
    num_msgs = len(verified_msgs)
    n = random.randint(0, num_msgs -1)
    msg = verified_msgs[n].content
 
    return msg