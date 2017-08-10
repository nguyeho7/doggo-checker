import requests
import os
import glob
import shutil

breeds_url = 'https://dog.ceo/api/breeds/list' 

def mv():
    r = requests.get(breeds_url)
    breed_list = r.json()['message']
    for breed in breed_list:
        try:
            os.mkdir("images/{}/".format(breed))
            for f in glob.glob("images/{}_*".format(breed)):
                shutil.copy(f, "images/{}".format(breed))
        except:
            print("{} exists".format(breed))   
