from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


def open_website(navegador):
    return navegador.get("http://automationpractice.com/")


def open_sign_in(navegador):
    return navegador.find_element_by_xpath(
        "/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a"
    ).click()


def open_forgot_password(navegador):
    return navegador.find_element_by_xpath('//*[@id="login_form"]/div/p[1]/a').click()


def cadastro_correct_email(navegador):
    email = navegador.find_element_by_xpath('//*[@id="email_create"]')
    email.send_keys("qwerty@gmaiol.com")
    return


def cadastro_incorrect_email(navegador):
    email = navegador.find_element_by_xpath('//*[@id="email_create"]')
    email.send_keys("qwerty")
    return


def cadastro_repeat_email(navegador):
    email = navegador.find_element_by_xpath('//*[@id="email_create"]')
    email.send_keys("kamsauxilar@gmail.com")
    return


def login_correct_email(navegador):
    email = navegador.find_element_by_xpath('//*[@id="email"]')
    email.send_keys("kamsauxilar@gmail.com")
    return


def login_incorrect_email(navegador):
    email = navegador.find_element_by_xpath('//*[@id="email"]')
    email.send_keys("qwerty1234@gemaiol.com")
    return


def login_incorrect_password(navegador):
    senha = navegador.find_element_by_xpath('//*[@id="passwd"]')
    senha.send_keys("qwerty123#")
    return


def login_correct_password(navegador):
    senha = navegador.find_element_by_xpath('//*[@id="passwd"]')
    senha.send_keys("jnF@p9M!rkg2y2U")
    return


def submit_login(navegador):
    return navegador.find_element_by_xpath('//*[@id="SubmitLogin"]/span').click()


def submit_cadastro(navegador):
    return navegador.find_element_by_xpath('//*[@id="SubmitCreate"]/span').click()


def submit_register(navegador):
    try:
        register_button = WebDriverWait(navegador, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="submitAccount"]/span')
            )
        )
        register_button.click()
    except:
        return


# //*[@id="form_forgotpassword"]/fieldset/p/button/span
def retrieve_password(navegador):
    try:
        retrieve_password = WebDriverWait(navegador, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="form_forgotpassword"]/fieldset/p/button/span')
            )
        )
        retrieve_password.click()
    except:
        return


def cadastro_correto(navegador):
    try:
        first_name = WebDriverWait(navegador, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="customer_firstname"]')
            )
        )
        first_name.send_keys("qwerty")
    except:
        return
    last_name = navegador.find_element_by_xpath('//*[@id="customer_lastname"]')
    last_name.send_keys("asdf")
    password = navegador.find_element_by_xpath('//*[@id="passwd"]')
    password.send_keys("Qwr32#1sad")
    adress = navegador.find_element_by_xpath('//*[@id="address1"]')
    adress.send_keys("Rua 123")
    adress = navegador.find_element_by_xpath('//*[@id="city"]')
    adress.send_keys("City6745")
    state = Select(navegador.find_element_by_xpath('//*[@id="id_state"]'))
    state.select_by_value("3")
    zipcode = navegador.find_element_by_xpath('//*[@id="postcode"]')
    zipcode.send_keys("12345")
    phone = navegador.find_element_by_xpath('//*[@id="phone_mobile"]')
    phone.send_keys("12345678910")
    # //*[@id="submitAccount"]/span


def cadastro_incorreto(navegador):
    try:
        first_name = WebDriverWait(navegador, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="customer_firstname"]')
            )
        )
        first_name.send_keys("qwerty")
    except:
        return
    last_name = navegador.find_element_by_xpath('//*[@id="customer_lastname"]')
    last_name.send_keys("asdf")
    password = navegador.find_element_by_xpath('//*[@id="passwd"]')
    password.send_keys("Qwr32#1sad")
    adress = navegador.find_element_by_xpath('//*[@id="address1"]')
    adress.send_keys("Rua 123")
    adress = navegador.find_element_by_xpath('//*[@id="city"]')
    adress.send_keys("City6745")
    state = navegador.find_element_by_xpath('//*[@id="id_state"]')
    state.send_keys("Alabama")
    state.send_keys(Keys.RETURN)
    zipcode = navegador.find_element_by_xpath('//*[@id="postcode"]')
    zipcode.send_keys("1234578910")
    phone = navegador.find_element_by_xpath('//*[@id="phone_mobile"]')
    phone.send_keys("12345678910")
    # //*[@id="submitAccount"]/span


def check_sucessful_login(navegador):
    try:
        my_account = WebDriverWait(navegador, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="center_column"]/div/div[1]/ul/li[4]/a/span')
            )
        )
        return True
    except:
        return False


def check_create_empty_fields_error(navegador):
    try:
        authentication_error = WebDriverWait(navegador, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="center_column"]/div')
            )
        )
        return True
    except:
        return False


def check_error_box(navegador):
    try:
        authentication_error = WebDriverWait(navegador, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CLASS_NAME, "alert-danger")
            )
        )
        return True
    except:
        return False


def check_sucess_box(navegador):
    try:
        authentication_error = WebDriverWait(navegador, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CLASS_NAME, "alert-success")
            )
        )
        return True
    except:
        return False


# //*[@id="create_account_error"]/ol/li
# An account using this email address has already been registered. Please enter a valid password or request a new one.
