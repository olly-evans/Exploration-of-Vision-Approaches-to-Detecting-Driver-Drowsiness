import os
import cv2

def parse_landmark_file(file_path):
    """
    Parse the landmark data file and return the landmarks for each frame.
    :param file_path: Path to the file containing landmark data.
    :return: A list of frames, where each frame contains 68 (x, y) tuples.
    """
    frames = []
    with open(file_path, 'r') as f:
        for line in f:
            # Split the line by spaces and convert each item to float
            landmarks = list(map(float, line.split()))
            # Group the landmarks into (x, y) tuples (68 pairs of coordinates)
            frame_landmarks = [(landmarks[i], landmarks[i + 1]) for i in range(0, len(landmarks), 2)]
            frames.append(frame_landmarks)
    return frames

def generate_video_with_landmarks(image_folder, landmark_file, output_video, fps=30):
    """
    Generate a video with landmarks drawn on each frame.
    :param image_folder: Folder containing the raw images.
    :param landmark_file: File containing landmarks for each frame.
    :param output_video: Path for the output video file.
    :param fps: Frames per second for the video.
    """
    print(f"Loading images from folder: {image_folder}")
    print(f"Parsing landmark file: {landmark_file}")

    # Parse landmark file
    landmarks_data = parse_landmark_file(landmark_file)
    print(f"Parsed {len(landmarks_data)} frames.")

    # Get image file names (assume they are already sorted correctly)
    image_files = [img for img in os.listdir(image_folder) if img.endswith(('.jpg', '.png', '.jpeg'))]
    if len(image_files) != len(landmarks_data):
        print("Error: Mismatch between number of images and landmarks.")
        return

    # Read the first image to get the frame dimensions
    first_image_path = os.path.join(image_folder, image_files[0])
    frame = cv2.imread(first_image_path)
    height, width, _ = frame.shape

    # Initialize video writer
    print(f"Initializing video writer for: {output_video}")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    # Process each image
    print("Processing frames and adding landmarks...")
    for img_file, landmarks in zip(image_files, landmarks_data):
        img_path = os.path.join(image_folder, img_file)
        frame = cv2.imread(img_path)

        # Draw landmarks
        for x, y in landmarks:
            cv2.circle(frame, (int(x), int(y)), 2, (0, 255, 0), -1)

        # Add frame to video
        video_writer.write(frame)

    # Release video writer
    video_writer.release()
    print(f"Video saved as {output_video}")


# Paths and parameters
image_folder = r'C:\Users\evans\OneDrive\Desktop\Vision_DROZY\data\images_i8\1-1\raw_data'
landmark_file = r'C:\Users\evans\OneDrive\Desktop\Vision_DROZY\data\annotations-auto\1-1-s2.txt'
output_video = r'C:\Users\evans\OneDrive\Desktop\Vision_DROZY\data\output_video.avi'

# Generate video
generate_video_with_landmarks(image_folder, landmark_file, output_video, fps=30)
