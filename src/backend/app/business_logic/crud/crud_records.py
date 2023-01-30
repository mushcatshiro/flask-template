from ..schemas import Project_Name_Schema, Project_Status
from ..models import Project_Name, Project_Status
from ..custom_exceptions import ResourceNotFoundError


def create_new_project(db, new_project):
    proj = Project_Name(**new_project)
    db.session.add(proj)
    db.session.commit()
    db.session.refresh(proj)
    '''
    TODO - to verify if relation is also returned
    '''
    return Project_Name_Schema().dump(proj)


def create_new_status(db, new_status):
    stat = Project_Status(**new_status)
    db.session.add(stat)
    db.session.commit()
    db.session.refresh(stat)
    return Project_Status().dump(stat)