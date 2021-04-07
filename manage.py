from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from App.main import app, db

from App.controllers import (
    parse_excel,
    get_products,
    delete_products,
    get_users,
    create_user,
    create_admin,
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
def addAdmin(fname, lname, email, password):
    user = create_user(fname, lname, email, password)
    admin = create_admin(user)
    return admin

@manager.command
def getUsers():
    x = get_users()
    print(x)

@manager.command
def products():
    products = get_products()
    print(products)

@manager.command
def addProducts():
    print('Calling parse excel')
    x = parse_excel()
    print('Done')

@manager.command
def getProducts():
    x = get_products()
    print(x)

@manager.command
def deleteProducts():
    x = delete_products()

if __name__ == "__main__":
    manager.run()

