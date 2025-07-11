import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from caption_bank import get_caption
from instagrapi import Client
import time

# Instagram Login
cl = Client()
USERNAME = "iot.device"
PASSWORD = "mistuu@321"

try:
    cl.login(USERNAME, PASSWORD)
    print("✅ Logged in successfully!")
except Exception as e:
    print("❌ Login failed:", e)
    exit()

# Upload function
def upload_post(video_path, caption):
    try:
        print(f"📤 Uploading: {video_path}")
        print(f"📝 Caption: {caption}")
        cl.clip_upload(video_path, caption)
        print("✅ Uploaded successfully!")
    except Exception as e:
        print("❌ Upload failed:", e)

# Scheduling posts from Excel
def schedule_posts():
    try:
        df = pd.read_excel("upload_schedule.xlsx", engine='openpyxl')
    except Exception as e:
        print(" Failed to read Excel:", e)
        return

    scheduler = BackgroundScheduler()

    for _, row in df.iterrows():
        video_path = row['video_path']
        post_time = pd.to_datetime(row['upload_time'])
        category = row.get('category', 'motivation')
        caption = get_caption(category) if row['caption'] == "auto" else row['caption']

        print(f"📅 Scheduling post: {video_path} at {post_time}")
        scheduler.add_job(upload_post, 'date', run_date=post_time, args=[video_path, caption])

    scheduler.start()
    print("🚀 Agent is running... Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(10)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print(" Agent stopped.")

if __name__ == "__main__":
    schedule_posts()
