import keyring
from keyrings.alt import Windows
import os
import platform
from selenium import webdriver, common

if platform.system() == 'Windows':
    path = 'chromedriver.exe'
    keyring.set_keyring(Windows.RegistryKeyring())
elif platform.system() == 'Mac':
    if platform.machine() == "arm64":
        path = 'chromedriver_m1'
    else:
        path = 'chromedriver'
else:
    path = ''

if not os.path.exists("mrsb.config"):
    account = input("输入学号：")
    with open("mrsb.config", 'w') as f:
        if keyring.get_password('mrsb', account) == None:
            password = input("输入密码：")
        else:
            password = keyring.get_password('mrsb', account)
        f.write(account)
        keyring.set_password('mrsb', account, password)
else:
    with open("mrsb.config", 'r') as f:
        account = f.read()
        password = keyring.get_password('mrsb', account)

mobileEmulation = {'deviceName': 'iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(executable_path=path, chrome_options=options)
driver.get("https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/shsj/loginChange")
driver.execute_script("location.replace(\"\/zhxy-xgzs/xg_mobile/shsj/common\")")
driver.find_element_by_id('mobileUsername').send_keys(account)
driver.find_element_by_id('mobilePassword').send_keys(password)
driver.find_element_by_id("load").click()
driver.find_element_by_id("mrsb").click()
driver.execute_script("add()")
while True:
    try:
        driver.find_element_by_id("checkbox").click()
        break
    except common.exceptions.NoSuchElementException:
        pass
driver.execute_script("save()")
driver.quit()
