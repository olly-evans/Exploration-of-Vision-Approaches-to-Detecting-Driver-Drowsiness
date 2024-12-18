import os
import cv2
from natsort import natsorted

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

def generate_video(image_directory, landmark_directory, output_video_path):
    '''
    Applies landmarks to frames and writes the frames to a video file.

    This function reads image files from the specified `image_directory`, and corresponding 
    landmarks from the `landmark_directory`. It then overlays the landmarks on the frames and 
    compiles them into a video, which is saved to the specified `output_video_path`.

    :param image_directory: The directory containing the image files (in PNG format) that will be processed.
    :type image_directory: str
    
    :param landmark_directory: The path to the file containing landmark data. Each line in the file represents 
    the landmarks for one frame, with 68 (x, y) coordinate pairs.
    :type landmark_directory: str
    
    :param output_video_path: The path where the output video will be saved. The video is written in AVI format 
    using the XVID codec.
    :type output_video_path: str

    :return: None
    :rtype: None

    :raises FileNotFoundError: If any image or landmark file cannot be read.
    :raises ValueError: If the number of landmarks is less than the number of frames in the images.

    :note: 
    - The images in the `image_directory` should be named in a way that they can be 
    sorted correctly (e.g., numerically).
    - The landmarks file contains data for each frame, with one line of 136 values (68 pairs of 
    x, y coordinates) per frame.
    - If there are more images than landmarks, the function will stop when the landmarks run out.
    - If the video cannot be created, the function will print error messages.
    '''

    landmarks = parse_landmark_file(landmark_directory)
    
    # Images into a list
    image_files = [f for f in os.listdir(image_directory) if f.endswith('.png')]
    
    # Sort the list numerically.
    sorted_image_files = natsorted(image_files)

    i = 0
    # Initialize the video writer (ensure the frame size matches your image resolution)
    first_frame = cv2.imread(os.path.join(image_directory, sorted_image_files[0]))
    if first_frame is None:
        print("Failed to read the first image.")
        return

    # Get the frame dimensions (height, width) and set the video writer
    height, width, _ = first_frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can choose another codec, like 'MJPG' or 'MP4V'
    video_writer = cv2.VideoWriter(output_video_path, fourcc, 30, (width, height))  # 30 FPS

    for img in sorted_image_files:
        if i >= len(landmarks):
            print("Not enough landmarks for all frames!")
            break

        # Get landmarks for frame.
        landmarks_for_frame = landmarks[i]
        # print(landmarks_for_frame)
        # print(len(landmarks_for_frame))

        # Construct the full image path
        img_path = os.path.join(image_directory, img)
        
        print(img_path)
        # Read the frame.
        frame = cv2.imread(img_path)

        if frame is None:
            print(f"Failed to read image: {img}")
            continue
        
        # Apply the landmarks to the frame
        for (x, y) in landmarks_for_frame:
            cv2.circle(frame, (int(x), int(y)), 1, (0, 255, 0), -1) 
        
        # cv2.imwrite(f"frame{i}.png", frame) # Write frame, was testing the landmark match.
        video_writer.write(frame)
        
        # Testing
        # if i == 1000:
        #     break

        i += 1
    video_writer.release()

image_directory = 'C:/Users/evans/OneDrive/Desktop/Vision_DROZY/data/images_i8/1-1/raw_data'
landmark_directory = 'C:/Users/evans/OneDrive/Desktop/Vision_DROZY/data/annotations-auto/1-1-s2.txt'
output_video_path = 'C:/Users/evans/OneDrive/Desktop/Vision_DROZY/data/images_i8/1-1/1-1-annotated.avi'  # Specify the output video file path

generate_video(image_directory, landmark_directory, output_video_path)