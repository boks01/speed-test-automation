from selenium import webdriver
import time
from bs4 import BeautifulSoup
class SpeedBot:
    def __init__(self, speed_test_url, form_url, path):
        self.path = path
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.speed_test_url = speed_test_url
        self.form_url = form_url    
    
    def speed_testing(self):
        self.driver.get(self.speed_test_url)
        time.sleep(1)
        start_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_button.click()
        time.sleep(60)
        download_text = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        upload_text = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        self.download = f'{download_text} Mbps'
        self.upload = f'{upload_text} Mbps'
        self.driver.quit()
        print(self.download)
        print(self.upload)
    
    def form_filling(self):
        self.driver_2 = webdriver.Chrome(executable_path=self.path)
        self.driver_2.get(self.form_url) 
        time.sleep(1)
        upload_question = self.driver_2.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        upload_question.click()
        upload_question.send_keys(self.upload)
        time.sleep(1)

        download_question = self.driver_2.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        download_question.click()
        download_question.send_keys(self.download)
        time.sleep(3)

        submit_button = self.driver_2.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        submit_button.click()
        self.driver_2.quit()
        print('done')