"""These are functions for the Image EDA Scripts."""

import os
import matplotlib.pyplot as plt
import cv2
import pandas as pd

def avg_pixel_intensity(dataset_path, img_resize = (624, 624)):
    """Generates average pixel intensity histogram for a dataset of images.
    
    Args:
    dataset_path: string, path to the folder containing the images
    
    Returns:
    
    pixel_values: numpy array, average pixel intensity histogram
    
    """
    img_count = len(os.listdir(dataset_path))
    pixel_values = np.zeros(img_resize[0]*img_resize[1])
    for image in os.listdir(dataset_path):
        img = cv2.imread(os.path.join(dataset_path, image),0)
        # resize the image
        if img.shape[0] != img_resize[0] or img.shape[1] != img_resize[1]: 
            img = cv2.resize(img, (624, 624))
        pixel_values += img.ravel()
    pixel_values = pixel_values / img_count
    return pixel_values


def plot_avg_pixel_intensity(pixel_values):
    """Plots the average pixel intensity histogram.
    
    Args:
            pixel_values: numpy array, average pixel intensity histogram
    
    Returns:
            None
    """
    plt.hist(pixel_values,256,[0,256])
    plt.show()


import numpy as np
from scipy.stats import skew, kurtosis, mode



def get_descriptive_statistics(pixel_values):
    """Generates descriptive statistics for the average pixel intensity histogram.

    Args:
        pixel_values: numpy array, average pixel intensity histogram

    Returns:
        dictionary of descriptive statistics
    """
    desc = {
        "mean": np.mean(pixel_values),
        "median": np.median(pixel_values),
        "sd": np.std(pixel_values),
        "var": np.var(pixel_values),
        "minimum": np.min(pixel_values),
        "maximum": np.max(pixel_values),
        "percentile_25": np.percentile(pixel_values, 25),
        "percentile_75": np.percentile(pixel_values, 75),
        "iqr": np.percentile(pixel_values, 75) - np.percentile(pixel_values, 25),
        "skewness": skew(pixel_values),
        "kurt": kurtosis(pixel_values),
        "a_mode": mode(pixel_values),
    }
    return desc

def combine_descriptive_statistics(dataset_path, img_resize = (624, 624)):
    """Combines descriptive statistics for a dataset of images.
    """
    stats_list = []
    for image in os.listdir(dataset_path):
        img = cv2.imread(os.path.join(dataset_path, image),0)
        # resize the image
        if img.shape[0] != img_resize[0] or img.shape[1] != img_resize[1]:
            img = cv2.resize(img, (624, 624))
        pixel_values = img.ravel()
        desc_stats = get_descriptive_statistics(pixel_values)
        stats_list.append(desc_stats)
    return round(pd.DataFrame(stats_list),0)


def make_img_histogram(dataset_path, img_resize = (624, 624)):
    """Generates histograms of descriptive statistics for a dataset of images.
    """
    stats_df = combine_descriptive_statistics(dataset_path, img_resize = img_resize)
    # make subplots of histograms
    fig, axs = plt.subplots(3, 4, figsize=(20, 15))
    for i, col in enumerate(stats_df.columns):
        if col == "a_mode":
            final_val_list = []
            for val in stats_df[col].values:
                for i in range(0, val[1]):
                    final_val_list.append(val[0])
            axs[i//4, i%4].hist(final_val_list, 256,[0,256])
        elif col in ["sd", "mean", "median", "iqr"]:
            axs[i//4, i%4].hist(stats_df[col].values, 256,[0,256])
        else:
            axs[i//4, i%4].hist(stats_df[col].values, bins=30)
        axs[i//4, i%4].set_title(col)
    plt.show()