import mongoengine
from data.config import *

alias_core = 'core'
db = 'flaav'

data = dict(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    authentication_source='admin',
    authentication_mechanism='SCRAM-SHA-1',
    ssl=False,
    # ssl_cert_reqs = ssl.CERT_NONE
)


def global_init():
    mongoengine.register_connection(alias='core', db='flaav')
