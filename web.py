from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import drivers
import data as d
import time
def fnt_login(iteration = 1):
    for driver in drivers.remoteList:
        driver.implicitly_wait(20)
        wait = WebDriverWait(driver, 20)
        try:
            for i in range(0, iteration):
                driver.get(d.url_fntmain)
                wait.until(EC.url_to_be(d.url_base + d.url_login))
                driver.find_element_by_id("username").send_keys(d.username)
                driver.find_element_by_id("password").send_keys(d.password)
                driver.find_element_by_id("ok").send_keys(Keys.ENTER)
                wait.until(EC.url_to_be(d.url_base + d.url_mandant))
                driver.find_element_by_id("ok").click()
                wait.until(EC.url_to_be(d.url_base + d.url_command))
                driver.set_page_load_timeout(10)
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='logout']/span").click()
        except WebDriverException as e:
            print("Execution error {}".format(e))
            return False
        finally:
            #for loginHARD
            #driver.quit()
            #driver.close()
            pass
    return True
