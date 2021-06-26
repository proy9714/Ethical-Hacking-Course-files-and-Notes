#!/usr/bin/env python

import requests
import re
import urlparse
from bs4 import BeautifulSoup

class scanner:
    def __init__(self, url, ignore_links):
        # Creating a session object which represents the current session
        # So all GET and POST requests will be using this session
        self.session = requests.Session()
        
        self.target_url = url
        self.target_links = []
        self.links_to_ignore = ignore_links
    
    def extract_links_from(self, url):
        # Using the session to call the get function
        response = self.session.get(url)    
        
        # Using regex to findall href links
        return re.findall('(?:href=")(.*?)"', response.content)

    def crawl(self, url=None): 
        # If the method has been called from outside the class
        if url == None:
            url = self.target_url
         
        # The response.content returns the HTML code
        href_links = self.extract_links_from(url)
        for link in href_links:
            # Convert relative URLs to full URLs
            link = urlparse.urljoin(self.target_url, link)

            if "#" in link:
                link = link.split("#")[0]

            # Using condition to check for native URLs and also URLs to ignore
            if (self.target_url in link) and (link not in self.target_links) and (link not in self.links_to_ignore):
                self.target_links.append(link)
                print(link)
                self.crawl(link)
    
    def extract_forms(self, url):
        response = self.session.get(url)
        
        # Parsing the html page 
        parsed_html = BeautifulSoup(response.content, features="html.parser")

        # Extracting all the forms on the page
        # Using findAll() to get all HTML elements
        return parsed_html.findAll("form")
    
    def submit_form(self, form, value, url):
        # Extracting the action attribute value from the form tag
        # Using get() to get the value of a property in a tag
        action = form.get("action")
        
        # Concatinating the action to get complete path
        post_url = urlparse.urljoin(url, action)
        print("Action url = " + post_url)
        
        method = form.get("method")
        print("Method = " + method)

        inputs_list = form.findAll("input")
        post_data = {}
        for inputtag in inputs_list:
            input_name = inputtag.get("name")
            input_type = inputtag.get("type")
            input_value = inputtag.get("value")

            if input_type == "text":
                input_value = value

            post_data[input_name] = input_value

        if method == "post":
            return self.session.post(post_url, data=post_data)
        return self.session.get(post_url, params=post_data)
    
    def run_scanner(self):
        for link in self.target_links:
            forms = self.extract_forms(link)
            for form in forms:
                print("[+] Testing form in " + link)
                is_vulnerable_to_xss = self.test_xss_in_form(form, link)
                if is_vulnerable_to_xss:
                    print("\n\n===============================================================================\n")
                    print("[***] XSS discovered in " + link + " in the following form")
                    print(form)
                    print("\n===============================================================================\n\n")
            
            # To find out whether there is a query string
            if "=" in link:
                print("[+] Testing " + link)
                is_vulnerable_to_xss = self.test_xss_in_link(link)
                if is_vulnerable_to_xss:
                    print("\n\n===============================================================================\n")
                    print("[***] XSS discovered in " + link)
                    print("\n===============================================================================\n\n")
             
    def test_xss_in_link(self, url):
        xss_test_script = "<sCript>alert('XSS')</scriPt>" 
        
        # Modifying query string
        url  = url.replace("=", "=" + xss_test_script)
        response = self.session.get(url)
        
        # Checking whether the HTML code contains the XSS code
        return xss_test_script in response.content
                
    def test_xss_in_form(self, form, url):
        xss_test_script = "<sCript>alert('XSS')</scriPt>" 
        response = self.submit_form(form, xss_test_script, url)
        # Testing whether the XSS code was succesfully submitted using the form
        return xss_test_script in response.content