from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  # Added to prevent closing of browser
driver = webdriver.Chrome(options=options)  # Creating object
# driver.maximize_window()

driver.get("https://elgoog.im/t-rex/")

game = driver.find_element(By.XPATH, '//*[@id="main-frame-error"]/div[5]')
time.sleep(5)
game.send_keys(Keys.SPACE)


class Coordinates:
    dinosaur = (200, 200)


def press_space():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')

    time.sleep(0.05)

    # print("jump")
    time.sleep(0.10)

    pyautogui.keyUp('space')
    pyautogui.keyDown('down')


def image_grab():
    box = (Coordinates.dinosaur[0] + 30, Coordinates.dinosaur[1], Coordinates.dinosaur[0] + 120, Coordinates.dinosaur[1] + 2)
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    a = np.array(gray_image.getcolors())
    return a.sum()


pyautogui.keyDown('down')
while True:
    if image_grab() != 435:
        press_space()
        time.sleep(0.1)

driver.quit()

