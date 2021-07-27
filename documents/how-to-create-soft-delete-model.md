## How to create a soft delete model


## How to use?

Implement your model inherit soft delete model

```python
from .soft_delete_model import SoftDeleteModel


class User(SoftDeleteModel):
    __tablename__ = 'users'


    id = db.Column('id',
                   db.BigInteger().with_variant(sqlite.INTEGER(), 'sqlite'),
                   primary_key=True)
    email = db.Column('email', db.String(255), nullable=False)
```

## Detail design of Soft delete model

```python
from flask_sqlalchemy import BaseQuery

from ..database import db


class QueryWithSoftDelete(BaseQuery):
    def __new__(cls, *args, **kwargs):
        obj = super(QueryWithSoftDelete, cls).__new__(cls)

        if len(args) > 0:
            super(QueryWithSoftDelete, obj).__init__(*args, **kwargs)
            return obj.filter_by(deleted_at=None)
        return obj

    def __init__(self, *args, **kwargs):
        pass


class SoftDeleteModel(db.Model):
    __abstract__ = True

    __soft_delete__ = True

    query_class = QueryWithSoftDelete

    deleted_at = db.Column('deleted_at', db.TIMESTAMP, nullable=True)

```
