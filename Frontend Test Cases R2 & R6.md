# Frontend Test Cases R2(Remainder) & R6

# Juliana Brown 
# 20010601

## Test Data for all cases

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

## Test Case R2.04: Email has to follow addr-spec defined in RFC 5322 
### Mocking
* Get sample user via backend.get_user call

### Actions
* open / login
* input email into user interface
* Check email against RFC 5222 requirement
* if email meets the required specifications accept input
* Else display error message

## Test Case R2.05: Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character
### Mocking
* Get sample user via backend.get_user call

### Actions
* open / login 
* input password 
* if password meets criteria, accept password
* store password in #password element
* if password is less than six characters display error message
    * "password must be at least 6 characters long"
* if all characters are lower case display error message
    * "password must contain at least one upper case character"
* if all characters are upper case display error message 
    * "password must contain at least one lower case character"
* if no special characters display error message
    * "password must contain at least one special character"

## Test Case R2.06: Password and password2 have to be exactly the same
### Mocking
* Get sample user via backend.get_user call

### Actions
* input password 
* input password2
* If password = password2 accept password
* Save password to user account
* Else display error message:
    * "passwords must match"

## Test Case R2.07: User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.
### Mocking
* Get sample user via backend.get_user call

### Actions
* input username
* if username meets criteria store username to field #username
* If username is empty do not save and display error message:
    * "username cannot be empty"
* If username contains special characters, do not save and display error message:
    * "username must only contain alphanumeric characters"
* If username of length n contains space that is not in space 1 or n do not save and display error message:
    * "spaces may only be used in first or last character"

## Test Case R2.08: Email does not exist in the known accounts
### Mocking
* Get sample user via backend.get_user call

### Actions
* input email 
* if email does not match display error message:
    * "this email does not match any existing accounts"

## Test Case R2.09: For any formatting errors, show message '{} format is incorrect.'.format(the_corresponding_attribute), end the registration session, and print the landing screen
## Mocking:
* Get sample user via backend.get_user call

### Actions:
* input necessary information
* if information has correct formatting accept
* if formatting is incorrect:
    * show message '{} format is incorrect.'.format(the_corresponding_attribute)
    * end registration session
    * load home page

## Test Case R2.10: Otherwise, show message 'account registered', end the registration session/process, print the landing screen according to R1

### Mocking
* Get sample user via backend.get_user call

### Action
* input information into all relevant fields
* if information is formatted correctly accept and save
* Show message: "account registered"
* Load landing page (see R1)

## Test Case R2.11: New account will get a balance of 3000.
### Mocking
* Get sample user via backend.get_user call
* Account Balance =+ 3000

### Action
* Open account balances page
* Show new account balance (where balance equals balance = balance +3000)

## Test Case R2.12: Append a new registration transaction if successfully registered.
### Mocking
* Get sample user via backend.get_user call
* Process new transaction via backend.get_transaction call

### Action
* load / open page
* display all transactions


-------------------------------------------------------------------------------------------------------------------------------------

## Test Case R6.01: Command invalid if the user has not logged in.
### Mocking
* Get sample user via backend.get_user call
* Check login status via backend.login

### Action
* If user is not logged in display message:
    *"command invalid"

## Test Case R6.02: Starts a ticket updating session
### Mocking
* Request ticket information via backend.ticket
* Update ticket information

### Actions
* Open page
* Complete login process
* Select update ticket
* Display updated ticket information

## Test Case R6.03: Should ask for ticket name, price, quantity, date
### Mocking
* Request and store ticket information via backend.ticketInfo

### Action
* load / open
* input ticket name, price and quantity
* confirm choices via select button

## Test Case R6.04: The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.
### Mocking
* Request ticket information via backend.ticket

### Actions
* open / load page
* input ticket name
* if ticket name is within guidelines accept name
* if ticket name has non-alphanumeric characters display error message
    * "ticket name must contain only alphanumeric characters"
* if ticket (of length n) name has space character that is not character 1 or n 
    * "ticket name can only contain space character in the firs or last character" 

## Test Case R6.05: The name of the ticket is no longer than 60 characters
### Mocking
* Request ticket information via backend.ticket

### Actions
* open / load page
* input ticket name 
* if ticket name < 60 characters name is accepted
* if ticket name is longer than 60 characters display error message:
    * "ticket name must be less than 60 characters"

## Test Case R6.06: The quantity of the tickets has to be more than 0, and less than or equal to 100.
### Mocking
* Request ticket information via backend.ticket

### Action
* open / load page
* if 0 < ticket quantity < 100 action accepted
* if ticket number < 0 error message 
    * ticket number must be greater than zero
* if ticket number > 100 error message 
    * ticket number must be less than 100

## Test Case R6.07: Price has to be of range [10, 100]
### Mocking
* Request ticket information via backend.ticket

### Action
* open / load page
* if 10 < ticket price < 100 action accepted
* if ticket price < 10 error message 
    * ticket price must be greater than or = $10
* if ticket price > 100 error message 
    * ticket price must be less than or = $100

## Test Case R6.08: Date must be given in the format YYYYMMDD (e.g. 20200901)
### Mocking
* Request ticket information via backend.ticket

### Action
* open / load
* if date is in correct format accept 
* if date is in incorrect format display error message
    *  please enter date in the following format YYYYMMDD

## Test Case R6.09: Append a new update transaction if successful.
### Mocking
* Process transaction via backend.transaction

### Action
* open / load
* complete login process
* access transactions
* display transaction
 
## Test Case R6.10: For any errors, show an error message
### Mocking
* backend identifies errors in any functions 

### Action
* display error message "error"

## Test Case R6.11: Command invalid if the user has not logged in.
### Mocking
* Get sample user via backend.get_user call

### Actions
* open / load
* complete action
* display error message if user is not loged in
    * 'action invalid, please sign in'

## Test Case R6.12: Invalidate login user and go back to the landing session/screen
### Mocking
* Get sample user via backend.get_user call

### Action
* open / load
* enter email or username for login
* enter password
* if password and user name do not match account records return to landing screen 
* load landing page




