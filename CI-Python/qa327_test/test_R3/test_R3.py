# import pytest
# import requests
# from seleniumbase import BaseCase
# from qa327_test.conftest import base_url
# from unittest.mock import patch
# from qa327.models import db, User, Tickets
# from werkzeug.security import generate_password_hash, check_password_hash
# """
# These are the test cases for R3 requirements
# """

# @pytest.mark.usefixtures('server')
# class R3(BaseCase):
#     def register(self):
#         """register new user"""
#         self.open(base_url + '/register')
#         self.type("#email", "test@something.com")
#         self.type("#name", "Bob")
#         self.type("#password", "Testing#0")
#         self.type("#password2", "Testing#0")
#         self.click('input[type="submit"]')

#     def login(self):
#         self.open(base_url + '/login')
#         self.type("#email", "test@something.com")
#         self.type("#password", "Testing#0")
#         self.click('input[type="submit"]')

#     def profile(self):
#         self.open(base_url + '/sell')
#         self.type("#ticket_name", "test")
#         self.type("#quantity", 5)
#         self.type("#price", 20)
#         self.type("#expiration_date", "december 12 2020")
#         self.click('input[type="submit"]')

#     def logout(self):
#         self.open(base_url + '/logout')


    
  
#     # R3.1 If the user is not logged in, redirect to login page
#     def test_no_user_logged_in(self):
#         self.open(base_url + '/login')
#         self.assertTrue(self.get_current_url() == base_url + '/login')

   
#     # R3.2 This page shows a header 'Hi {}'.format(user.name)
#     def test_profile_message(self):
#          self.open(base_url + '/')
#          self.assert_element("#message")
         

   
#     # R3.3 This page shows user balance.
#     def test_balance(self):
#          self.open(base_url + '/')

#     # R3.4 This page shows a logout link, pointing to /logout
#     def test_logout_link(self):
#         self.register()
#         self.login()
#         self.open(base_url + '/')
#         self.assert_element("#btn-logout")


#     # R3.5 This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.
#     def test_available_tickets(self):
#         self.register()
#         self.login()
#         self.open(base_url + '/sell')
#         self.assert_element("#ticket_name")
#         self.assert_element("#quantity")
#         self.assert_element("#price")


  
#     # R3.6 This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date
#     def test_sell_tickets(self):
#         self.register()
#         self.login()
#         self.open(base_url + '/sell')
#         self.assert_element("#ticket_name")
#         self.assert_element("#quantity")
#         self.assert_element("#price")
#         self.assert_element("#expiration_date")

#     # R3.7 	This page contains a form that a user can buy new tickets. Fields: name, quantity
#     def test_buy_tickets(self):
#         self.register()
#         self.login()
#         self.open(base_url + '/sell')
#         self.assert_element("#ticket_name")
#         self.assert_element("#quantity")



#     # R3.8 This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date
#     def test_update_tickets(self):
#         self.register()
#         self.login()
#         self.open(base_url + '/sell')
#         self.assert_element("#ticket_name")
#         self.assert_element("#quantity")
#         self.assert_element("#price")
#         self.assert_element("#expiration_date")

#     # R3.9 The ticket-selling form can be posted to /sell
#     def test_posted_to_sell(self):
#         self.register()
#         self.login()
#         self.profile()


#     # R3.10 The ticket-buying form can be posted to /buy
#     def test_posted_to_buy(self):
#         self.register()
#         self.login()
#         self.open(base_url + '/sell')
#         self.type("#ticket_name", "")
#         self.type("#quantity", 0)
#         self.type("#price", 0)
#         self.type("#expiration_date", "")
#         self.type("#ticket_name", "test2")
#         self.type("#quantity", 10)
#         self.click('input[type="submit"]')

#     # R3.11 The ticket-update form can be posted to /update
#     def test_posted_to_update(self):
#         self.register()
#         self.login()
#         self.profile()
