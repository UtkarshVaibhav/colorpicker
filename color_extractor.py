import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def extract_colors(image, num_colors=5):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    pixels = image.reshape(-1, 3)
    
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    
    colors = kmeans.cluster_centers_
    colors = colors.astype(int)
    
    return colors

def plot_colors(colors):
    plt.figure(figsize=(8, 2))
    
    for i, color in enumerate(colors):
        plt.bar(i, 1, color=np.array(color)/255)
    
    plt.xticks([])
    plt.yticks([])
    plt.show()
