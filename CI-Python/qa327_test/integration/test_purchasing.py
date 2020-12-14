import pytest
import requests
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
@pytest.mark.usefixtures('server')
class Registered(BaseCase):

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

    def test_purchase(self):
        """ This test checks the implemented login/logout feature """
        self.register()
        self.login()
        self.click('#sell-btn')
        self.type("#ticket_name", "testTicket")
        self.type("#quantity", "10")
        self.type("#price", "10")
        self.type("#expiration_date", "20200801")
        self.click('input[type="submit"]')
        self.assert_text("Ticket added successfully!", "#error_message")
        self.open(base_url + '/')
        self.click('#buy-btn')
        self.type("#ticket_name", "testTicket")
        self.type("#quantity", "10")
        #self.type("#price", "10")
        #self.type("#expiration_date", "20200801")
        self.click('input[type="submit"]')

    def test_sell(self):
        self.register()
        self.login()
        self.click('#sell-btn')
        self.type("#ticket_name", "testTicket")
        self.type("#quantity", "10")
        self.type("#price", "10")
        self.type("#expiration_date", "20200801")
        self.click('input[type="submit"]')
        self.assert_text("Ticket added successfully!", "#error_message")

    def test_backend_white_box(self):
        # use basic block coverage
        # testing get_ticket_quantity
        self.register()
        self.login()
        self.click('#sell-btn')
        self.type("#ticket_name", "testTicket")
        self.type("#quantity", "10")
        self.type("#price", "10")
        self.type("#expiration_date", "20200801")
        self.click('input[type="submit"]')
        self.assert_element('#quantity')
        self.logout()
        self.login()
        self.click('#sell-btn')
        self.type("#ticket_name", "testNextTicket")
        self.type("#quantity", "100000")
        self.type("#price", "10")
        self.type("#expiration_date", "20200701")
        self.click('input[type="submit"]')
        self.assert_element('#quantity')
