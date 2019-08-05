import clx.xms
import json
import os
from flask import Flask

app = Flask(__name__)

client = clx.xms.Client(
    os.environ.get('SINCH_SERVICE_PLAN_ID'),
    os.environ.get('SINCH_API_TOKEN')
)


@app.route('/send-sms/<recipient>/')
def send_sms(recipient):
    result = client.create_text_message(
        sender=os.environ.get('SINCH_SENDER'),
        recipient=recipient,
        body='This is a test message from your Sinch account :)'
    )
    print('result', result)
    return 'Message sent!'