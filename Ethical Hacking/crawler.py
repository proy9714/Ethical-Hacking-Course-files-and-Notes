#!/usr/bin/env python

import requests

def request(url):
    try: 
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError: 
        pass
    
### AGAINST METASPLOITABLE ###    
target_url = "10.0.2.11/mutillidae/"

# Opening and apending all words in a word list file    
# word_file = "subdomains.list.txt"
extension_file = "files-and-dirs-wordlist.list.txt"
with open(extension_file, mode='r') as wordlist_file:
    for line in wordlist_file:
        # Removing any white space characters
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> " + test_url)