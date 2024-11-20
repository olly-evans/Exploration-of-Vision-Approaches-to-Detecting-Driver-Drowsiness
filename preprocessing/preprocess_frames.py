from PIL import Image
import numpy as np

# Path to videos.
image_directory = 'C:/Users/evans/OneDrive/Desktop/Vision_DROZY/data/images_i8/'

# for folder in images_i8
    # convert each image to a np.array
    # save np.array somehow.
    
def imgToArr(imagePath):
    """
    Converts a PNG image into a NumPy array.

    rtype: 
    """

    try:
        # Open the image.
        image = Image.open(imagePath)
        
        # Convert the image to a NumPy array.
        return np.array(image)
    except Exception as e:
        print(f"Error converting image to NumPy array: {e}")
        return None




# # Get path.
# video_path = os.path.join('C:\\', 'Users', 'evans', 'OneDrive', 'Desktop', 'DROZY', 'data', 'videos_i8', '1-1.mp4')

# # Load video from path.
# video = cv2.VideoCapture(video_path)
# # Check if video is opened.
# if not video.isOpened(): 
#     print("Error: Could not open video.")


# fps = video.get(cv2.CAP_PROP_FPS)
# totalFrames = video.get(cv2.CAP_PROP_FRAME_COUNT)

# frameIterations = 1
# while True:
#     # Set the video to desired frame.
#     video.set(cv2.CAP_PROP_POS_FRAMES, frameIterations)
#     ret, frame = video.read()

#     if not ret:
#         break
    
#     print(f"Writing frame {frameIterations}...")

#     # Generate a unique filename for each frame
#     output_filename = f"1-1-{frameIterations:0d}.png"
#     output_path = os.path.join('C:\\', 'Users', 'evans', 'OneDrive', 'Desktop', 'DROZY', 'data', '1-1', output_filename)

#     # Save the frame as a PNG file
#     cv2.imwrite(output_path, frame)

#     frameIterations += 1