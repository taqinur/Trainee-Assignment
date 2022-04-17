from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

#going to website
driver.get("http://automationpractice.com/index.php")

#finding login button and click
driver.find_element_by_class_name('login').click()

#signing in

def logged_in(email,password):
  driver.find_element_by_id('email').send_keys(email)
  driver.find_element_by_id('passwd').send_keys(password)
  driver.find_element_by_id('SubmitLogin').click()

  #Going to the Casual Dresses section and adding a dress into the cart
  driver.find_element_by_css_selector('#block_top_menu > ul > li:nth-child(2) > a').click()
  driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div[2]/div[2]/ul/li[1]/div[1]/a').click()
  driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/h5/a').click()
  driver.find_element_by_id('add_to_cart').click()
  driver.implicitly_wait(10)
  driver.find_element_by_xpath('/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/span').click()

  #Going to the T-shirt section, Filtering the list with blue color, Adding a shirt from the filter list
  driver.find_element_by_xpath('/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[3]/a').click()
  driver.find_element_by_id('layered_id_attribute_group_14').click()
  driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/h5/a').click()
  driver.find_element_by_id('color_14').click()
  driver.find_element_by_id('add_to_cart').click()
  driver.find_element_by_xpath('/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a').click()

  #checkout
  driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]').click()
  driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/form/p/button').click()
  driver.find_element_by_id('cgv').click()
  driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/p/button').click()
  driver.find_element_by_class_name('cheque').click()
  driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/form/p/button').click()

  #logout
  driver.find_element_by_class_name('logout').click()

#input login info and sign in
logged_in("taqi1662@gmail.com","taqi1")
logged_in("alicia.jones@xyz.com","aj123")

driver.close()
