#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load packages
import os
#!pip install opencv-python
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


# In[2]:


# Set directory
base_dir = "/Users/kaleighwest/Downloads/DS_4002/ds4002/Project 3/Brain Tumor data"


# ## Resize images to optimal size (only run once)

# In[3]:


# Set size
new_size = (224, 224)

# Iterate through training and testing sets
for split in ["Training", "Testing"]:
    split_path = os.path.join(base_dir, split)

    # Iterate through each folder
    for label in os.listdir(split_path):
        label_path = os.path.join(split_path, label)

        # For each image, convert to RGB, resize, and save
        if os.path.isdir(label_path):
            for filename in os.listdir(label_path):
                file_path = os.path.join(label_path, filename)

                try:
                    with Image.open(file_path) as img:
                        img = img.convert("RGB")
                        img = img.resize(new_size)
                        img.save(file_path)
                except Exception as e:
                    print(f"Skipped {file_path}: {e}")

print("All images resized.")


# ## Determine Class Sizes

# In[4]:


# Get class sizes as a dataframe
counts = {}

for split in ["Training", "Testing"]:
    split_path = os.path.join(base_dir, split)
    counts[split] = {}

    for label in os.listdir(split_path):
        label_path = os.path.join(split_path, label)

        if os.path.isdir(label_path):
            num_images = len([
                f for f in os.listdir(label_path)
                if f.endswith(".jpg")
            ])

            counts[split][label] = num_images

counts_df = pd.DataFrame(counts).T

# Combine train and test counts
counts_df.loc["Total"] = counts_df.sum()

print(counts_df)


# In[5]:


# Plot class sizes for whole data set
counts_df.loc["Total"].plot(kind='pie', autopct='%1.1f%%', title='Distribution of Tumor Categories (Combined Dataset)')

plt.savefig('Distribution_of_Tumor_Categories_combined.png',
            dpi=300,
            bbox_inches='tight',
            pad_inches=0.25
           )
plt.show()


# In[7]:


# Plot class sizes for train and test sets
# Create a figure and a set of subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot the first pie chart on ax1
ax1.pie(counts_df.loc["Training"].values, labels=counts_df.loc["Training"].index, autopct='%1.1f%%')
ax1.set_title('Distribution of Categories (Training Set)')
ax1.axis('equal') # Ensure the pie charts are equal sizes

# Plot the second pie chart on ax2
ax2.pie(counts_df.loc["Testing"].values, labels=counts_df.loc["Testing"].index, autopct='%1.1f%%')
ax2.set_title('Distribution of Categories (Testing Set)')
ax2.axis('equal') # Ensure the pie charts are equal sizes

# Adjust layout and display the plots (prevent titles/labels from overlapping)
plt.tight_layout() 

# Save figure as .png and show
plt.savefig('Distribution_of_Categories_separate.png')
plt.show()


# In[ ]:




