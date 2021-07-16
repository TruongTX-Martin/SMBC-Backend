import boto3
from botocore.exceptions import ClientError
from flask import current_app

from app.config import Config
from app.exceptions import APIResponseError


class MailService(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = boto3.client('ses',
                                   region_name=Config.AWS_SES_REGION,
                                   aws_access_key_id=Config.AWS_KEY,
                                   aws_secret_access_key=Config.AWS_SECRET)

    def send_mail(self,
                  recipients: [],
                  subject: str = "",
                  content: str = "",
                  html: str = "") -> bool:
        try:
            # Provide the contents of the email.
            response = self.client.send_email(
                Destination={
                    'ToAddresses': recipients,
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': Config.MAIL_CHARSET,
                            'Data': html,
                        },
                        'Text': {
                            'Charset': Config.MAIL_CHARSET,
                            'Data': content,
                        },
                    },
                    'Subject': {
                        'Charset': Config.MAIL_CHARSET,
                        'Data': subject,
                    },
                },
                Source=Config.MAIL_SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
                # ConfigurationSetName=Config.MAIL_CONFIGURATION_SET,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            raise APIResponseError('Send email failed - {}'.format(
                e.response['Error']['Message']))
        else:
            current_app.logger.info("Email sent! Message ID:"),
            current_app.logger.info(response['MessageId'])

        return True
