from config import *
import praw
redditsave_format = 'https://redditsave.com/info?url='
redditvideodl_format = 'https://redditvideodl.com/dl.php?url=https://www.reddit.com'


def give_reply(url):
    reply = f'''#[Download Link]({redditsave_format + url})
#[Alternate Link]({redditvideodl_format + url})
^(Beep beep boop boop. I am a bot. I just automatically give download links cause I download from this subreddit a LOT and am too lazy to do the whole procedure when I can just scroll down the comments ya know. View my source code On [GitHub here](github.com/stupid-melon/downloadlinkbot))'''
    
    return reply


reddit = praw.Reddit(client_id = client_id,
client_secret = client_secret,
username = username,
password = password,
user_agent = 'Whatever')


subreddit = reddit.subreddit('startledcats')


print('\nDownload bot is up\n')

for post in subreddit.stream.submissions(skip_existing = True):
    try:
        post_type = post.post_hint
    except:
        post_type = 'error'

    if post_type == 'hosted:video':
        post.reply( give_reply(post.permalink) )

