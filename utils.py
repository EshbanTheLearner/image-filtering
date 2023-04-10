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

def plot_comparison(original, filtered, filter_name="Filtered", grayscale=False):
    plt.figure(figsize=(11, 6))
    plt.subplots(121)
    if grayscale:
        plt.imshow(original, cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(original, cv2.COLOR_HSV2RGB))
    plt.title("Original")
    plt.xticks([]), plt.yticks([])
    plt.subplots(122)
    if grayscale:
        plt.imshow(filtered, cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(filtered, cv2.COLOR_HSV2RGB))
    plt.title(f"{filter_name}")
    plt.xticks([]), plt.yticks([])
    plt.show()