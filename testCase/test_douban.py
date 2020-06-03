import sys
sys.path.append('.')
import pytest
from PageObject.pageMethon import Login
from framework.logger import Logger
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import unittest

logger = Logger('log').getlogger()
class TestDouban(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.indexUrl = 'https://movie.douban.com/'
        self.driver.get(self.indexUrl)

    def tearDown(self):
        self.driver.quit()

    # 登录默认正确的账号和密码
    def test_login(self):
        Login(self.driver, 'xiaoyang20122712@126.com', 'azy688987').login_db()
        self.accountMsg = WebDriverWait(self.driver, 20, 0.2).until(
            lambda x: x.find_element_by_class_name('bn-more')).text
        assert('小杨阳的帐号', self.accountMsg)

    # 搜索
    def test_searchMovie(self):
        self.searchNav = self.driver.find_element_by_id('inp-query')
        self.searchNav.send_keys('少年的你')
        logger.info('搜索框输入"少年的你"')
        self.searchBtn = self.driver.find_element_by_xpath(
            '//*[@id="db-nav-movie"]/div[1]/div/div[2]/form/fieldset/div[2]/input')
        self.searchBtn.click()
        logger.info('点击搜索按钮')
        self.title = WebDriverWait(self.driver, 20, 0.2).until(lambda x: x.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/a'))
        self.title.click()
        logger.info('点击搜索到的关键词内容')
        self.subjectTitleText = self.driver.find_element_by_xpath(
            '//*[@id="content"]/h1/span[1]').text
        assert('少年的你', self.subjectTitleText)

    # # 评论验证手机号码
    # def test_commentTmplPhone(self):
    #     Login(self.driver, 'xiaoyang20122712@126.com', 'azy688987').login_db()
    #     self.post1 = WebDriverWait(self.driver, 20, 0.2).until(
    #         lambda x: x.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[3]/div[3]/div/div[1]/div/div[2]/a[1]/div'))
    #     self.post1.click()
    #     self.start5CommentBtn = WebDriverWait(self.driver, 20, 0.2).until(
    #         lambda x: x.find_element_by_xpath('//*[@id="star5"]'))
    #     self.start5CommentBtn.click()
    #     self.tmplPhoneMsg = WebDriverWait(self.driver, 20, 0.2).until(
    #         lambda x: x.find_element_by_class_name('account-body-text')).text
    #     assert('验证手机号', self.tmplPhoneMsg)

    # 下载豆瓣客户的APP窗口正常显示弹出
    def test_downloadAppPanelisDisable(self):
        self.lnkDownloadApp = WebDriverWait(self.driver, 20, 0.2).until(
            lambda x: x.find_element_by_link_text('下载豆瓣客户端'))
        ActionChains(self.driver).move_to_element(self.lnkDownloadApp).perform()
        logger.info('鼠标悬浮在下载客户端hover出')
        doubanappCssValue = self.driver.find_element_by_class_name(
            'top-nav-doubanapp').value_of_css_property('display')
        logger.info('判断下载的二维码是否可见')
        assert('block', doubanappCssValue)
