# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
import os,sys
BASE_PATH = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(BASE_PATH)
from common.SeleniumMethon import BasePage
from common.BrowserDriver import BrowserDriver
from utils.config import Config
from utils.logger import Logger

logger = Logger(logger='HomePage').getlog()

class HomePage(BasePage):
    logger.info('page实例创建成功')

    """
    在这里写定位器，通过元素属性定位元素对象
    """
    loginByTel_tab = (By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/nav/ul/li[2]/span')#定位通过手机号码登录按钮
    loginByPassword_tab = (By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/section/div[2]/div/p')#定位通过密码登录按钮
    login_btn = (By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/section/div[2]/div/button')#定位提交登录按钮
    loginTel_input = (By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/section/div[2]/div/div[1]/div/div/input')#定位手机号码输入框
    loginPassword_input = (By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/section/div[2]/div/div[2]/div/div/input')#定位密码输入框
    homepage_title = (By.XPATH,'//*[@id="app"]/section/header/div[1]/span')#定位页面标题

    def click_loginByTel_tab(self):
        self.click(self.loginByTel_tab)

    def click_loginByPassword_tab(self):
        self.click(self.loginByPassword_tab)

    def input_loginTel(self,text):
        self.send_key(self.loginTel_input[0],self.loginTel_input[1],text=text)

    def input_loginPassword(self,text):
        self.send_key(self.loginPassword_input[0],self.loginPassword_input[1],text=text)

    def click_login_btn(self):
        self.click(self.login_btn)

    def login(self):
        self.click_loginByTel_tab()
        self.click_loginByPassword_tab()
        self.username = self.c.get_case_data('HomePage').get('username')
        self.input_loginTel(self.username)
        self.password = self.c.get_case_data('HomePage').get('password')
        self.input_loginPassword(self.password)
        self.click_login_btn()
        logger.info('登录成功')

    def show_homepage_title(self):
        return self.find_element(self.homepage_title[0],self.homepage_title[1]).text

# if __name__ == "__main__":
#     browser = BrowserDriver()
#     url = browser.getUrl('homepage_url')
#     driver = browser.openbrower(url)
#     page = HomePage(driver)
#     page.login()
#     print(page.show_homepage_title())