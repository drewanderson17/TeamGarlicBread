import pytest
import requests
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


@pytest.mark.usefixtures('server')
class R4(BaseCase):
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

    # R4.0.1, R4.0.2
    def test_validTicketName(self):
        validTicketNames = ['ticket 69', '2hE3lEhDEhjs PND4H', 'TESTTICKLET', 'ticket    time']
        invalidTicketNames = [' ticket', 'ticket ', ' ticket ', 't-c!h' '*', '* *', 'hello world!',
                              '0123456789012345678901234567890123456789012345678901234567891']
        self.register()
        for validName in validTicketNames:
            self.login()
            self.click('#sell-btn')
            self.type("#ticket_name", validName)
            self.type("#quantity", "10")
            self.type("#price", "10")
            self.type("#expiration_date", "20200901")
            self.click('input[type="submit"]')
            self.assert_text("Ticket added successfully!", "#error_message")
            self.logout()

        for invalidName in invalidTicketNames:
            self.login()
            self.click('#sell-btn')
            self.type("#ticket_name", invalidName)
            self.type("#quantity", "10")
            self.type("#price", "10")
            self.type("#expiration_date", "20200901")
            self.click('input[type="submit"]')
            self.assert_text("Ticket name is invalid", "#error_message")
            self.logout()

    # R4.0.3
    def test_validTicketQuantity(self):
        self.register()
        for i in [-1, 0, 101]:
            self.login()
            self.click('#sell-btn')
            self.type("#ticket_name", 'ticket')
            self.type("#quantity", i)
            self.type("#price", "10")
            self.type("#expiration_date", "20200901")
            self.click('input[type="submit"]')
            self.assert_text("Ticket quantity is invalid", "#error_message")
            self.logout()

        for i in [1, 25, 10]:
            self.login()
            self.click('#sell-btn')
            self.type("#ticket_name", 'ticket')
            self.type("#quantity", i)
            self.type("#price", "10")
            self.type("#expiration_date", "20200901")
            self.click('input[type="submit"]')
            self.assert_text("Ticket added successfully!", "#error_message")
            self.logout()

    # R4.0.4
    def test_validPrice(self):
        self.register()
        for i in [9, 101]:
            self.login()
            self.click('#sell-btn')
            self.type("#ticket_name", 'ticket')
            self.type("#quantity", "10")
            self.type("#price", i)
            self.type("#expiration_date", "20200901")
            self.click('input[type="submit"]')
            self.assert_text("Ticket price is invalid", "#error_message")
            self.logout()

        for i in [10, 25, 100]:
            self.login()
            self.click('#sell-btn')
            self.type("#ticket_name", 'ticket')
            self.type("#quantity", "10")
            self.type("#price", i)
            self.type("#expiration_date", "20200901")
            self.click('input[type="submit"]')
            self.assert_text("Ticket added successfully!", "#error_message")
            self.logout()

    # R4.0.5
    def test_validDate(self):
        self.register()
        validDates = ['20201001', '20201231', '20200101', '20211015']
        invalidDates = ['20190101', '00000000', '20201301', '20201132', '20200011', '20201000']
        for validDate in validDates:
            self.login()
            self.click('#sell-btn')
            self.type("#ticket_name", 'ticket')
            self.type("#quantity", "10")
            self.type("#price", "10")
            self.type("#expiration_date", validDate)
            self.click('input[type="submit"]')
            self.assert_text("Ticket added successfully!", "#error_message")
            self.logout()

        for invalidDate in invalidDates:
            self.login()
            self.click('#sell-btn')
            self.type("#ticket_name", 'ticket')
            self.type("#quantity", "10")
            self.type("#price", "10")
            self.type("#expiration_date", invalidDate)
            self.click('input[type="submit"]')
            self.assert_text("Ticket date is invalid", "#error_message")
            self.logout()

    # R4.0.7 - the added new ticket information will be posted on the user profile page
    def test_ticketShowsInProfilePage(self):
        self.register()
        self.login()
        self.click('#sell-btn')
        self.type("#ticket_name", 'TICKET TO SHOW')
        self.type("#quantity", "10")
        self.type("#price", '69')
        self.type("#expiration_date", "20200901")
        self.click('input[type="submit"]')
        self.assert_text("Ticket added successfully!", "#error_message")
        self.click("#home-btn")
        self.assert_element('#ticket_display_name')
        self.logout()






