# Data-Analyst-Assignment

# **Admin Dashboard for Telegram Group Analytics**

# Problem Statement

This project aims to develop an Admin Dashboard for managing Telegram Groups using Flask. The dashboard provides various analytics and visualizations to help admins track group engagement, user activity, and content trends.

# Folder Structure

├── logs/

│   ├── app.log

│   ├── error.log

├── app.py

├── config.py

├── analytics.py  # Main code file for analytics logic

├── Dockerfile

├── README.md

├── requirements.txt

└── analytics_dashboard.docx  # Contains analytics descriptions


# How to Run the Project

1. Clone the Repository

git clone repository-url

cd repository-folder

2. Install Dependencies

pip install -r requirements.txt

3. Run Flask Application

python app.py

The app will start at http://127.0.0.1:5000/.

4. Run in Docker (Optional)

Build the Docker image:

docker build -t telegram-dashboard .

Run the container:

docker run -p 5000:5000 telegram-dashboard

Configuration file (config.py)

# Database Configuration

DATABASE_URI = "sqlite:///telegram_groups.db"

# Flask Configuration

DEBUG = True

# Telegram API Configuration

TELEGRAM_API_KEY = "your_telegram_api_key"

TELEGRAM_CHAT_ID = "your_chat_id"

# Logging Configuration

LOG_FILE = "logs/app.log"

ERROR_LOG_FILE = "logs/error.log"

# Other Constants

MAX_ANALYTICS_RESULTS = 100

# Input and Output

Input: Telegram group data (users, messages, activity logs)

Output: JSON API endpoints and dashboard UI displaying analytics

# 30 Analytics/Visualizations Implemented

Total Members - Displays the total number of users in the group.

New Members Over Time - Tracks member growth over different periods.

Member Churn Rate - Identifies the percentage of members leaving.

Total Messages Sent - Analyzes group activity levels.

Most Active Users - Identifies top contributors.

Least Active Users - Highlights inactive members.

Media Shared (Images, Videos, GIFs) - Tracks media-sharing trends.

Most Shared Links - Identifies frequently shared URLs.

Top Hashtags Used - Highlights trending topics.

Admin Actions Taken - Monitors moderation efforts (bans, warnings, mutes).

Peak Activity Hours - Shows the busiest hours for engagement.

Banned Users Count - Tracks moderation actions.

Reported Messages Count - Displays flagged messages for review.

Bot Commands Usage - Analyzes bot interactions within the group.

Number of Polls Created - Monitors poll activity.

Poll Participation Rates - Measures how many users engage with polls.

Emoji and Sticker Usage - Tracks frequently used emojis and stickers.

Group Description Changes - Logs changes to the group's description.

Group Profile Photo Updates - Tracks changes to the group profile picture.

Pinned Messages Count - Counts messages pinned by admins.

Join Requests Received - Monitors user join requests.

Member Invitations Sent - Tracks how many users invite others.

Group Name Changes - Logs modifications to the group title.

User Inactivity Alerts - Flags users who haven't participated recently.

Most Mentioned Users - Highlights influential members.

Message Deletion Trends - Tracks how often messages are removed.

Admin Response Rate - Measures the percentage of admin responses to queries.

Group Growth Rate - Analyzes how fast the group is expanding.

User Engagement Rate - Calculates active participation relative to total members.

User Retention Rate - Shows how many users remain active over time.

# API Endpoints (Sample)

GET /api/total_members

Returns the total number of members in the group.

GET /api/messages_sent

Provides the total count of messages sent in the group.

GET /api/most_active

Lists the most active users based on message activity.

GET /api/media_shared

Returns statistics on media shared, including photos, videos, and documents.

GET /api/engagement_rate

Calculates and provides the user engagement rate in the group.

# Future Enhancements

Add interactive charts with D3.js

Implement role-based access for analytics

Improve sentiment analysis using AI models

