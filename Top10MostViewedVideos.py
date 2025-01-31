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

# Fetch data
query = "SELECT title, views FROM video_stats ORDER BY views DESC LIMIT 10;"
df = pd.read_sql(query, conn)

# Modify the titles to show only the first 3 words
df['short_title'] = df['title'].apply(lambda x: ' '.join(x.split()[:3]))

# Create the bar plot
plt.figure(figsize=(10, 5))
bars = plt.barh(df['short_title'], df["views"], color='skyblue')

# Add data labels on each bar
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, bar.get_width(),
             va='center', ha='left', color='black', fontsize=10)

plt.xlabel("Views")
plt.ylabel("Video Title")
plt.title("Top 10 Most Viewed Videos on PhysicsWallah")
plt.gca().invert_yaxis()  # Invert the Y axis to show the most viewed on top

plt.tight_layout()
plt.show()

# Close the connection
conn.close()