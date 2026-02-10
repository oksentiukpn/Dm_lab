from ucimlrepo import fetch_ucirepo
#from sklearn.model_selection import cross_val_score
#from sklearn.tree import DecisionTreeClassifier as dtc
#from sklearn import tree
from sklearn.model_selection import train_test_split
import numpy as np
from numpy import typing as npt
#import pandas as pd
import matplotlib.pyplot as plt

class Node:
    def __init__(self, predicted_class):
        """
        :param X: numpy array of form [[feature1,feature2, ... featureN], ...] (i.e. [[1.5, 5.4, 3.2, 9.8] , ...] for case with iris d.s.)
        :param y: numpy array of from [class1, class2, ...] (i.e. [0,1,1,2,1,0,...] for case with iris d.s.)
        """

        self.predicted_class = predicted_class
        self.feature_index = 0
        self.threshold = 0
        self.left = None
        self.right = None



class DecisionTreeClassifier:
    def __init__(self, max_depth: int) -> None:
        self.max_depth = max_depth
        self.tree = None
        self.number_of_classes = None


    def fit(self, X: npt.NDArray, y: npt.NDArray) -> None:
        """
        Basically, function that performs all the training (building of a tree)
        We recommend to use it as a wrapper of recursive building function
        """
        self.number_of_classes = len(np.unique(y))
        self.tree = self.grow_tree(X, y)


    def predict(self, X_test: npt.NDArray) -> list:
        """
        Traverse the tree while there is a child
        and return the predicted class for it
        """
        return [self.predict_one(sample) for sample in X_test]

    def gini(self, y):
        """
        Calculate Gini Impurity: 1 - sum(probabilities^2)
        """
        rows = len(y)
        if rows == 0:
            return 0

        # Count occurrencies of each class
        counts = np.bincount(y) if np.issubdtype(y.dtype, np.integer) else np.unique(y, return_counts=True)[1]
        probabilities = counts / rows
        return 1 - np.sum(probabilities ** 2)

    def best_split(self, X, y):
        """
        Find the best feature and threshold to spit the data
        """
        rows, cols = X.shape
        if rows <= 1:
            return None, None

        best_gini = 1.0
        best_idx, best_thr = None, None

        for idx in range(cols):
            # sorting unique value to find potential thresholds
            thresholds = np.unique(X[:, idx])

            for thr in thresholds:
                #creating boolean mask for split
                left_mask = X[:, idx] < thr

                # if split doesnt divide, just skip
                if np.sum(left_mask) == 0 or np.sum(left_mask) == rows:
                    continue

                y_left = y[left_mask]
                y_right = y[~left_mask]

                # calculating gini

                gini_left = self.gini(y_left)
                gini_right = self.gini(y_right)
                weighted_gini = (len(y_left) / rows) * gini_left + (len(y_right) / rows) * gini_right

                if weighted_gini < best_gini:
                    best_gini = weighted_gini
                    best_idx = idx
                    best_thr = thr
        return best_idx, best_thr

    def grow_tree(self, X, y, depth=0):
        """
        Recursive function to build the tree nodes.
        """
        predicted_class = np.argmax(np.bincount(y) if len(y) > 0 else 0)
        node = Node(predicted_class=predicted_class)

        # stopping criteria
        if len(np.unique(y)) == 1:
            return node
        if self.max_depth is not None and depth >= self.max_depth:
            return node

        # looking for best split
        idx, thr = self.best_split(X, y)

        if idx is not None:
            node.feature_index = idx
            node.threshold = thr

            # spliting data
            left_indices = X[:, idx] < thr
            X_left, y_left = X[left_indices], y[left_indices]
            X_right, y_right = X[~left_indices], y[~left_indices]

            # recursive
            node.left = self.grow_tree(X_left, y_left, depth=depth+1)
            node.right = self.grow_tree(X_right, y_right, depth=depth+1)
        return node

    def predict_one(self, sample):
        """
        Predict class for a single sample by traversing the tree.
        """
        node = self.tree
        while node.left:
            if sample[node.feature_index] < node.threshold:
                node = node.left
            else:
                node = node.right

        return node.predicted_class


def evaluate(X_test, y_test, model):
    """
    Returns accuracy of the model.
    """
    predictions = model.predict(X_test)
    y_test_flat = y_test.flatten() if hasattr(y_test, 'flatten') else y_test

    correct = np.sum(predictions == y_test_flat)
    return correct / len(y_test)


print("--- 1. Fetching Dataset ---")
phishing_websites = fetch_ucirepo(id=327)

X = phishing_websites.data.features.values
y = phishing_websites.data.targets.values

y = y.reshape(-1)
y = y.copy()
y[y == -1] = 0

print(f"Data loaded. Features shape: {X.shape}, Target shape: {y.shape}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\n--- 2. Training Custom Decision Tree ---")
my_model = DecisionTreeClassifier(max_depth=3)
my_model.fit(X_train, y_train)
print("Training complete.")

print("\n--- 3. Evaluation ---")
accuracy = evaluate(X_test, y_test, my_model)

print(f"Model Accuracy on Test Set: {accuracy * 100:.2f}%")

print("\n--- (Optional) Comparison with Sklearn ---")
from sklearn.tree import DecisionTreeClassifier as SklearnDTC
sk_model = SklearnDTC(max_depth=3, criterion='gini')
sk_model.fit(X_train, y_train)
sk_acc = sk_model.score(X_test, y_test)
print(f"Sklearn Accuracy: {sk_acc * 100:.2f}%")
