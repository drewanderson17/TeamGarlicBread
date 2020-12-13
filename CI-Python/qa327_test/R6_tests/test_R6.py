import pytest
import requests
from selenium import webdriver
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from qa327 import frontend as ft


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

    def sell(self):
        self.open(base_url + '/sell')
        self.type("#ticket_name", 'test')
        self.type("#quantity", "12")
        self.type("#price", '50')
        self.type("#expiration_date", "20200901")
        self.click('input[type="submit"]')

    # The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.
    def test_alphanum(self):
        self.register()
        self.login()

        self.open(base_url + '/buy')
        self.type("#ticket_name", "StevenA@kingstong.com")
        self.type("#quantity", "50")
        self.click('input[type="submit"]')
        self.assert_element("#error_message")
        self.assert_text("Error: invalid Ticket name", "#error_message")

    # The name of the ticket is no longer than 60 characters

    def test_ticketLength(self):
        self.login()
        self.open(base_url + '/buy')
        self.type("#ticket_name",
                  "StevenAkabasbfsakjfsabkjfbajkfbjksabfkabfjkbfjkasbfkjsabfksakjfbkjasfbkjsabfkabkjsabfjkafln32brpbfjekwfrbewlfkbrekjfrewbklrfjbingstongcom")
        self.type("#quantity", "10")
        self.click('input[type="submit"]')
        self.assert_element("#error_message")
        self.assert_text("Error: invalid Ticket name", "#error_message")

    # The quantity of the tickets has to be more than 0, and less than or equal to 100.
    def test_quantity(self):
        self.register()
        self.login()
        self.sell()
        self.open(base_url + '/buy')
        self.type("#ticket_name", "test")
        self.type("#quantity", "990")
        self.click('input[type="submit"]')
        self.assert_element("#error_message")
        self.assert_text("Error: Invalid Quantity (Tried To Buy Too Many Tickets)", "#error_message")

    # The ticket name exists in the database

    def test_ticket_exist(self):

        self.register()
        self.login()
        self.sell()
        self.open(base_url + '/buy')
        self.type("#ticket_name", 'bugsBunny')
        self.type("#quantity", "5")
        self.click('input[type="submit"]')
        self.assert_element("#error_message")
        self.assert_text("Error: Ticket does not exist", "#error_message")

    # the quantity is more than the quantity requested to buy
    def test_user_quantity(self):
        self.register()
        self.login()
        self.sell()
        self.open(base_url + '/buy')
        self.type("#ticket_name", "test")
        self.type("#quantity", "90")
        self.click('input[type="submit"]')
        self.assert_element("#error_message")
        self.assert_text("Error: Invalid Quantity (Tried To Buy Too Many Tickets)", "#error_message")

    #  The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)
    # the users balance has been set to 300$
    def test_user_balance(self):
        self.register()
        self.login()
        self.sell()
        self.open(base_url + '/buy')
        self.type("#ticket_name", "test")
        self.type("#quantity", "10")
        self.click('input[type="submit"]')
        self.assert_element("#error_message")
        self.assert_text("Error: account balance is invalid", "#error_message")

    # test a valid ticket entry
    def test_good_ticket(self):
        self.register()
        self.login()
        self.sell()
        self.open(base_url + '/buy')
        self.type("#ticket_name", "test")
        self.type("#quantity", "3")
        self.click('input[type="submit"]')
        self.assert_element("#error_message")
        self.assert_text("Tickets bought successfully!", "#error_message")

    # The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.
    # The name of the ticket is no longer than 60 characters
    # The quantity of the tickets has to be more than 0, and less than or equal to 100.

    # The ticket name exists in the database and the quantity is more than the quantity requested to buy
    # The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)
