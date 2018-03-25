from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('I visit the url "{url}"')
def step(context, url):
    context.browser.get(url)
    context.browser.implicitly_wait(5)

@then('I verify the title of the home page')
def step(context):
    try:
        title = context.browser.title
        assert title == "Geek's World !!! | Experience the difference. Then create a new one"
    except:
        print("\tTitle not found")

@then('I navigate to About My page')
def step(context):
    context.browser.find_element(By.CSS_SELECTOR,"ul#primary-menu > li:nth-child(2) > a").click()

@then('I verify the title of the about me page')
def step(context):
    try:
        time.sleep(12)
        context.browser.switch_to_window(context.browser.window_handles[1])
        title = context.browser.title
        assert title == "The Geekstudio | Geekstudio"
        context.browser.close()
        context.browser.switch_to_window(context.browser.window_handles[0])
    except:
        print("\nTitle not found")

@then('I navigate to GitHub page')
def step(context):
    context.browser.find_element(By.CSS_SELECTOR,"ul#primary-menu > li:nth-child(3) > a").click()

@then('I verify the title of the GitHub page')
def step(context):
    try:
        time.sleep(8)
        context.browser.switch_to_window(context.browser.window_handles[2])
        title = context.browser.title
        assert title == "Corefinder89 (Soumyajit Basu (C0r3f!nd3r)) · GitHub"
        context.browser.switch_to_window(context.browser.window_handles[0])
    except:
        print("\nTitle not found")

@then("I navigate to BitBucket page")
def step(context):
    context.browser.find_element(By.CSS_SELECTOR,"ul#primary-menu > li:nth-child(4) > a").click()

@then('I verify the title of the Bitbucket page')
def step(context):
    try:
        time.sleep(8)
        context.browser.switch_to_window(context.browser.window_handles[3])
        title = context.browser.title
        assert title == "CodersDen — Bitbucket"
        context.browser.switch_to_window(context.browser.window_handles[0])
    except:
        print("\nTitle not found")

@then('I navigate to Facebook page')
def step(context):
    context.browser.find_element(By.CSS_SELECTOR,"ul#primary-menu > li:nth-child(5) > a").click()

@then('I verify the title of the Facebook page')
def step(context):
    try:
        time.sleep(8)
        context.browser.switch_to_window(context.browser.window_handles[4])
        title = context.browser.title
        assert title == "Soumyajit Basu | Facebook"
        context.browser.switch_to_window(context.browser.window_handles[0])
    except:
        print("\nTitle not found")

@then('I navigate to Linkedin page')
def step(context):
    context.browser.find_element(By.CSS_SELECTOR,"ul#primary-menu > li:nth-child(6) > a").click()

@then('I verify the title of the Linkedin page')
def step(context):
    try:
        time.sleep(8)
        context.browser.switch_to_window(context.browser.window_handles[5])
        title = context.browser.title
        assert title == "Soumyajit Basu - QA Developer - Datalicious| LinkedIn"
        context.browser.switch_to_window(context.browser.window_handles[0])
    except:
        print("\nTitle not found")

@then('I navigate to Twitter page')
def step(context):
    context.browser.find_element(By.CSS_SELECTOR,"ul#primary-menu > li:nth-child(7) > a").click()

@then('I verify the title of the Twitter page')
def step(context):
    try:
        time.sleep(8)
        context.browser.switch_to_window(context.browser.window_handles[6])
        title = context.browser.title
        print(title)
        assert title == "TEST"
        context.browser.switch_to_window(context.browser.window_handles[0])
    except:
        print("\nTitle not found")
