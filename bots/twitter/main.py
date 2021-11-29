from auto import auto_follow
from auto import auto_fav
from auto import auto_follow_followers

#this is a sample program to use the auto.py script
#Favourite anybody with tweets containing these phrases
#Count is the number of most recent tweets

hashtag_list = ['nft','nftcollector','NFTGiveaway','NFTGiveaways','NFTdrop','Mystrios','MysMask','Moneyheist','followback','teamfollow']
for i in hashtag_list :
        auto_fav(i, count=100)
        

#Folows anybody with these phrases
for i in hashtag_list :
        auto_follow(i, count=100)
        
#Follows anybody that have followed you
auto_follow_followers()


'''
auto_fav("ubuntu", count=1)
auto_fav("teamfollow", count=1)
auto_fav("teamfollowback", count=0)



#auto follow 10 users who come when we search for keyword "followback"
auto_follow("followback", count=10)
auto_follow("teamfollow", count=5)
'''
