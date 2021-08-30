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
	print("\nInstalling 3 dependencies...\n")
	os.system("pip install fake_useragent")
	os.system("pip install selenium")
	os.system("pip install termcolor")
	os.system("clear")

user_agent = "Mozilla/5.0 (iPad; CPU OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B141 Safari/8536.25"

WhiteListLinks = ["https://pixabay.com/", "https://finance.yahoo.com/", "https://target.com/", "https://wired.com/", "https://lainchan.org", "https://libredd.it/", "https://harvard.edu/", "https://forbes.com/", "https://boards.4channel.org/", "https://google.com", "https://soundcloud.com", "https://spotify.com", "https://time.com", "https://cloudflare.com", "https://wordpress.org", "https://invidious-us.kavin.rocks", "https://europa.eu"]

os.system("clear")
print(colored(f"{LOGO}", "blue"))
time.sleep(2)

usr_input = sys.argv[1]

def webopen():
	usr_input = sys.argv[1]
	if usr_input.lower() == "show":
	   op = webdriver.ChromeOptions()
	   op.add_argument("--window-size=1200,800")
	   op.add_argument(f"user-agent={user_agent}")
	if usr_input.lower() == "run":
	   op = webdriver.ChromeOptions()
	   op.add_argument("headless")
	   op.add_argument("--window-size=1200,800")
	   op.add_argument(f"user-agent={user_agent}")

	driver = webdriver.Chrome(executable_path=r"/home/darksky/Downloads/chromedriver_linux64(1)/chromedriver", options=op) #path to your browser's webdriver 
	link = random.choice(WhiteListLinks)
	linkColors = colored(f"{link}", "cyan")
	print(colored(f"Opening {linkColors}", "green"))
	driver.get(link)

count = 0

def send_count():
    secs = int((time.time() - start_time))
    if secs < 60:
       print(f"\nSent {count} requests in " + "%s seconds." % (secs))
    if secs > 60:
       calc = secs / 60
       mins = int(calc)
       print(f"\nSent {count} requests in {mins} minutes.\n")
       print("")
    exit()

start_time = time.time()

try:
	while True:
		count += 1
		webopen()
		faster = int(random.randint(10,45))
		slower = int(random.randint(30,100))
		FS = faster, slower
		sleeper = random.choice(FS)
		sleeperColors = colored(f" {sleeper} ", "yellow")
		displayWait = colored("\nWaiting for", "red")
		displayRequest = colored("seconds before sending another request...\n", "red")
		print(displayWait + sleeperColors + displayRequest)
		time.sleep(sleeper)
except KeyboardInterrupt:
	send_count()
	time.sleep(3)
	os.system("clear")
