# DS4002_Project3
## This repository contains the dataset, EDA, and CNN model used to classify our brain tumor dataset. 
## Software and Platform
This project was developed and tested using the following  environment:

Operating System: macOS

Programming Language: Python

Developed Environment: Jupyter Notebook, Visual Studio Code

Required Python Packages:
- os
- numpy
- matplotlib
- scikit-learn
- PIL
- seaborn
- jupyter
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
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
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

### Step 5: Train the Model and Create the Analysis Dataset

Run:

```
python SCRIPTS/logistic_regression.py
```

This script will:

- Combine Fake.csv and True.csv
- Clean the headline text
- Create `DATA/headlines_clean.csv`
- Train the TF-IDF Logistic Regression classifier
- Output accuracy, precision, recall, F1 score, and confusion matrix

---

### Output Files

All figures and outputs in the `OUTPUT/` folder are reproducible.  
They will be regenerated automatically when the scripts above are executed.
