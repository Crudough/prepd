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
    #return imgs
    print(imgs)



def get_name(JSON):
    names = []
    imgs = []
    for arg in JSON["items"]:
        names.append(arg["name"])
        imgs.append(arg["clipping_image_url"])
    #return names, imgs
    print(names)
    print(imgs)

def find(keywords, JSON):
    names = get_name(JSON)
    match = []
    for word in keywords:
        for name in names:
            if word in name:
                match.append(name)
    print(match)


