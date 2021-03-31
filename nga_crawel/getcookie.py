from selenium import webdriver
import time
import json
driver = webdriver.Chrome()
driver.get("https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=101298318&redirect_uri=https://bbs.nga.cn/thirdpartylogin.php?from_host=bbs.nga.cn&oauth_from=1&state=038d6073b62cf55f8e921cdb6d76810f&scope=%3C?=$val?%3E")
time.sleep(30)
with open('cookies.txt', 'w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.close()
