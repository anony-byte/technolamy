from selenium import webdriver
import cv2

browser = webdriver.Safari()
browser.get('http://127.0.0.1:5000/output')
cropped = browser.find_element('xpath', '/html/body/div[1]')
location = cropped.location
size = cropped.size
browser.save_screenshot('test.png')
browser.quit()
read_image = cv2.imread('test.png')
cv2.imwrite("test.png", read_image[100:, 300:len(read_image[0]) - 300])
