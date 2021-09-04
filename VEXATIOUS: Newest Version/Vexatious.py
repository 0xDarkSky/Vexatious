import time
import os
import random
from os import path 
import sys

#IMPORTANT! Please read the README on Github to understand how it works and how to use it correctly.

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

def SiteOpen():
    with open("sites.txt") as f:
         SiteOpen.content = f.readlines()
         SiteOpen.WhiteListLinks = [x.strip() for x in SiteOpen.content]

os.system("clear")
print(colored(f"{LOGO}", "blue"))
time.sleep(2)

def ClientsOpen():
    with open("/home/darksky/Projects/Vexatious/clients.txt") as f:
         ClientsOpen.content = f.readlines()
         ClientsOpen.randUsers = [x.strip() for x in ClientsOpen.content]
         
def WebOpen():
    try:
        usr_input_min = sys.argv[1]
        usr_input_max = sys.argv[2]
        usr_input_show_run = sys.argv[3]
        
        ClientsOpen()

        if usr_input_show_run.lower() == "show":
           op = webdriver.ChromeOptions()
           op.add_argument("--window-size=1200,800")
           op.add_argument(f"user-agent={ClientsOpen.randUsers}")
        if usr_input_show_run.lower() == "run":
           op = webdriver.ChromeOptions()
           op.add_argument("headless")
           op.add_argument("--window-size=1200,800")
           op.add_argument(f"user-agent={ClientsOpen.randUsers}")
    
        SiteOpen()

        driver = webdriver.Chrome(executable_path=r"/home/darksky/Downloads/chromedriver_linux64(1)/chromedriver", options=op) #path to your browser's webdrive
        link = random.choice(SiteOpen.WhiteListLinks)
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
        ClientsOpen()

        op = webdriver.ChromeOptions()
        op.add_argument("headless")
        op.add_argument("--window-size=1200,800")
        op.add_argument(f"user-agent={randUsers}")
        driver = webdriver.Chrome(executable_path=r"/home/darksky/Downloads/chromedriver_linux64(1)/chromedriver", options=op) #path to your browser's webdriver 
        link = random.choice(ClientsOpen.WhiteListLinks)
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
