import pytest
import requests
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User

@pytest.mark.usefixtures('server')
class R5(BaseCase):
    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "juli@email.com")
        self.type("#name", "Juli")
        self.type("#password", "Password#0")
        self.type("#password2", "Password#0")
        self.click('input[type="submit"]')

    def login(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "juli@email.com")
        self.type("#password", "Password#0")
        self.click('input[type="submit"]')

    def logout(self):
        self.open(base_url + '/logout')

    # The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.
    # The name of the ticket is no longer than 60 characters
    def test_validTicket2(self):
            validTicketNames = ['ticket 99', '2hE3lEhDEhjs PND4H', 'TESTTICKLET', 'ticket    time']
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
    
    # The quantity of the tickets has to be more than 0, and less than or equal to 100.
    def test_validTicketQuantity2(self):
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
    
    # Price has to be of range [10, 100]
    def test_validPrice2(self):
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

    # Date must be given in the format YYYYMMDD (e.g. 20200901)
    def test_validDate2(self):
        self.register()
        validDates = ['20201005', '20201031', '20200101', '20211015']
        invalidDates = ['20170101', '11000001', '21201301', '20201145', '20200011', '20201000']
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

    
    # The ticket of the given name must exist and redirect if an error occurs
    def test_validTicket3(self):
        self.register()
        self.login()
        self.open(base_url + '/buy')
        self.type("#ticket_name", "test")
        self.type("#quantity", "5")
        self.click('input[type="submit"]')
        self.assert_element("#error_message")
        self.assert_text("Tickets bought successfully!", "#error_message")





