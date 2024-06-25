from flask import Flask, jsonify
import tweepy
import instaloader
from datetime import datetime

app = Flask(__name__)

# Twitter API credentials (replace with your own keys)
TWITTER_CONSUMER_KEY = 'your_consumer_key'
TWITTER_CONSUMER_SECRET = 'your_consumer_secret'
TWITTER_ACCESS_TOKEN = 'your_access_token'
TWITTER_ACCESS_SECRET = 'your_access_secret'

# Initialize Tweepy API
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
twitter_api = tweepy.API(auth)

# Initialize Instaloader
instagram_loader = instaloader.Instaloader()

# Route to fetch recent tweets
@app.route('/api/twitter')
def get_recent_tweets():
    username = 'example_twitter_username'  # Replace with the Twitter username you want to fetch tweets from
    count = 5  # Number of tweets to fetch
    tweets = []

    try:
        # Fetch recent tweets
        for tweet in tweepy.Cursor(twitter_api.user_timeline, screen_name=username, tweet_mode="extended").items(count):
            tweets.append({
                'text': tweet.full_text,
                'created_at': tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
            })
    except tweepy.TweepError as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'tweets': tweets})

# Route to fetch recent Instagram posts
@app.route('/api/instagram')
def get_recent_instagram_posts():
    username = 'example_instagram_username'  # Replace with the Instagram username you want to fetch posts from
    count = 5  # Number of posts to fetch
    posts = []

    try:
        # Fetch recent posts
        profile = instaloader.Profile.from_username(instagram_loader.context, username)
        for post in profile.get_posts():
            if len(posts) < count:
                posts.append({
                    'url': f'https://www.instagram.com/p/{post.shortcode}/',
                    'caption': post.caption,
                    'likes': post.likes,
                    'comments': post.comments,
                    'timestamp': post.date_utc.strftime("%Y-%m-%d %H:%M:%S")
                })
    except instaloader.InstaloaderException as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'instagramPosts': posts})

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
