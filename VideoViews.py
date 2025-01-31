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

# Fetch video data (views and upload date)
query = "SELECT title, views, upload_date FROM video_stats ORDER BY upload_date;"
df = pd.read_sql(query, conn)

# Convert upload_date to datetime
df['upload_date'] = pd.to_datetime(df['upload_date'])

# Sort the data by upload_date (if it's not already sorted)
df = df.sort_values('upload_date')

# Plot views over time
plt.figure(figsize=(10, 6))
plt.plot(df['upload_date'], df['views'], marker='o', linestyle='-', color='skyblue')

# Add labels and title
plt.xlabel("Upload Date")
plt.ylabel("Views")
plt.title("Video Views Over Time for PhysicsWallah")

# Rotate the X-axis labels for better visibility
plt.xticks(rotation=45)

# Ensure the plot window appears
plt.tight_layout()  # Adjusts the layout to prevent clipping
plt.show()

# Close the connection
conn.close()