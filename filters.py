import numpy as np
import cv2
from PIL import Image, ImageFilter
from utils import *

def apply_mean_filter(image, kernel_size=9):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    new_image = cv2.blur(image, (kernel_size, kernel_size))
    plot_comparison(image, new_image, "Mean Filter")

def apply_mean_filter_grayscale(image, kernel_size=9):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    new_image = cv2.blur(image, (kernel_size, kernel_size))
    plot_comparison_grayscale(image, new_image, "Mean Filter")

def apply_gaussian_filter(image, kernel_size=9):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    new_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    plot_comparison(image, new_image, "Gaussian Filter")

def apply_gaussian_filter_grayscale(image, kernel_size=9):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    new_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    plot_comparison_grayscale(image, new_image)

def apply_median_filter(image, kernel_size=9):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    new_image = cv2.medianBlur(image, kernel_size)
    plot_comparison(image, new_image, "Median Filter")

def apply_median_filter_grayscale(image, kernel_size=9):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    new_image = cv2.medianBlur(image, kernel_size)
    plot_comparison_grayscale(image, new_image)

def apply_laplacian(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    filter = cv2.Laplacian(image, cv2.CV_64F)
    new_image = image + filter
    plot_comparison(image, new_image, "Laplacian Filter")

def apply_laplacian_grayscale(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filter = cv2.Laplacian(image, cv2.CV_64F)
    new_image = image + filter
    plot_comparison_grayscale(image, new_image, "Laplacian Filter")

def apply_conservative_smoothing(image, kernel_size=9):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    temp = []
    indexer = kernel_size // 2
    new_image = image.copy()
    nrow, ncol, _ = image.shape
    for i in range(nrow):
        for j in range(ncol):
            for k in range(i - indexer, i + indexer + 1):
                for m in range(j - indexer, j + indexer + 1):
                    if (k > -1) and (k < nrow):
                        if (m > -1) and (m < ncol):
                            temp.append(image[k, m])
            print(temp)
            print(type(temp))
            print(type(temp[0]))
            print(image[i, j])
            print(type(image[i, j]))
            print(temp[0].shape, image[i, j].shape)
            #temp.remove(image[i, j]).any()
            temp = [a for a, skip in zip(temp, [np.allclose(a, image[i, j]) for a in temp]) if not skip]
            max_value = np.array(temp).max()
            min_value = np.array(temp).min()
            if image[i, j] > max_value:
                new_image[i, j] = max_value
            elif image[i, j] < min_value:
                new_image[i, j] = min_value
            temp = []
    plot_comparison(image, new_image)

def apply_unsharp_filter_grayscale(image):
    image = Image.fromarray(image.astype("uint8"))
    new_image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150))
    plot_comparison_grayscale(image, new_image)

def apply_conservative_smoothing_grayscale(image, kernel_size=9):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    temp = []
    indexer = kernel_size // 2
    new_image = image.copy()
    nrow, ncol = image.shape
    for i in range(nrow):
        for j in range(ncol):
            for k in range(i - indexer, i + indexer + 1):
                for m in range(j - indexer, j + indexer + 1):
                    if (k > -1) and (k < nrow):
                        if (m > -1) and (m < ncol):
                            temp.append(image[k, m])
            temp.remove(image[i, j].any())
            max_value = max(temp)
            min_value = min(temp)
            if image[i, j] > max_value:
                new_image[i, j] = max_value
            elif image[i, j] < min_value:
                new_image[i, j] = min_value
            temp = []
    plot_comparison_grayscale(image, new_image)