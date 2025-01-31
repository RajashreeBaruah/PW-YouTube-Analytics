use youtube_analytics;

CREATE TABLE channel_stats (
    channel_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    subscribers INT,
    total_views INT,
    total_videos INT
);

CREATE TABLE video_stats (
    video_id VARCHAR(50) PRIMARY KEY,
    title TEXT,
    views INT,
    likes INT,
    comments INT,
    upload_date DATETIME
);

show tables;

DESCRIBE video_stats;

ALTER TABLE channel_stats MODIFY COLUMN total_views BIGINT;
ALTER TABLE channel_stats MODIFY COLUMN subscribers BIGINT;

ALTER TABLE video_stats
MODIFY COLUMN views BIGINT,
MODIFY COLUMN likes BIGINT,
MODIFY COLUMN comments BIGINT;

select * from channel_stats;
select * from video_stats;

SELECT title, views FROM video_stats ORDER BY views DESC LIMIT 10;

SELECT DAYNAME(upload_date) AS day, SUM(views) AS view_count FROM video_stats GROUP BY day ORDER BY view_count DESC;

SELECT ((likes + comments)/views)*100 AS engagement_rate, title FROM video_stats ORDER BY engagement_rate DESC;

SELECT title, views FROM video_stats ORDER BY views DESC LIMIT 10;