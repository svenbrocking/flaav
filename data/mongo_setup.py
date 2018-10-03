import mongoengine
from data.config import USERNAME, PASSWORD
# Define the database settings
alias_core = 'core'
db = 'flaav'

data = dict(
    username=USERNAME,
    password=PASSWORD,
    # host=HOST,
    # port=PORT,
    # authentication_source='admin',
    # authentication_mechanism='SCRAM-SHA-1',
    # ssl=False,
    # ssl_cert_reqs = ssl.CERT_NONE
)

# Database initialisation
def global_init():
    mongoengine.register_connection(alias='core', db='flaav', **data)
