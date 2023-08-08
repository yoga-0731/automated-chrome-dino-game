from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from PIL import ImageGrab


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  # Added to prevent closing of browser
driver = webdriver.Chrome(options=options)  # Creating object
driver.maximize_window()

driver.get("https://elgoog.im/t-rex/")

game = driver.find_element(By.XPATH, '//*[@id="main-frame-error"]/div[5]')
time.sleep(5)
game.send_keys(Keys.SPACE)


def detect_collision():
    # Bird
    for i in range(800, 560):
        for j in range(80, 127):
            if data[i, j] < 171:
                game.send_keys(Keys.ARROW_DOWN)
                return

    # Cactus
    for i in range(530, 620):
        for j in range(130, 160):
            if data[i, j] < 100:
                game.send_keys(Keys.ARROW_UP)
                return
    return


while True:
    image = ImageGrab.grab().convert('L')
    print(image)
    data = image.load()
    detect_collision()


driver.quit()
