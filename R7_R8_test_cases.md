# Frontend Test Cases R7 + R8

#### Ramtin Kalkhoran, 20067387

## Test Data
test_user = User(

    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Test_frontend#')
)


## Test case R7.1 - Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.
### Mocking:

* Mock backend.get_user to return a test_user instance

### Actions:

* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* open /logout 
* validate that return to login page occurs
* click element input[type="submit]
* validate that access to restricted pages is not given without re-entry of email and password 


## Test case R8.1 - For any other requests except the ones above, the system should return a 404 error
### Mocking:
* none

### Actions:

* if action is not accounted for
    * validate that 404 error message is visible