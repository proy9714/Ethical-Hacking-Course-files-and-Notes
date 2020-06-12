#!/usr/bin/env python 

import requests

def download(url):
    get_response = requests.get(url)
    
    # Accessing the last element of the list (i.e actual file name)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)
        
download("https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY1200_CR93,0,630,1200_AL_.jpg")
