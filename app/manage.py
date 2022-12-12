import base64

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
import pymysql

from dbsession import db

pymysql.install_as_MySQLdb()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # autoincrement 默认是True
    username = db.Column(db.String(80), unique=True, comment="用户名")
    password = db.Column(db.String(120), comment="密码")
    role = db.Column(db.Integer, comment="用户角色")

    def to_json(self):
        info = {}
        info["id"] = self.id
        info["username"] = self.username
        info["password"] = self.password
        info["role"] = self.role
        return info


class ImageFile(db.Model):

    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(30), index=True)
    image = db.Column(db.LargeBinary(length=65535))
    dig_count = db.Column(db.Integer, default=0)
    belong_user = db.Column(db.Integer)
    comment = db.Column(db.String(200))

    def to_json(self):
        info = {}
        info["id"] = self.id
        info["image_name"] = self.image_name
        info["dig_count"] = self.dig_count
        info["belong_user"] = self.belong_user
        info["comment"] = self.comment
        info["image"] = "data:image/png;base64," + base64.b64encode(self.image).decode()

        return info


@manager.command
def deploy():
    """
    数据库升级命令
    migrate database to latest revision
    """
    user = User(username="admin", password="admin", role=1)
    db.session.add(user)
    db.session.commit()


if __name__ == "__main__":
    manager.run()