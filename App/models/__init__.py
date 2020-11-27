from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .order import Order
from .user import User
from .admin import Admin
from .customer import Customer
from .invoice import Invoice
from .payment import Payment
from .prescriptionOrder import PrescriptionOrder
from .product import Product
from .database import *
