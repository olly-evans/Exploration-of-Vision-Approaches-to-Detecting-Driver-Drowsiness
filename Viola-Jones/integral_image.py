import numpy as np

'''
Integral Image calculation file.
'''

def compute_integral_image(image_arr):
    # Create new array for integral.
    # Tuple, (x, y) where x and y are rows and cols.
    row_sum = np.zeros(image_arr.shape)
    
    # Additional row to simplify boundary conditions and indexing.
    integral_image_arr = np.zeros((image_arr.shape[0] + 1, image_arr.shape[1] + 1))

    # Loop through each pixel in the image
    for i in range(image_arr.shape[0]):  
        for j in range(image_arr.shape[1]):  
            # Update row-wise cumulative sum
            row_sum[i, j] = row_sum[i, j - 1] + image_arr[i, j] if j > 0 else image_arr[i, j]
            
            # Update integral image with row_sum and the value from the row above
            integral_image_arr[i + 1, j + 1] = integral_image_arr[i, j + 1] + row_sum[i, j]

    # Print the resulting integral image (excluding the padding)
    # print(integral_image_arr[1:, 1:])

    pass

def sum_region(integral_image_array, top_left, bottom_right):
    '''
    Calculates the sum in the rectangle specified using its top
    left and bottom right coordinate.

    :param integral_image_array
    :type numpy.ndarray

    :param top_left: (x,y) of rectangles top left corner
    :type (int, int)

    :param bottom_right: (x,y) of rectangles bottom right corner.
    :type bottom_right: (int, int)

    :return The sum of all pixels in a given rectangle.
    :rtype int
    '''
    pass

array_dir = 'C:/Users/evans/OneDrive/Desktop/Vision_DROZY/data/images_i8/1-1/npy_arrays/1-1-0.npy'

array = np.load(array_dir)

print(array[100:105, 100:105])
compute_integral_image(array[100:105, 100:105])

