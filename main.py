import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from selenium.common.exceptions import NoSuchElementException
import keyboard


def _translate_text(text):
    while True:
        keyboard.wait('Ctrl + Q')

        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")
        browser = webdriver.Chrome("D:\\translate\\chromedriver.exe", options=options)
        text = pyperclip.paste()
        browser.get('https://translate.google.com/?sl=en&tl=ru&op=translate')
        browser.implicitly_wait(5)
        paste_eng_text = browser.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea")
        paste_eng_text.click()
        browser.implicitly_wait(5)
        paste_eng_text.send_keys(text)
        browser.implicitly_wait(5)
        text = browser.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]").text
        pyautogui.alert(text=text, title='Translate', button='OK')
        pyperclip.copy(text)
        browser.close()
        browser.quit()
spam = pyperclip.paste()
_translate_text(spam)
