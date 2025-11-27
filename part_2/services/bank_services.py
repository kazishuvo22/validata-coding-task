from models.bank_model import db, Bank
from werkzeug.exceptions import BadRequest

def fetch_all():
    return Bank.query.all()

def fetch_one(bank_id):
    return Bank.query.get_or_404(bank_id)

def create(name, location):
    if not name or not location:
        raise BadRequest("Both 'name' and 'location' are required.")
    bank = Bank(name=name, location=location)
    db.session.add(bank)
    db.session.commit()
    return bank

def update(bank_id, name, location):
    if not name or not location:
        raise BadRequest("Both 'name' and 'location' are required.")
    bank = Bank.query.get_or_404(bank_id)
    bank.name = name
    bank.location = location
    db.session.commit()
    return bank

def delete(bank_id):
    bank = Bank.query.get_or_404(bank_id)
    db.session.delete(bank)
    db.session.commit()
    return True