from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
chrome_options = Options()
chrome_options.add_experimental_option('prefs',{
 'credentials_enable_service':False,
    'profile':{
        'password_manager_enabled':False
    }
})

def before_all(context):
    bin_path = "/Users/apple/.npm-global/bin/chromedriver"
    context.browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=bin_path)
    context.browser.maximize_window()
    context.browser.implicitly_wait(5)

def after_all(context):
    context.browser.quit()
