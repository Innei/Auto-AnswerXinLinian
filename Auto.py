from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from selenium.webdriver.support.ui import Select
import time
from parse_answer import *
from answer import *

browser = webdriver.Chrome()
browser.get('http://192.168.9.12/npels/')
wait = WebDriverWait(browser, 10)
current = 1  # 题号
ansll = []


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
        return intotest()


def answer_part_one():
    global ansll
    global current
    time.sleep(3)
    pageSource = browser.page_source
    with open('source.html', 'w+', encoding='utf-8') as f:
        f.write(pageSource)
    prase_result()
    ansll = callback()
    browser.switch_to.default_content()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#aPart1'))).click()
    browser.switch_to.frame('mainFrame')
    content = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                              '#form1 > div.content_test > div.class_mag.class_main_tab > div.test_frame > div > ul.choiceList')))
    anlist = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                             'ul.choiceList > li > input')))

    flag = 1

    for item in anlist:
        # for item in anlist:
        if flag == 0:
            flag = 1
        if flag == 1 and 'A' == ansll[current - 1]:
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            item.click()
            flag = -4
            current += 1
        if flag == 2 and 'B' == ansll[current - 1]:
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            item.click()
            flag = -3
            current += 1
        if flag == 3 and 'C' == ansll[current - 1]:
            item.click()
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            flag = -2
            current += 1
        if flag == 4 and 'D' == ansll[current - 1]:
            item.click()
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            flag = -1
            current += 1

        flag += 1
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnNextPart'))).click()


def answer_part_two():
    global current, ansll
    read_part = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                           '#form1 > div.content_test > div.class_mag.class_main_tab > div.test_frame > div:nth-child(4) > ul.test_list_5_2 > li > ul.choiceList')))
    anlist = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                             'ul.choiceList > li > input')))
    flag = 1
    for item in anlist:
        if flag == 0:
            flag = 1
        if flag == 1 and 'A' == ansll[current - 1]:
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            item.click()
            flag = -4
            current += 1
        if flag == 2 and 'B' == ansll[current - 1]:
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            item.click()
            flag = -3
            current += 1
        if flag == 3 and 'C' == ansll[current - 1]:
            item.click()
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            flag = -2
            current += 1
        if flag == 4 and 'D' == ansll[current - 1]:
            item.click()
            print('当前第' + str(current - 1) + '题,选择了' + ansll[current - 1])
            flag = -1
            current += 1

        flag += 1
    section_b = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                                '#form1 > div.content_test > div.class_mag.class_main_tab > div.test_frame > div:nth-child(7) > ul.test_list_2 > li > input')))

    for item in section_b:
        item.clear()
        item.send_keys(ansll[current - 1])
        current += 1

    section_c = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                                '#form1 > div.content_test > div.class_mag.class_main_tab > div.test_frame > div:nth-child(10) > ul > li > span > select')))
    for select in section_c:
        if ansll[current - 1] == 'A':
            Select(select).select_by_index(0)
            current += 1
        elif ansll[current - 1] == 'B':
            Select(select).select_by_index(1)
            current += 1
        elif ansll[current - 1] == 'C':
            Select(select).select_by_index(2)
            current += 1
        elif ansll[current - 1] == 'D':
            Select(select).select_by_index(3)
            current += 1
        elif ansll[current - 1] == 'E':
            Select(select).select_by_index(4)
            current += 1
        elif ansll[current - 1] == 'F':
            Select(select).select_by_index(5)
            current += 1
        elif ansll[current - 1] == 'G':
            Select(select).select_by_index(6)
            current += 1
        elif ansll[current - 1] == 'H':
            Select(select).select_by_index(7)
            current += 1
        elif ansll[current - 1] == 'I':
            Select(select).select_by_index(8)
            current += 1
        elif ansll[current - 1] == 'J':
            Select(select).select_by_index(9)
            current += 1
        elif ansll[current - 1] == 'K':
            Select(select).select_by_index(10)
            current += 1
        elif ansll[current - 1] == 'L':
            Select(select).select_by_index(11)
            current += 1
        elif ansll[current - 1] == 'M':
            Select(select).select_by_index(12)
            current += 1
        elif ansll[current - 1] == 'N':
            Select(select).select_by_index(13)
            current += 1


def main(user, passwd):
    login(user, passwd)
    intotest()
    answer_part_one()
    answer_part_two()


if __name__ == '__main__':
    user = input('username: ')
    passwd = input('password: ')
    main(user, passwd)
