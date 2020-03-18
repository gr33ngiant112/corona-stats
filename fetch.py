#!/usr/bin/env python3
import os
import sys
import requests
from bs4 import BeautifulSoup 

def parsePage(content):
    soup = BeautifulSoup(content, 'html.parser')
    search = soup.find_all("div", {"id": "maincounter-wrap"})
    cases = search[0].get_text()
    deaths = search[1].get_text()
    recovered = search[2].get_text()

    return cases, deaths, recovered

def main(url = 'https://www.worldometers.info/coronavirus/'): 
    if "https_proxy" in os.environ:
      proxies = {
        "https_proxy": os.environ['https_proxy']
      }
      r = requests.get(url, proxies=proxies)
    else:
      r = requests.get(url)
    cases, deaths, recovered = parsePage(r.text)
    print("===== Coronavirus Data =====")
    print(cases)
    print(deaths)
    print(recovered)
    print("============================")

if __name__ == '__main__':
  main()