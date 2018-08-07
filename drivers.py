from selenium import webdriver
import data as d
def chrome():
    return webdriver.Chrome(d.chromedriver)
def firefox():
    return webdriver.Firefox(executable_path=d.geckodriver)
list = [chrome(), firefox()]