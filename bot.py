#Python Reddit API Wrapper
import praw 

#bot constructor 
bot = praw.Reddit(user_agent='example_bot v0.1',
                  client_id='your_id',
                  client_secret='your_secret',
                  username='your_username',
                  password='your_password')

#subreddit contructor 
bitcoin_sub = bot.subreddit('all')


#instantiates a comment stream 
bitcoin_sub_comments = bitcoin_sub.stream.comments()

#combs through stream
for comment in bitcoin_sub_comments:
    text = comment.body
    if "example" in text:
            print(text)
            print("\n")
	

                            
