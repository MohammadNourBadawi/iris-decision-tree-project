from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)
df["target"] = iris.target
print(df.head())
print("\n")
print(df.info())
print("\n")
print(df.describe())


import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("results", exist_ok=True)

# Class Distribution Plot
plt.figure(figsize=(6,4))
sns.countplot(x="target", data=df)
plt.title("Class Distribution")
plt.savefig("results/class_distribution.png")
plt.close()

# Histograms
df.iloc[:, :4].hist(figsize=(10,8))
plt.suptitle("Feature Distributions")
plt.savefig("results/feature_distributions.png")
plt.close()

# Boxplot
plt.figure(figsize=(10,6))
sns.boxplot(data=df.iloc[:, :4])
plt.title("Feature Boxplots")
plt.savefig("results/boxplot.png")
plt.close()
# Pairplot
pair = sns.pairplot(df, hue="target")
pair.savefig("results/pairplot.png")
plt.close()

print("Plots saved successfully!")