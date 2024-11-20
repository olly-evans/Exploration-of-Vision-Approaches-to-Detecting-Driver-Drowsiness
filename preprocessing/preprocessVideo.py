import cv2
import os

# Path to videos.
video_directory = 'C:/Users/evans/OneDrive/Desktop/Vision_DROZY/data/videos_i8/'

videos = 1
# Iterate through each file in the directory
for filename in os.listdir(video_directory):
    # Videos in directory to process.
    if videos == 3:
        break
    # Check if the file is a video by checking its extension
    if filename.endswith('.mp4'):
        video_path = os.path.join(video_directory, filename)
        print("Processing video:", video_path)

        # Load video from path.
        video = cv2.VideoCapture(video_path)
        # Check if video is opened.
        if not video.isOpened(): 
            print("Error: Could not open video.")

        # Extract filename only. (no .mp4)
        filenameOnly = os.path.splitext(filename)[0]
        print(filenameOnly)

        # Create a new directory for this video
        output_dir = os.path.join('C:\\', 'Users', 'evans', 'OneDrive', 'Desktop', 'Vision_DROZY', 'data', 'images_i8', filenameOnly)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created directory: {output_dir}")
        
        frameIterations = 0
        while True:
            # Set the video to desired frame.
            video.set(cv2.CAP_PROP_POS_FRAMES, frameIterations)
            ret, frame = video.read()

            if not ret:
                break
            
            print(f"Video: {filename} Frame: {frameIterations}...")

            # Generate a unique filename for each frame
            output_filename = f"{filenameOnly}-{frameIterations}.png"
            output_path = os.path.join(output_dir, output_filename)

            # Save the frame as a PNG file
            cv2.imwrite(output_path, frame)
            
            # Iterate.
            frameIterations += 1

        videos += 1
    # maybe don't add the massive fucking giles