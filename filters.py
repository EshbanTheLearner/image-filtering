import cv2
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