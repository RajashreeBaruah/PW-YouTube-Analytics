import requests
import json
import mysql.connector
from datetime import datetime


API_KEY = "GENERATE_YOUR_API_KEY"
CHANNEL_ID = "UCiGyWN6DEbnj2alu7iapuKQ"
url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}"

response = requests.get(url)
data = response.json()

if "items" in data:
    stats = data["items"][0]["statistics"]
    print("Subscribers:", stats["subscriberCount"])
    print("Total Views:", stats["viewCount"])
    print("Total Videos:", stats["videoCount"])
else:
    print("Error fetching data.")

#get video IDs
video_url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&part=id&order=date&type=video&maxResults=50"

response = requests.get(video_url)
video_data = response.json()

video_ids = [item["id"]["videoId"] for item in video_data["items"]]

#fetch video stats
video_stats_url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics,snippet&id={','.join(video_ids)}&key={API_KEY}"

response = requests.get(video_stats_url)
video_stats = response.json()

for item in video_stats["items"]:
    title = item["snippet"]["title"]
    views = item["statistics"].get("viewCount", 0)
    likes = item["statistics"].get("likeCount", 0)
    comments = item["statistics"].get("commentCount", 0)
    upload_date = item["snippet"]["publishedAt"]
    # Convert to MySQL DATETIME format
    upload_date = upload_date.replace('T', ' ').replace('Z', '')

    #print(f"Title: {title}, Views: {views}, Likes: {likes}, Comments: {comments}, Uploaded on: {upload_date}")

#connect to db
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="India123@R",
    database="youtube_analytics"
)

cursor = conn.cursor()

# Insert Channel Data
channel_insert = """
INSERT INTO channel_stats (channel_id, name, subscribers, total_views, total_videos)
VALUES (%s, %s, %s, %s, %s)
"""
channel_values = (CHANNEL_ID, "PhysicsWallah", stats["subscriberCount"], stats["viewCount"], stats["videoCount"])
cursor.execute(channel_insert, channel_values)

# Insert Video Data
video_insert = """
INSERT INTO video_stats (video_id, title, views, likes, comments, upload_date)
VALUES (%s, %s, %s, %s, %s, %s)
"""

for item in video_stats["items"]:
    title = item["snippet"]["title"]
    views = item["statistics"].get("viewCount", 0)
    likes = item["statistics"].get("likeCount", 0)
    comments = item["statistics"].get("commentCount", 0)
    upload_date = item["snippet"]["publishedAt"]

    # Convert to MySQL DATETIME format
    upload_date = upload_date.replace('T', ' ').replace('Z', '')

    values = (
        item["id"],
        title,
        views,
        likes,
        comments,
        upload_date
    )
    cursor.execute(video_insert, values)

conn.commit()
cursor.close()
conn.close()
