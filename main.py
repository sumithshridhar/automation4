import os
import requests
import random
import tempfile
from dotenv import load_dotenv
from moviepy.editor import VideoFileClip
from pydub import AudioSegment, silence
import praw

load_dotenv()

# Reddit and IG credentials from .env
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="motivational_bot"
)

IG_USER_ID = os.getenv("IG_USER_ID")
IG_ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN")

# -------------------------------- #
# 1. Download top motivational video from Reddit
def download_video_from_reddit(subreddits=["GetMotivated", "motivational"]):
    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.hot(limit=10):
            if post.url.endswith((".mp4", ".mov")):
                video_url = post.url
                print(f"Found video: {video_url}")
                response = requests.get(video_url)
                if response.status_code == 200:
                    temp_path = tempfile_
