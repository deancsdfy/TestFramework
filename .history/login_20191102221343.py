from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.pageMethon import login
from lib.myLog import loggert
import unittest

logger = loggert('douban')

class Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.indexUrl = 'https://movie.douban.com/'
        self.driver.get(self.indexUrl)

    def tearDown(self):
        self.driver.quit()

    # 登录默认正确的账号和密码
    @unittest.skip('...')
    def test_login(self):
        login(self.driver)
        self.accountMsg = WebDriverWait(self.driver,20,0.2).until(lambda x:x.find_element_by_class_name('bn-more')).text
        self.assertEqual('小杨阳的帐号',self.accountMsg)
        logger.info('页面跳转成功')

    # @unittest.skip('...')
    def test_login_errorPassword(self):
        login(self.driver,'xiaoyang20122712@126.com','123')
        self.accountMsg = WebDriverWait(self.driver,20,0.2).until(lambda x:x.find_element_by_class_name('account-form-error')).text
        logger.info('页面跳转成功')
        self.assertEqual('用户名或密码错误',self.accountMsg)


    # 搜索
    @unittest.skip('...')
    def test_searchMovie(self):
        self.searchNav = self.driver.find_element_by_id('inp-query')
        self.searchNav.send_keys('少年的你')
        self.searchBtn = self.driver.find_element_by_xpath('//*[@id="db-nav-movie"]/div[1]/div/div[2]/form/fieldset/div[2]/input')
        self.searchBtn.click()
        logger.info('页面跳转成功')
        self.title = WebDriverWait(self.driver,20,0.2).until(lambda x:x.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/a'))
        self.title.click()
        logger.info('页面跳转成功')
        self.subjectTitleText = self.driver.find_element_by_xpath('//*[@id="content"]/h1/span[1]').text
        self.assertEqual('少年的你',self.subjectTitleText)

    @unittest.skip('...')
    def test_commentTmplPhone(self):
        login(self.driver)
        self.post1 = WebDriverWait(self.driver,20,0.2).until(lambda x:x.find_element_by_xpath('//*[@id="screening"]/div[2]/ul/li[6]/ul/li[1]'))
        self.post1.click()
        logger.info('页面跳转成功')
        self.start5CommentBtn = WebDriverWait(self.driver,20,0.2).until(lambda x:x.find_element_by_id('star5'))
        self.start5CommentBtn.click()
        logger.info('页面跳转成功')
        self.tmplPhoneMsg = WebDriverWait(self.driver,20,0.2).until(lambda x:x.find_element_by_class_name('account-body-text'))
        self.assertEqual('验证手机号',self.tmplPhoneMsg)

if __name__ == "__main__":
    unittest.main()