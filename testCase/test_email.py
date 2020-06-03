import sys,unittest
import pytest,time
sys.path.append('.')
from PageObject.pageMethon import Login
from framework.logger import Logger
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

logger = Logger('log').getlogger()
class TestEmail163(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.indexUrl = 'https://email.163.com/'
        self.driver.get(self.indexUrl)

    def tearDown(self):
        self.driver.quit()

    # 登录
    def test_login(self):
        Login(self.driver,'deancsdfy@163.com','163688987').login_email163()
        
        self.uid =  WebDriverWait(self.driver, 10, 0.2).until(
            lambda x: x.find_element_by_id('spnUid')).text
        assert(self.uid,'deancsdfy@163.com')

    # 打开第一封邮件
    def test_openEmail(self):
        Login(self.driver,'deancsdfy@163.com','163688987').login_email163()
        self.emailComponentBtn =  WebDriverWait(self.driver, 20, 0.2).until(
            lambda x: x.find_element_by_xpath('/html/body/div[1]/nav/div[1]/ul/li[1]'))
        self.emailComponentBtn.click()
        logger.info('已点击收件箱')
        self.emailTitleBtn = WebDriverWait(self.driver, 20, 0.2).until(
            lambda x: x.find_element_by_class_name('dP0'))
        self.emailTitleBtn.click()
        logger.info('点击邮件收件人icon')
        time.sleep(2)
        self.emailAddrText = self.driver.find_element_by_class_name('nui-addr-email').text
        assert(self.emailAddrText,'<deancsdfy@163.com> ')


if __name__ == "__main__":
    unittest.main()