from qa327.models import db, User, Tickets
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all backend logic that interacts with database and other services
"""


def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw)

    db.session.add(new_user)
    db.session.commit()
    successfulRegister = db.session.query(User.email).filter_by(email=email).scalar() is not None
    return successfulRegister


def get_all_tickets():
    return db.session.query(Tickets).all()


def get_ticket(ticket_name):
    ticket = Tickets.query.filter_by(ticket_name=ticket_name).first()  # whoever did this - it won't work!
    return ticket


def ticket_exist(ticket_name):
    value = Tickets.query.filter_by(ticket_name=ticket_name).first()
    if value is None:
        return False
    else:
        return True


def get_ticket_quantity(ticket_name):
    if ticket_exist(ticket_name):
        ticket = Tickets.query.filter_by(ticket_name=ticket_name).first()
        quantity = ticket.quantity
        return quantity
    else:
        return -1


def get_ticket_price(ticket_name):
    if ticket_exist(ticket_name):
        ticket = Tickets.query.filter_by(ticket_name=ticket_name).first()
        price = ticket.price
        return price
    else:
        return -1


def get_user_balance(user):
    return 50000


def add_tickets(ticket_name, quantity, price, expiration_date):
    new_ticket = Tickets(ticket_name=ticket_name, quantity=quantity, price=price, expiration_date=expiration_date)
    if not db.session.query(Tickets.ticket_name).filter_by(ticket_name=ticket_name).scalar():  # ticket not in db
        db.session.add(new_ticket)
        db.session.commit()
    successfulTicket = db.session.query(Tickets.ticket_name).filter_by(ticket_name=ticket_name).scalar() is not None
    return successfulTicket


def profile_user(balance, ticket_name, quantity, price, expiration_date):
    # user_balance = User(balance = balance)
    new_ticket = Tickets(ticket_name=ticket_name, quantity=quantity, price=price, expiration_date=expiration_date)
    db.session.add(new_ticket)
    # db.session.add(user_balance)
    db.session.commit()
    return new_ticket
