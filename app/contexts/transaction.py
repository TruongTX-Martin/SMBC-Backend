from contextlib import contextmanager

from ..database import db


@contextmanager
def transaction():
    try:
        db.session.info['in_transaction'] = True
        yield
        db.session.info['in_transaction'] = False
        db.session.commit()
    except Exception as e:
        db.session.info['in_transaction'] = False
        db.session.rollback()
        raise
