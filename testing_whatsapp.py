from utils.whatsapp_message import get_driver, send_message
import time

driver = get_driver()
while True:
    target = ["Sanchit"]
    for name in target:
        time.sleep(10)
        print("Sending message to ", name)
        send_message(driver, target=name, message_txt="Trying Something! Ignore!")

driver.close()
