from app.models import EmailToken

from .base_repository import BaseRepository


class EmailTokenRepository(BaseRepository):
    model_class = EmailToken
