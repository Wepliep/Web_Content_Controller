import feedparser
import requests

def send_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=payload)
    print(response.json())

def check_for_new_entries(feed_url, last_entry_id):
    feed = feedparser.parse(feed_url)
    latest_entry_id = feed.entries[0].id

    if latest_entry_id != last_entry_id:
        title = feed.entries[0].title
        link = feed.entries[0].link
        published = feed.entries[0].published
        message = f"{title}\n{link}\n{published}"
        return latest_entry_id, message
    else:
        return last_entry_id, None

def save_last_entry_ids(last_entry_ids):
    with open("last_entry_ids.txt", "w") as f:
        for entry_id in last_entry_ids:
            f.write(f"{entry_id}\n")

def load_last_entry_ids():
    last_entry_ids = []
    try:
        with open("last_entry_ids.txt", "r") as f:
            for line in f:
                last_entry_ids.append(line.strip())
    except FileNotFoundError:
        pass
    return last_entry_ids

def main():
    bot_token = "BOT_TOKEN"
    chat_id = "CHAT_ID"
    feed_urls = [
        "https://techcrunch.com/feed/",
        "https://feeds.feedburner.com/venturebeat/SZYF",
        "https://feeds.feedburner.com/TheHackersNews",
        "https://feeds.feedburner.com/securityweek",
        "https://threatpost.com/feed/",
        "https://www.darkreading.com/rss.xml"
    ]

    last_entry_ids = load_last_entry_ids()

    while len(last_entry_ids) < len(feed_urls):
        last_entry_ids.append(None)

    for i, feed_url in enumerate(feed_urls):
        last_entry_id = last_entry_ids[i]
        latest_entry_id, message = check_for_new_entries(feed_url, last_entry_id)
        if message:
            send_message(bot_token, chat_id, message)
            last_entry_ids[i] = latest_entry_id

    save_last_entry_ids(last_entry_ids)
if __name__ == "__main__":
    main()
