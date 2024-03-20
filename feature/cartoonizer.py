import cv2 as cv
import os

def cartoonize_image(img_path, output_folder, output_suffix='_cartoonized'):
    # Read the image
    img = cv.imread(img_path)
    if img is None:
        return None, None

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

    # Save the cartoonized image
    base, _ = os.path.splitext(os.path.basename(img_path))
    output_path = os.path.join(output_folder, f"{base}{output_suffix}.png")
    cv.imwrite(output_path, cartoon)

    return img, cartoon

def cartoonize_images_in_folder(input_folder, output_folder, output_suffix='_cartoonized'):
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if os.path.isfile(file_path):
            try:
                original, cartoonized = cartoonize_image(file_path, output_folder, output_suffix)
                if original is not None and cartoonized is not None:
                    # Combine the original and cartoonized image for display
                    combined = cv.hconcat([original, cartoonized])
                    # Save the combined image
                    combined_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_combined.png")
                    cv.imwrite(combined_path, combined)
                    # Display the combined image
                    cv.imshow("Original and Cartoonized Image", combined)
                    cv.waitKey(0)  # Wait for any key to be pressed
                    cv.destroyAllWindows()  # Close the display window
                    print(f"Combined image saved and displayed: {combined_path}")
            except Exception as e:
                print(f"Failed to cartoonize {file_path}: {e}")

# 경로 설정 (실제 경로로 수정 필요)
input_folder = '/Users/seok/IdeaProjects/ImageCartoonizer/images'
output_folder = '/Users/seok/IdeaProjects/ImageCartoonizer/results'
cartoonize_images_in_folder(input_folder, output_folder)
