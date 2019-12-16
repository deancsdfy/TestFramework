from selenium import webdriver
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
        self.login_button = self.driver.find_element_by_link_text('登录/注册')
        self.login_button.click()
        self.passwordLoginTab = self.driver.find_element_by_class_name('account-tab-account')
        self.passwordLoginTab.click()
        self.usernameInput = self.driver.find_element_by_id('username')
        self.usernameInput.send_keys('xiaoyang20122712@126.com')
        self.passwordInput = self.driver.find_element_by_id('password')
        self.passwordInput.send_keys('azy688987')
        self.loginButtin = self.driver.find_element_by_link_text('登录豆瓣')
        self.loginButtin.click()
        time.sleep(3)
        self.accountMsg = self.driver.find_element_by_class_name('bn-more').text
        self.assertEqual('小杨阳的帐号',self.accountMsg)
    
    # 搜索
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

if __name__ == "__main__":
    unittest.main()
