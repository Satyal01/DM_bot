from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random






class Bot:
    def __init__(self, email, password):
        self.wait = [1,2,3,4,5,6,7]
        self.email = email
        self.password = password
        self.file = open("./name.text","a")


        #  set options for not prompting devtools infromation
        options = Options()
        options.add_experimental_option("detach",True)  #this will  keep browser open after the automation is completed
        options.add_experimental_option("excludeSwitches", ["enable-logging"])


        print("program started")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.linkedin.com/login")

        self.driver.implicitly_wait(1)

        title = self.driver.title
        assert "LinkedIn Login, Sign in | LinkedIn" in title , "this not likedin login page"


        

        print("test 0 : `title` test passed")

        sleep(random.choice(self.wait))
        self.driver.find_element(By.ID, "username").send_keys(self.email)
        sleep(random.choice(self.wait))
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        sleep(random.choice(self.wait))
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'][aria-label='Sign in']").click()
        sleep(random.choice(self.wait))

    
    def coldDm(self):

        print("cold dms")
        sleep(random.choice(self.wait))

        self.driver.get("https://www.linkedin.com/search/results/people/?currentCompany=%5B%221756%22%2C%22157240%22%2C%223067%22%2C%222525300%22%2C%224661%22%5D&network=%5B%22F%22%5D&origin=FACETED_SEARCH&sid=03(")
        
        msg_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view')
        print("buttons captured")
        print(msg_buttons)

        for btn in msg_buttons:
            try:
                sleep(random.choice(self.wait))
                print("BUTTON \n", btn)
                btn.click()
                sleep(random.choice(self.wait))
                person_name = self.driver.find_element(By.CLASS_NAME,"truncate").text
                self.file.write(person_name+"\n")
                

            except Exception as e:
                print("error occured in massgae click", e)
                break

 



    def killSession(self):
        self.driver.quit()
        self.file.close()


