import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/darwoft/PycharmProjects/SeleniumUdemy/resources/chromedriver")
driver = webdriver.Chrome(service=service_obj)
# added a global implicit wait
driver.implicitly_wait(5)
driver.get("https://github.com/%5D(https://github.com/)")
driver.find_element(By.CSS_SELECTOR, "button[placeholder='Search or jump to...']").click()
driver.find_element(By.ID, "query-builder-test").send_keys("react")
driver.find_element(By.CLASS_NAME, "ActionListItem-label.text-normal").click()

# This explicit is because the driver sometimes fail trying to find the web element
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.ID, ":r2u:")))
driver.find_element(By.ID, ":r2u:").click()

dropdown_language = Select(driver.find_element(By.ID, "search_language"))
dropdown_language.select_by_visible_text("JavaScript")
dropdown_state = Select(driver.find_element(By.ID, "search_state"))
dropdown_state.select_by_visible_text("closed")
driver.find_element(By.ID, "search_stars").send_keys(">45")
driver.find_element(By.ID, "search_followers").send_keys(">50")
dropdown_licence = Select(driver.find_element(By.ID, "search_license"))
dropdown_licence.select_by_visible_text("Boost Software License 1.0")
driver.find_element(By.XPATH, "//div[@class='d-flex d-md-block']/button").click()

# This sleep is added due to the page load the same locator but with 0 results text
time.sleep(2)

results = driver.find_element(By.CLASS_NAME, "Box-sc-g0xbh4-0.cgQapc")
print("Results Count:", results.text)
assert results == "1 results";

repoName = driver.find_element(By.XPATH, "//span[text() ='mvoloskov/decider']")
assert "mvoloskov/decider" in repoName.text

repoName.click()

readme_content = driver.find_element_by_id("readme").text
print(readme_content[:300])

# Close the browser
driver.quit()
