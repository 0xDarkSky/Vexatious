import time
import os
import random
from os import path 
import sys

LOGO = """
                  ░██████╗░██╗░░░░░░█████╗░██████╗░  
                  ██╔═══██╗██║░░░░░██╔══██╗██╔══██╗ 
                  ██║██╗██║██║░░░░░██║░░██║██████╔╝  
                  ╚██████╔╝██║░░░░░██║░░██║██╔══██╗  
                  ░╚═██╔═╝░███████╗╚█████╔╝██║░░██║  
                  ░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝

██╗░░░██╗███████╗██╗░░██╗░█████╗░████████╗██╗░█████╗░██╗░░░██╗░██████╗
██║░░░██║██╔════╝╚██╗██╔╝██╔══██╗╚══██╔══╝██║██╔══██╗██║░░░██║██╔════╝
╚██╗░██╔╝█████╗░░░╚███╔╝░███████║░░░██║░░░██║██║░░██║██║░░░██║╚█████╗░
░╚████╔╝░██╔══╝░░░██╔██╗░██╔══██║░░░██║░░░██║██║░░██║██║░░░██║░╚═══██╗
░░╚██╔╝░░███████╗██╔╝╚██╗██║░░██║░░░██║░░░██║╚█████╔╝╚██████╔╝██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░░╚═════╝░╚═════╝░
"""

try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from fake_useragent import UserAgent
    from termcolor import colored
except ImportError:
    os.system("clear")
    print("Some of the dependencies might not be installed!")
    print("Run: pip install -r requirements.txt")
    exit()

WhiteListLinks = "https://instagram.com", "https://netflix.com", "https://twitter.com", "https://shopify.com", "https://pixabay.com/", "https://www.duckduckgo.com", "https://target.com/", "https://wired.com/", "https://lainchan.org", "https://libredd.it/", "https://harvard.edu/", "https://forbes.com/", "https://google.com", "https://soundcloud.com", "https://spotify.com", "https://time.com", "https://cloudflare.com", "https://wordpress.org", "https://invidious-us.kavin.rocks", "https://europa.eu"

os.system("clear")
print(colored(f"{LOGO}", "blue"))
time.sleep(2)

def WebOpen():
    try:
        usr_input_min = sys.argv[1]
        usr_input_max = sys.argv[2]
        usr_input_show_run = sys.argv[3]
        
        user_agent_Acer = "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko"
        user_agent_Ipad = "Mozilla/5.0 (iPad; CPU OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B141 Safari/8536.25"
        user_agent_MacOS = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
        user_agent_Huawei = "Mozilla/5.0 (Linux; Android 10; CDY-AN00 Build/HUAWEICDY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36"
        user_agent_Samsung = "Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T350 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Safari/537.36"
        #added some user_agents that you can use, choose which ever you want or add more
        
        if usr_input_show_run.lower() == "show":
           op = webdriver.ChromeOptions()
           op.add_argument("--window-size=1200,800")
           op.add_argument(f"user-agent={user_agent_MacOS}")
        if usr_input_show_run.lower() == "run":
           op = webdriver.ChromeOptions()
           op.add_argument("headless")
           op.add_argument("--window-size=1200,800")
           op.add_argument(f"user-agent={user_agent_MacOS}")
    
        driver = webdriver.Chrome(executable_path=r"/home/darksky/Downloads/chromedriver_linux64(1)/chromedriver", options=op) #path to your browser's webdrive
        link = random.choice(WhiteListLinks)
        linkColors = colored(f"{link}", "cyan")
        print(colored(f"Opening {linkColors}", "green"))
        driver.get(link)
        usr_input_MIN = usr_input_min.replace("min", "")
        min_time = int(usr_input_MIN) 

        usr_input_MAX = usr_input_max.replace("max", "")
        max_time = int(usr_input_MAX)
        custom = random.randint(min_time, max_time)
        sleeperColors = colored(f" {custom} ", "yellow")
        displayWait = colored("\nWaiting for", "red")
        displayRequest = colored("seconds before sending another request...\n", "red")
        print(displayWait + sleeperColors + displayRequest)
        time.sleep(custom)

    except IndexError:
        
        user_agent_Acer = "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko"
        user_agent_Ipad = "Mozilla/5.0 (iPad; CPU OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B141 Safari/8536.25"
        user_agent_MacOS = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
        user_agent_Huawei = "Mozilla/5.0 (Linux; Android 10; CDY-AN00 Build/HUAWEICDY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36"
        user_agent_Samsung = "Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T350 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Safari/537.36"
        
        op = webdriver.ChromeOptions()
        op.add_argument("headless")
        op.add_argument("--window-size=1200,800")
        op.add_argument(f"user-agent={user_agent_MacOS}")
        driver = webdriver.Chrome(executable_path=r"/home/darksky/Downloads/chromedriver_linux64(1)/chromedriver", options=op) #path to your browser's webdriver 
        link = random.choice(WhiteListLinks)
        linkColors = colored(f"{link}", "cyan")
        print(colored(f"Opening {linkColors}", "green"))
        driver.get(link)
        faster = int(random.randint(10,45))
        slower = int(random.randint(30,100))
        FS = faster, slower
        sleeper = random.choice(FS)
        sleeperColors = colored(f" {sleeper} ", "yellow")
        displayWait = colored("\nWaiting for", "red")
        displayRequest = colored("seconds before sending another request...\n", "red")
        print(displayWait + sleeperColors + displayRequest)
        time.sleep(sleeper)

count = 0

def send_count():
    secs = int((time.time() - start_time))
    if secs < 60:
       print(f"\nSent {count} requests in " + "%s seconds." % (secs))
    if secs > 60:
       calc = secs / 60
       mins = int(calc)
       print(f"\nSent {count} requests in {mins} minutes.\n")

start_time = time.time()

try:
    while True:
        count += 1
        WebOpen()
except KeyboardInterrupt:
    send_count()
    time.sleep(3)
    os.system("clear")
    exit()

