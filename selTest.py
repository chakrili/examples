import os
import configparser
from scripts import AppLogging
import time
from selenium import webdriver

print(os.path)
objLogging = AppLogging
objLogging.AppLogging()
objLogging.info_function("Reading config parameters")

try:
    config = configparser.ConfigParser()
    config.read('param.ini')
    # url_link = config.get('URL')
    url_link = config['DEFAULT']['URL']
    login_id = config['DEFAULT']['LOGINID']
    login_pwd = config['DEFAULT']['PASSWORD']
    search_key = config['DEFAULT']['SEARCHKWD']
except EnvironmentError:
    print("Kindly check file location")
    objLogging.error_function("Kindly check file location")
except ValueError:
    print(ValueError)
finally:
    objLogging.warn_function("Parameters read is done successfully!!")


#print(url_link)
#for key in config['DEFAULT']:
    #print(key)



driver = webdriver.Chrome(executable_path="C:/Users/chakravarthil/Downloads/chromedriver_win32/chromedriver.exe")
driver.get(url_link)

objLogging.info_function(url_link + "clicked")
objLogging.info_function("logging in with username " + login_id)
username = driver.find_element_by_id("login_field")
username.clear()
username.send_keys(login_id)

objLogging.info_function("logging in with password ******")
password = driver.find_element_by_name("password")
password.clear()
password.send_keys(login_pwd)

time.sleep(3)
submit_btn = driver.find_element_by_name("commit")
submit_btn.click()
time.sleep(3)
search_filed = driver.find_element_by_name("q")
search_filed.send_keys(search_key)
search_filed.send_keys(u'\ue007')

# point1_field = driver.find_element_by_link_text("LambdaSchool/Intro-Python-I")

# point1_field.click()

# search_sub_btn = driver.find_element_by_class_name("btn ml-2 d-none d-md-block")

# search_sub_btn.click()
current_window = driver.current_window_handle
link = driver.find_element_by_link_text("LambdaSchool/Intro-Python-I")
href = link.get_attribute('href')
if href:
    driver.execute_script('window.open(arguments[0]);', href)
else:
    link.click()
new_window = [window for window in driver.window_handles if window != current_window][0]
driver.switch_to.window(new_window)
# Execute required operations
#dwnload_btn = driver.find_element_by_class_name("btn btn-outline get-repo-btn  ")
#driver.find_element_by_xpath("(//a[contains(text(),'Download ZIP')])").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@class='btn btn-sm ml-2 btn-primary']").click()
driver.find_element_by_link_text("Download ZIP").click()
#driver.close()
#driver.switch_to.window(current_window)
