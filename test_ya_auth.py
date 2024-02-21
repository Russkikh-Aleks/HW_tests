from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from unittest import TestCase


class TestYaAuth(TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_1_correct_data(self):

        driver = self.driver
        login = ""
        password = ""

        driver.get("https://passport.yandex.ru/auth/")
        time.sleep(2)
        self.assertIn('Авторизация', driver.title)
        element = driver.find_element(By.ID, 'passp-field-login')
        element.clear()
        element.send_keys(login)
        button = driver.find_element(By.ID, 'passp:sign-in')
        button.click()
        time.sleep(5)

        element = driver.find_element(By.ID, 'passp-field-passwd')
        element.clear()
        element.send_keys(password)

        button = driver.find_element(By.ID, 'passp:sign-in')
        button.click()

        time.sleep(5)
        self.assertIn('Яндекс ID', driver.title)

    def tearDown(self):
        self.driver.close()
