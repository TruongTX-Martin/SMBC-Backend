from datetime import datetime
import json

import urllib3

from app.config import Config


class SlackHelper(object):
    http_client = urllib3.PoolManager()
    channel_name = Config.SLACK_CHANNEL_NAME
    webhook_url = Config.SLACK_WEBHOOK_URL
    webhook_user = Config.SLACK_WEBHOOK_USER

    @classmethod
    def prepare_message(cls, title='Message', message=''):
        body = {
            'channel': "#" + cls.channel_name,
            'username': cls.webhook_user,
            'text': title
        }
        try:
            body['attachments'] = [{
                'text': f'[{Config.FLASK_ENV}] - {message}',
                'fields': [{
                    'title': 'Time',
                    'value': datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                    'short': True,
                }],
            }]
            return body
        except Exception as e:
            return body

    @classmethod
    def send_error(cls, error):
        if not Config.SLACK_ENABLED:
            return False

        try:
            body = cls.prepare_message('Error', error)
            encoded_msg = json.dumps(body).encode('utf-8')
            resp = cls.http_client.request('POST',
                                           cls.webhook_url,
                                           body=encoded_msg)
            return True
        except Exception as e:
            return False
