import keyring
from keyrings.alt import Windows
import os
import platform
from selenium import webdriver

if platform.system() == 'Windows':
    path = 'chromedriver.exe'
    keyring.set_keyring(Windows.RegistryKeyring())
elif platform.system() == 'Mac':
    path = 'chromedriver'
else:
    path = ''

if not os.path.exists("mrsb.config"):
    with open("mrsb.config", 'w') as f:
        account = input("输入学号：")
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
driver.find_element_by_id("txfscheckbox").click()
driver.execute_script("save()")
