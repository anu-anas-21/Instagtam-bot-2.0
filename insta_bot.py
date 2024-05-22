from time import sleep
from turtle import delay
from instabot import Bot

my_bot = Bot()


my_bot.login(username="username" , password="password")

#unfollow section
my_bot.unfollow_non_followers()
delay(2)

#like section
my_bot.like_hashtag(["bmw","lulu mall","kerala"], amount=100)
sleep(30)

#follow section
user_id=my_bot.get_user_id_from_username(["tfm._play","team_kuttusan"])
my_bot.follow_followers(user_id, nfollows=30)
sleep(20)

my_bot.logout()
