from data.msgs import Msg


def create_msg(content: str) -> Msg:
    msg = Msg()
    msg.content = content

    msg.save()

    return Msg
