from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from App.main import app, db

from App.controllers import (
    create_user,
    create_customer
)

manager = Manager(app)
migrate = Migrate(app, db)

#add migrate command
manager.add_command('db', MigrateCommand)

#add initDB command
@manager.command
def initDB():
    db.create_all(app=app)
    print('database initialized!')

@manager.command
def users():
    #newUser = create_user("1101", "Kim", "Jones","kim@email.com", "kimpass")
    #newCustomer = create_customer(newUser)

    #newUser = create_user("1200","Mary", "White","mary@email.com","mary")
    #print(newUser.toDict())
    #newCustomer = create_customer(newUser)

    newUser = create_user("1300","Michael", "Doe","michael@email.com","michael")
    #newCustomer = create_customer(newUser)

if __name__ == "__main__":
    manager.run()

