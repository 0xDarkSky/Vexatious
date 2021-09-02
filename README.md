# Vexatious

![fishes](https://user-images.githubusercontent.com/84932430/131382979-c86a0a35-6585-4a07-ab0e-41c9863982f4.jpg)

**Program that generates Fake WebTraffic to hide yours, (Written in Python). Improved version of Traffic-Confuser.**

![Screenshot from 2021-08-30 20-57-50](https://user-images.githubusercontent.com/84932430/131383448-87603607-e526-4e93-8a63-9287de7b4ad6.png)

This is a V2 of Traffic-Confuser. The program uses Selenium module to open websites in Google Chrome browser.

***Note***: *I highly recommend reading the whole documentation to understand how it works, and how to use it properly.*

# Dependencies to install:

Just run  `pip install -r requirements.txt`

# How to use?

**First of all** install GoogleChrome webdriver: https://sites.google.com/a/chromium.org/chromedriver/downloads and paste-in it's path to the script.

(And obviously have Google-Chrome itself installed)

![driver](https://user-images.githubusercontent.com/84932430/131385179-894426f7-8545-4d97-8290-3db2da688d63.png)

`python3 Vexatious.py` to run in headless mode (recommended), it will open websites on Google-Chrome in the background without actually opening the Browser with default settings.

**You can run it with custom settings**:

Ex. `python3 Vexatious.py [arg1] [arg2] [arg3]`

**Arguments**: 

*Arg1* = min timeouts, ex. `min50`. 

*Arg2* = max timeouts, ex. `max120`. 

*Arg3* = `show` / `run`.

`show` will display Google-Chrome and open tabs (not recommended, might get laggy after a number of tabs are opened) 

`run` will open the websites in Google-Chrome with *"headless"* mode, which means that the Browser will run in the background without displaying tabs (***recommended***) 

**Note**: *your ISP sees the same no matter what mode you use.*

***Important***: *if you use Custom Settings, all 3 arguments are necessary.* 

**Show mode:**

![Screenshot from 2021-08-30 21-08-13](https://user-images.githubusercontent.com/84932430/131384667-db63a97c-8da8-46b0-bece-36bb5492495e.png)

# How does it work?

Basically it just opens random websites from the list, the websites are opened on Google-Chrome, you can choose whether to do it in the background or to display the tabs (your Internet Provider still sees those websites if you run this in the background).

The times between sending each request are also random, from 10 to 100 seconds, (you can use *Custom Settings* like *mentioned before*).

Also added some user agents.

# What's the purpose?

**Your ISP sells your data** for cents and does whatever they want with it, it goes against your privacy, while you use this, it's **difficult to see what you are actually browsing**, your actual data is *hidden* since most of the requests will be fake because they're generated by the script.

# You can buy me a coffee for the sleepless nights XD

BTC: `bc1q9wxz3vk43sv9yd0aacmpta55q42tg2ffprkut4`

ETH: `0x468A5110389f80a5C16642Dc2D70d5E117c73e64`

XMR: `49eSWZyQqT4Wwik4bQqPiKJyN3GGKQkkXAZ5WuPJdkCT3HGysh58k96ZWCy1H4fmHGNmTcRTb9HvERzWVTfFAvkaBpH9yRP`

# The program is still on development

I'm thinking of making this project BIG and updating it and improving it as often as I can.
