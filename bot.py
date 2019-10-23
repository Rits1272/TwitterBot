from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 
import pyautogui as pg


class TwitterBot:
    def __init__(self, username, password):
        self.username = username 
        self.password = password 
        self.bot = webdriver.Firefox(executable_path='./geckodriver')

    def login(self):
        bot = self.bot 
        bot.get('https://twitter.com/')
        time.sleep(2)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(0.5)
        pg.press('enter')
        time.sleep(5)

    def like_tweets(self, hashtag):
        bot = self.bot 
        link = 'https://twitter.com/search?q=' + hashtag  + '&src=typd'
        bot.get(link)
        time.sleep(5)
        all_links = []

        # Here you set how many tweets you want to like by tweaking the value inside for loop(here 10)
        for _ in range(110):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_xpath('//a[@dir="auto"]')

            links = [elem.get_attribute('href') for elem in tweets]
            all_links.append(links[1])

        for link in all_links:
            bot.get(link)
            time.sleep(5)
            like = bot.find_elements_by_xpath('//div[@data-testid="like"]')
            try:
                like[0].click()
            except:
                print('Unable to like tweet :(')
            time.sleep(1)

rits = TwitterBot('<YOUR_USERNAME_HERE>', '<YOUR_PASSWORD_HERE>')
rits.login()
# Here Give Your Hashtag(replace ArtificialIntellingence with your hashtag)
rits.like_tweets('ArtificialIntelligence')
