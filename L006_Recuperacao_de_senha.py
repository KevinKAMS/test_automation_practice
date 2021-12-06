import unittest
from selenium import webdriver
from lib import *


class L006(unittest.TestCase):
    def setUp(self):
        self.navegador = webdriver.Chrome()
        self.navegador.get("http://automationpractice.com/")

    def runTest(self):
        navegador = self.navegador
        open_website(navegador)
        open_sign_in(navegador)
        open_forgot_password(navegador)
        login_correct_email(navegador)
        retrieve_password(navegador)
        assert check_sucess_box(navegador)

    def tearDown(self):
        return self.navegador.close()


if __name__ == "__main__":
    unittest.main()
