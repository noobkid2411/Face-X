import cv2
import os 
import numpy as np
import matplotlib.pyplot as plt
  
def applygauss(classPath):
    ''' 
      Applies Gaussian Filter to all the images in the given folder. 
      Args : 
        classPath : (string) directory containing images for a particular class.
    '''
    try:
      os.mkdir(classPath+"/Gaussian_Filtered_Images")    
    
    except Exception as e:
      print(f"Cannot create directory with given name due to: {e}")
      pass

    for image in list(os.listdir(classPath)):
      # Read image
      img = cv2.imread(classPath + "/" + image)

      if img is not None:
        # applying Gaussian filter
        gaussian = cv2.GaussianBlur(img,(5,5),0)
        
        # saving the image.
        cv2.imwrite(classPath+"/Gaussian_Filtered_Images/gaussian"+image, gaussian)
image1=input("Enter folder path for gaussian smoothening:")
applygauss(image1) 