# LaTeCT: Lamproite Tectonic Classification Tool

**LaTeCT** is an open source Python workflow for the tectonic classification of lamproites using whole rock geochemical data. The repository provides a fully reproducible pipeline from data compilation and quality control through exploratory analysis, preprocessing, unsupervised analysis and Random Forest classification.

The workflow accompanies the associated research publication in Lithos and is designed to promote transparent, reproducible and extensible tectonic discrimination of lamproites.

## Launch LaTeCT Online

You can run the LaTeCT graphical classification tool directly in your web browser without installing any software locally. Click the badge below to launch a temporary cloud environment via Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rahulrox9/RahulS_LaTeCT/main?filepath=LaTeCT_Application.ipynb)

**Instructions for use:**
1. Click the Binder badge above.
2. Wait for the cloud environment to build and load.
3. Once the `LaTeCT_Application.ipynb` notebook opens, select the code cell and press `Shift + Enter` to execute it.
4. Use the generated graphical interface to upload your `.csv` dataset and download the classified results.

## Requirements

The complete software environment is specified in `environment.yml`. Core dependencies include:

* Python 3.11+
* NumPy
* Pandas
* Matplotlib
* SciPy
* scikit-learn
* joblib
* Graphviz
* JupyterLab

## Installation

Clone the repository:

```bash
git clone [https://github.com/rahulrox9/RahulS_LaTeCT.git](https://github.com/rahulrox9/RahulS_LaTeCT.git)
cd RahulS_LaTeCT

## Repository Structure

```text
LaTeCT/
│
├── model_data/
│   ├── raw/
│   ├── processed/
│   └── external_validation/
│
├── dev-notebooks/
│   ├── 01_Exploratory_Geochemical_Visualisation.ipynb
│   ├── 02_Data_Audit_and_Feature_Selection.ipynb
│   ├── 03_Data_Preprocessing.ipynb
│   ├── 04_Unsupervised_Analysis.ipynb
│   └── 05_Supervised_Analysis.ipynb
│
├── final_rf.joblib
│
├── model_output/
│   ├── exports/
│   └── figures/
│
├── LaTeCT.ipynb
├── environment.yml
├── LICENSE
└── README.md
---
## Workflow

### 01 Data Visualisation

Generate exploratory geochemical visualisations including:

- Chondrite normalised REE diagrams
- Primitive mantle normalised spider diagrams
- Location summaries
- Element distribution plots

### 02 Data Audit and Feature Selection

Construct the modelling dataset through:

- Data auditing
- Element availability assessment
- Sample completeness assessment
- Location coverage evaluation
- Feature selection

### 03 Data Preprocessing

Prepare the dataset for machine learning by:

- Log transformation
- Standardisation
- Distribution assessment
- Correlation analysis
- Train/test split generation

### 04 Unsupervised Analysis

Investigate the natural structure of the dataset using:

- Principal Component Analysis (PCA)
- K means clustering
- Cluster validation
- Geochemical cluster interpretation

### 05 Supervised Classification

Develop and interpret a Random Forest classifier through:

- Baseline model training
- Five and ten fold cross validation
- Hyperparameter optimisation using GridSearchCV
- Final model evaluation
- Random Forest decision structure analysis
- Representative decision trees
- Misclassified sample analysis

Model performance is evaluated using:

- Accuracy
- Balanced Accuracy
- Precision
- Recall
- F1 score
- ROC AUC

---

## Citation

If you use LaTeCT in published work, please cite: 

---

## Licence

This project is distributed under the MIT Licence.

See `LICENSE` for details.

---

## Author

Rahul Subbaraman
Associate Editor, Communications Earth and Environment, Springer Nature
(Formerly: Department of Earth and Environmental Sciences, The University of Manchester)
