# Vexatious

![fishes](https://user-images.githubusercontent.com/84932430/131382979-c86a0a35-6585-4a07-ab0e-41c9863982f4.jpg)

Program that generates Fake WebTraffic to hide yours, (Written in Python). Improved version of Traffic-Confuser. 

![Screenshot from 2021-08-30 20-57-50](https://user-images.githubusercontent.com/84932430/131383448-87603607-e526-4e93-8a63-9287de7b4ad6.png)

This is a V2 of Traffic-Confuser. The program uses Selenium module to open websites in your chosen browser. 

# Dependencies to install:

**Note** *you don't have to install them manually since the code does that for you*. 

![Screenshot from 2021-08-30 21-01-09](https://user-images.githubusercontent.com/84932430/131383816-760b1b60-19b8-43f7-a5e0-84ebbeeafad0.png)

`pip install selenium`

`pip install fake_useragent`

`pip install termcolor`

# How to use?

**First of all** install GoogleChrome webdriver: https://sites.google.com/a/chromium.org/chromedriver/downloads and paste-in it's path to the script.

![driver](https://user-images.githubusercontent.com/84932430/131385179-894426f7-8545-4d97-8290-3db2da688d63.png)

`python3 Vexadious.py run` to run in headless mode (recommended), it will open websites on Google-Chrome in the background without actually opening the Browser.

`python3 Vexadious.py show` if you want it to open Google-Chrome tabs and display it (not recommended, might be laggy after a number of tabs are opened).

**Show mode:**

![Screenshot from 2021-08-30 21-08-13](https://user-images.githubusercontent.com/84932430/131384667-db63a97c-8da8-46b0-bece-36bb5492495e.png)

