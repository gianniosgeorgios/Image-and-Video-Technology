# Image-and-Video-Technology

The main purpose of the first exercise was to construct code for Image Cartoonification. The input images (.jpg)  are people's faces in the dimension of 512 x 288 pixels.

![input](https://user-images.githubusercontent.com/50829499/111067665-fd6eef00-84cd-11eb-9af7-3d8f1d7dfad2.png)


First we add Noise to these Images, so as to increase variability. The noise is either:

- Gaussian 
- Salt and Pepper

![add_noise](https://user-images.githubusercontent.com/50829499/111067639-de705d00-84cd-11eb-8f23-22f33549322a.png)

Then we apply filtering to these images in order to reduce noise. The types of filtering that were studied, are: 

- Gaussian Filtering
- Mean Filtering
- Median Filtering

![filtering](https://user-images.githubusercontent.com/50829499/111067936-3360a300-84cf-11eb-99d4-54e0790558b0.png)

Now are ready to detect the edges in filtered images. The methods for Edge Detection were:

- Laplacian 
- Canny 
- Marr - Hildreth 

![detection](https://user-images.githubusercontent.com/50829499/111067939-39ef1a80-84cf-11eb-9cdc-f075896c022d.png)

After all, the final result was:

![final](https://user-images.githubusercontent.com/50829499/111067838-b0d7e380-84ce-11eb-87ac-b2d53825eec3.png)


