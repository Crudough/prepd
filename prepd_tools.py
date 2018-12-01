#!/usr/bin/env python
import urllib.request as req
import json 


def get_JSON(locale, store, code):
    base_url = "https://backflipp.wishabi.com/flipp/items/search?"
    url = base_url + "locale=" + locale + "&postal_code=" + str(code) + "&q=" + store
    flyer = req.urlopen(url)
    return json.loads(flyer.read())        
            



def get_img(JSON):
    imgs = []
    for arg in JSON["items"]: 
        imgs.append(arg["clipping_image_url"])
    return imgs



def get_name(JSON):
    names = []
    for arg in JSON["items"]:
        names.append(arg["name"])
    return names

def find(keywords, JSON):
    match = []
    for item in JSON["items"]:
        for word in keywords:
            if word in item["name"]:
                match.append(item)
    v = { "items": match }
    return json.dumps(v)
