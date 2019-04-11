# CROS-SEARCH WITH HOG 
## HISTOGRAM OF ORIENTED GRAPHS
Extracts the features of all the pictures in the file named "images" via HOG Feature Descriptor using OpenCV. Saves all of those files in a .npy file. This .npy file is used as a database for keeping the feature descriptors of the pictures in the "images" file. The data that is kept in the .npy file is later compared to to the features of the desired image (the image that the user wants to search).
## Comparison
### Cros-Search
The images are queried to consequtive images. The features of each image is queried to one another. This creates a two dimentinal query making this comparison method as robust and fast as posssible. The names of the images are reordered after the comparison of their feature vectors. The most similar picture in the "images" file is returned. A .csv file is created to indicate the order of similarity of all of the pictures to the image that the user wants to search.
