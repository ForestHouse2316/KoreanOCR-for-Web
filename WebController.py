from selenium import webdriver
import os
import time
import threading


# Init browser
driver = webdriver.Chrome('./Korean OCR/WebDriver.exe')
driver.maximize_window()

while True:
    command = input()
    if command = 'exit':
        break
    elif command = '':
        print(" page source . . .")
        print("Analyzing page source . . .")





