from selenium import webdriver
from framework.logger import Logger

logger = Logger('pageMethon').getlogger()

class Login():
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def login_db(self):
        self.login_button = self.driver.find_element_by_link_text('登录/注册')
        self.login_button.click()
        self.passwordLoginTab = self.driver.find_element_by_class_name(
            'account-tab-account')
        self.passwordLoginTab.click()
        self.usernameInput = self.driver.find_element_by_id('username')
        self.usernameInput.send_keys(self.username)
        self.passwordInput = self.driver.find_element_by_id('password')
        self.passwordInput.send_keys(self.password)
        self.loginButtin = self.driver.find_element_by_link_text('登录豆瓣')
        self.loginButtin.click()

    def login_email163(self):
        self.switch_email163Btn = self.driver.find_element_by_xpath('//*[@id="targetNav"]/a[1]')
        self.switch_email163Btn.click()
        iframe = self.driver.find_elements_by_tag_name('iframe')[0]
        logger.info('find iframe_ele')
        self.driver.switch_to_frame(iframe)
        logger.info('switch sucessful')
        self.usernameInput = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input')
        assert self.usernameInput