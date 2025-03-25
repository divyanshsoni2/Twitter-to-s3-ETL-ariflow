
import tweepy
import pandas as pd
from datetime import datetime
import s3fs

def run_twitter_etl():

    bearer_token = "AAAAAAAAAAAAAAAAAAAAAO5m0AEAAAAADmVbMjqTTIwFb3tIRQR%2B7XsA1%2FM%3DzMs3TEwNiZ0vSlRGWwCYobcBJeoYWZhI1KRzagyBDqCYbRVybJ"
    client = tweepy.Client(bearer_token=bearer_token)
    user = client.get_user(username="elonmusk")
    user_id = user.data.id


    response = client.get_users_tweets(
        id=user_id,
        max_results=200,
        tweet_fields=["created_at", "public_metrics"],
        exclude=["retweets", "replies"]
    )

    tweet_list = []


    if response.data:
        for tweet in response.data:
            refined_tweet = {
                "user": "elonmusk",
                "text": tweet.text,
                "favorite_count": tweet.public_metrics["like_count"],
                "retweet_count": tweet.public_metrics["retweet_count"],
                "created_at": tweet.created_at
            }
            tweet_list.append(refined_tweet)


        df = pd.DataFrame(tweet_list)
        df.to_csv("s3://airflow-twitter-bucket-divyansh/elon_musk_twitter_data.csv", index=False)
        
        print("Saved to elon_musk_twitter_data.csv")
    else:
        print("No tweets found.")
