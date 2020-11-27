from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from App.main import app
from App.models import (User, Admin, Customer)
from App.models.database import db
from App.controllers import (
    create_user,
    create_customer
)

manager = Manager(app)
migrate = Migrate(app, db)

#add migrate command
manager.add_command('db', MigrateCommand)

#add initDB command
'''@manager.command
def initDB():
    db.create_all(app=app)
    print('database initialized!')'''

if __name__ == "__main__":
    manager.run()

newUser = User("1000","Bob", "Smith","bob@email.com","bob")
print(newUser.toDict())
newCustomer = Customer(newUser)
print(newCustomer.toDict())

newUser = create_user("1100","Kim", "Jones","kim@email.com","kim")
newCustomer = create_customer(newUser)

newUser = create_user("1200","Mary", "White","mary@email.com","mary")
newCustomer = create_customer(newUser)

newUser = create_user("1300","Michael", "Doe","michael@email.com","michael")
newCustomer = create_customer(newUser)