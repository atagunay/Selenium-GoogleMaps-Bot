from __future__ import absolute_import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Assigned chrome driver to the wd
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# -----------------------------------------------------------
# Find input box
# Enter a value
# Click submit button
# -----------------------------------------------------------
def search_place():
    arrival_destination_input = wd.find_element(By.XPATH, value="""//*[@id="searchboxinput"]""")  # Find search input
    arrival_destination_input.send_keys(arrive_destination)   # Enter arrive destination

    sleep(2)  # Wait 2 sec

    # Find search button
    search_button = wd.find_element(By.XPATH,
        value="/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    search_button.click()  # Click search button


# -----------------------------------------------------------
# Find direction button for routing
# Click button
# -----------------------------------------------------------
def directions():
    sleep(10)  # Wait 10 sec

    # Find button of directions
    directions_button = wd.find_element(By.XPATH,
        value="/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button/span/img")
    directions_button.click()  # Click Button


# -----------------------------------------------------------
# Find start destination
# Enter value
# Find submit button
# Click the button
# -----------------------------------------------------------
def find():
    sleep(6)  # Wait 6 sec

    # Find input box for starting point
    start_destination_input = wd.find_element(By.XPATH,
        value="/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
    start_destination_input.send_keys("maltepe")  # Enter your starting point

    sleep(6)  # Wait for 6 sec

    # Find search button for calculate the route
    search_button = wd.find_element(By.XPATH,
        value="/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search_button.click()  # Click the button


# -----------------------------------------------------------
# Find travel information and print
# -----------------------------------------------------------
def get_information():
    sleep(3)  # Wait 3 sec

    # Find total km text
    total_kilometers = wd.find_element(By.XPATH,
        value="/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[1]/div[1]/div[2]/div")
    print("Total Kilometers:", total_kilometers.text)  # Print total km

    sleep(5)  # Wait 5 sec

    # Find arrival time with car based on the current traffic
    car_time = wd.find_element(By.XPATH,
        value="//html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[1]/div[1]/div[1]/span[1]")
    print("Car (Based On Current Traffic):", car_time.text)  # Print arrival time

    # Find train button for transportation information
    transport_button = wd.find_element(By.XPATH,
        value="/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[3]/button/img")
    transport_button.click()  # Click the button

    sleep(3)  # Wait 3 sec

    try:
        # Find transportation route time
        transport_time = wd.find_element(By.XPATH,
            value="/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[2]/div[3]/div/span[1]")
        print("Shortest Transport Path:", transport_time.text)  # Print the travel time

        transport_time = wd.find_element(By.XPATH,
            value="/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[2]/div[1]/div")
        print("Transport Time:", transport_time.text)
    except ValueError:
        print("No transportation :(")


# -----------------------------------------------------------
# PROGRAM STARTING POINT
# -----------------------------------------------------------
print("WELCOME")
start_destination = input("Please Enter Your Start Destination => ")
arrive_destination = input("Please Enter Your Arrive Destination => ")

# Call Functions
wd.get("https://www.google.com/maps/@40.9491153,29.1087699,14z")  # Go to the URL (Google Maps)
sleep(2)  # Wait 2 sec

search_place()
directions()
find()
get_information()
wd.quit()
