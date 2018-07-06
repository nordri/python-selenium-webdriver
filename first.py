from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Remote(
   command_executor='http://192.168.1.54:4444/wd/hub',
   desired_capabilities={'browserName': 'firefox'})
driver.get("http://www.python.org")

# Si no tiene Python en el titulo sale
assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# Si no encuentro resultados sale con error
assert "No results found." not in driver.page_source

# Esperar 2 segundos para ver algo
sleep(2)

# Cerrar el browser
driver.close()

