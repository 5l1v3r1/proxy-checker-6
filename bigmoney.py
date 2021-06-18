from discord_webhook import DiscordWebhook, DiscordEmbed
import threading
import csv
import requests
import concurrent.futures
from colorama import init
from termcolor import colored
from os import system

goodproxies = 0
badproxies = 0
def updatetitle():
    system("title "+f"DomIsOffline Proxy Checker - Alive: {goodproxies} - Dead: {badproxies}")

updatetitle()

init()

print(colored("""\

   ____  ___________               ________              __            
  / __ \/ __/ __/ (_)___  ___     / ____/ /_  ___  _____/ /_____  _____
 / / / / /_/ /_/ / / __ \/ _ \   / /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
/ /_/ / __/ __/ / / / / /  __/  / /___/ / / /  __/ /__/ ,< /  __/ /    
\____/_/ /_/ /_/_/_/ /_/\___/   \____/_/ /_/\___/\___/_/|_|\___/_/     """, 'red', 'on_blue', attrs=['bold']))

print(colored("Made By DomIsOffline#4762", 'red', attrs=['bold']))


num_of_threads = input("Number Of Threads?" + "\n")

proxies = {
  'http': 'http://67.207.83.225:80',
  'https': 'http://136.226.33.115:443',
}
f = open('avaliable.txt', 'r+')
f.truncate(0) # need '0' when using r+

proxylist = []
working = []
with open('proxylist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

def extract(proxy):
    global goodproxies
    try:
        r = requests.get('https://httpbin.org/ip', proxies={'http' : proxy, 'https' : proxy}, timeout=2)
        rjson = r.json()
        print(proxy, ' - working')
        goodproxies = goodproxies + 1
        updatetitle()
        f = open("avaliable.txt", "a")
        f.write(proxy + "\n")
        f.close()
        return proxy
    except:
        global badproxies
        print("Bad Proxy.")
        badproxies = badproxies + 1
        updatetitle()
        pass

with concurrent.futures.ThreadPoolExecutor() as exector:
    exector.map(extract, proxylist)

for _ in range(num_of_threads):
    x = threading.Thread(target=extract)

