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
- Images with distinct contrash and simple backgrounds
- Portrait or Close-up Images with Clear Contours
- High illumination images

## Images that express a cartoon-like badly
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
