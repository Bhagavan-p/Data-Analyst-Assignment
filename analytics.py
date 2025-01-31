import logging
import requests
from collections import defaultdict
from datetime import datetime, timedelta
from config import TELEGRAM_API_KEY, chat_id_key

# Configure logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_analytics_data():
    try:
        # 🔹 Telegram Bot API Token and Chat ID
        api_token = TELEGRAM_API_KEY
        chat_id = chat_id_key

        # 🔹 Fetch Total Group Members
        response = requests.get(f"https://api.telegram.org/bot{api_token}/getChatMembersCount?chat_id={chat_id}")
        total_members = response.json().get("result", 0)

        # 🔹 Fetch Chat Administrators
        response = requests.get(f"https://api.telegram.org/bot{api_token}/getChatAdministrators?chat_id={chat_id}")
        admins = response.json().get("result", [])

        # 🔹 Fetch Updates (Messages)
        response = requests.get(f"https://api.telegram.org/bot{api_token}/getUpdates")
        updates = response.json().get("result", [])

        # 🔹 Initialize Data Structures
        new_members = 0
        members_left = 0
        banned_users_count = 0
        messages_sent = 0
        most_active_users = defaultdict(int)
        least_active_users = defaultdict(int)
        media_shared = {"photos": 0, "videos": 0, "documents": 0}
        most_shared_links = []
        top_hashtags = []
        admin_actions = {"bans": 0, "mutes": 0, "deletions": 0}
        message_timestamps = []
        reported_messages = 0
        bot_commands_usage = defaultdict(int)
        polls_created = 0
        polls_participation = 0
        stickers_emojis_usage = 0
        group_description_changes = 0
        group_photo_changes = 0
        pinned_messages_count = 0
        join_requests = 0
        member_invitations = 0
        group_title_changes = 0
        user_inactivity_alerts = []
        most_mentioned_users = defaultdict(int)
        message_deletion_rate = 0
        admin_response_rate = 0
        group_growth_rate = 0
        user_engagement_rate = 0
        user_retention_rate = 0
        spam_message_count = 0
        group_event_participation = 0

        # 🔹 Process Updates
        for update in updates:
            if "message" in update:
                msg = update["message"]
                messages_sent += 1
                user_id = msg.get("from", {}).get("id")
                if user_id:
                    most_active_users[user_id] += 1

                # Track Media Shared
                if "photo" in msg:
                    media_shared["photos"] += 1
                if "video" in msg:
                    media_shared["videos"] += 1
                if "document" in msg:
                    media_shared["documents"] += 1

                # Track Links and Hashtags
                if "text" in msg:
                    text = msg["text"]
                    if "http" in text:
                        most_shared_links.append(text)
                    if "#" in text:
                        top_hashtags.extend([word for word in text.split() if word.startswith("#")])

                # Track Bot Commands
                if "entities" in msg:
                    for entity in msg["entities"]:
                        if entity.get("type") == "bot_command":
                            bot_commands_usage[msg["text"]] += 1

                # Track Stickers and Emojis
                if "sticker" in msg or any(char in msg.get("text", "") for char in ["😀", "😂", "❤️"]):
                    stickers_emojis_usage += 1

                # Track Message Timestamps
                message_timestamps.append(msg.get("date", 0))

                # Track Reported Messages
                if "reply_to_message" in msg and "report" in msg.get("text", "").lower():
                    reported_messages += 1

                # Track Most Mentioned Users
                if "entities" in msg:
                    for entity in msg["entities"]:
                        if entity.get("type") == "mention":
                            mentioned_user = msg["text"][entity["offset"]:entity["offset"] + entity["length"]]
                            most_mentioned_users[mentioned_user] += 1

            # Track Admin Actions
            if "new_chat_members" in update.get("message", {}):
                new_members += 1
            if "left_chat_member" in update.get("message", {}):
                members_left += 1
            if "pinned_message" in update.get("message", {}):
                pinned_messages_count += 1
            if "delete_chat_photo" in update.get("message", {}):
                group_photo_changes += 1
            if "new_chat_title" in update.get("message", {}):
                group_title_changes += 1
            if "new_chat_description" in update.get("message", {}):
                group_description_changes += 1

        # 🔹 Calculate Derived Metrics
        # Peak Activity Times
        message_timestamps = [datetime.fromtimestamp(ts) for ts in message_timestamps if ts > 0]
        hourly_activity = defaultdict(int)
        for ts in message_timestamps:
            hourly_activity[ts.hour] += 1
        peak_activity_times = [f"{hour}:00" for hour, count in sorted(hourly_activity.items(), key=lambda x: x[1], reverse=True)]

        # Most Active Users
        most_active_users = sorted(most_active_users.items(), key=lambda x: x[1], reverse=True)[:10]

        # Least Active Users
        least_active_users = sorted(least_active_users.items(), key=lambda x: x[1])[:10]

        # Top Hashtags
        top_hashtags = sorted(top_hashtags, key=lambda x: top_hashtags.count(x), reverse=True)[:10]

        # Most Mentioned Users
        most_mentioned_users = sorted(most_mentioned_users.items(), key=lambda x: x[1], reverse=True)[:10]

        # Group Growth Rate
        group_growth_rate = ((new_members - members_left) / total_members) * 100 if total_members > 0 else 0

        # User Engagement Rate
        user_engagement_rate = (messages_sent / total_members) * 100 if total_members > 0 else 0

        # User Retention Rate
        user_retention_rate = ((total_members - members_left) / total_members) * 100 if total_members > 0 else 0

        # Admin Response Rate
        admin_response_rate = (reported_messages / messages_sent) * 100 if messages_sent > 0 else 0

        # Message Deletion Rate
        message_deletion_rate = (admin_actions["deletions"] / messages_sent) * 100 if messages_sent > 0 else 0

        # 🔹 Prepare Final Data
        data = {
            "total_members": total_members,
            "new_members": new_members,
            "members_left": members_left,
            "messages_sent": messages_sent,
            "most_active_users": most_active_users,
            "least_active_users": least_active_users,
            "media_shared": media_shared,
            "most_shared_links": most_shared_links,
            "top_hashtags": top_hashtags,
            "admin_actions": admin_actions,
            "peak_activity_times": peak_activity_times,
            "banned_users_count": banned_users_count,
            "reported_messages": reported_messages,
            "bot_commands_usage": bot_commands_usage,
            "polls_created": polls_created,
            "polls_participation": polls_participation,
            "stickers_emojis_usage": stickers_emojis_usage,
            "group_description_changes": group_description_changes,
            "group_photo_changes": group_photo_changes,
            "pinned_messages_count": pinned_messages_count,
            "join_requests": join_requests,
            "member_invitations": member_invitations,
            "group_title_changes": group_title_changes,
            "user_inactivity_alerts": user_inactivity_alerts,
            "most_mentioned_users": most_mentioned_users,
            "message_deletion_rate": message_deletion_rate,
            "admin_response_rate": admin_response_rate,
            "group_growth_rate": group_growth_rate,
            "user_engagement_rate": user_engagement_rate,
            "user_retention_rate": user_retention_rate,
        }
        logging.info("Analytics data generated successfully.")
        return data
    except Exception as e:
        logging.error(f"Error generating analytics data: {e}")
        return {}