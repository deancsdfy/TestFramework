from selenium import webdriver
from lib.pageMethon import login
import time,unittest


class Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.indexUrl = 'https://movie.douban.com/'
        self.driver.get(self.indexUrl)

    def tearDown(self):
        time.sleep(2)
        self.driver.refresh()

    # 登录
    # @unittest.skip('skip-----')
    def test_login(self):
        login(self.driver)
        time.sleep(3)
        self.accountMsg = self.driver.find_element_by_class_name('bn-more').text
        self.assertEqual('小杨阳的帐号',self.accountMsg)
    
    # 搜索
    @unittest.skip('skip-----')
    def test_searchMovie(self):
        self.searchNav = self.driver.find_element_by_id('inp-query')
        self.searchNav.send_keys('少年的你')
        self.searchBtn = self.driver.find_element_by_xpath('//*[@id="db-nav-movie"]/div[1]/div/div[2]/form/fieldset/div[2]/input')
        self.searchBtn.click()
        time.sleep(2)
        self.title = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/a')
        self.title.click()
        self.subjectTitleText = self.driver.find_element_by_xpath('//*[@id="content"]/h1/span[1]').text
        self.assertEqual('少年的你',self.subjectTitleText)

    def test_commentTmplPhone(self):
        login(self.driver)
        self.url = 'https://movie.douban.com/subject/30166972/?from=showing'
        self.start5CommentBtn = self.driver.find_element_by_id('star5')
        self.start5CommentBtn.click()
        time.sleep(2)
        self.tmplPhoneMsg = self.driver.find_element_by_class_name('account-body-text').text
        self.assertEqual('验证手机号',self.tmplPhoneMsg)

if __name__ == "__main__":
    unittest.main()
