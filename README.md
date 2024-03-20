# Image Cartoonizer

An application that makes images cartoon-like using Python and OpenCV.

## Development Environment
- **Python Version:** 3.9.6
- **OpenCV Version:** 4.9.0

## Features

### Cartoonize an Image
The application can convert an image to a cartoon-like version of itself.

## Principle

### Gray Scale Conversion
Convert the image to a gray scale version. This is done to simplify the image and reduce the number of colors.

### Median Blur
Reduce noise without significantly reducing the edges in the image.

### Laplacian Edge Detection
Highlight the edges in the image.
if ksize is bigger, the edges will be more visible.

### Bilateral Filter
Smooth the image while keeping the edges sharp.

### Combining Edges with Color
Combine the edges with the color to create a cartoon-like effect.

## Images that express a cartoon-like well

![1_combined](https://github.com/seokkkkkk/image_cartoonizer/assets/66684504/298d6e86-34d0-4e1c-9b54-4cbc99932158)

![6_combined](https://github.com/seokkkkkk/image_cartoonizer/assets/66684504/35529e59-fd4f-4754-bf74-56193aff1c13)

- Images with distinct contrash and simple backgrounds
- Portrait or Close-up Images with Clear Contours
- High illumination images


## Images that express a cartoon-like badly

![5_combined](https://github.com/seokkkkkk/image_cartoonizer/assets/66684504/33e26d82-e2b6-4b60-9004-7ef84a8dbba6)

![2_combined](https://github.com/seokkkkkk/image_cartoonizer/assets/66684504/d494ebd7-f1a6-4cff-9b99-cc0b77af1422)

- Images with low light or high noise
- Images with many details and complex textures
- Images with complex backgrounds


## Limitations
- loss of details
- sensitivity of parameters for different images
- edge detection is not perfect
- the result is not always a cartoon-like image

## Installation

To run this application, ensure you have Python 3.9.6 and OpenCV 4.9.0 installed. Clone this repository, navigate to the project directory, and execute the main script. Please note that operation on versions other than Python 3.9.6 and OpenCV 4.9.0 is not guaranteed.
