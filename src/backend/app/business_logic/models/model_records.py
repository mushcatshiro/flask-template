from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


BaseModel = declarative_base()


class Project_Name(BaseModel):
    __tablename__ = 'project_name'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    project_status = relationship("Project_Status")

    def __repr__(self):
        return '<Project Name %r>' % self.name


class Project_Status(BaseModel):
    __tablename__ = 'project_status'
    ref_id = Column(Integer, ForeignKey('project_name.id'))
    id = Column(Integer, primary_key=True)
    desc = Column(String(64))
    next_id = Column(Integer, default=None)

    def __repr__(self):
        return '<ProjectName %r>' % self.name
    
    '''
    [
        {id:1, nid:2}, {id:2, nid:},
        {id:3, nid:4}, {id:4, nid:5}, {id:5, nid:}
    ] 
    ->
    [
        [1, 2],
        [3, 4, 5]
    ]
    '''
    
    def get_status_list(self):
        status_list = []
        return