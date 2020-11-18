# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os,sys
BASE_PATH = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(BASE_PATH)
sys.path.append(os.path.join(BASE_PATH,'utils'))
from utils.config import Config
from utils.logger import Logger

logger = Logger(logger='BrowserDriver').getlog()

class BrowserDriver():
    def __init__(self):
        self.c = Config()

    def getUrl(self,url):
        self.url = self.c.get('URL').get(url)
        logger.info('选择的URL为：{}'.format(self.url))
        return self.url

    def openbrower(self,url):
        broswer = self.c.get('brwserType').get('browserName')
        logger.info('选择的浏览器为：{}浏览器'.format(broswer))
        if broswer == 'Chrome':
            driver = webdriver.Chrome(self.c.get_chrom_driver_path()) #用于Windows系统加载驱动使用
            # driver = webdriver.Chrome() #用于linux系统加载驱动使用
            logger.info("启动谷歌浏览器")            
        elif broswer == "Firefox":
            driver = webdriver.Firefox()
            logger.info("启动火狐浏览器")
        elif broswer == "IE":
            driver = webdriver.Ie(self.c.get_ie_driver_path())
            logger.info("启动IE浏览器")
        else:
            logger.error('不支持该浏览器')
        
        driver.get(url)
        logger.info('打开URL：{}'.format(url))
        # driver.maximize_window()
        # logger.info("全屏当前窗口")
        driver.implicitly_wait(5)
        logger.info("设置5秒隐式等待时间")
        self.driver = driver
        return self.driver
    
    def quit_browser(self):
        logger.info("关闭浏览器")
        self.driver.quit()

# if __name__ == "__main__":
#     browser = BrowserDriver()
#     browser.getBaiduUrl()
#     browser.openbrower()
#     browser.quit_browser()
