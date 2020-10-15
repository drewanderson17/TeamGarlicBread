# Front End Testing Requirements R3 + 4 of R4 

##### Daniel Goldstein, 20119615

---
# Test Data:
```
test_user = User(
    email='test_frontend@queensu.ca'
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```
---
##### Test Case R3.0.1 
If the user is not logged in, redirect to login page

----
Mocking: 
 * Forward captured information to the back-end via a [POST] call
 * If user is registering: 
    * Create instance of new user in database via createNewUser(User) [POST] call
 * If user is logging in:
    * Call backend.authenticateLogin
    
 
Actions:
* Open /login
* If user has account:
    * Capture text entered in the email field and store it in #email element 
    * Capture text entered in the name field and store it in #name element 
    * Capture text entered in the password field and store it in #password element
    * See mocking for next steps 
* If user does not have an account:
    * Redirect to /register 
    * Capture text entered in the email field and store it in #email element 
    * Capture text entered in the name field and store it in #name element 
    * Capture text entered in the password field and store it in #password element
    * Click register button and then refer to mocking for next steps 

---
##### Test Case R3.02
This page shows a header 'Hi {}'.format(user.name)

---
Mocking:
* Get user instance via backend.get_user call

Actions:
* Open /page
* Store username from user instance fetched from backend in #username element
* Ensure header displays HI #user.name correctly 

---
##### Test case R3.0.3
This page shows user balance.

---
Mocking:
* Get user instance from backend via backend.get_user call
* Get account balance via backend.user.getBalance call

Actions:
* Display data stored in #user_balance element 
* Ensure data correctly reflects user's actual balance 

---
##### Test case R3.0.4
This page shows a logout link, pointing to /logout

Mocking: 
* Login test user via backend.login call 
* Call backend.logout 

Actions:
* Ensure logout button is available in top left corner 
* Open button being clicked backend request to logout is sent 
* Refer to second mocking step 

---
##### Test case R3.0.5
This page lists all available tickets. Information including the quantity of each ticket, 
the owner's email, and the price, for tickets that are not expired.
		
Mocking:
* Call backend.allTickets, which fetches all available tickets from the database  

Actions: 
* Open /available_tickets 
* Store each ticket name in #ticket element 
* Store each ticket quantity in #quantity element 
* Store each ticket owner's email in #owner_email element 
* Store each ticket's price in #price element 
* Display each ticket with all it's respective elements in list format
* Ensure all tickets are being displayed 

---
##### Test case R3.0.6
This page contains a form that a user can submit new tickets for sell. 
Fields: name, quantity, price, expiration date

Mocking:
* Submit user's form that came from frontend.postForm [POST]
* Call backend.StoreUsersForm, which stores user's form in database 

Actions:
* Load page that contains said form 
* Load entered name into #name element
* Load entered quantity into #quantity element 
* Load entered price into #price element  
* Load entered expiration date in #date element
* Call frontend.postForm, which is a [POST] call to the backend 
* Load page listing tickets user is selling and verify information is correct

---
##### Test case R3.0.7
This page contains a form that a user can buy new tickets. Fields: name, quantity

Mocking: 
* Get user instance via backend.get_user call
* Get ticket via backend.get_ticket(name, quantity) call

Actions: 
* Open /PurchaseTickets
* Load entered name into #name field
* Load entered quantity into #quantity field 
* Ensure correct results appear when user clicks 'enter' on their query
* Call frontend.buy_ticket [GET]
* Open /user_profile
* Check purchased tickets and ensure correct tickets have been purchased 

---
##### Test case R3.0.8
The ticket-selling form can be posted to /sell

Mocking:
* Get sample user via backend.get_user call
* Post ticket-selling form's information to the database via backend.formToDB call

Actions:
* Fill out all fields in ticket-selling form
* Store each field in it's respective #field element 
* Call frontend.postFormToSell with respective fields [POST]
* Refer to mocking step 2
* Open /sell
* Ensure ticket being sold is available there with correct fields

---
##### Test case R3.0.9
The ticket-buying form can be posted to /buy

Mocking:
* Get sample user via backend.get_user call
* Call backend.buyTicket to confirm transaction 

Actions:
* Fill out all fields in ticket-buy form 
* Store each field in it's respective #field element 
* Call frontend.postFormToBuy with respective fields [POST]
* Refer to mocking step 2
* OPen /buy
* Ensure form has been correctly posted


---
##### Test case R3.1.0
The ticket-update form can be posted to /update

Mocking:
* Get sample user via backend.get_user call
* Call backend.updateTicket to reflect updates in database  

Actions:
* Fill out all fields in ticket-update form 
* Store each field in it's respective #field element 
* Call frontend.updateTicketForm with respective fields [POST]
* Refer to mocking step 2
* Open /tickets 
* Ensure form has been correctly updated 

---
##### Test case R4.0.1
The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.

Mocking:
* Call backend.getTicket to get ticket 

Actions:
* Parse ticket (received from mocking) name and ensure all characters are alphanumeric
* Check if space exists and ensure it is not the first index or last index of the string

---
##### Test case R4.0.2
The name of the ticket is no longer than 60 characters

Mocking:
* Call backend.getTicket  

Actions:
* Check the length of the ticket name string
* Do: len(ticket) < 60

---
### Test case R4.0.3
The quantity of the tickets has to be more than 0, and less than or equal to 100.

Mocking:
* Call backend.getAllTickets

Actions:
* Check quantity variable is > 0
* Check quantity variable is <= 100

---
##### Test case R4.0.4
Price has to be of range [10, 100]

Mocking:
* Call backend.getAllTickets

Actions:
* Iterate over each ticket
* Check price attribute is bounded by both 10 and 100
* 100 >= price >= 10



 