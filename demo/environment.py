from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

def before_all(context):
    context.browser = webdriver.Firefox()
    context.Keys = Keys

def after_all(context):
    context.browser.quit()