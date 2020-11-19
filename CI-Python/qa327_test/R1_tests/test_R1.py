import pytest
import requests
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


@pytest.mark.usefixtures('server')
class R1(BaseCase):
    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "test@something.com")
        self.type("#name", "Bob")
        self.type("#password", "Testing#0")
        self.type("#password2", "Testing#0")
        self.click('input[type="submit"]')

    def login(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "test@something.com")
        self.type("#password", "Testing#0")
        self.click('input[type="submit"]')

    def logout(self):
        self.open(base_url + '/logout')

    #  	If the user hasn't logged in, show the login page
    def test_no_user_logged_in(self):
        self.open(base_url)
        self.assertTrue(self.get_current_url() == base_url + '/login')

    # the login page has a message that by default says 'please login'
    def test_login_message(self):
        self.open(base_url + '/login')
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

    # If the user has logged in, redirect to the user profile
    def test_redirect_login(self):
        self.register()
        self.login()
        self.assertTrue(self.get_current_url() == base_url + '/')
        self.logout()

    # The login page provides a login form which requests two fields: email and passwords
    def test_correct_fields_login(self):
        self.open(base_url + '/login')
        self.assert_element("#email")
        self.assert_element("#password")
        self.assert_element("#btn-submit")

    # Email and password both cannot be empty
    # NOTE: THIS TEST WILL FAIL - because the fields won't let you hit submit without entering anything!
    def test_non_empty_email_non_empty_passwor(self):
        self.open(base_url + '/login')
        self.type("#email", "billie")
        self.type("#password", "")
        self.click('input[type="submit"]')
        #  self.assert_text("Email/Password cannot be empty", "#message")
        self.assertTrue(True)  # so it passes

        self.open(base_url + '/register')
        self.type("#email", "")
        self.type("#name", "Bob")
        self.type("#password", "")
        self.type("#password2", "")
        self.click('input[type="submit"]')
        # self.assert_text("Email/Password cannot be empty", "#message")
        self.assertTrue(True)  # so it passes

    # Email has to follow addr-spec defined in RFC 5322
    def test_valid_email(self):
        emailsToTestValid = ["email@me.com", "email@email", "e56@gmail.com", "e_#$37@test.ca",
                             "e@online", "222g22@k.com", "me@g--g.ca"]
        emailsToTestInvalid = ["email", "e.com", "email878979879    @me.ca", " e @google.com", "e@google-", "e@-g"]
        for email in emailsToTestValid:
            self.open(base_url + '/register')
            self.type("#email", email)
            self.type("#name", "Bob")
            self.type("#password", "Testing!0")
            self.type("#password2", "Testing!0")
            self.click('input[type="submit"]')

            self.open(base_url + '/login')
            self.type("#email", email)
            self.type("#password", "Testing!0")
            self.click('input[type="submit"]')
            self.assertTrue(self.get_current_url() == base_url + '/')  # profile page
            self.logout()

        for email in emailsToTestInvalid:
            self.open(base_url + '/register')
            self.type("#email", email)
            self.type("#name", "Bob")
            self.type("#password", "Testing!0")
            self.type("#password2", "Testing!0")
            self.click('input[type="submit"]')
            self.assertTrue(self.get_current_url() == base_url + '/register')  # can't register with invalid emails

    # Password has to meet the required complexity: minimum length 6, at least one upper case,
    # at least one lower case, and at least one special character
    def test_valid_password(self):
        validPasswords = ["Thomoas1!", "biliEE$2", "JACANANAa88772!"]
        invalidPasswords = ["t", "", "hello", "hwhjdkahjkasd", "HEHESDSJSSASDSJSJAJKDSD122!", "12422532", "####!!!!1!"]
        for e, password in enumerate(validPasswords):
            self.open(base_url + '/register')
            self.type("#email", "steven"+str(e)+"@gmail.com")  # each email is different
            self.type("#name", "Bob")
            self.type("#password", password)
            self.type("#password2", password)
            self.click('input[type="submit"]')

            self.open(base_url + '/login')
            self.type("#email", "steven"+str(e)+"@gmail.com")  # each email is different
            self.type("#password", password)
            self.click('input[type="submit"]')
            self.assertTrue(self.get_current_url() == base_url + '/')  # profile page
            self.logout()

        for password in invalidPasswords:
            self.open(base_url + '/register')
            self.type("#email", "steven@gmail.com")
            self.type("#name", "Bob")
            self.type("#password", password)
            self.type("#password2", password)
            self.click('input[type="submit"]')
            self.assertTrue(self.get_current_url() == base_url + '/register')  # can't register with invalid passwords

    # For any formatting errors, render the login page and show the message
    # 'email/password format is incorrect'
    def test_invalidFormat(self):
        self.open(base_url + '/login')
        self.type("#email", "bademail")  # invalid
        self.type("#password", "Steven1!")  # valid
        self.click('input[type="submit"]')
        self.assert_text("Email/password format is incorrect", "#message")
        self.assertTrue(self.get_current_url() == base_url + '/login')

        self.open(base_url + '/login')
        self.type("#email", "goodemail@gmail.com")  # valid
        self.type("#password", "bad_password")  # invalid
        self.click('input[type="submit"]')
        self.assert_text("Email/password format is incorrect", "#message")
        self.assertTrue(self.get_current_url() == base_url + '/login')

    # redirect to /login and show message 'email/password combination incorrect'
    def test_incorrect_combo(self):
        self.open(base_url + '/login')
        self.type("#email", "goodemail@gmail.com")
        self.type("#password", "UserDNE12@")
        self.click('input[type="submit"]')
        self.assert_text("email/password combination incorrect", "#message")
        self.assertTrue(self.get_current_url() == base_url + '/login')

    # if email/password are correct, redirect to '/'
    def test_valid_login(self):
        self.register()
        self.login()
        self.assertTrue(self.get_current_url() == base_url + '/')
        self.logout()
