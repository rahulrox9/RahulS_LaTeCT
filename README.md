# LaTeCT: Lamproite Tectonic Classification Tool

**LaTeCT** is an open source machine learning framework for tectonic classification of lamproites using whole rock geochemical data. The project provides a fully reproducible workflow from data compilation and quality control through exploratory geochemical analysis, preprocessing, dimensionality reduction and supervised machine learning.

The repository accompanies the associated research publication and is intended to provide a transparent and extensible framework for tectonic discrimination of lamproites.

---

## Features

- Reproducible data compilation and quality control workflows
- Chondrite normalised REE and primitive mantle normalised spider diagrams
- Data completeness assessment and feature selection
- Geochemical data preprocessing and transformation
- Dimensionality reduction and exploratory multivariate analysis
- Supervised machine learning for tectonic classification
- Publication quality figures and tables

---

## Repository Structure

```text
LaTeCT/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 00_Data_Compilation.ipynb
│   ├── 01_Data_Visualisation.ipynb
│   ├── 02_Data_Audit_and_Feature_Selection.ipynb
│   ├── 03_Data_Preprocessing.ipynb
│   ├── 04_Unsupervised_Analysis.ipynb
│   └── 05_Supervised_Classification.ipynb
│
├── figures/
├── exports/
│
├── src/
│   ├── preprocessing.py
│   ├── plotting.py
│   ├── modelling.py
│   └── utils.py
│
├── environment.yml
├── LICENSE
└── README.md
```

---

## Workflow

### 00 Data Compilation

Compile geochemical analyses from multiple literature sources into a unified database.

### 01 Data Visualisation

Generate exploratory geochemical figures including:

- Chondrite normalised REE diagrams
- Primitive mantle normalised spider diagrams
- Location level summaries
- Distribution plots

### 02 Data Audit and Feature Selection

Evaluate data completeness by:

- Element availability
- Sample completeness
- Location coverage
- Feature retention threshold optimisation

Produce the final modelling dataset.

### 03 Data Preprocessing

Prepare the modelling dataset through:

- Data transformation
- Scaling
- Distribution assessment
- Correlation analysis
- Training and testing dataset generation

### 04 Unsupervised Analysis

Explore the dataset using:

- Principal Component Analysis
- UMAP
- t-SNE
- Clustering

### 05 Supervised Classification

Train and evaluate machine learning classifiers including:

- Random Forest
- Support Vector Machine
- Gradient Boosting
- XGBoost (optional)

Model performance is assessed using:

- Cross validation
- ROC curves
- Confusion matrices
- Feature importance
- SHAP interpretation

---

## Installation

Clone the repository

```bash
git clone https://github.com/<username>/LaTeCT.git
cd LaTeCT
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
    raw/
    processed/
```

Raw data should not be modified. All processed datasets are generated automatically by the notebooks.

---

## Requirements

- Python 3.11+
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy
- scikit-learn
- XGBoost
- SHAP
- JupyterLab

The complete software environment is specified in `environment.yml`.

---

## Citation

If you use LaTeCT in published work, please cite the associated publication.

Citation information will be added following publication.

---

## Licence

This project is distributed under the MIT Licence.

See the `LICENSE` file for details.

---

## Author

Rahul Subbaraman

Department of Earth and Environmental Sciences

The University of Manchester

---

## Status

LaTeCT is currently under active development.
