import unittest
from selenium import webdriver
from lib import *


class C005(unittest.TestCase):
    def setUp(self):
        self.navegador = webdriver.Chrome()
        self.navegador.get("http://automationpractice.com/")

    def runTest(self):
        navegador = self.navegador
        open_website(navegador)
        open_sign_in(navegador)
        cadastro_correct_email(navegador)
        submit_cadastro(navegador)
        cadastro_incorreto(navegador)
        submit_register(navegador)
        assert check_error_box(navegador)

    def tearDown(self):
        return self.navegador.close()


if __name__ == "__main__":
    unittest.main()
