from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from progressbar import ProgressBar
import time
import os
import os.path
from os import system
from bs4 import BeautifulSoup
import re

def startChrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_size(1000, 1000)
    return driver

def goToEducativeMainPage(driver):
    driver.get("https://www.educative.io/")

def getPTags(driver):
    contents = driver.find_elements(By.TAG_NAME, "p")
    file_object = open('course.txt', 'a')
    for i in range(0,len(contents)-34):
        file_object.write(contents[i].text + "\n")
    file_object.close()
    
def getH1Tags(driver):
    contents = driver.find_elements(By.TAG_NAME, "h1")
    file_object = open('course.txt', 'a')
    for content in contents:
        file_object.write("Answer Title: " + content.text + "\n")
    file_object.close()
    
def getliTags(driver):
    contents = driver.find_elements(By.TAG_NAME, "li")
    file_object = open('course.txt', 'a')
    for content in contents:
        file_object.write(content.text + "\n")
        
    file_object.close()
    
    
def myProgressBar(n):
    pbar = ProgressBar()
    for _ in pbar(range(n)):
        time.sleep(1)
def main():
    if os.path.exists('course.txt') == True:
        os.remove("course.txt")
    driver=startChrome()
    system('clear')
    print("Please log in using your account and then press enter to continue.")
    print('')
    goToEducativeMainPage(driver)
    input("")
    print('Validating if you are logged in. Please wait...')
    print('')
    driver.get("https://www.educative.io/learn")

    myProgressBar(10)
    print('')
    if driver.current_url not in "https://www.educative.io/learn")":
        system('clear')
        print("We detected you are not logged in yet! Program aborted.")
        driver.quit()
    else:
        system('clear')
        print("Please enter URL of any Answer you want to scrape.")
        print('')
        while True:
            firstURL = input("Enter URL here: ")
            regex1 = re.compile('^https://www.educative.io/answereditor/')
            regex2 = re.compile('^https://www.educative.io/answers/')
            flag1 = bool(re.match(regex1, firstURL))
            flag2 = bool(re.match(regex2, firstURL))
            if flag1 == True:
                if len(firstURL.split("//")[1].split("/")) != 3:
                    print('URL does not seem to be from the lesson of an Educative course. Please enter again.')
                    print('')
                else:
                    break
            elif flag2 == True:
                if len(firstURL.split("//")[1].split("/")) != 3:
                    print('URL does not seem to be from the lesson of an Educative course. Please enter again.')
                    print('')
                else:
                    print("URL is ok ")
                    break
            else:
                print('URL does not seem to be from the lesson of an Educative course. Please enter again.')
                print('')
                
        try:
            system('clear')
            print('Content scrapping started. Please be patient.')
            print('You can open the course.txt file in any editor to monitor its contents side by side.')
            print('')
            driver.get(firstURL)
            myProgressBar(8)
            print('')
            p_tags=driver.find_elements(By.TAG_NAME, "p")
            li_tags=driver.find_elements(By.TAG_NAME, "li")
            temp=li_tags[0].get_attribute("innerHTML")
            temp1=BeautifulSoup(temp)
            unwanted=temp1.find_all('p')
            check=False
            l=len(temp1.text)
            for tag in p_tags:
                if temp1.text[0:l-2] == tag.text[0:len(tag.text)-1]:
                    check=True
                else:
                    continue

            if check == True:
                getH1Tags(driver)
                getPTags(driver)
                driver.quit()
            elif check == False:
                getH1Tags(driver)
                getPTags(driver)
                getliTags(driver)
                driver.quit()
            else:
                print("Error")
        except:
            system('clear')
            print('Sorry! Something went wrong. Please try again later. Program aborted.')
            driver.quit()

main()
                    
