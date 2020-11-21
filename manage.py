from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from App.main import app
from App.models import db

manager = Manager(app)
migrate = Migrate(app, db)

#add migrate command
manager.add_command('db', MigrateCommand)

#add initDB command
@manager.command
def initDB():
    db.create_all(app=app)
    print('database initialized!')

if __name__ == "__main__":
    manager.run()
