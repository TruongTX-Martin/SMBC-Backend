import hashlib
from pathlib import Path
import random
import string
import time
from typing import List


class Base(object):
    def create_file(self,
                    path: Path,
                    media_type: str,
                    parent_dirs: List = None) -> str:
        pass

    def get_url(self, key: str) -> str:
        pass

    @staticmethod
    def _generate_key(name) -> str:
        return str(
            hashlib.sha256((name + "".join([
                random.choice(string.ascii_letters + string.digits)
                for i in range(4)
            ]) + str(time.time())).encode()).hexdigest())
