from selenium.webdriver.support.wait import WebDriverWait

# selenium隐形等待，等待页面加载出对应元素，返回webelement
def getElement(driver,by,locate):
    '''
   　查找单一个元素
   　:param driver: 浏览器驱动
   　:param by: 定位方式，id, name, class, xpath...
   　:param locate: 定位表达式
   　:return: 元素
   　'''

    try:
        element = WebDriverWait(driver,10,0.2).until(lambda x:x.find_element(by,locate))
    except Exception as e:
        raise e
    else:
        return element