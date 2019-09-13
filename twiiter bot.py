from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self,hashtag):
        count = 0
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_css_selector('a')
            links = [tweet.get_attribute('href') for tweet in tweets]
            perma = []
            for link in links:
                if 'status' in link and 'photo' not in link:
                    perma.append(link)
            #print(perma)
            for link in perma:
                count+=1
                print(count)
                if count < 45:
                    bot.get(link)
                    time.sleep(6)
                    t = bot.find_elements_by_xpath("//div[@data-testid='like']")
                    for hi in t:
                        hi.click()
                        time.sleep(7)
                else:
                    bot.close()
               
                
        

ed = TwitterBot('rocketBaba1998@yahoo.com','msdhoni1998')
ed.login()
ed.like_tweet('virat')
