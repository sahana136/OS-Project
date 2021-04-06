from selenium import webdriver
from pynput.keyboard import Key, Controller

keyboard = Controller()

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/bin/chromedriver')

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.google.com")
        #search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(query)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)