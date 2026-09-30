from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split data
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y,
    test_size=0.10,
    stratify=y,
    random_state=42
)

X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp,
    test_size=0.1111,
    stratify=y_temp,
    random_state=42
)

# Train model
tree = DecisionTreeClassifier(random_state=42)

tree.fit(X_train, y_train)

# Predictions
train_pred = tree.predict(X_train)
val_pred = tree.predict(X_val)
test_pred = tree.predict(X_test)

# Accuracy
train_acc = accuracy_score(y_train, train_pred)
val_acc = accuracy_score(y_val, val_pred)
test_acc = accuracy_score(y_test, test_pred)

print("Training Accuracy:", train_acc)
print("Validation Accuracy:", val_acc)
print("Test Accuracy:", test_acc)

# Tree info
print("\nTree Depth:", tree.get_depth())
print("Number of Leaves:", tree.get_n_leaves())

# Feature Importance
print("\nFeature Importances:")

for feature, importance in zip(iris.feature_names, tree.feature_importances_):
    print(feature, ":", round(importance, 4))

# Confusion Matrix
cm = confusion_matrix(y_test, test_pred)

print("\nConfusion Matrix:")
print(cm)

from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

disp.plot(cmap="Blues")

plt.savefig("results/confusion_matrix.png")
plt.close()

# Save Tree Visualization
plt.figure(figsize=(14, 8))

plot_tree(
    tree,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)

plt.savefig("results/decision_tree.png")
plt.close()

print("\nTree visualization saved successfully!")