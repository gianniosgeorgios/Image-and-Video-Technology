# Image-and-Video-Technology

The main purpose of the first exercise was to construct code for Image Cartoonification. The input images (.jpg)  are people's faces in the dimension of 512 x 288 pixels. Below you can see an example of two people's faces:

![input](https://user-images.githubusercontent.com/50829499/111068018-96ead080-84cf-11eb-8237-78ce4f8602d6.png)


First we add Noise to these Images, so as to increase variability. The noise is either:

- Gaussian: It is statistical noise having a probability density function (PDF) equal to that of the normal distribution
- Salt and Pepper:  This noise can be caused by sharp and sudden disturbances in the image signal. It presents itself as sparsely occurring white and black pixels.

![add_noise](https://user-images.githubusercontent.com/50829499/111067639-de705d00-84cd-11eb-8f23-22f33549322a.png)

Then we apply filtering to these images in order to reduce noise. The types of filtering that were studied, are: 

- Gaussian Filtering: Filter whose impulse response is a Gaussian function 
- Mean Filtering: Replacing each pixel value in an image with the mean (average) value of its neighbors, including itself.
- Median Filtering:  Rplacing each entry with the median of neighboring entries

![filtering](https://user-images.githubusercontent.com/50829499/111067936-3360a300-84cf-11eb-99d4-54e0790558b0.png)

Now are ready to detect the edges in filtered images. The methods for Edge Detection were:

- Laplacian:  The Laplacian is a 2-D isotropic measure of the 2nd spatial derivative of an image. The Laplacian of an image highlights regions of rapid intensity change and is therefore often used for edge detection 
- Canny: After applying gaussian filtering, find the intensity gradients of the image. Then apply gradient magnitude thresholding or lower bound cut-off suppression to get rid of spurious response to edge detection
- Marr - Hildreth: Convolving the image with the Laplacian of the Gaussian function

![detection](https://user-images.githubusercontent.com/50829499/111067939-39ef1a80-84cf-11eb-9cdc-f075896c022d.png)

After all, the final result was:

![final](https://user-images.githubusercontent.com/50829499/111067838-b0d7e380-84ce-11eb-87ac-b2d53825eec3.png)


