from backend.app import ma
from backend.app import ma
from ..models import Project_Name, Project_Status


class Project_Name_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = Project_Name

    id = ma.auto_field()
    name = ma.auto_field()


class Project_Name_CRUP(ma.SQLAlchemySchema):
    class Meta:
        model = Project_Name

    name = ma.auto_field()


class Project_Status_CRUP(ma.SQLAlchemySchema):
    class Meta:
        model = Project_Status

    desc = ma.auto_field()
    next_id = ma.auto_field(missing=None)