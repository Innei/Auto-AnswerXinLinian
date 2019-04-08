from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import time
from parse_answer import *

browser = webdriver.Chrome()
browser.get('http://192.168.9.12/npels/')
wait = WebDriverWait(browser, 10)
current = 1  # 题号
ansll = callback()

def login(name, password):
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tbName'))).send_keys(name)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tbPwd'))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnLogin'))).click()


def intotest():
    try:
        browser.switch_to.frame('mainFrame')
        start = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#ctl00_cphContent_divWarning > div > div.homework_3 > ul > li.homework_3_2 > span > a')))
        start.click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                               '#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl03_Action > span > input[type="button"]'))).click()
        time.sleep(1)
    except TimeoutError:
        return  intotest()


def answer_part_one():
    content = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                              '#form1 > div.content_test > div.class_mag.class_main_tab > div.test_frame > div > ul.choiceList')))
    anlist = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                             'ul.choiceList > li > input')))
    flag = 1
    global ansll
    global current
    for item in anlist:
        # for item in anlist:
        if flag == 0:
            flag = 1
        if flag == 1 and 'A' == ansll[current - 1]:
            print(ansll[current - 1])
            item.click()
            flag = -4
            current+=1
        if flag == 2 and 'B' == ansll[current - 1]:
            print(ansll[current - 1])
            item.click()
            flag = -3
            current += 1
        if flag == 3 and 'C' == ansll[current - 1]:
            item.click()
            print(ansll[current - 1])
            flag = -2
            current += 1
        if flag == 4 and 'D' == ansll[current - 1]:
            item.click()
            print(ansll[current - 1])
            flag = -1
            current += 1

        flag += 1
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#btnNextPart'))).click()


def main():
    login('','')
    intotest()
    answer_part_one()


if __name__ == '__main__':
    main()
