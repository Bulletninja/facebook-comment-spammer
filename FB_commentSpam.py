# https://github.com/blaklites/fb

import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy

def spam():
    token = "CAACEdEose0cBAJcHxTrv4N9agGjaXro12OfBZAvZCYiksMqnRud9ZBxS2ED1hCq8AVZClHlb34qwzTgx0hD8h6SXi3qpK4kK6ZB2uk9ZCitFGlN7UbZCZCxox0V6hhKxNS6AVwoXcEkAIue83Se6stxPOPG4tQEKnw0uRC0WxQXXcG9rZAWZA0awY7bomGAVVvnfbyujazt8OHujMXziTJfeHEFjoSl0mBDLkZD"#Insert access token here.
    facebook = fb.graph.api(token)
    graph1 = GraphAPI(token)

    vid=input("Enter victim's id: ")
    query=str(vid)+"/posts?fields=id&limit=5000000000"
    r=graph1.get(query)

    token = "CAAHC0JZBitP8BAMaKZCqrwtJUnPtLdiwfCHaYfTjZBxuW0ZCvYR147IlZBZAsxpjjeHcZBu5I4rsRto4jBcZA4HQHxlB8RZCexZC0ns0d9nQPF38LzHWCR5tzlf1nHG1buflOjGRc3Gz9LyTtWKRaA08JbF2xg1BReEiVSDuZBKejihnnf1ebUc4NNNFiFvFG4s06wJky3pisQaGgZDZD"#Insert access token here.
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
              #facebook.publish(cat = "comments", id = indid, message = mess) #Comments on each post
              #facebook.publish(cat = "likes", id = indid)                 #Likes each post
              #facebook.publish(cat = "share", id = indid)                 #Shares each post
              post_to_post = "http://www.facebook.com/" + str(indid).split('_')[0] + "/posts/" + str(indid).split('_')[1]
              facebook.publish(cat = "feed", id = "me", message="how funny is this", link = post_to_post)
              count = count + 1
              print("Notification number: "+ str(count) + " on " + post_to_post)
        else:
              print("Not that many spammable posts available. No spam happening.")
    else:
      print("No spam happening then.")

spam()
