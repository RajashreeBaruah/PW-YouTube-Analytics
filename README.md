# PhysicsWallah YouTube Channel Analytics

## Project Overview
This project analyzes the **PhysicsWallah** YouTube channel using the **YouTube Data API**, **MySQL**, and **Python**. The objective is to extract and analyze key metrics such as **video views, engagement, upload frequency, and trends** to gain insights into channel performance.

## Features
- **Data Collection**: Used **YouTube Data API** to fetch publicly available video and channel statistics.
- **Data Storage**: Stored extracted data in a **MySQL database** (youtube_analytics) on **MySQL Workbench**.
- **SQL-Based Analysis**:
  - Identified **Top 10 Most Viewed Videos**.
  - Analyzed **Best Performing Upload Day**.
  - Computed **Engagement Rate**.
- **Python-Based Visualization (Matplotlib, Seaborn)**:
  - Plotted **Top 10 Most Viewed Videos**.
  - Tracked **Video Views Over Time**.
  - Visualized **Engagement Rate Per Video**.
  - Analyzed **Engagement Metrics (Likes, Views, Comments) Over Time**.

## Technologies Used
- **Programming Language:** Python
- **Database:** MySQL (MySQL Workbench for local storage)
- **APIs Used:** YouTube Data API v3
- **Data Processing & Visualization:** Pandas, Matplotlib




### SQL queries are -
- **Top 10 Most Viewed Videos**

  SELECT title, views FROM video_stats ORDER BY views DESC LIMIT 10;
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- **Best Performing Upload Day**

  SELECT DAYNAME(upload_date) AS day, SUM(views) AS view_count FROM video_stats GROUP BY day ORDER BY view_count DESC;
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- **Engagement Rate Calculation**

  SELECT ((likes + comments)/views)*100 AS engagement_rate, title FROM video_stats ORDER BY engagement_rate DESC;
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Below are the screenshots of the visualizations done using Python:
- Top 10 most viewed videos

![Top10MostViewed](https://github.com/user-attachments/assets/475db29a-2496-4c4d-9aa5-7ea7f2d10c26)

- Video views over time

![VideoViews](https://github.com/user-attachments/assets/fb706754-9ec3-4ac1-9e1b-8b3ec21c471f)

- Engagement rate per video (Top 10)

![EngagementRatePerVid](https://github.com/user-attachments/assets/479c0fc3-659e-41df-bdc5-20aa4fd50e3e)

- Engagement metrics (likes, views, comments) over time

![EngtOverTime](https://github.com/user-attachments/assets/4150b344-e853-4632-b638-be783efb272e)



## Future Enhancements
- Automate data updates using **cron jobs** or **Airflow**.
- Integrate **Power BI** for interactive dashboards.
- Perform **sentiment analysis** on video comments.


Thank you!

