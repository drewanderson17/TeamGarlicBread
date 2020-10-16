# Front End Testing Requirements R4  /sell Last 3 and R5 /update
## Test Data

test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=10,
    price=10,
    date='20200901'
)
---
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)



## Test case R4.5 - Date must be given in the format YYYYMMDD (e.g. 20200901)

### Mocking:

* Mock backend.get_user to return an instance of test_user
* Mock Backend.getticket to return a instance a test_ticket

### Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* open /
* pass through test_ticket_bad date a ticket with an invalid date
* enter test_ticket's quantity into element #sell_quantity
* click element #sell_submit
* validate that the #buy_message element shows error invalid date format
open /sell   (refresh the page)


## Test case R4.6 - For any errors, redirect back to / and show an error message

### Mocking:

* Mock backend.get_user to return an instance of test_user
* Mock Backend.getticket to return a instance a test_ticket

### Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
*click element input[type='submit]
*open /sell
*enter negative values to #sell_qunatity
*click element sell_submit
* validate that opened go back to / and input[type= "message] display error message having negative values 

## Test case R4.7 - The added new ticket information will be posted on the user profile page

### Mocking:

* Mock backend.get_user to return an instance of test_user
* Mock Backend.getticket to return a instance a test_ticket

### Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* open /sell
* enter test_tickets information
* click #sell_submit
* open /update
* validate that test_ticket is displays owner, name, quantity, price and date on user profile

## Test case R5.1 /update  - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character

### Mocking:

* Mock backend.get user to get an instance test_user
* Mock backend.get_ticket to get an instance of test_ticket

### Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type = "submit]
* open /update
* enter the test_tickets name into element #update_name
* click element #update_element
* validate that the test_ticket name is alphanumeric-only and space isn't the first or last character
* open /logout to clean up


## Test case R5.2 -	The name of the ticket is no longer than 60 characters

### Mocking:


* Mock backend.get user to get an instance test_user
* Mock backend.get_ticket to get an instance of test_ticket


### Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* open /update
* enter test_ticket name into element  #update_name
* validate that the name is not longer than 60 characters and show element #buy_message show's a small check mark validating the input
* else with element #buy_message display an error message



## Test case R5.3 -	The quantity of the tickets has to be more than 0, and less than or equal to 100.

### Mocking:

* Mock BackEnd.get user to get an instance of the user
* Mock backend.get_ticket to get an instance of test_ticket


### Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type = "submit"]
* open /update
* enter the ticket_quantity in element #update_quantity
* validate that the quantity of the tickets is more than 0 and less than 100
* enter the rest of test_ticket information
* validate that the #buy_message or #sell_message is sucessful
*go to /update




## Test case R5.4 -		Price has to be of range [10, 100]

### Mocking:

* Mock BackEnd.get user to get an instance of the user
* Mock backend.get_ticket to get an instance of test_ticket
	
### Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* open /update
* enter Price  into element #update_price
* * click element #update_submit
* validate that price range is in between [10,100]
* go to /logout to clear cache



## Test case R5.5 -		Date must be given in the format YYYYMMDD (e.g. 20200901)

### Mocking:

* Mock BackEnd.get user to get an instance of the user
* Mock backend.get_ticket to get an instance of test_ticket
	
### Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type = "submit"]
* open /update
* click element #update_date and enter information
* click element #update_submite
* validate that the date is in the format YYYYMMDD
* open /logout


## Test case R5.6 -		The ticket of the given name must exist

### Mocking:

* Mock BackEnd.get user to get an instance of the user
* Mock backend.get_ticket to get an instance of test_ticket
* Mock backend.database to get an instance of the database
	
### Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* open /update
* enter ticket of the name the ticket in element #update_name
* validate that the ticket name is in the database
* return to /logout 




## Test case R5.7 -		For any errors, redirect back to / and show an error message

### Mocking:

* Mock BackEnd.get user to get an instance of the user
* Mock backend.get_ticket to get an instance of test_ticket
	
### Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter the user_information into the elements #email, #password
* click element input[type="submit"]
* open /update
* enter ticket_invalalid_ticker into  the following elements #update_name,#update_quantity, #update_submit
* validate that error message appears