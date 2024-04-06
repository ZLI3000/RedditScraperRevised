import praw

reddit = praw.Reddit(
    client_id='fXy-16VprltamlV0kpEuDQ',
    client_secret='_tXlzrPE-34k5AvsxWXX42wasLVS0g',
    user_agent='linux:com.nosleepscraper:0.1 (by /u/Middle_Reputation310)',
)

subreddit = reddit.subreddit("nosleep") #grabs subreddit ID and attaches var
hot_submissions = subreddit.hot(limit=5) #creates variable for hot submissions
for submission in hot_submissions: #grabbing hot submissions
    with open("nosleep.txt", "w") as ns: #opens nosleep.txt in write mode ns is the nosleep file path
        print(submission.selftext, file=ns) #self text grabs the submissions text and the print is forwarded to a txt file



