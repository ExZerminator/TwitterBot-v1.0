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

# defines comment possibilites. comments can be added w/o updating code below because of random int function
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

# this didnt really work only liked abt 5-8 posts before breaking. 
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
    inter = 0  # declares the counter
    while inter < x:
        try: #everything is in a try loop to catch all errors and continue regardless
            time.sleep(numpy.random.randint(low= 2, high= 6)) # random sleep inorder to create a time gap between loops

            # declares tweet as the code necessary to find a tweet
            tweet = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[4]/div/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[2]/div[1]")
            time.sleep(1)
            tweet  
            tweet.click() #clicks on the tweet element
            
            time.sleep(numpy.random.randint(low= 2, high= 6)) # random sleep again just so that everything isnt as predicatable (idk if that was necessary but added complexity to the code to make it a bit more challanging)
            
            like_button = driver.find_element_by_xpath("//div[@data-testid='like']") #sets variable = to code that finds like button element
            like_button #finds like button element
            like_button.click() #clicks element
            
            comment_button = driver.find_element_by_xpath("//div[@data-testid='reply']") 
            comment_button #finds reply button
            comment_button.click() #clicks reply button
            
            
            comment_field = driver.find_element_by_xpath("//div[@data-testid='tweetTextarea_0']") #finds and declares comment_field? im not sure if when you set a variable = to a path if it calls it without having to state that variable on a seperate line lol... seems like it worked here.
            comment_selector = numpy.random.randint(low = 0, high = len(comments) -1) # pretty proud of this one: declares a variable that will randomly select a comment (note i set it so that the highest comment is the len of the list -1 so if i add more comment possibilities i dont have to go back and change it here)
            comment_field.send_keys(comments[comment_selector]) # sends random comment to comment field

            time.sleep(numpy.random.randint(low= 2, high= 6)) # random sleep

            reply_button = driver.find_element_by_xpath("//div[@data-testid='tweetButton']") # finds the actual button named reply
            reply_button # calling the variable just to be sure
            reply_button.click() # clicking the element 


            time.sleep(numpy.random.randint(low= 1, high= 5)) #random sleep

            back_button = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div") # finds back button
            back_button #called it just incase
            back_button.click() # clicks that back button

            time.sleep(numpy.random.randint(low= 1, high= 5)) #random sleep

            driver.get('https://twitter.com/home') #reloads the page

            time.sleep(numpy.random.randint(low= 40, high= 60)) # random long sleep to allow new posts to generate seeing that the function just targets the first post

            driver.get('https://twitter.com/home') # refreshes one more time before starting the loop over again


            inter += 1 # adds one to variable inter which is used to control how long the while loop goes for. 

            print(inter, 'Sucessful Interactions') # inter is also used to spit out a counter to the terminal for the user
        except Exception: # pretty much if any error occurs it'll just refresh the page a few times and wait then continue which will continue the for loop. essentially just refreshes home page and waits if any error occurs
            print('an error occured. I will attempt to reload and try again')
            
            driver.get('https://twitter.com/home')

            time.sleep(60)
            
            driver.get('https://twitter.com/home')

            print(Exception) #this didnt fucking work lmao. i was hoping id be able to see the FULL error AND get it to continue without stopping 

            continue




feed_inter(999999) # calls the function above w the argument being how many "interactions" or loops you'd like the function to do :) 