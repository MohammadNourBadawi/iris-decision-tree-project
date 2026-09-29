# Iris Decision Tree Project

## What is Git?
Git is a version control system used to track changes in files.

## What is GitHub?
GitHub is a cloud platform used to host Git repositories.

## Working Directory
The place where files are modified.

## Staging Area
The area where changes are prepared before a commit.

## Commit
A saved snapshot of project changes.

## Main Branch
The primary branch used for development.
## Project Goal

This project explores the Iris dataset and Decision Tree classification.
## Phase 2 - Dataset Exploration

### Dataset Summary

- Total Rows: 150
- Total Columns: 5

### Column Names

- sepal length (cm)
- sepal width (cm)
- petal length (cm)
- petal width (cm)
- target

### Missing Values

No missing values were found in the dataset.

### Minimum and Maximum Values

| Feature | Min | Max |
|----------|-----|-----|
| sepal length (cm) | 4.3 | 7.9 |
| sepal width (cm) | 2.0 | 4.4 |
| petal length (cm) | 1.0 | 6.9 |
| petal width (cm) | 0.1 | 2.5 |

### Observations

- The dataset contains 150 samples.
- There are 4 input features and 1 target column.
- The dataset is clean and contains no missing values.
## Phase 3: Data Preparation and Dataset Splitting

### Dataset Split Strategy

The Iris dataset was split into:

- Training Set: 120 samples (80%)
- Validation Set: 15 samples (10%)
- Test Set: 15 samples (10%)

Stratification was used to preserve class distribution across all subsets.

A random_state value of 42 was used to ensure reproducibility. Re-running the workflow produces the same split results.

### Class Distribution

Training Set:
- Class 0: 40
- Class 1: 40
- Class 2: 40

Validation Set:
- Class 0: 5
- Class 1: 5
- Class 2: 5

Test Set:
- Class 0: 5
- Class 1: 5
- Class 2: 5

### Data Leakage Prevention

The test set was kept isolated from training and model-selection activities.

Feature scaling was fitted only on the training data and then applied to the test data to avoid data leakage.

### Feature Scaling Investigation

A StandardScaler experiment was performed.

Feature scaling changes the numerical scale of input features. It is important for distance-based and gradient-based models, but it is generally not necessary for Decision Tree classifiers because Decision Trees split based on feature thresholds rather than distances.