from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


BaseModel = declarative_base()


class Todo(BaseModel):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    descr = Column(String(64))

    def __repr__(self):
        return '<Todo %r>' % self.name
