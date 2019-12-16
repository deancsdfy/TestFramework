import sys,unittest
sys.path.append('.')
from framework.logger import Logger
from PageObject.pageMethon import Login
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

logger = Logger('163').getlogger()

class Test_email163(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.indexUrl = 'https://email.163.com/'
        self.driver.get(self.indexUrl)

    def tearDown(self):
        self.driver.quit()

    # # 登录
    # def test_login(self):
    #     Login(self.driver,'deancsdfy@163.com','163688987').login_email163()
    #     self.uid =  WebDriverWait(self.driver, 20, 0.2).until(
    #         lambda x: x.find_element_by_id('spnUid')).text
    #     self.assertEqual(self.uid,'deancsdfy@163.com')

    # 打开第一封邮件
    # def test_openEmail(self):
    #     Login(self.driver,'deancsdfy@163.com','163688987').login_email163()
    #     logger.info('login sucessful')
    #     self.emailComponentBtn =  WebDriverWait(self.driver, 20, 0.2).until(
    #         lambda x: x.find_element_by_xpath('/html/body/div[1]/nav/div[1]/ul/li[1]'))
    #     self.emailComponentBtn.click()
    #     logger.info('open EmailComponent suessful')
    #     self.emailTitleBtn = WebDriverWait(self.driver, 20, 0.2).until(
    #         lambda x: x.find_element_by_class_name('dP0'))
    #     self.emailTitleBtn.click()
    #     logger.info('open Email suessful')
    #     self.emailAddrText = WebDriverWait(self.driver, 20, 0.2).until(
    #         lambda x: x.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[2]/ul[2]/li[3]/div[2]/div/span[2]')).text
    #     self.assertEqual(self.emailAddrText,'<deancsdfy@163.com> ')

    # 关闭首页广告
    def test_closeIndexAd(self):
        Login(self.driver,'deancsdfy@163.com','163688987').login_email163()
        logger.info('login sucessful')
        self.adWindow = WebDriverWait(self.driver, 20, 0.2).until(
            lambda x: x.find_element_by_class_name('gWel-recommend  nui-closeable'))
        self.isadWindow = self.assertTrue(self.adWindow)
        print(self.isadWindow)
        self.closeAdBtn =  self.driver.find_element_by_class_name('js-component-component nui-closeable-x')
        self.closeAdBtn.click()

if __name__ == "__main__":
    unittest.main()