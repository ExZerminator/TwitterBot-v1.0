from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
import time 
import numpy


driver = webdriver.Chrome(executable_path='/home/chris/Desktop/InstagramAuto/chromedriver')
driver.get('https://twitter.com/home')

username = input("Enter in your username: ")
password = getpass("Enter your password: ")

username_textbox = driver.find_element_by_name('session[username_or_email]')
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name('session[password]')
password_textbox.send_keys(password)

login_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
login_button.submit()

time.sleep(4)

# defines comment possibilites (change to a list in the future and use a randomint() function to randomize the comment sent)
comments = ['Damn that looks good', 'fuck, i wish that was me', 'who wants to dick me down', 
'that dick looks tastey asf', 'omg thats hot daddy', 'imagine ;)','thats so fucking sexy',
 'i want you to do dirty things to me', 'dm me you might get something special ;)', 
 'if only... ;)', 'omfg thats hot!!!', 'this makes me want to get my ass ate lmao ', 
 'this makes me want to get my pussy destroyed holy shit', 'if only i had some big black dick to ravage this pussy',
 'you + me alone in a room = lots of fun ;) thats the only equation i know', 'im dripping... ', 
 'i want to cum on someones face tbh', 'if only i had a face to ride smh. wheres daddy', 
 'do you ever just scroll through twitter porn at work while ur panties get soaking wet bc um me lmao', 'im so hot rn', 
 'wish i could take my pants off rn and play w my pussy but im in public :((', 'anyone else get random horny thoughts cuz same',
 'this post is making me think dirty things... oops', 'what did i do to be left horny and alone :( ima go cry and masturbate', 
 'my hearing is at 100x magnification... that means im rubbing on my pussy lmao', 
 'rubbing my pussy gives me super hearing lmao cant be getting caught', 'this is good content... but mines better ;)',
  'do you ever get the horny shakes cuz same', 'man oh man my nipples are getting hard asf... fuck', '😍😍😍😍', '😍😍😍', 
  '😍😍', '😍', '😍😍😍😍', '😍😍😍', '😍😍', '😍', '😍😍😍😍', '😍😍😍', '😍😍', '😍', '😍😍😍😍', '😍😍😍', '😍😍', '😍',
  '😍😍😍😍', '😍😍😍', '😍😍', '😍', '😍😍😍😍', '😍😍😍', '😍😍', '😍','😍😍😍😍', '😍😍😍', '😍😍', '😍','😍😍😍😍', '😍😍😍', '😍😍', '😍'] 

# searches for like buttons and automatically turns into a list 
def find_like_buttons():
    like_buttons = driver.find_elements_by_xpath("//div[@data-testid='like']")

#finds comment buttons
def find_comment_buttons():
    comment_buttons = driver.find_elements_by_xpath("//div[@data-testid='reply']")
 
 # finds the only comment field on the page once comment button is clicked
def find_comment_field():
    comment_field = driver.find_element_by_xpath("//div[@data-testid='tweetTextarea_0']")

 #finds and defines reply button once comment_buttons has been clicked
def find_reply_button():
    reply_button = driver.find_element_by_xpath("//div[@data-testid='tweetButton']")

#scrolls down the page
def scrollbottom():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

def feed_auto_like(x):
    likes = 0
    scrollbottom()
    time.sleep(5)
    scrollbottom()
    time.sleep(5)
    scrollbottom()
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(10)
    like_buttons = list(driver.find_elements_by_xpath("//div[@data-testid='like']"))
    while likes < x:
        driver.execute_script("arguments[0].scrollIntoView();", like_buttons[likes])
        driver.execute_script("arguments[0].click();", like_buttons[likes])
        likes += 1
        like_buttons.append(driver.find_elements_by_xpath("//div[@data-testid='like']"))
        print(likes, 'Sucessful Likes')
        time.sleep(5) 
    


# will comment and like posts through feed
def feed_inter(x):
    inter = 0 
    while inter < x:
        try:
            time.sleep(numpy.random.randint(low= 2, high= 6))

            tweet = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[4]/div/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[2]/div[1]")
            time.sleep(1)
            tweet
            tweet.click()
            
            time.sleep(numpy.random.randint(low= 2, high= 6))
            
            like_button = driver.find_element_by_xpath("//div[@data-testid='like']")
            like_button
            like_button.click()
            
            comment_button = driver.find_element_by_xpath("//div[@data-testid='reply']")
            comment_button
            comment_button.click()
            
            
            comment_field = driver.find_element_by_xpath("//div[@data-testid='tweetTextarea_0']")
            comment_selector = numpy.random.randint(low = 0, high = len(comments) -1)
            comment_field.send_keys(comments[comment_selector])

            time.sleep(numpy.random.randint(low= 2, high= 6))

            reply_button = driver.find_element_by_xpath("//div[@data-testid='tweetButton']")
            reply_button
            reply_button.click()





            time.sleep(numpy.random.randint(low= 1, high= 5))

            back_button = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div")
            back_button
            back_button.click()

            time.sleep(numpy.random.randint(low= 1, high= 5))

            driver.get('https://twitter.com/home')

            time.sleep(numpy.random.randint(low= 40, high= 60))

            driver.get('https://twitter.com/home')


            inter += 1

            print(inter, 'Sucessful Interactions')
        except Exception: 
            print('an error occured. I will attempt to reload and try again')
            
            driver.get('https://twitter.com/home')

            time.sleep(60)
            
            driver.get('https://twitter.com/home')

            print(Exception)

            continue




feed_inter(999999)