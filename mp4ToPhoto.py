import cv2
import os

video_path = 'C:\\Users\\ZJendex\\Pictures\\Camera Roll\\WIN_20250703_11_48_15_Pro.mp4'
output_folder = 'output_frames'
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = int(fps)  # 每秒提取一帧

frame_idx = 0
saved_idx = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_idx % frame_interval == 0:
        filename = os.path.join(output_folder, f"frame_{saved_idx:04d}.png")
        cv2.imwrite(filename, frame)
        saved_idx += 1
    frame_idx += 1

cap.release()
print(f"Saved {saved_idx} frames at 1Hz to '{output_folder}'")
