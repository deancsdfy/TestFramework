from selenium import webdriver
from lib.pageMethon import login
import time,unittest,logging

# create logger
logger_name = "douban_testCase"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.INFO)

# create file handler
log_path = "./log/douban.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.WARN)

# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(funcName)s %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)

class Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.indexUrl = 'https://movie.douban.com/'
        self.driver.get(self.indexUrl)

    def tearDown(self):
        time.sleep(2)
        self.driver.refresh()

    # 登录
    @unittest.skip('skip-----')
    def test_login(self):
        login(self.driver)
        time.sleep(3)
        self.accountMsg = self.driver.find_element_by_class_name('bn-more').text
        self.assertEqual('小杨阳的帐号',self.accountMsg)
        logger.info('登陆成功')
    
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
