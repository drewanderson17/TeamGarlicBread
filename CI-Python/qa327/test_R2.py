# Test Cases for R2 requirements 
import pytest
import requests
from selenium import webdriver
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User

'''
class R2(BaseCase):

    # User has logged in redirect them to the homepage, otherwise show registration page
    def test_user_loggedin(self):
        self.open(base_url)
        self.assertTrue(self.get_current() == base_url + '/')


    # Registration page shows a form requesting: email, user name, password, password 2
    def test_fieldsRegistration (self):
        self.open(base_url + '/') 
        self.assert_element("#username")
        self.assert_element("#email")
        self.assert_element("#password")
        self.assert_element("#password2")
        self.assert_element("#btn-submit") 

    # Registration for can be sumbitted as a POST
    # Email, password, password2 all have to satisfy the same required as defined in R1
    def test_valid_entries(self):
        emailsToTestValid = ["email@me.com", "email@email", "e56@gmail.com", "e_#$37@test.ca","e@online", "222g22@k.com", "me@g--g.ca"]
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


    # Password and password2 have to be exactly the same
    def test_password_match(self):
        self.open(base_url + '/')
        self.assert_True("#password" === "password2")
    
    # User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.
    def test_username_valid(self):
        validName = ["Juliana", " Alex " ]
        invalidName = ["666", "7juli", "#adam" ]

        for name in validName:
            self.open(base_url + '/register')
            self.type("#email", "nick@email.com")
            self.type("#name", name)
            self.type("#password", "Test12!")
            self.type("#password2", "Test12!")
            self.click('input[type="submit"]')
            self.assertTrue(self.get_current_url() == base_url + '/')
            self.logout()

        for name in invalidName:
            self.open(base_url + '/register')
            self.type("#email", "nick@email.com")
            self.type("#name", name)
            self.type("#password", "Test12!")
            self.type("#password2", "Test12!")
            self.click('input[type="submit"]')
            self.assertTrue(self.get_current_url() == base_url + '/')
    
        # User name has to be longer than 2 characters and less than 20 characters.
    def test_name_length(self):
        validname = ["ramtin", "daniel","drew"]
        invalidname = ["an", "bl", "qwertyuiopasdfghjklzxcv"]
            for name in validName:
                self.open(base_url + '/register')
                self.type("#email", "nick@email.com")
                self.type("#name", name)
                self.type("#password", "Test12!")
                self.type("#password2", "Test12!")
                self.click('input[type="submit"]')
                self.assertTrue(self.get_current_url() == base_url + '/')
                self.logout()

            for name in invalidName:
                self.open(base_url + '/register')
                self.type("#email", "nick@email.com")
                self.type("#name", name)
                self.type("#password", "Test12!")
                self.type("#password2", "Test12!")
                self.click('input[type="submit"]')
                self.assertTrue(self.get_current_url() == base_url + '/')

    # For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)
    # This is covered in R1 - running a similar test here with username added 

     def test_invalidFormat(self):
        self.open(base_url + '/')
        self.type("#email", "bademail")  # invalid
        self.type("#password", "Steven1!")  # valid
        self.type("username", "Steven") #valid
        self.click('input[type="submit"]')
        self.assert_text("format is incorrect", "#message")
        self.assertTrue(self.get_current_url() == base_url + '/')
        self.open(base_url + '/')
        self.type("#email", "goodemail@gmail.com")  # valid
        self.type("#password", "bad_password")  # invalid
        self.type("username", "Steven") #valid
        self.click('input[type="submit"]')
        self.type("#email", "goodemail@gmail.com")  # valid
        self.type("#password", "Steven1!")  # valid
        self.type("username", "Stev7en") #invalid
        self.assert_text("Email/password format is incorrect", "#message")
        self.assertTrue(self.get_current_url() == base_url + '/')

    # If the email already exists, show message 'this email has been ALREADY used'
     def  test_email_exists(self):
         usedemail = ["email@email", "juli@me"]
         self.open(base_url+ '/register')
         for email in usedemail:
            self.type("#email", "nick@email.com")
            # removed for errors
           # if (self.elf.assert_True("email" === email):
            #    self.assert_text("this email has been ALREADY used", "#message")
            


    # If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
    #def test_works(self):
     #   self.register()
      #  self.login()
       # self.assertTrue(balance = balance +5000)

'''
