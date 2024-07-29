import cv2
import os

# Function to extract frames
def extract_frames(video_path, output_folder, interval):
    # Get the video file name without extension
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Get the frame rate of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Calculate the interval in terms of frames
    frame_interval = int(fps * interval)
    
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    frame_count = 0
    saved_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break
        
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"{video_name}_frame_{saved_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1
        
        frame_count += 1
    
    cap.release()
    print(f"Extracted {saved_count} frames.")

# Path to the video file
video_path = '/home/achintya-trn0175/Desktop/DATA/output_video.mp4'


# Output folder for the frames
output_folder = 'extracted_frames_traffic'

# Interval in seconds
interval = 1

# Extract frames
extract_frames(video_path, output_folder, interval)
