from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_driver():
    # you can use chromeDriver in its place
    driver = webdriver.Firefox("D:\PycharmProjects\Algorithm\lib")
    driver.get("https://web.whatsapp.com/")
    return driver


def send_message(driver, target, message_txt):
    try:
        wait = WebDriverWait(driver, 600)
        target = '"{}"'.format(target)
        x_arg = "//span[contains(@title," + target + ")]"
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        print(group_title)
        print("Wait for few seconds")
        group_title.click()
        message = driver.find_elements_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        )[0]
        message.send_keys(message_txt)
        sendbutton = driver.find_elements_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[3]/button'
        )[0]
        sendbutton.click()
        print("Sent")
    except Exception as e:
        print(f"Unable to Send Message to {target} Error:{e}")
