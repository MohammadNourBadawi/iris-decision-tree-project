from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.preprocessing import StandardScaler
iris = load_iris()

X = iris.data
y = iris.target
X_train, X_temp, y_train, y_temp = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

print("Training samples:", len(X_train))
print("Remaining samples:", len(X_temp))
X_val, X_test, y_val, y_test = train_test_split(
    X_temp,
    y_temp,
    test_size=0.5,
    stratify=y_temp,
    random_state=42
)

print("Validation samples:", len(X_val))
print("Test samples:", len(X_test))
print("Features shape:", X.shape)
print("Labels shape:", y.shape)
print("\nTraining class distribution:")
print(Counter(y_train))

print("\nValidation class distribution:")
print(Counter(y_val))

print("\nTest class distribution:")
print(Counter(y_test))
print("\nRandom State Used: 42")
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nFirst training sample before scaling:")
print(X_train[0])

print("\nFirst training sample after scaling:")
print(X_train_scaled[0])