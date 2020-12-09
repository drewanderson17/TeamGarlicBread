from flask import render_template, request, session, redirect
from qa327 import app
import qa327.backend as bn

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""


def validEmailFormat(email):
    email, printableChars = email.lower(), ['!', '#', '$', '%', '&', "'", '*', '+', '-', '/',
                                            '=', '?', '^', '_', '`', '{', '|', '}', '~', '.']
    try:
        atIdx = email.index('@')
    except:
        atIdx = None
    if atIdx:
        localPart = email[:atIdx]
        domainPart = email[atIdx + 1:]
    else:
        return False

    if localPart == "" or domainPart == "":
        return False

    for e, char in enumerate(localPart):
        if e > 0 and char == '.' and localPart[e - 1] == '.':  # checks for consecutive '.'
            return False
        if e == len(localPart) - 1 and char == '.':  # if last character is a '.'
            return False
        if e == 0 and char == '.':  # if first character is a '.'
            return False
        if char not in printableChars and not (97 <= ord(char) <= 122) and not (
                48 <= ord(char) <= 57):  # invalid character
            return False

    domainPeriodCount = 0
    for e, char in enumerate(domainPart):
        if char == '.' and domainPeriodCount == 0:
            domainPeriodCount = 1
            continue
        if char == '-' and (e == 0 or e == len(domainPart) - 1):  # can't have '-' as first or last character
            return False
        if not ((97 <= ord(char) <= 122) or (48 <= ord(char) <= 57) or char == '-'):  # ensures alphanumeric values or -
            return False
    return True


def validPassword(password):
    if len(password) < 6:
        return False
    specialChar, upperChar, lowerChar = False, False, False
    for char in password:
        if 97 <= ord(char) <= 122:
            lowerChar = True
        if 65 <= ord(char) <= 90:
            upperChar = True
        if not (97 <= ord(char) <= 122) and not (65 <= ord(char) <= 90):
            specialChar = True
    return specialChar and upperChar and lowerChar


def validName(name):
    if len(name) < 2 or len(name) > 20:
        return False
    upperChar, lowerChar = False, False

    for char in name:
        if 97 <= ord(char) <= 122:
            lowerChar = True
        if 65 <= ord(char) <= 90:
            upperChar = True
    return lowerChar and upperChar


@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    # R2:password and password 2 meet requirements as defined by R1
    if password != password2:  # password && password2 must match thus they must both meet the same requirements
        error_message = "The passwords do not match"
    elif email == "" or password == "":
        error_message = "Email/Password cannot be empty"
    elif len(email) < 1:
        error_message = "Email format error"
    elif len(password) < 1:
        error_message = "Password not strong enough"
    elif not validEmailFormat(email):
        error_message = "Invalid email/password format"
    elif not validPassword(password):
        error_message = "Invalid email/password format"
    else:
        user = bn.get_user(email)  # R2 if email exists displayy error message
        if user:
            error_message = "User exists"
        elif not bn.register_user(email, name, password, password2):
            error_message = "Failed to store user info."

    # R2: if user name has formatting error
    if not validName(name):
        error_message = "incorrect format of user name"

    # if there is any error messages when registering new user
    # at the backend, go back to the register page 
    # satisfies R2 requirement for redicrect with user name errors
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        # R2: if no error increase balance by 5000 and redirecto to login
        # balance = bn.get_user(balance) + 5000     This makes no sense :)
        return redirect('/login')


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = bn.login_user(email, password)
    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.
        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.
        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)  # change redirect
    if validEmailFormat(email) and validPassword(password):
        message = 'email/password combination incorrect'
    else:
        message = "Email/password format is incorrect"
    if email == "" or password == "":
        message = 'Email/Password cannot be empty'
    return render_template('login.html', message=message)


@app.route('/', methods=['POST'])
def profile_post():
    ticket_name = request.form.get('ticket_name')
    quantity = request.form.get('quantity')
    price = request.form.get('price')
    expiration_date = request.form.get('expiration_date')
    return render_template('index.html', message='sucessful')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
        # if the user has logged in redirect to profile page
        return redirect('/')
    # otherwise show the user registration page
    else:
        return redirect('/register')


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object
    Wrap any python function and check the current session to see if
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.
    To wrap a function, we can put a decoration on that function.
    Example:
    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


'''
@app.route('/', methods=['GET'])
@authenticate
def profile_get():
    tickets = bn.get_all_tickets()
    return render_template('index.html', message='Hi test!', tickets=tickets)
'''


@app.route('/', endpoint='auth_func1')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    tickets = bn.get_all_tickets()
    return render_template('index.html', message=user.name, user=user, tickets=tickets)


@app.errorhandler(404)
def error404(error):
    return render_template('error.html')


# R4 Below


@app.route('/sell', methods=['GET'], endpoint="get_end")
@authenticate
def sell(user):
    return render_template('sell.html', user=user, message=user.name, error_message="")


def validTicketName(ticketName):
    for e, c in enumerate(ticketName):
        if c == " " and (e == 0 or e == len(ticketName) - 1):
            return False
        if not (48 <= ord(c) <= 57 or 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122 or c == " "):
            return False
    return len(ticketName) <= 60


def validQuantity(numOfTickets):
    return 0 < numOfTickets <= 100


def validPrice(ticketPrice):
    return 10 <= ticketPrice <= 100


def validDate(date):
    days = date % 100
    date //= 100
    month = date % 100
    date //= 100
    year = date
    return year >= 2020 and 1 <= month <= 12 and 1 <= days <= 31


# NOTE: if there is an error I don't redirect to '/' but stay on '/sell' so the user can try and add their ticket again
@app.route('/sell', methods=['POST'], endpoint='post_end')
@authenticate
def sellValidTicket(user):
    ticket_name = request.form.get('ticket_name')
    quantity = request.form.get('quantity')
    price = request.form.get('price')
    expiration_date = request.form.get('expiration_date')

    badName = render_template('sell.html', user=user, message=user.name, error_message="Ticket name is invalid")
    badQuantity = render_template('sell.html', user=user, message=user.name, error_message="Ticket quantity is invalid")
    badPrice = render_template('sell.html', user=user, message=user.name, error_message="Ticket price is invalid")
    badDate = render_template('sell.html', user=user, message=user.name, error_message="Ticket date is invalid")

    try:
        quantity = int(quantity)
    except Exception as e:
        return badQuantity
    try:
        price = int(price)
    except Exception as e:
        return badPrice
    try:
        expiration_date = int(expiration_date)
    except Exception as e:
        return badDate

    if not validTicketName(ticket_name):
        return badName
    if not validQuantity(quantity):
        return badQuantity
    if not validPrice(price):
        return badPrice
    if not validDate(expiration_date):
        return badDate
    ticketAdded = bn.add_tickets(ticket_name, quantity, price, expiration_date)
    return render_template('sell.html', user=user, message=user.name, error_message="Ticket added successfully!") if \
        ticketAdded \
        else render_template('sell.html', user=user, message=user.name, error_message="Ticket could not be added!")


#  R6 buy tickets

@app.route('/buy', methods=['GET'], endpoint="buy_end")
@authenticate
def buy(user):
    return render_template('buy.html', user=user, message=user.name, error_message="")


# R6.1, R6.2 and part of R6.4 checks if ticket exist and name is valid format
def validTicket(ticket_name):
    val = validTicketName(ticket_name)
    return bn.ticket_exist(ticket_name) and val


# R6.3 and part of R6.4 the quantity is more than the quantity requested and quant is [0,100]
# bn.get_ticket_quantity will return -1 if ticket isn't found
def valid_quantity_buy(numTickets, ticket_name):
    availTickets = bn.get_ticket_quantity(ticket_name)
    return availTickets - numTickets  # return difference between tickets bought and sold
    # (0 <= numTickets <= 100) and (numTickets > availTickets)


# R6.5 test user balance, for the purpose of testing every user start with balance of 300
def validBalance(quantity, ticket_name):
    price = bn.get_ticket_price(ticket_name)
    balance = bn.get_user_balance('user')
    total = quantity * price
    total_w_tax = (total + (total * 0.35) + (total * 0.05))
    return balance - total_w_tax


@app.route('/buy', methods=['POST'], endpoint='posted_end')
@authenticate
def sellValidTicket2(user):
    ticket_name = request.form.get('ticket_name')
    quantity = request.form.get('quantity')

    bad_Quantity = render_template('buy.html', user=user, message=user.name,
                                   error_message="Error: Ticket quantity must be between [0,100]")
    badBuy = render_template('buy.html', user=user, message=user.name,
                             error_message="Error: Invalid Quantity (Tried To Buy "
                                           "Too Many Tickets)")
    badBalance = render_template('buy.html', user=user, message=user.name,
                                 error_message="Error: account balance is invalid")
    bad_ticket_null = render_template('buy.html', user=user, message=user.name,
                                      error_message="Error: Ticket does not exist")

    bad_ticket_name = render_template('buy.html', user=user, message=user.name,
                                      error_message="Error: invalid Ticket name")
    try:
        quantity = int(quantity)
    except Exception as e:
        return bad_Quantity
    diff = valid_quantity_buy(quantity, ticket_name)

    if not validTicketName(ticket_name):
        return bad_ticket_name

    if not validTicket(ticket_name):
        return bad_ticket_null

    if (valid_quantity_buy(quantity, ticket_name)) < 0:
        return badBuy

    if not validQuantity(quantity):
        return bad_Quantity

    balance = validBalance(quantity, ticket_name)
    if validBalance(quantity, ticket_name) < 0:
        return badBalance

    else:
        return render_template('buy.html', user=user, message=user.name,
                               error_message="Tickets bought successfully!")
        # add information to update the ticket


# R5 Requirements
@app.route('/update', methods=['GET'], endpoint="update_end")
@authenticate
def update(user):
    return render_template('update.html', user=user, message=user.name, error_message="")


# R5.1, 5.2 Check valid ticket name
def validTicket2(ticket_name):
    val = validTicketName(ticket_name)
    return bn.ticket_exist(ticket_name) and val


# R5.3 Check quantity of tickets
def validQuantity2(numOfTickets):
    return 0 <= numOfTickets <= 100


# R5.4 Ticket price
def validPrice2(ticketPrice):
    return 10 <= ticketPrice <= 100


# R5.5 Check date format
def validDate2(date):
    days = date % 100
    date //= 100
    month = date % 100
    date //= 100
    year = date
    return year >= 2020 and 1 <= month <= 12 and 1 <= days <= 31


# R5.6 ticket exists
def validTicket3(ticket_name):
    val = validTicketName(ticket_name)
    return bn.ticket_exist(ticket_name) and val


# R5.7 Error message
# doesn't return to '/'

@app.route('/update', methods=['POST'], endpoint='postee_end')
@authenticate
def sellValidTicket3(user):
    ticket_name = request.form.get('ticket_name')
    quantity = request.form.get('quantity')

    bad_Quantity = render_template('update.html', user=user, message=user.name,
                                   error_message="Ticket quantity is invalid (quantity must be between [0,100]")
    badBuy = render_template('update.html', user=user, message=user.name,
                             error_message="Invalid Quantity (Tried To update "
                                           "Too Many Tickets)")
    badBalance = render_template('update.html', user=user, message=user.name,
                                 error_message=" account  balance is invalid")
    bad_ticket_null = render_template('update.html', user=user, message=user.name,
                                      error_message="Ticket does not exist")

    bad_ticket_name = render_template('update.html', user=user, message=user.name, error_message="invalid Ticket name")
    try:
        quantity = int(quantity)
    except Exception as e:
        return bad_Quantity

    if not validTicketName(ticket_name):
        return bad_ticket_name

    if not validTicket(ticket_name):
        return bad_ticket_null

    if not valid_quantity_buy(quantity, ticket_name):
        return badBuy

    if not validQuantity(quantity):
        return bad_Quantity

    if not validBalance(quantity, ticket_name):
        return badBalance

    else:
        return render_template('update.html', user=user, message=user.name,
                               error_message="Tickets have been updated")
