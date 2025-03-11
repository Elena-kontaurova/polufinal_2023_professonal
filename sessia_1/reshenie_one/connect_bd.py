''' j'''
from peewee import Model, MySQLDatabase, IntegerField, ForeignKeyField, \
                    CharField, DateField, DateTimeField

db = MySQLDatabase('prodi_poluf_2023', user='root', password='lenok',
                   host='localhost', port=3306)


class DataBase(Model):
    ''' k'''
    class Meta:
        ''' k'''
        database = db


class Project(DataBase):
    ''' k'''
    full_title = CharField()
    short_title = CharField()
    icon = CharField()
    created_time = DateTimeField()
    delete_time = DateTimeField()
    start_scheduled_date = DateField()
    finish_schedule_date = DateField()
    description = CharField()
    creator_employee_id = IntegerField()
    responsible_employe_id = IntegerField()


class TaskStatus(DataBase):
    ''' j'''
    name = CharField()
    color_hex = CharField()


class Task(DataBase):
    ''' k'''
    project_id = ForeignKeyField(Project, backref='task')
    full_title = CharField()
    short_title = CharField()
    description = CharField()
    executive_employeel_id = IntegerField()
    status_id = ForeignKeyField(TaskStatus, backref='task')
    created_time = DateTimeField()
    update_time = DateTimeField()
    daleted_time = DateTimeField()
    deadline = CharField()
    start_actual_time = DateTimeField()
    finish_actual_time = DateTimeField()
    previous_task_id = IntegerField()


db.connect()
db.create_tables([Project, TaskStatus, Task], safe=True)
db.close()
