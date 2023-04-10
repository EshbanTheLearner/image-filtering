import cv2
import matplotlib.pyplot as plt

def load_image(path, to_color=False):
    image = cv2.imread(path)
    if to_color:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def show_image(image):
    plt.figure(figsize=(11, 6))
    plt.imshow(image)
    plt.title("Image")
    plt.xticks([])
    plt.yticks([])
    plt.show()

def plot_comparison(original, filtered, filter_name="Filtered"):
    plt.figure(figsize=(11, 6))
    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(original, cv2.COLOR_HSV2RGB)), plt.title("Original")
    plt.xticks([]), plt.yticks([])
    plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(filtered, cv2.COLOR_HSV2RGB)), plt.title(f"{filter_name}")
    plt.xticks([]), plt.yticks([])
    plt.show()

def plot_comparison_grayscale(original, filtered, filter_name="Filtered"):
    plt.figure(figsize=(11, 6))
    plt.subplot(1, 2, 1), plt.imshow(original, cmap="gray"), plt.title("Original")
    plt.xticks([]), plt.yticks([])
    plt.subplot(1, 2, 2), plt.imshow(filtered, cmap="gray"), plt.title(f"{filter_name}")
    plt.xticks([]), plt.yticks([])
    plt.show()