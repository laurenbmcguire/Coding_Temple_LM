from selenium import webdriver


#credentials
username = "username"
password = "password"

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")

# head to login page
driver.get("https://modest-jennings-77f32e.netlify.app/login")
# find username/email field and send the username itself to the input field
driver.find_element_by_id("login_field").send_keys(username)
# find password input field and insert password as well
driver.find_element_by_id("password").send_keys(password)
# click login button
driver.find_element_by_name("commit").click()