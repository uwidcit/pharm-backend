from flask import redirect, render_template, request, session, url_for

from App.models import Invoice
from App.models.database import db

def create_invoice(invoice_num, order_id):
    newInvoice = Invoice(invoice_number = invoice_num, order_id = order_id)
    db.session.add(newInvoice)
    db.session.commit()
    return newInvoice