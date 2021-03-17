from backend.app import db


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    desc = db.Column(db.String(64))

    def __repr__(self):
        return '<Todo %r>' % self.name
