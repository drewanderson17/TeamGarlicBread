# import pytest
# import requests
# from selenium import webdriver
# from seleniumbase import BaseCase
# from qa327_test.conftest import base_url
# from unittest.mock import patch
# from qa327.models import db, User



# """
# test cases required for R7
# Logout will invalid the current session and redirect to the login page.
# After logout, the user shouldn't be able to access restricted pages.

# steps 
# 1. Mock backend.get_user to return a test_user instance

# 2. open /login
# 3. enter test_user's email into element #email
# 4. enter test_user's password into element #password
# 5. click element input[type="submit"]
# 6. open /logout
# 7. validate that return to login page occurs
# 8. click element input[type="submit]
# 9. validate that access to restricted pages is not given without re-entry of email and password
# """


# def test_check():
#     assert 10 >= 10


# class R7(BaseCase):
#     # mock a user information and register
#     def register(self):
#         # mock a user information
#         self.open(base_url + '/register')
#         self.type("#email", "StevenA@kingstong.com")
#         self.type("#name", "stevena")
#         self.type("#password", "scrum#Master1")
#         self.type("#password2", "scrum#Master1")
#         self.click('input[type="submit"]')

#     # test after logging out user is returned to /login page
#     def login(self):
#         self.open(base_url + '/login')
#         self.type("#email", "StevenA@kingstong.com")
#         self.type("#password", "scrum#Master1")
#         self.click('input[type="submit"]')

#     def test_logout(self):
#         self.register()
#         self.login()
#         self.open(base_url + '/logout')
#         self.assertTrue(self.get_current_url() == base_url + '/login')

#         #  	If the user hasn't logged in, show the login page

#     def test_restrictedPages(self):
#         self.register()
#         self.login()
#         self.open(base_url + '/logout')
#         self.open(base_url + '/profile')
#         self.assertTrue(self.get_current_url() == base_url + '/login')


    # def test_error_404(self):
    #     """register new user"""
    #     self.login()
    #     self.register()
    #     self.open(base_url + '/invalidadress')
    #     self.assertTrue(self.get_current_url() == base_url + '/invalidadress')

