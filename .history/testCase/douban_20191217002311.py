import sys
sys.path.append('.')
from framework.logger import Logger
from PageObject.pageMethon import Login
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import unittest

logger = Logger('douban').getlogger()


class Douban(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.indexUrl = 'https://movie.douban.com/'
        self.driver.get(self.indexUrl)

    def tearDown(self):
        self.driver.quit()

    # 登录默认正确的账号和密码
    def test_login(self):
        Login(self.driver, 'xiaoyang20122712@126.com', 'azy688987').login_db()
        self.accountMsg = WebDriverWait(self.driver, 20, 0.2).until(
            lambda x: x.find_element_by_class_name('bn-more')).text
        self.assertEqual('小杨阳的帐号', self.accountMsg)
        logger.info('页面跳转成功')

    # 搜索
    def test_searchMovie(self):
        self.searchNav = self.driver.find_element_by_id('inp-query')
        self.searchNav.send_keys('少年的你')
        self.searchBtn = self.driver.find_element_by_xpath(
            '//*[@id="db-nav-movie"]/div[1]/div/div[2]/form/fieldset/div[2]/input')
        self.searchBtn.click()
        logger.info('页面跳转成功')
        self.title = WebDriverWait(self.driver, 20, 0.2).until(lambda x: x.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/a'))
        self.title.click()
        logger.info('页面跳转成功')
        self.subjectTitleText = self.driver.find_element_by_xpath(
            '//*[@id="content"]/h1/span[1]').text
        self.assertEqual('少年的你', self.subjectTitleText)

    # 评论验证手机号码
    def test_commentTmplPhone(self):
        Login(self.driver, 'xiaoyang20122712@126.com', 'azy688987').login_db()
        self.post1 = WebDriverWait(self.driver, 20, 0.2).until(
            lambda x: x.find_element_by_xpath('//*[@id="screening"]/div[2]/ul/li[6]/ul/li[1]'))
        self.post1.click()
        logger.info('页面跳转成功')
        self.start5CommentBtn = WebDriverWait(self.driver, 20, 0.2).until(
            lambda x: x.find_element_by_id('star5'))
        self.start5CommentBtn.click()
        logger.info('页面跳转成功')
        self.tmplPhoneMsg = WebDriverWait(self.driver, 20, 0.2).until(
            lambda x: x.find_element_by_class_name('account-body-text')).text
        self.assertEqual('验证手机号', self.tmplPhoneMsg)

    # 下载豆瓣客户的APP窗口正常显示弹出
    def test_downloadAppPanelisDisable(self):
        self.lnkDownloadApp = WebDriverWait(self.driver, 20, 0.2).until(
            lambda x: x.find_element_by_link_text('下载豆瓣客户端'))
        ActionChains(self.driver).move_to_element(self.lnkDownloadApp).perform()
        doubanappCssValue = self.driver.find_element_by_class_name(
            'top-nav-doubanapp').value_of_css_property('display')
        self.assertEqual('block', doubanappCssValue)
        logger.info('test ok')


if __name__ == "__main__":
    unittest.main()
