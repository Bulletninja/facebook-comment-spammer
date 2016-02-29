import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy

def spam():
    token = "CAACEdEose0cBAKZCj1Cu3EFMlFJ6cnRiowpnNBAy5R0M0s58UDZCy2XLaZAPmi8KbuwY7fXSlc9yDza2aeuGV1fIHHwoYOndn8mtZAnkyoLVss4ahYsc5SJ02ZCeOQgrNcuinWhLRScaxfUynDWfWklIG2BCx0SBPTn0TNoc8SkfdtoPF8Y7KcJagwIZAe6Kyp38VwZAbFaxfW8vpK89h3lZAUSok0AZAFM8ZD"#Insert access token here.
    facebook = fb.graph.api(token)
    graph1 = GraphAPI(token)

    vid=input("Enter victim's id: ")
    query=str(vid)+"/posts?fields=id&limit=5000000000"
    r=graph1.get(query)

    idlist = [x['id'] for x in r['data']]
    idlist.reverse()
    print("There are "+ str(len(idlist)) +" spammable posts.")

    char1 = input("Do you want to spam? (y/n) ")
    count = 0
    if char1 =='y':
        nos = input("Enter number of posts to be spammed with comments: ")
        nos = int(nos)
        mess = input("Enter the message to be commented: ")
        mess = str(mess)
        if nos <= len(idlist):
           for indid in (idlist[(len(idlist)-nos):]):
              facebook.publish(cat = "comments", id = indid, message = mess) #Comments on each post
              facebook.publish(cat = "likes", id = indid)                 #Likes each post
              count = count + 1
              print("Notification number:"+str(count)+" on www.facebook.com/"+str(indid).split('_')[0]+"/posts/"+str(indid).split('_')[1])
        else:
              print("Not that many spammable posts available. No spam happening.")
    else :
      print("No spam happening then.")

spam()
