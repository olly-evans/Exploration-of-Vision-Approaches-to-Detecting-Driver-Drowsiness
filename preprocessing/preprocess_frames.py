import cv2
import os

# Get path.
video_path = os.path.join('C:\\', 'Users', 'evans', 'OneDrive', 'Desktop', 'DROZY', 'data', 'videos_i8', '1-1.mp4')

# Load video from path.
video = cv2.VideoCapture(video_path)
# Check if video is opened.
if not video.isOpened(): 
    print("Error: Could not open video.")


fps = video.get(cv2.CAP_PROP_FPS)
totalFrames = video.get(cv2.CAP_PROP_FRAME_COUNT)

frameIterations = 1
while True:
    # Set the video to desired frame.
    video.set(cv2.CAP_PROP_POS_FRAMES, frameIterations)
    ret, frame = video.read()

    if not ret:
        break
    
    print(f"Writing frame {frameIterations}...")

    # Generate a unique filename for each frame
    output_filename = f"1-1-{frameIterations:0d}.png"
    output_path = os.path.join('C:\\', 'Users', 'evans', 'OneDrive', 'Desktop', 'DROZY', 'data', '1-1', output_filename)

    # Save the frame as a PNG file
    cv2.imwrite(output_path, frame)

    frameIterations += 1

    # Okay now do it for every video.