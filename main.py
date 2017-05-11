import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def hasXpath(xpath):
    try:
        self.browser.find_element_by_xpath(xpath)
        return True
    except:
        return False

driver = webdriver.Chrome()

driver.get("http://youtube.com")

usernames = ["amyelizabeth12222@gmail.com"]
passwords = ["athletic"]
mainComments = [ \
'1', \
'2', \
'3' ]

#,"seantvfukns@gmail.com", "carolthecaroler@gmail.com"
#,"athletic1234", "athletic"

signIn = driver.find_element_by_xpath('//*[@id="yt-masthead-signin"]/div/button/span')
if signIn is None:
    print("noning")
    signIn = driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer[2]')
signIn.click()

for i in xrange(0,len(usernames)):
    username = usernames[i]
    password = passwords[i]

    usernameInput = driver.find_element_by_xpath('//*[@id="identifierId"]')
    usernameInput.send_keys(username)

    usernameNextButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/content')
    usernameNextButton.click()

    time.sleep(1)

    passwordInput = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    passwordInput.send_keys(password)

    passwordNextButton = driver.find_element_by_xpath('//*[@id="passwordNext"]/content')
    passwordNextButton.click()

    time.sleep(1)

    if (i != (len(usernames) - 1)):
        profilePhoto = driver.find_element_by_xpath('//*[@id="yt-masthead-account-picker"]/button')
        profilePhoto.click()

        time.sleep(1)

        addAccount = driver.find_elements_by_class_name('yt-masthead-picker-button')[2]
        addAccount.click()

time.sleep(1)

if len(usernames) > 1:
    profilePhoto = driver.find_element_by_xpath('//*[@id="yt-masthead-account-picker"]/button')
    profilePhoto.click()

    mainAccount = driver.find_element_by_xpath('//*[@id="yt-masthead-multilogin"]/a[1]')
    mainAccount.click()

# subscriptionsButton = driver.find_element_by_xpath('//*[@id="appbar-nav"]/ul/li[3]/a[1]')
# subscriptionsButton.click()
#
# time.sleep(3)
#
# subVids = driver.find_elements_by_xpath('//*[@id="browse-items-primary"]/ol/li[1]/ol/li/div/div[1]/div[2]/ul/*/div/div[1]/div[2]/h3/a')
# for video in subVids:
#     print video.text
#     video.click()
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)

driver.get("https://www.youtube.com/watch?v=CDXOp12kwh4&t=0s")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 400);")
time.sleep(2)
comment = driver.find_element_by_xpath('//*[@id="comment-section-renderer"]/div[1]/div[1]/div/div[1]').click()
driver.implicitly_wait(5)
commentText = driver.find_element_by_xpath('//*[@id="comment-simplebox"]/div[1]')
commentText.click()
commentText.send_keys("comment")



# # this checks whether new youtube is being used
# if hasXpath('//*[@id="button"]/yt-icon')
#     driver.find_element_by_xpath('//*[@id="button"]/yt-icon').click()
#     driver.find_element_by_xpath('//*[@id="settings"]/ytd-account-settings/paper-item[8]').click()
#     driver.find_element_by_xpath('//*[@id="radio"]').click()
#     driver.find_element_by_xpath('//*[@id="submit"]').click()






# driver.get("https://www.youtube.com/feed/trending")
#
# # #xpath list one
# # //*[@id="browse-items-primary"]/ol/li[1]/ol/li/div/div[1]/div[2]/ul/li[1]/div/div/div/div[2]/h3/a
# # //*[@id="browse-items-primary"]/ol/li[1]/ol/li/div/div[1]/div[2]/ul/li[2]/div/div/div/div[2]/h3/a
#
# first = driver.find_elements_by_xpath('//*[@id="browse-items-primary"]/ol/li[1]/ol/li/div/div[1]/div[2]/ul/*/div/div/div/div[2]/h3/a')
# for name in first:
#      print name.text



# driver.get("https://www.youtube.com/watch?v=ijxqCobcyXE")
#
# time.sleep(3)
#
# # scroll to bottom of page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
# time.sleep(3)
#
#
# for name in driver.find_elements_by_xpath('//*[@id="comment-section-renderer-items"]/*/div[1]/div[2]/div[1]/a'):
#     print name.text
