import os
from pathlib import Path
from typing import List

import boto3

from app.config import Config

from .base import Base


class S3(Base):
    @staticmethod
    def _get_client():
        return boto3.client('s3',
                            aws_access_key_id=Config.AWS_KEY,
                            aws_secret_access_key=Config.AWS_SECRET,
                            region_name=Config.STORAGE_S3_REGION)

    def create_file(self,
                    path: Path,
                    media_type: str,
                    parent_dirs: List = None) -> str:
        key = self._generate_key(path.name)
        if parent_dirs:
            key = "/".join(parent_dirs + [key])

        s3 = self._get_client()
        s3.upload_file(Filename=str(path.resolve()),
                       Bucket=Config.STORAGE_S3_BUCKET_NAME,
                       Key=key,
                       ExtraArgs={'ContentType': media_type})

        return key

    def get_url(self, key: str) -> str:
        s3 = self._get_client()
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': Config.STORAGE_S3_BUCKET_NAME,
                'Key': key
            },
            ExpiresIn=180,
            HttpMethod='GET')

        return url
