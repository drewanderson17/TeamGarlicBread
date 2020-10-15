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
    * Forward captured information to the back-end via a [POST] call
    * Click login button and see mocking for next steps 
* If user does not have an account:
    * Redirect to /register 
    * Capture text entered in the email field and store it in #email element 
    * Capture text entered in the name field and store it in #name element 
    * Capture text entered in the password field and store it in #password element after hashing
    * Ensure text entered in both password fields match (enter password, repeat password)
    * Forward captured information to the back-end via a [POST] call
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
* Ensure header displays Hi #user.name correctly by sight
* Ensure header display Hi #user.name correctly by inspecting the html using browser developer tools

---
##### Test case R3.0.3
This page shows user balance.

---
Mocking:
* Get user instance from backend via backend.get_user call
* Get account balance via backend.user.getBalance call

Actions:
* Display data stored in #user_balance element in the webpage 
* Compare displayed data to the data received via mocking calls

---
##### Test case R3.0.4
This page shows a logout link, pointing to /logout

Mocking: 
* Login test user via backend.login call 
* Call backend.logout 

Actions:
* Ensure logout button is available in top left corner 
* Open /logout when button is clicked 
* Register this occurs via browser developer tools
* Backend request to logout is sent via frontend.logout call 
* Refer to second mocking step 

---
##### Test case R3.0.5
This page lists all available tickets. Information including the quantity of each ticket, 
the owner's email, and the price, for tickets that are not expired.
		
Mocking:
* Call backend.allTickets, which fetches all available tickets from the database  

Actions: 
* Open /available_tickets 
* Store each tickets' name in #ticket element 
* Store each tickets' quantity in #quantity element 
* Store each tickets' owner's email in #owner_email element 
* Store each tickets' price in #price element 
* Display each ticket with all it's respective elements in list format
* Ensure all tickets are being displayed via eye sight and browser developer tools

---
##### Test case R3.0.6
This page contains a form that a user can submit new tickets for sell. 
Fields: name, quantity, price, expiration date

Mocking:
* Call backend.get_user to get instance of a test user 
* Submit user's form that came from frontend.postForm [POST]
* Call backend.storeUsersForm, which stores user's form in the database 

Actions:
* Load page that contains said form 
* Load entered name into #name element
* Load entered quantity into #quantity element 
* Load entered price into #price element  
* Load entered expiration date in #date element
* Click submit form button 
* Call frontend.postForm, which is a [POST] call to the backend 
* Open /allTickets and ensure ticket just submitted is being correctly displayed 
* Displayed ticket should show, name, available quantity, price and it's expiration date 

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
* Ensure correct results appear when the user clicks 'enter' on their query
* Call frontend.buy_ticket [GET], which will call mocking step 2
* Open /user_profile
* Check purchased tickets in /user_profile and ensure correct tickets have been purchased 

---
##### Test case R3.0.8
The ticket-selling form can be posted to /sell

Mocking:
* Get sample user via backend.get_user call
* Post ticket-selling form's information to the database via backend.formToDB call 

Actions:
* Fill out all fields in ticket-selling form, which includes name, quantity, price and seller's email
* Store each field in it's respective #field element (i.e name, quantity, price, email)
* Call frontend.postFormToSell with respective #field elements (i.e name, quantity, price, email)  [POST]
* Refer to mocking step 2
* Open /sell
* Ensure ticket being sold is available and all fields (i.e name, quantity price, email) are correct 

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
* Open /buy
* Ensure form has been correctly posted by making sure all fields are correct


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
* Ensure form has been correctly updated by verifying fields match intended values

---
##### Test case R4.0.1
The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.

Mocking:
* Call backend.getTicket to get ticket 

Actions:
* Call frontend.getTicket, which calls mocking step 1
* Obtain ticket name by calling getTicketName method on ticket received in above step 
* Parse ticket name and ensure all characters are alphanumeric
* Check if space exists and ensure it is not the first index or last index of the string
* If either of the two bullet points above fail
    * Output message via alert box which contains the message: 
      "Invalid name for ticket, must be alphanumeric and spaces are not allowed for the first and last character"
    * Request user to update said ticket 
---
##### Test case R4.0.2
The name of the ticket is no longer than 60 characters

Mocking:
* Call backend.getTicket  

Actions:
* Store ticket name in a name variable
* Check the length of the ticket name string
* If len(ticket) < 60:
    * Allow for ticket to exist
    * Call frontend.createTicket, or frontend.updateTicket - if ticket already exists
* Else:
    * Report message to user via alert box:
      "Ticket name must be 60 or less characters"
    * Prompt user to re-enter ticket name via text field 
    
---
### Test case R4.0.3
The quantity of the tickets has to be more than 0, and less than or equal to 100.

Mocking:
* Call backend.add_ticket, which adds ticket to database 

Actions:
* Open /createTicket
* Enter value given for quantity into #quantity element 
* Check quantity variable is <= 100
* If variable is > 100 or  <= 0:
    Prompt user with alert message:
    "Ticket Quantity must be at least 1, and less than or equal to 100"
* Else:
    * Call frontend.add_ticket [POST]
    * Refer to Mocking 
    
---
##### Test case R4.0.4
Price has to be of range [10, 100]

Mocking:
* Call backend.add_ticket, which adds ticket to database

Actions:
* Capture data entered into price field and place it in #price element 
* Check price element is bounded by both 10 and 100
* 100 >= price >= 10
* If price is not bounded by 100 and 10:
    * Notify user with alert message:
    "Ticket price must be between, 100 and 10 (inclusive)"
* Else:
    * Call frontend.add_ticket 
    * Refer to mocking

 