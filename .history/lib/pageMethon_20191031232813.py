from selenium import webdriver
import time

def login(driver,username='xiaoyang20122712@126.com',password='azy688987'):
    login_button = driver.find_element_by_link_text('登录/注册')
    login_button.click()
    passwordLoginTab = driver.find_element_by_class_name('account-tab-account')
    passwordLoginTab.click()
    usernameInput = driver.find_element_by_id('username')
    usernameInput.send_keys(username)
    passwordInput = driver.find_element_by_id('password')
    passwordInput.send_keys(password)
    loginButtin = driver.find_element_by_link_text('登录豆瓣')
    loginButtin.click()