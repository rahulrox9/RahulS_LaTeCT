# LaTeCT: Lamproite Tectonic Classification Tool

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rahulrox9/RahulS_LaTeCT/main?filepath=LaTeCT_Application.ipynb)

**LaTeCT** is an open source Python workflow for the tectonic classification of lamproites using whole rock geochemical data. The repository provides a fully reproducible pipeline from data compilation and quality control through exploratory analysis, preprocessing, unsupervised analysis and Random Forest classification.

The workflow accompanies the associated research publication in Lithos and is designed to promote transparent, reproducible and extensible tectonic discrimination of lamproites.

---

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

## Installation

Clone the repository

```bash
git clone https://github.com/rahulrox9/RahulS_LaTeCT.git
cd RahulS_LaTeCT
```

Create the conda environment

```bash
conda env create -f environment.yml
conda activate tectonic_ml
```

---

## Data

The repository expects the following directory structure:

```text
data/
├── raw/
└── processed/
```

---

## Requirements

- Python 3.11+
- NumPy
- Pandas
- Matplotlib
- SciPy
- scikit-learn
- -joblib
- Graphviz
- JupyterLab

The complete software environment is specified in `environment.yml`.

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
Associate Editor, Springer Nature
(Formerly: Department of Earth and Environmental Sciences, The University of Manchester)
