''' j'''
from peewee import Model, MySQLDatabase, IntegerField, ForeignKeyField, \
                    CharField, DateField, DateTimeField, TextField, \
                    DecimalField, BooleanField, AutoField

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
    id = AutoField()
    name = CharField()
    color_hex = CharField()


class Task(DataBase):
    ''' k'''
    id = AutoField()
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
    finish_actual_time = DateTimeField(null=True)
    previous_task_id = CharField()
    icon = CharField()


class Observer(DataBase):
    ''' k'''
    task_id = ForeignKeyField(Task, backref='observers')
    employee_id = IntegerField()


class Comment(DataBase):
    ''' k'''
    task_id = ForeignKeyField(Task, backref='comments')
    employee_id = IntegerField()
    comment_text = TextField()
    create_date = DateTimeField()


class Attachment(DataBase):
    '''m '''
    task_id = ForeignKeyField(Task, backref='attachments')
    file_path = CharField()
    create_date = DateTimeField()


class StatusHistory(DataBase):
    ''' k'''
    task_id = ForeignKeyField(Task, backref='status_history')
    old_status_id = IntegerField()
    new_status_id = IntegerField()
    change_date = DateTimeField()


class ProjectPortfolio(DataBase):
    ''' j'''
    name = CharField()
    description = TextField()
    create_date = DateTimeField()


class PortfolioProject(DataBase):
    ''' k'''
    portfolio = ForeignKeyField(ProjectPortfolio, backref='projects')
    project = ForeignKeyField(Project, backref='portfolios')


class PortfolioCategory(DataBase):
    ''' k'''
    parent_category = ForeignKeyField('self', backref='subcategories')
    name = CharField()


class ProjectPortfolioAssociation(DataBase):
    ''' k'''
    project = ForeignKeyField(Project, backref='portfolios')
    portfolio = ForeignKeyField(ProjectPortfolio, backref='project')
    category = ForeignKeyField(PortfolioCategory, backref='associations')


class ProjectAnalytics(DataBase):
    ''' k'''
    project = ForeignKeyField(Project, backref='analytics')
    report_date = DateField()
    budget = DecimalField()
    actual_expense = DecimalField()
    task_completed = IntegerField()
    task_pending = IntegerField()


class User(DataBase):
    ''' k'''
    full_name = CharField()
    organization = CharField()


class Email(DataBase):
    ''' k'''
    sender = ForeignKeyField(User, backref='send_email')
    recipient = ForeignKeyField(User, backref='recieved_email')
    subject = CharField()
    description = TextField()
    date_send = DateTimeField()
    is_replied = BooleanField(default=False)


class TaskEmail(DataBase):
    ''' k'''
    email = ForeignKeyField(Email, backref='tasks')
    description = TextField()
    status = CharField(choices=[('Current', 'Текущая'),
                                ('Overdue', 'Простроченная')],
                       default='Current')
    deadline = DateTimeField()
    create_date = DateTimeField()


class TaskTask(DataBase):
    ''' j'''
    id = AutoField()
    idtask = ForeignKeyField(Task, backref='tasktask')
    nubver = CharField()
    vaib = CharField()
    opinasin = CharField()
    name = CharField()
    dedline = DateTimeField()


db.connect()
db.create_tables([Project, TaskStatus, Task, Observer, Comment,
                  Attachment, StatusHistory, ProjectPortfolio,
                  PortfolioProject, PortfolioCategory,
                  ProjectPortfolioAssociation, ProjectAnalytics,
                  User, Email, TaskEmail, TaskTask], safe=True)
db.close()
