# Challenge Number 8:
#    Open any web page
#    Delete all cookies
#    Make sure that all cookies deleted by printing them and see none
from selenium import webdriver
driver = webdriver.Chrome(r"E:\Selenium\chromedriver.exe")
driver.get('https://devopsexperts.co.il/')
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(cookies)

# Challenge Number 9:
#    Open GitHub homepage
#    Write in search field "Selenium"
#    Then Press ENTER
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"E:\Selenium\chromedriver.exe")
driver.get('https://github.com/')
element = driver.find_element_by_name("q")
element.send_keys("Selenium")
element.send_keys(Keys.ENTER)

# Challenge Number 10: (The hardest one)
# Disable all extensions in chrome + run browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(r"E:\Selenium\chromedriver.exe", chrome_options=chrome_options)
driver.get("https://www.ynet.co.il/")

# Disable all extensions in Firefox + run browser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
firefox_options = Options()
firefox_options.add_argument("--disable-extensions")
driver_firefox = webdriver.Firefox(executable_path=r'E:\Selenium\geckodriver.exe', firefox_options=firefox_options)
driver_firefox.get("https://www.ynet.co.il/")

# Disable all extensions in opera + run browser
from selenium import webdriver
from selenium.webdriver.opera.options import Options
opera_options = Options()
opera_options.add_argument("--disable-extensions")
driver_opera = webdriver.Opera(executable_path=r'E:\Selenium\operadriver.exe', options=opera_options)
driver_opera.get("https://www.ynet.co.il/")
