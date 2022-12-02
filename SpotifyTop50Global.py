from selenium import webdriver
# from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui

PATH = ".\chromedriver.exe"
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
driver = webdriver.Chrome(PATH,chrome_options=chromeOptions)
driver.get('https://open.spotify.com/')
xpath = '//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a'
searchBar = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, xpath)))
searchBar = driver.find_element(By.XPATH,xpath).click()
searchFieldXpath = '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input'
searchFieldWait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, searchFieldXpath)))
searchField = driver.find_element(By.XPATH,searchFieldXpath).send_keys("Top 50 Global Spotify")
#pyautogui.press("enter")
playlistXpath = '//*[@id="searchPage"]/div/div/section[1]/div[2]/div/div'
playlistWait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, playlistXpath)))
playlistResult = driver.find_element(By.XPATH,playlistXpath).click()
top50 = []
for item in range(1,14):
    gxpath = f'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[{item}]/div/div[2]/div/div'
    xpath = '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/a/div'
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, gxpath)))
        try:
            element = driver.find_element(By.XPATH,gxpath).get_attribute("innerHTML")
            top50.append(element)
            # print(item)
        except:
            print("Can't get text!")
    except:
        print("Couldnt Find!")
        driver.close()
        driver.quit()
pyautogui.press("end")
for item in range(1,38):
    gxpath = f'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[{item}]/div/div[2]/div/div'
    xpath = '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/a/div'
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, gxpath)))
        try:
            element = driver.find_element(By.XPATH,gxpath).get_attribute("innerHTML")
            top50.append(element)
            # print(item)
        except:
            print("Can't get text!")
    except:
        print("Couldnt Find!")
        driver.close()
        driver.quit()
driver.quit()
# print(top50)
f = open("./top50.txt", "w")
f.write("")
f.close()
f = open("./top50.txt", "a+")
for songName in top50:
    f.write(songName+"\n")
f.close()