# Lesson 4 Homework [OS: Windows]

# Question 1
# a.
from selenium import webdriver
driver = webdriver.Chrome(r'E:\Selenium\chromedriver.exe')
driver.get('http://www.walla.co.il')
# b.
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'E:\Selenium\geckodriver.exe')
driver.get('http://www.ynet.co.il')

# Question 2 (a + b + c)
from selenium import webdriver
driver = webdriver.Chrome(r'E:\Selenium\chromedriver.exe')
driver.get('http://www.walla.co.il')
title = driver.title
driver.refresh()
title2 = driver.title
print(f'First Title was:\n{title}\nAfter refresh the title is\n{title2}')

# Question 3
from selenium import webdriver
driver_chrome = webdriver.Chrome(r'E:\Selenium\chromedriver.exe')
driver_firefox = webdriver.Firefox(executable_path=r'E:\Selenium\geckodriver.exe')
driver_opera = webdriver.Opera(executable_path=r'E:\Selenium\operadriver.exe')
driver_opera.get("https://google.com")
driver_chrome.get("https://google.com")
driver_firefox.get("https://google.com")
search_key = driver_chrome.find_element_by_name('q')
search_key.send_keys('Same place')
search_key2 = driver_opera.find_element_by_name('q')
search_key2.send_keys('Same place')
search_key3 = driver_firefox.find_element_by_name('q')
search_key3.send_keys('Same place')
# Answer: YES, any element has the same locators in other browsers

# Question 4
from selenium import webdriver
driver_chrome = webdriver.Chrome(r'E:\Selenium\chromedriver.exe')
driver_chrome.get('https://translate.google.com')
text = driver_chrome.find_element_by_id("source").send_keys("כותב בעברית")

# Question 5
from selenium import webdriver
driver = webdriver.Chrome(r"E:\Selenium\chromedriver.exe")
driver.get("https://youtube.com")
search = driver.find_element_by_name("search_query")
search.send_keys("Popstar")
driver.find_element_by_id("search-icon-legacy").click()

# Question 6
from selenium import webdriver
driver = webdriver.Chrome(r"E:\Selenium\chromedriver.exe")

driver.get('https://translate.google.com')
text_field = driver.find_element_by_id("source")
text_field2 = driver.find_element_by_xpath('//*[@id="source"]')
text_field3 = driver.find_element_by_class_name("orig")
print(f"{text_field}\n{text_field2}\n{text_field3}")

# Question 7
from selenium import webdriver
driver = webdriver.Chrome(r"E:\Selenium\chromedriver.exe")

driver.get('https://www.facebook.com/')
driver.find_element_by_id("email").send_keys("MyEmail@mail.com")
driver.find_element_by_id("pass").send_keys("Password")
driver.find_element_by_name("login").click()


# All challenges (8, 9 ,10) in other py files
