from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import data as d
import os
def chrome():
    return webdriver.Chrome(d.chromedriver)
def firefox():
    return webdriver.Firefox(executable_path=d.geckodriver)
def remoreChrome():
    return webdriver.Remote(command_executor=d.hub, desired_capabilities=DesiredCapabilities.CHROME)
def remoreFireFox():
    return webdriver.Remote(command_executor=d.hub, desired_capabilities=DesiredCapabilities.FIREFOX)
remoteList = [remoreFireFox(),remoreChrome()]
#localList = [chrome(), firefox()]