from .base_entity import BaseEntity


class User(BaseEntity):
    def build_from_model(self):
        return {
            "id": self._model.id,
            "email": self._model.email,
        }
