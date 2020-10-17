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

## Test Case R2.04: The registration form can be submitted as a POST request to the current URL (/register)
### Mocking
* Get sample user via backend.get_user call

### Actions
* open / login
* input necessary requirements
* If form does not meet post request requirementents display error message

## Test Case R2.05: Email, password, password2 all have to satisfy the same required as defined in R1
### Mocking
* Get sample user via backend.get_user call

### Actions
* open / login 
* input password 
* input password2 
* if password1 and password2 meet requirements accept
* else display error message 


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

## Test Case R2.08: User name has to be longer than 2 characters and less than 20 characters.
### Mocking
* Get sample user via backend.get_user call

### Actions
* input username
* if 2 < username < 20 accept 
* else display error message  

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

## Test Case R2.10: If the email already exists, show message 'this email has been ALREADY used'
### Mocking
* Get sample user via backend.get_user call

### Action
* input email
* if email has not been used accept
* Else display message "this email has already been used"

## Test Case R2.11: If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
### Mocking
* Get sample user via backend.get_user call
* Account Balance =+ 5000
* Load login page

### Action
* create new user
* display account balance
* load login page

-------------------------------------------------------------------------------------------------------------------------------------

## Test Case R6.01: The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.
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

## Test Case R6.02: The name of the ticket is no longer than 60 characters
### Mocking
* Request ticket information via backend.ticket

### Actions
* open / load page
* input ticket name 
* if ticket name < 60 characters name is accepted
* if ticket name is longer than 60 characters display error message:
    * "ticket name must be less than 60 characters"

## Test Case R6.03: The quantity of the tickets has to be more than 0, and less than or equal to 100.
### Mocking
* Request ticket information via backend.ticket

### Action
* open / load page
* if 0 < ticket quantity < 100 action accepted
* if ticket number < 0 error message 
    * ticket number must be greater than zero
* if ticket number > 100 error message 
    * ticket number must be less than 100

## Test Case R6.04: The ticket name exists in the database and the quantity is more than the quantity requested to buy

### Mocking
* Request ticket information via backend.ticket

### Action
* open / load page
* if ticket name exists && quantity is more than quantity requested to buy complete sale
* show purchase confirmation

## Test Case R6.05: The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)
### Mocking
* Request ticket information via backend.ticket
* calculate ticket price = ticket price * quantity + service fee (35%) + tax (5%)
* deduct ticket price from balance

### Action
* open / load
* purchase ticket
* display new balance and updated transactions
* if date is in incorrect format display error message
    *  please enter date in the following format YYYYMMDD

## Test Case R6.06: For any errors, redirect back to / and show an error message

### Mocking
* backend identifies errors in any functions 

### Action
* display error message "error"
* redirect back to home page 







