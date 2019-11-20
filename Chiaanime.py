from selenium import webdriver
import urllib.request
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def reqrd(txt):
    anime_list = ["Black Clover TV", "One Piece", "Shokugeki no Souma Shin no Sara", "Enen no Shouboutai", "Dr Stone"]
    if txt.text in anime_list:
        return txt
    else:
        return False


def download(txt):
    driver.get(txt)
    a_text = []
    a_text = driver.find_elements_by_tag_name("a")
    for i in range(len(a_text)):
        if a_text[i].text == "Download":
            a_text[i].click()


def login(url):
    driver.get(url)
    driver.set_window_size(900,900)
    element =[]
    final_ele = ""
    element = driver.find_elements_by_class_name('series')
    element_len = len(element)
    for i in range(len(element)):
        print(element[i].text)
        final_ele = reqrd(element[i])
        last_ele = element[element_len - 1].text
        if final_ele:
            finished_page = final_ele.text
            final_ele.click()
            next_page = driver.current_url
            driver.get(next_page)
            download(next_page)
            if finished_page == last_ele:
                break
            else:
                driver.back()
                driver.get(driver.current_url)
                element = driver.find_elements_by_class_name('series')
    next_page = driver.current_url
    print(next_page)
    if next_page == url:
        next_element = driver.find_elements_by_tag_name("strong")
        for i in range(len(next_element)):
            print(next_element[i].text)
            if next_element[i].text == "NEXT PAGE":
                next_element[i].click()
                login(driver.current_url)
            elif next_element[i].text == "⏭":
                print(3)
                next_element[i].click()


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="D:\\New folder (2)\\chromedriver.exe")
    login(url = "https://m.chia-anime.me/")
