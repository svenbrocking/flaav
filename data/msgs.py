import datetime
import mongoengine


class Msg(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    content = mongoengine.StringField(required=True)
    verified = mongoengine.BooleanField(default=False)

    meta = {
        'db_alias': 'core',
        'collection': 'msgs'
    }