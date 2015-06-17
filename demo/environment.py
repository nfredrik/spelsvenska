from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def before_all(context):
    context.browser = webdriver.Firefox()
    context.Keys = Keys
    context.By = By
    context.NoSuchElementException = NoSuchElementException
    context.WebDriverWait = WebDriverWait
    context.ActionChains = ActionChains
def after_all(context):
    context.browser.quit()