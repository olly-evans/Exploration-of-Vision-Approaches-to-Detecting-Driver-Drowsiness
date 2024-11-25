import cv2
import os
import numpy as np

def process_video(video_path, output_base_dir):
    """
    Processes a video by extracting frames and saving them as PNG images, 
    NumPy arrays, and their corresponding integral images in an organized 
    directory structure.

    This function is intended to reduce preprocessing time by precomputing 
    data for further use in models. It supports grayscale frames and stores 
    the results in separate folders for raw data (PNGs), NumPy arrays, and 
    integral images.

    :param video_path: Path to the video file to be processed.
    :type video_path: str
    :param output_base_dir: Directory where the processed data will be stored. 
    The function creates subfolders for each type of data.
    :type output_base_dir: str

    :return: None
    :rtype: None
    """

    # Extract video name without extension
    filename_only = os.path.splitext(os.path.basename(video_path))[0]
    print(f"Processing video: {filename_only}")

    # Create base directory for the video
    output_dir = os.path.join(output_base_dir, filename_only)
    os.makedirs(output_dir, exist_ok=True)

    # Create subdirectories for raw PNGs, NumPy arrays, and integral images
    raw_data_dir = os.path.join(output_dir, "raw_data")
    npy_array_dir = os.path.join(output_dir, "npy_arrays")
    integral_image_dir = os.path.join(output_dir, "integral_images")

    os.makedirs(raw_data_dir, exist_ok=True)
    os.makedirs(npy_array_dir, exist_ok=True)
    os.makedirs(integral_image_dir, exist_ok=True)

    print(f"Saving raw PNGs to: {raw_data_dir}")
    print(f"Saving NumPy arrays to: {npy_array_dir}")
    print(f"Saving integral images to: {integral_image_dir}")

    # Load the video
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Error: Could not open video.")
        return

    # Initialise frame counter
    frame_iterations = 0

    while True:
        # Read a frame
        ret, frame = video.read()
        if not ret:
            break

        # Check if frame is already grayscale
        if len(frame.shape) == 3:  # If it's a color image
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Generate filenames
        raw_png_filename = f"{filename_only}-{frame_iterations}.png"
        npy_array_filename = f"{filename_only}-{frame_iterations}.npy"
        integral_image_filename = f"{filename_only}-integral-{frame_iterations}.npy"

        # Full paths for saving
        raw_png_path = os.path.join(raw_data_dir, raw_png_filename)
        npy_array_path = os.path.join(npy_array_dir, npy_array_filename)
        integral_image_path = os.path.join(integral_image_dir, integral_image_filename)

        # Save the raw frame as PNG
        cv2.imwrite(raw_png_path, frame)

        # Save the grayscale frame as a NumPy array
        np.save(npy_array_path, frame.astype(np.uint8))  # Ensure data type is uint8

        '''
        Want to write my own integral algorithm, will test against this OpenCV
        implementation.
        '''
        integral_image = cv2.integral(frame)[1:, 1:]  # Exclude the zero-padding
        np.save(integral_image_path, integral_image)

        frame_iterations += 1

        # Log progress every 1000 frames
        if frame_iterations % 1000 == 0:
            print(f"Processed {frame_iterations} frames...")

    print(f"Finished processing video: {filename_only}, total frames: {frame_iterations}")

    # Release resources
    video.release()

if __name__ == "__main__":
    # Specify the base directories for videos and output
    video_directory = 'C:/Users/evans/OneDrive/Desktop/Vision_DROZY/data/videos_i8/'
    output_base_dir = 'C:/Users/evans/OneDrive/Desktop/Vision_DROZY/data/images_i8/'

    # Get the list of video files
    video_files = [f for f in os.listdir(video_directory) if f.endswith('.mp4')]
    if not video_files:
        print("No videos found in the directory.")
    else:
        print("Available videos:")
        for i, video_name in enumerate(video_files):
            print(f"[{i}] {video_name}")

        # Ask the user to select a video
        video_index = int(input(f"Select the video to process (0-{len(video_files) - 1}): "))
        if 0 <= video_index < len(video_files):
            video_path = os.path.join(video_directory, video_files[video_index])
            process_video(video_path, output_base_dir)
        else:
            print("Invalid selection. Exiting.")
