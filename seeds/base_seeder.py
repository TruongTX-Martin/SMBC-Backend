class BaseSeeder:
    model_class = None
    require_truncate = False
    buck_insert = False

    def __init__(self, db):
        self.db = db

    def execute(self):
        if self.require_truncate:
            self.truncate()

        items = self._generate_data()
        if self.buck_insert:
            print(
                f'bulk inserting {len(items)} to {self.model_class.__tablename__}'
            )
            self.db.session.bulk_save_objects(
                [self.model_class(**item) for item in items],
                return_defaults=True)
        else:
            print(
                f'inserting {len(items)} to {self.model_class.__tablename__}')
            for item in items:
                self.insert_or_update(item['id'], item)

        self.db.session.commit()

    def insert_or_update(self, id_, fields):
        existing = self.model_class.query.filter_by(id=id_).first()
        if existing:
            for key in fields.keys():
                setattr(existing, key, fields[key])
            print('update existing id = {}'.format(id_))
            self.db.session.add(existing)
        else:
            model_ = self.model_class(**fields)
            print('insert new record id = {}'.format(id_))
            self.db.session.add(model_)

    def truncate(self):
        self.db.session.execute(f'SET FOREIGN_KEY_CHECKS = 0;')
        self.model_class.query.delete()
        self.db.session.commit()
        self.db.session.execute(f'SET FOREIGN_KEY_CHECKS = 1;')

    @staticmethod
    def _generate_data(self):
        return []
