from selenium import webdriver
from process import SpeedBot
import time

speed_test_url = 'https://www.speedtest.net/id'
form_url = 'https://forms.gle/hMar56nabK5Lu7Cy5'
path = "C:\selenium_web_driver\chromedriver.exe"

bot = SpeedBot(speed_test_url, form_url, path)
# speed test
bot.speed_testing()
time.sleep(3)
# speed test
# filling form
bot.form_filling()
# filling form
