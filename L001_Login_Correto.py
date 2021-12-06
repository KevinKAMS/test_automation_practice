import unittest
from selenium import webdriver
from lib import *


class L001(unittest.TestCase):
    def setUp(self):
        self.navegador = webdriver.Chrome()
        self.navegador.get("http://automationpractice.com/")

    def runTest(self):
        navegador = self.navegador
        open_website(navegador)
        open_sign_in(navegador)
        login_correct_email(navegador)
        login_correct_password(navegador)
        submit_login(navegador)
        assert check_sucessful_login(navegador)

    def tearDown(self):
        return self.navegador.close()


if __name__ == "__main__":
    unittest.main()
