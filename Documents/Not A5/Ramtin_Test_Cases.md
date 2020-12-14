# Frontend Test Cases R1 + 3 of R2

#### Ramtin Kalkhoran, 20067387

## Test Data
test_user = User(

    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Test_frontend#')
)


test_invalid_email = User(

    email='test_frOntend@@@@test.com',
    name='test_frontend',
    password=generate_password_hash('Test_frontend#')
)

test_invalid_password = User(

    email='test_frontend@test.com',
    name='test_frontend',
    invalid_password1 = generate_password_hash('T#g')
    invalid_password2 = generate_password_hash('no_upper_case#')
    invalid_password3 = generate_password_hash('NO_LOWER_CASE#')
    invalid_password4 = generate_password_hash('NoSpecialCharacter')
)
## Test case R1.1 - If the user hasn't logged in, show the login page

### Mocking:

* None

### Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login


## Test case R1.2 - the login page has a message that by default says 'please login'

### Mocking:

* None

### Actions:
* open /login
* ensure that 'please login' message is seen



## Test case R1.3 - If the user has logged in, redirect to the user profile page (as given in example)
### Mocking:

* Mock backend.get_user to return a test_user instance

### Actions:

* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* open /login again
* validate that current page contains #welcome-header element

## Test case R1.4 - The login page provides a login form which requests two fields: email and passwords
### Mocking:

* Mock backend.get_user to return a test_user instance

### Actions:

* open /login
* ensure login form with two fields: email and password is visible



## Test case R1.5 - The login form can be submitted as a POST request to the current URL (/login)
### Mocking:

* Mock backend.get_user to return a test_user instance

### Actions:

* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* validate that current login form can be submitted as a POST request to the current URL (/login)

## Test case R1.6 - Email and password both cannot be empty
### Mocking:

* Mock backend.get_user to return a test_user instance

### Actions:
* open /login
* ensure that email AND password are empty
* click element input[type="submit"]
* validate that the #submit element shows error message; must have both elements filled
* open /logout (clean up)
* open /login again
* enter test_user's email into element #email
* ensure that password is empty
* click element input[type="submit"]
* validate that the #submit element shows error message; must have both elements filled
* open /logout (clean up)
* open /login again
* enter test_user's password into element #password
* ensure that email is empty
* click element input[type="submit"]
* validate that the #submit element shows error message; must have both elements filled



## Test case R1.7 - Email has to follow addr-spec defined in RFC 5322
### Mocking:

* Mock backend.get_user to return a test_invalid_email instance

### Actions:
* open /login
* enter test_invalid_email's email into element #email
* enter test_invalid_email's password into element #password
* click element input[type="submit"]
* if email is invalid
    * validate that the #submit element shows inputted email is invalid, please follow addr-spec defined in RFC 5322
* else
    * open /

## Test case R1.8 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character
### Mocking:

* Mock backend.get_user to return a test_invalid_password instance

### Actions:
* open /login
* enter test_invalid_password's email into element #email
* enter test_invalid_password's password1 into element #password
* click element input[type="submit"]
* validate that the #submit element shows error message
* open /login agiain
* enter test_invalid_password's email into element #email
* enter test_invalid_password's password2 into element #password
* click element input[type="submit"]
* validate that the #submit element shows error message
* open /login agiain
* enter test_invalid_password's email into element #email
* enter test_invalid_password's password3 into element #password
* click element input[type="submit"]
* validate that the #submit element shows error message
* open /login agiain
* enter test_invalid_password's email into element #email
* enter test_invalid_password's password3 into element #password
* click element input[type="submit"]
* validate that the #submit element shows error message
* open /login agiain
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* validate that the #submit element was successful
* open /

## Test case R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect.'
### Mocking:

* Mock backend.get_user to return a test_user instance
* Mock backend.get_user to return a test_invalid_email instance
* Mock backend.get_user to return a test_invalid_password instance

### Actions:

* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_invalid_email's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* validate that the #submit element displays 'email/password format is incorrect'

## Test case R1.10 - If email/password are correct, redirect to /
### Mocking:

* Mock backend.get_user to return a test_user instance

### Actions: (positive)

* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* validate that redirect to / is successful


## Test case R1.11 - Otherwise, redict to /login and show message 'email/password combination incorrect'
### Mocking:

* Mock backend.get_user to return a test_invalid_email instance

### Actions: (negative)

* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_invalid_email's email into element #email
* enter test_invalid_email's password into element #password
* click element input[type="submit"]
* validate that the #submit element shows 'email/password combination incorrect'
* validate that the #submit element redirects to /login

## Test case R2.1 - If the user has logged in, redirect back to the user profile page /
### Mocking:

* Mock backend.get_user to return a test_user instance

### Actions:
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* validate that open / is true


## Test case R2.2 - otherwise, show the user registration page
### Mocking:

* Mock backend.get_user to return a test_user instance

### Actions:

* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* if test_user instance does not exist in database
    * open /register

## Test case R2.3 - the registration page shows a registration form requesting: email, user name, password, password2
### Mocking:

* Mock backend.get_user to return a test_user instance

### Actions:
* open /register
* validate that /register shows registration form
* enter test_user's email into element #email
* enter test_user's user name into element #user_name
* enter test_user's password into element #password
* re-enter test_user's password into element #password2
* click element input[type="submit"]
