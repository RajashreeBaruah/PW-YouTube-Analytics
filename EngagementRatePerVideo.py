import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Establish MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="India123@R",
    database="youtube_analytics"
)

# Fetch video statistics (likes, comments, views, title)
query = "SELECT title, views, likes, comments FROM video_stats;"
df = pd.read_sql(query, conn)

# Calculate engagement rate per video
df['engagement_rate'] = (df['likes'] + df['comments']) / df['views'] * 100

# Sort by highest engagement rate
df_sorted = df.sort_values('engagement_rate', ascending=False)

# Plot the engagement rates for the top 10 videos
plt.figure(figsize=(10, 6))
bars = plt.barh(df_sorted['title'].head(10), df_sorted['engagement_rate'].head(10), color='skyblue')

# Add data labels on each bar
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{bar.get_width():.2f}%', 
             va='center', ha='left', color='black', fontsize=10)

plt.xlabel("Engagement Rate (%)")
plt.ylabel("Video Title")
plt.title("Top 10 Videos by Engagement Rate")
plt.gca().invert_yaxis()  # Invert the Y axis to show the highest on top

plt.tight_layout()
plt.show()

# Close the connection
conn.close()
