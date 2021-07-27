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

[soft_delete_model.py](../app/models/soft_delete_model.py)
