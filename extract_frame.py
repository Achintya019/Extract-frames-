import os
import cv2
import random
import string
from yt_dlp import YoutubeDL

def get_video_stream_url(url):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict['url']
        video_title = info_dict.get('title', '').replace(' ', '_')
    return video_url, video_title

def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def extract_frames(video_url, title, output_folder, frame_interval=60):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    random_folder = generate_random_string()
    video_folder = f"yt-{title}/{random_folder}"
    full_output_path = os.path.join(output_folder, video_folder)
    if not os.path.exists(full_output_path):
        os.makedirs(full_output_path)

    cap = cv2.VideoCapture(video_url)
    frame_count = 0
    success = True
    
    while success:
        success, frame = cap.read()
        if frame_count % frame_interval == 0 and success:
            image_name = f"{title}_{random_folder}_{frame_count}.jpg"
            image_path = os.path.join(full_output_path, image_name)
            cv2.imwrite(image_path, frame)
        frame_count += 1
    
    cap.release()

def process_videos(video_urls, output_folder, frame_interval=60):
    for url in video_urls:
        video_url, title = get_video_stream_url(url)
        extract_frames(video_url, title, output_folder, frame_interval)

# List of YouTube video URLs
video_urls = [
    "https://www.youtube.com/watch?v=2BqWhDQskXE"
]

output_folder = 'extracted_frames'
frame_interval = 60  # Extract one frame every 60 frames

process_videos(video_urls, output_folder, frame_interval)
