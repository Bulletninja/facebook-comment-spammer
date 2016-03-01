# https://github.com/blaklites/fb

import yaml
import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy

with open("cfg.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

def spam():
    token = cfg['fbtoken']['me'] #Insert access token here.
    facebook = fb.graph.api(token)
    graph1 = GraphAPI(token)

    vid=input("Enter victim's id: ")
    query=str(vid)+"/posts?fields=id&limit=5000000000"
    r=graph1.get(query)

    token = cfg['fbtoken']['other'] #Insert access token here.
    facebook = fb.graph.api(token)
    graph1 = GraphAPI(token)

    idlist = [x['id'] for x in r['data']]
    idlist.reverse()
    print("There are " + str(len(idlist)) + " spammable posts.")

    char1 = input("Do you want to spam? (y/n) ")
    count = 0

    if char1 == 'y':
        nos = input("Enter number of posts to be spammed with comments: ")
        nos = int(nos)
        mess = input("Enter the message to be commented: ")
        mess = str(mess)
        if nos <= len(idlist):
           for indid in (idlist[(len(idlist)-nos):]):
              facebook.publish(cat = "comments", id = indid, message = mess) #Comments on each post
              facebook.publish(cat = "likes", id = indid)                 #Likes each post
              
              post_to_post = "http://www.facebook.com/" + str(indid).split('_')[0] + "/posts/" + str(indid).split('_')[1]
              facebook.publish(cat = "feed", id = "me", message = mess, link = post_to_post)
              count = count + 1
              print("Notification number: "+ str(count) + " on " + post_to_post)
        else:
              print("Not that many spammable posts available. No spam happening.")
    else:
      print("No spam happening then.")

spam()
