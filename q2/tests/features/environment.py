__author__ = '30070_VS'

from selenium import webdriver

def before_feature(context, feature):
    # Create a new instance of the Firefox driver.
    context.driver = webdriver.Firefox()

def after_feature(context, feature):
    context.driver.quit()