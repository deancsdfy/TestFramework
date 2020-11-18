import unittest,pytest
import os,sys
BASE_PATH = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(BASE_PATH)
from page.Email163Page import Email163Page
from common.BrowserDriver import BrowserDriver
from utils.logger import Logger
from utils.config import Config

logger = Logger('test_Email163').getlog()

class TestDouban(unittest.TestCase,Email163Page):
    def setUp_method(self):
        self.browser = BrowserDriver()
        self.url = self.browser.getUrl('email163_url')
        self.driver = self.browser.openbrower(self.url)
        self.page = Email163Page(self.driver)

    def tearDown_method(self):
        self.driver.close()

    def test_byAccountLoginDouban(self):
        logger.info('-----测试账号密码登录-----')
        self.page.click_switchEmail163_btn()
        logger.info('点击切换163邮箱登录')
        self.page.switch_login_iframe()
        logger.info('切换163邮箱登录iframe')
        self.c = Config()
        username = self.c.get_case_data('Email163').get('username')
        self.page.input_account(username)
        logger.info('输入账号')
        password = self.c.get_case_data('Email163').get('password')
        self.page.input_password(password)
        logger.info('输入密码')
        self.page.click_loginSubmit_btn()
        logger.info('点击登录按钮')
        pageTitle = self.page.get_page_title()
        assert('网易邮箱6.0版',pageTitle)

    def test_openFirstRecEmail(self):
        logger.info('-----测试收件箱邮件收件人-----')
        self.page.loggin()
        self.page.click_emailComponent_btn()
        logger.info('点击收件箱')
        self.page.click_recEmailTitle()
        logger.info('点击收件箱第一封邮件')
        emailAddr = self.page.get_emailAddr()
        logger.info('断言是否符合预期的收件人地址')
        assert('<deancsdfy@163.com>',emailAddr)