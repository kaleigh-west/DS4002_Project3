# DS4002_Project3
## This repository contains the scripts, outputs, and documentation used to explore and classify a brain tumor MRI image dataset using exploratory data analysis and a MobileNetV2-based CNN model. 
## Software and Platform
This project was developed and tested using the following  environment:

Operating System: macOS

Programming Language: Python

Developed Environment: Jupyter Notebook, Visual Studio Code

Required Python Packages:
- os
- numpy
- pandas
- matplotlib
- scikit-learn
- sklearn.metrics
- PIL
- seaborn
- jupyter
- tensorflow
- tensorflow.keras
- tensorflow.keras.preprocessing.image
- tensorflow.keras.models
- tensorflow.keras.layers
- tensorflow.keras.callbacks
- tensorflow.keras.applications
## Documentation
### Data Folder
&emsp;README.md with instructions on how to download raw dataset\
&emsp;Data_Appendix.pdf
### Output Folder
EDA Folder\
&emsp;Distribution_of_Categories_separate.png\
&emsp;Distribution_Tumor_Categories_combined.png\
Model Folder\
&emsp;accuracy_epoch.png\
&emsp;confusion_matrix.png\
&emsp;loss_epoch.png\
&emsp;metrics.png\
&emsp;model.png
### Scripts Folder
&emsp;EDA.py\
&emsp;cnn.py
## Reproducibility
### Step 1: Download or Clone the Repository

Download this repository as a ZIP file or clone it:

```
git clone https://github.com/kaleigh-west/DS4002_Project3.git
cd DS4002_Project3
```

All commands below must be run from the project root directory: `DS4002_Project3`

---

### Step 2: Install Required Packages

This project was developed using Python 3.11.

Install dependencies:

```
pip install pandas numpy matplotlib pillow tensorflow scikit-learn jupyter
```

---

### Step 3: Download the Original Dataset

The project uses the **Brain Tumor Data** from Mendeley Data:

https://data.mendeley.com/datasets/w4sw3s9f59/1 

After downloading, unzip the folder and place the following files into:

`DATA/`

Folders required:
```
Training folder: contains meningioma, pituitary, glioma, and notumor folders
Testing folder: contains meningioma, pituitary, glioma, and notumor folders
```

---

### Step 4: Run the Exploratory Data Analysis (EDA)

Run:

```
python SCRIPTS/EDA.py
```

This recreates the exploratory visualizations used in the report and data appendix.

Pre-generated figures are also included in the `OUTPUT/` folder for reference.

---

### Step 5: Establish, run, and evaluate CNN model

Run:

```
python SCRIPTS/cnn.py
```

This script will:

- Augment training data
- Reserve 20% of the training data for validation while training
- Apply MobileNetV2 preprocessing
- Plot training and validation loss across epochs
- Evaluate final MobileNetV2 model on the test set
- Output a classification report showing precision, recall, F1-score, and support for each diagnosis class in the test set
- Output a confusion matrix as a heatmap plot

---

### Output Files

All figures and outputs in the `OUTPUT/` folder are reproducible.  
They will be regenerated automatically when the scripts above are executed.

---

### References
[1] “Meningioma,” Brain Tumor Center, 2023. https://med.stanford.edu/brain-tumor/conditions/meningioma.html
[2]“Pituitary Tumors,” www.hopkinsmedicine.org. https://www.hopkinsmedicine.org/health/conditions-and-diseases/pituitary-tumors
[3] A. Ghaffar, “Brain Tumor Data,” data.mendeley.com, vol. 1, Jan. 2024, doi: https://doi.org/10.17632/w4sw3s9f59.1.
