#!/usr/bin/env python
import urllib.request as req
import json 


def get_JSON(locale, store, code):
    #print(STORE, POSTAL)
    base_url = "https://backflipp.wishabi.com/flipp/items/search?"
    url = base_url + "locale=" + locale + "&postal_code=" + str(code) + "&q=" + store
    #print(url)
    flyer = req.urlopen(url)
    #print(flyer.read())
    return flyer.read()        
            



def get_img(JSON):
    imgs = []
    for arg in JSON["items"]: 
        imgs.append(arg["clipping_image_url"])
    #print(imgs)



def get_name(JSON):
    names = []
    for arg in JSON["items"]:
        names.append(arg["name"])
    #print(names)



#'''
print("-------------------------- starting script ------------------------------------")
code = "V9L6A8"         #input("please enter postal code: ")
store = "superstore"    #input("please enter prefered store: ")
locale = "francais"     #input("please enter locale: ")
b = get_JSON(locale, store, code)
#print (b)
flyer_JSON = json.loads(b)

get_img(flyer_JSON)
get_name(flyer_JSON)
print("--------------------------- ending  script ------------------------------------")
#'''

