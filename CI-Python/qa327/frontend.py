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
        if char not in printableChars and not (97 <= ord(char) <= 122) and not (48 <= ord(char) <= 57):  # invalid character
            return False

    for e, char in enumerate(domainPart):
        if char == '-' and (e == 0 or e == len(domainPart) - 1):  # can't have '-' as first or last character
            return False
        if not ((97 <= ord(char) <= 122) or (48 <= ord(char) <= 57)):  # ensures only alphanumeric values
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

    if password != password2:
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
        user = bn.get_user(email)
        if user:
            error_message = "User exists"
        elif not bn.register_user(email, name, password, password2):
            error_message = "Failed to store user info."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
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
    message = 'email/password combination incorrect'
    if email == "" or password == "":
        message = 'Email/Password cannot be empty'
    return render_template('login.html', message=message)


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


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

@app.route('/', methods=['GET'])
def profile_get():
    # templates are stored in the templates folder
    # R3.1 If the user is not logged in, redirect to login page
    if 'logged_in' == False:     
        return redirect('/login')
    # R3.2 This page shows a header 'Hi {}'.format(user.name)
    hi_message = render_template('profile.html', message='Hi'+ bn.user.name))
    # R3.3 This page shows user balance.
    user_balance = bn.profile_user(balance)
    balance_message = render_template('profile.html', message=user_balance)
    # R3.4 This page lists all available tickets. Information including 
    # the quantity of each ticket, the owner's email, and the price, 
    # for tickets that are not expired.
    available_tickets = bn.get_all_tickets()
    ticket_message = render_template('profile.html', message=available_tickets)
    # R3.5 This page contains a form that a user can submit new tickets
    # for sell. Fields: name, quantity, price, expiration date
    sell_ticket = bn.profile_user(ticket_name, quantity, price, expiration_date)
    # R3.6 This page contains a form that a user can buy new tickets.
    # Fields: name, quantity
    buy_ticket = bn.profile_user(ticket_name, quantity)
    # R3.7 This page contains a form that a user can update existing tickets. 
    # Fields: name, quantity, price, expiration date
    update_ticket = bn.profile_user(ticket_name, quantity, price, expiration_date)
    # R3.8 The ticket-selling form can be posted to /sell
    if sell_ticket != None:
        return redirect('/sell')
    # R3.9 The ticket-buying form can be posted to /buy
    if buy_ticket != None:
        return redirect('/buy')
    # R3.10 The ticket-update form can be posted to /update
    if update_ticket != None:
        return redirect('/sell')
    return(hi_message, balance_message, ticket_message) 

@app.route('/', endpoint='auth_func1')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets)


@app.route('/profile', endpoint='auth_func2')
@authenticate
def userProfile(user):
    return render_template('profile.html', user=user)
