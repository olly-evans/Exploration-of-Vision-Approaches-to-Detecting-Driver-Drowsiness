import cv2
import os

def process_video(video_path, output_base_dir):
    # Extract video name without extension
    filename_only = os.path.splitext(os.path.basename(video_path))[0]
    print(f"Processing video: {filename_only}")

    # Create a directory for the video frames
    output_dir = os.path.join(output_base_dir, filename_only)
    os.makedirs(output_dir, exist_ok=True)
    print(f"Saving frames to: {output_dir}")

    # Load the video
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Error: Could not open video.")
        return

    # Initialize frame counter
    frame_iterations = 0

    while True:
        # Read a frame
        ret, frame = video.read()
        if not ret:
            break

        # Create subdirectories for every 1000 frames
        batch_dir = os.path.join(output_dir, f"batch_{frame_iterations // 1000}")
        os.makedirs(batch_dir, exist_ok=True)

        # Generate output file path
        output_filename = f"{filename_only}-{frame_iterations}.png"
        output_path = os.path.join(batch_dir, output_filename)

        # Save the frame as a PNG
        cv2.imwrite(output_path, frame)

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
