from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from App.main import app, db

from App.controllers import (
    create_user,
    parse_excel,
    get_products,
    delete_products,
    create_customer,
    create_product,
    create_admin,
    get_product_by_name,
    get_users,
    create_cart,
    get_cart,
    set_checked_out,
    create_cart_item,
    delete_cart_item,
    get_cart_items,
    get_profile
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
def createCart():
    x = create_cart(1)
    print('Cart: ', x)

@manager.command
def getCart():
    x = get_cart(1)
    print('Cart: ', x)

@manager.command
def setCheckedOut():
    x = set_checked_out(1)
    print('Result: ', x)

@manager.command
def addCartItem():
    x = create_cart_item(2,1,5)
    print('Cart item: ', x.toDict())

    x = create_cart_item(2,2,7)
    print('Cart item: ', x.toDict())

    x = create_cart_item(2,3,9)
    print('Cart item: ', x.toDict())

@manager.command
def getCartItems():
    x = get_cart_items(2)
    print('Cart items:', x)

@manager.command
def removeCartItem():
    x = delete_cart_item(2,2)
    print('Result:', x)

@manager.command
def users():
    print('Creating user')
    #newUser = create_user("1101", "Kim", "Jones","kim@email.com", "kimpass")
    #newCustomer = create_customer(newUser)

    #newUser = create_user("1200","Mary", "White","mary@email.com","mary")
    #print(newUser.toDict())
    #newCustomer = create_customer(newUser)

    #newUser = create_user("1300","Michael", "Doe","michael@email.com","michael")
    #newCustomer = create_customer(newUser)

    #newUser = create_user("1400","Caleb", "Danvers","Caleb@email.com","caleb")
    #newAdmin = create_admin(newUser,"Pharmacist")

    #newUser = create_user("1500","Pogue", "Perry","pogue@email.com","pogue")
    #newAdmin = create_admin(newUser,"Pharmacist")
    #print(newAdmin.toDict())

    newUser = create_user("1000","Shiv", "Singh","shiv@email.com","shivpass")
    print(newUser.toDict())
    newAdmin = create_admin(newUser,"Pharmacist")
    print(newAdmin.toDict())

    newUser = create_user("2000", "Arun", "Singh","arun@email.com", "arunpass")
    print(newUser.toDict())
    newCustomer = create_customer(newUser)
    print(newCustomer.toDict())

    

@manager.command
def getUsers():
    x = get_users()
    print(x)

@manager.command
def products():
    #newProd = create_product("Advil","Pain Reliever","",2)
    #newProd = create_product("Panadol","Pain Reliever","",2)
    #newProd = create_product("Tylenol","Pain Reliever","",5)
    #products = get_all_products()
    product = get_product_by_name("Advil")
    print(product)

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

@manager.command
def getProfile():
    x = get_profile(1000)
    print(x)

if __name__ == "__main__":
    manager.run()

