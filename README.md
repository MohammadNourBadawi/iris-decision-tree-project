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
### Dataset Description

The Iris dataset contains 150 flower samples divided into three species:

- Setosa (50 samples)
- Versicolor (50 samples)
- Virginica (50 samples)

Each sample contains four numerical features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The target column represents the flower species.

### Additional Observations

- The dataset is perfectly balanced because each class contains 50 samples.
- No missing values were detected.
- Petal Length and Petal Width appear to provide better separation between classes.
- Setosa samples are easier to distinguish from the other flower species.
- Some overlap is expected between Versicolor and Virginica classes.
- The dataset is clean and suitable for machine learning experiments.

### Statistical Insights

- Petal Length has the largest value range among the features.
- Sepal Width shows noticeable variation between samples.
- The absence of missing values means no data cleaning was required before analysis.
- Feature values are measured on similar scales, making the dataset easy to inspect and visualize.

### Visual Analysis

The following visualizations were generated during dataset inspection:

#### Class Distribution
The dataset is balanced, with 50 samples in each class.

#### Feature Distributions
Histograms were used to examine the distribution of feature values and identify variations across measurements.

#### Feature Boxplots
Boxplots were used to compare feature ranges and detect potential outliers.

#### Pairplot Analysis
The pairplot provides a visual comparison between all feature combinations.

Observations from the pairplot:

- Setosa is clearly separated from the other classes.
- Petal Length and Petal Width provide the strongest class separation.
- Some overlap exists between Versicolor and Virginica.
- A strong positive relationship can be observed between Petal Length and Petal Width.

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

# Phase 4A: Initial Decision Tree Model

## Model Performance

| Dataset | Accuracy |
|----------|----------|
| Training | 1.00 |
| Validation | 0.93 |
| Test | 0.87 |

## Tree Properties

- Tree Depth: 5
- Number of Leaves: 8

## Feature Importance

| Feature | Importance |
|----------|----------|
| Sepal Length | 0.0042 |
| Sepal Width | 0.0292 |
| Petal Length | 0.5386 |
| Petal Width | 0.4281 |

## Visual Outputs

- Decision Tree Visualization
- Confusion Matrix

## Observations

The model achieved perfect training accuracy and strong validation accuracy. Petal length and petal width were the most important features for classification. The confusion matrix shows that most flower classes were classified correctly.

## Decision Tree Concepts

### Root Node
The root node is the first decision point in the tree. In this model, the root node uses petal length to divide the dataset into different groups.

### Internal Nodes
Internal nodes are intermediate decision points that continue splitting the data based on feature values.

### Branches
Branches connect nodes and represent decision outcomes from a specific condition.

### Leaf Nodes
Leaf nodes are the final nodes of the tree. Each leaf represents the predicted class for samples reaching that node.

### Gini Impurity
Gini impurity measures how mixed the classes are within a node. A Gini value of 0 means that all samples in the node belong to a single class, making it a pure node.
## GitHub Web Edit Test

This line was added directly from the GitHub web interface for Phase 5 synchronization testing.

# Final Evaluation

## Model Performance

| Dataset | Accuracy |
|----------|----------|
| Training | 1.00 |
| Validation | 0.93 |
| Test | 0.87 |

## Generalization Analysis

The Decision Tree achieved perfect training accuracy and strong validation accuracy.

The difference between training and validation performance suggests that the model may contain slight overfitting, but the validation and test results remain strong.

Overall, the model demonstrates reasonable generalization on unseen data.

## Future Improvements

- Compare multiple Decision Tree depth configurations.
- Apply cross-validation for more reliable evaluation.
- Compare Decision Trees with other classification algorithms.
# Setup Instructions

## Requirements

- Python 3.x
- pandas
- matplotlib
- scikit-learn

## Install Dependencies

```bash
pip install -r requirements.txt

```

# Execution Instructions

Run dataset exploration:

```bash
python explore_data.py

Run Decision Tree training:
 
```bash
python train_decision_tree.py
```
# Limitations

- Only the Iris dataset was used.
- The dataset contains a limited number of samples.
- Only a Decision Tree classifier was tested.

# Reflection

This project improved my understanding of Git, GitHub, dataset analysis, data preparation, Decision Trees, and machine learning evaluation. I also gained practical experience in documenting and organizing a reproducible AI project.
