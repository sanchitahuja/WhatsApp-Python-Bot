from utils.whatsapp_message import get_driver, send_message
import time

driver = get_driver()
while True:
    input_names = input("Input names of users you want to text(Space separated)").split(" ")
    message_text = input("Enter the text of the message")
    target = input_names
    for name in target:
        time.sleep(10)
        print("Sending message to ", name)
        send_message(driver, target=name, message_txt=message_text)

driver.close()
