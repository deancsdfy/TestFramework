from selenium import webdriver
from lib.pageMethon import login
from lib.myLog import loggert
import time,unittest

logger = loggert('douban')

class Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.indexUrl = 'https://movie.douban.com/'
        self.driver.get(self.indexUrl)

    def tearDown(self):
        time.sleep(2)
        self.driver.refresh()

    # 登录默认正确的账号和密码
    @unittest.skip('skip-----')
    def test_login(self):
        login(self.driver)
        time.sleep(3)
        self.accountMsg = self.driver.find_element_by_class_name('bn-more').text
        self.assertEqual('小杨阳的帐号',self.accountMsg)
        logger.info('页面跳转成功')
    
    def test_login_errorPassword(self):
        login(self.driver,username,'123')
        time.sleep(3)


    # 搜索
    @unittest.skip('skip-----')
    def test_searchMovie(self):
        self.searchNav = self.driver.find_element_by_id('inp-query')
        self.searchNav.send_keys('少年的你')
        self.searchBtn = self.driver.find_element_by_xpath('//*[@id="db-nav-movie"]/div[1]/div/div[2]/form/fieldset/div[2]/input')
        self.searchBtn.click()
        logger.info('页面跳转成功')
        time.sleep(2)
        self.title = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/a')
        self.title.click()
        logger.info('页面跳转成功')
        self.subjectTitleText = self.driver.find_element_by_xpath('//*[@id="content"]/h1/span[1]').text
        self.assertEqual('少年的你',self.subjectTitleText)
    
    @unittest.skip('skip-----')
    def test_commentTmplPhone(self):
        login(self.driver)
        time.sleep(2)
        self.post1 = self.driver.find_element_by_xpath('//*[@id="screening"]/div[2]/ul/li[6]/ul/li[1]')
        self.post1.click()
        logger.info('页面跳转成功')
        time.sleep(3)
        self.start5CommentBtn = self.driver.find_element_by_id('star5')
        self.start5CommentBtn.click()
        logger.info('页面跳转成功')
        time.sleep(2)
        self.tmplPhoneMsg = self.driver.find_element_by_class_name('account-body-text').text
        self.assertEqual('验证手机号',self.tmplPhoneMsg)

if __name__ == "__main__":
    unittest.main()
