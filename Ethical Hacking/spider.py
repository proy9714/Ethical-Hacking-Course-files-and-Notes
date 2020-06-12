#!/usr/bin/env python

import re
import urlparse
import requests

### AGAINST METASPLOITABLE ###
target_url = "http://10.0.2.11/mutillidae/"
target_links = []


def extract_links_from(url):
    response = requests.get(target_url)    
    # Using regex to findall href links
    return re.findall('(?:href=")(.*?)"', response.content)

def crawl(url):  
    # The response.content returns the HTML code
    href_links = extract_links_from(url)
    for link in href_links:
        # Convert relative URLs to full URLs
        link = urlparse.urljoin(target_url, link)

        if "#" in link:
            link = link.split("#")[0]

        # Using condition to check for native URLs
        if (target_url in link) and (link not in target_links):
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url) 
