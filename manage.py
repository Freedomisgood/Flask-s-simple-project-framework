from app import app
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from models import *
# from DB_script import DB_manager


manager = Manager(app)
migrate = Migrate(app,db)


manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()