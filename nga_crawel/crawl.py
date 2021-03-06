from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
import json
# import page
import re

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def operate():
    try:
        page = driver.get("https://bbs.nga.cn/")
        set_cookie()
        # input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        ad = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#jump2 > a")))
        ad.click()
        # driver.close()
        main_page = page
        print(main_page)
        return 1

    except TimeoutException:
        return operate()


def set_cookie():
    with open('cookies.txt', 'r') as f:
        # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
        cookies_list = json.load(f)
        for cookie in cookies_list:
            driver.add_cookie(cookie)
        driver.refresh()


def next_page(page_num):
    try:
        input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input")))
        btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")))
        input.clear()
        input.send_keys(page_num)
        btn.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > ul > li.item.active > span"), str(page_num)))
    except TimeoutException:
        return next_page(page_num)


def main():
    # total = operate()
    operate()
    # total = int(re.compile('(\d+)').search(total).group(1))
    # print(total)
    # for i in range(1, total):
    #     next_page(i)


main()
