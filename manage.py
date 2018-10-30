from main import app
from flask_script import Manager
from DB_script import DB_manager


manager = Manager(app)

@manager.command
def runserver():
    '''
    there is document
    '''
    print('run!')


manager.add_command('前缀',DB_manager)
if __name__ == '__main__':
    manager.run()