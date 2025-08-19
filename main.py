from time import sleep 
from bot import Bot



# driver.find_element(By.XPATH , "//*[@id='global-nav']/div/nav/ul/li[2]/a").click()

# search_box = driver.find_element(By.XPATH, "//*[@id=\'global-nav-typeahead']/input")
# search_box.send_keys("software engineer")
# search_box.send_keys(Keys.RETURN)



obj = Bot("yourUserName","yourPassword")

obj.coldDm()


sleep(1000)

obj.killSession()


# artdeco-button artdeco-button--2 artdeco-button--secondary ember-view
# artdeco-button artdeco-button--2 artdeco-button--secondary ember-view
