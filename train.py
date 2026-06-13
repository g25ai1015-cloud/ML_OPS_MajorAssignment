import joblib
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print("Fetching dataset...")
data = fetch_olivetti_faces()
X, y = data.data, data.target

# 70% training, 30% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("Training Decision Tree Model...")
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Save the trained model file
joblib.dump(clf, 'savedmodel.pth')
print("Model saved successfully as savedmodel.pth")