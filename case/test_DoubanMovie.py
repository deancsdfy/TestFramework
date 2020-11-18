import unittest,pytest
import os,sys
BASE_PATH = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(BASE_PATH)
from page.DoubanMoviePage import DoubanMoviePage
from common.BrowserDriver import BrowserDriver
from utils.logger import Logger
from utils.config import Config

logger = Logger('test_Douban').getlog()

class TestDoubanMovie(unittest.TestCase,DoubanMoviePage):
    def setUp(self):
        self.browser = BrowserDriver()
        self.url = self.browser.getUrl('douban_url')
        self.driver = self.browser.openbrower(self.url)
        self.page = DoubanMoviePage(self.driver)

    def tearDown(self):
        self.page.close()

    def test_byAccountLoginDouban(self):
        logger.info('-----测试账号密码登录-----')
        self.page.click_login_btn()
        logger.info('点击注册/登录按钮')
        self.page.switch_accountLogin_btn()
        logger.info('切换通过账号登录')
        self.c = Config()
        username = self.c.get_case_data('DoubanMovie').get('username')
        self.page.input_account(username)
        logger.info('输入账号')
        password = self.c.get_case_data('DoubanMovie').get('password')
        self.page.input_password(password)
        logger.info('输入密码')
        self.page.click_loginSubmit_btn()
        logger.info('点击登录按钮')
        username = self.page.show_username()
        logger.info('断言是否符合预期的账号昵称')
        assert('小杨阳的帐号',username)

    def test_search(self,text='少年的你'):
        logger.info('-----测试搜索结果准确性-----')
        self.page.input_search(text)
        logger.info('搜索框输入：{}'.format(text))
        self.page.click_search_btn()
        logger.info('点击搜索按钮')
        self.page.click_searchList1_title()
        logger.info('点击搜索结果列表第一项标题')
        searchContent_title = self.page.show_searchContent_title()
        logger.info('断言内容标题是否符合预期值')
        assert(text,searchContent_title)

    def test_downloadAppPanel(self):
        logger.info('-----测试首页悬浮二维码能否弹出-----')
        self.page.move_toLnkDownloadAppBtn()
        logger.info('鼠标悬浮在下载客户端hover出')
        doubanappCssValue = self.page.show_doubanappBoxCssValue('display')
        logger.info('判断下载的二维码是否可见')
        assert('block', doubanappCssValue)