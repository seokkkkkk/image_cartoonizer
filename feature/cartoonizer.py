import cv2 as cv
import os

def cartoonize_image(img_path, output_suffix='_cartoonized'):
    # Read the image
    img = cv.imread(img_path)

    # Convert image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Apply median filter
    gray = cv.medianBlur(gray, 5)

    # Detect edges using Laplacian
    edges = cv.Laplacian(gray, cv.CV_8U, ksize=5)
    edges = 255 - edges

    # Apply bilateral filter to reduce the color palette
    color = cv.bilateralFilter(img, 9, 300, 300)

    # Combine the edges and color
    cartoon = cv.bitwise_and(color, color, mask=edges)

    # Prepare to display the original and cartoonized images side by side
    combined = cv.hconcat([img, cartoon])

    # Save the cartoonized image
    base, extension = os.path.splitext(img_path)
    output_path = f"{base}{output_suffix}{extension}"
    cv.imwrite(output_path, cartoon)

    # Display the original and cartoonized images in one window
    cv.imshow("Original and Cartoonized Image", combined)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Example usage
cartoonize_image('/Users/seok/IdeaProjects/ImageCartoonizer/images/image.jpg')