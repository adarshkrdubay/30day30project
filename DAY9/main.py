import requests as req
import sys
import os
Sitemap = []
def start(URL, wordlist):
    print("\n****************************************************************")
    print("\n* Copyright of AKD 2023                                        *")
    print("\n* https://www.adarshkrdubay.github.io                          *")
    print("\n* WebBuster v0.5                                               *")
    print("\n****************************************************************")
    print("\n****************************************************************")
    print(f"\n* Host:                {URL} *")
    print(f"\n* wordlist:            {wordlist} *")
    print("\n****************************************************************")

def hostcheek(URL):
    try:
        print("Cheeking Host status")
        res=req.post(f"{URL}")
        print("Host is up")
        print("----------")
    except Exception as e:
        print(f"{URL} is down")
        exit()
def cheeksite(url,site):
        sitelist = open(filelis, "r")
        for site in sitelist:  
            Sitemap.append(site.replace("\n", ""))
        for site in Sitemap:
        	res=req.get(f"{URL}{site}")
        	if res.status_code==200:
        	     print(f"/{site}            :{res.status_code}")
if __name__ == '__main__':
    try:
        URL = sys.argv[1].strip()
        try:
            filelis=sys.argv[2].strip
        except:
        	filelis="test.list"
        else:
        	print("[-] Usage: %s <url> <wordlist>" % sys.argv[0])
        	sys.exit()
    except:
    	print("[-] Example: %s www.example.com 'wordlist.txt'" % sys.argv[0])
    	sys.exit()
    start(URL,filelis)
    hostcheek(URL)
    cheeksite(URL,filelis)
