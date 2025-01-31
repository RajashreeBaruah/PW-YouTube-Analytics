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

# Fetch video statistics and upload date
query = "SELECT upload_date, views, likes, comments FROM video_stats ORDER BY upload_date;"
df = pd.read_sql(query, conn)

# Convert upload_date to datetime
df['upload_date'] = pd.to_datetime(df['upload_date'])

# Plot views, likes, and comments over time
plt.figure(figsize=(10, 6))

plt.plot(df['upload_date'], df['views'], label='Views', color='skyblue', marker='o')
plt.plot(df['upload_date'], df['likes'], label='Likes', color='green', marker='o')
plt.plot(df['upload_date'], df['comments'], label='Comments', color='orange', marker='o')

# Add labels and title
plt.xlabel("Upload Date")
plt.ylabel("Count")
plt.title("Engagement Metrics (Views, Likes, Comments) Over Time")

# Rotate the X-axis labels for better visibility
plt.xticks(rotation=45)

# Add legend
plt.legend()

# Ensure the plot window appears
plt.tight_layout()  # Adjusts the layout to prevent clipping
plt.show()

# Close the connection
conn.close()
