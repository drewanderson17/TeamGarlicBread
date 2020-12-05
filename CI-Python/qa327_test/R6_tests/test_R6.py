import pytest
import requests
from selenium import webdriver
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User


class R7(BaseCase):

    def register(self):
        # mock a user information
        self.open(base_url + '/register')
        self.type("#email", "StevenA@kingstong.com")
        self.type("#name", "stevena")
        self.type("#password", "scrum#Master1")
        self.type("#password2", "scrum#Master1")
        self.click('input[type="submit"]')

        # test after logging out user is returned to /login page

    def login(self):
        self.open(base_url + '/login')
        self.type("#email", "StevenA@kingstong.com")
        self.type("#password", "scrum#Master1")
        self.click('input[type="submit"]')

    # The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.
    def test_alphanum(self):
        self.login()
        self.open(base_url + '/buy')
        self.type("#ticket_name", "StevenA@kingstong.com")
        self.type("#quantity", "50")
        self.click('input[type="submit"]')
        self.assert_element("#error_message")
        self.assert_text("invalid Ticket name", "#error_message")

    def test_ticketLength(self):
        self.login()
        self.open(base_url + '/buy')
        self.type("#ticket_name", "StevenAkabasbfsakjfsabkjfbajkfbjksabfkabfjkbfjkasbfkjsabfksakjfbkjasfbkjsabfkabkjsabfjkafln32brpbfjekwfrbewlfkbrekjfrewbklrfjbingstong.com")
        self.type("#quantity", "50")
        self.click('input[type="submit"]')
        self.assert_element("#error_message")
        self.assert_text("invalid Ticket name", "#error_message")





    #The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.
    #The name of the ticket is no longer than 60 characters
    #The quantity of the tickets has to be more than 0, and less than or equal to 100.
    #The ticket name exists in the database and the quantity is more than the quantity requested to buy
    #The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)

    '''
    basic steps
    
    register as a user and login,
    then create a valid ticket
    
    use as a fixture so only needs to run once
    
    
    '''