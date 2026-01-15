#!/usr/bin/env python3
"""Test ANN models to diagnose isnan error"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
import numpy as np
import scipy.sparse as sp

# Test DenseTransformer
class DenseTransformer:
    def __init__(self):
        self.n_features_in_ = None
        
    def fit(self, X, y=None):
        if sp.issparse(X):
            self.n_features_in_ = X.shape[1]
        else:
            self.n_features_in_ = X.shape[1]
        return self
    
    def transform(self, X):
        if sp.issparse(X):
            arr = X.toarray().astype(np.float64)
        elif isinstance(X, np.ndarray):
            arr = X.astype(np.float64)
        else:
            arr = np.asarray(X, dtype=np.float64)
        
        # Check for NaN values
        if np.any(np.isnan(arr)):
            print(f"WARNING: NaN values found in data! Replacing with 0")
            arr = np.nan_to_num(arr, nan=0.0)
        return arr
    
    def get_feature_names_out(self, input_features=None):
        return np.arange(self.n_features_in_)

# Create simple test pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,3), max_features=100)),
    ("to_dense", DenseTransformer()),
    ("clf", MLPClassifier(hidden_layer_sizes=(64,), max_iter=50, solver='lbfgs', alpha=0.01, random_state=42))
])

# Test data
texts = ["test document one", "test document two", "another test", "more text"] * 25
labels = ["A", "B", "A", "B"] * 25

# Test
try:
    print("Training ANN...")
    pipeline.fit(texts[:50], labels[:50])
    print("Predicting...")
    pred = pipeline.predict(texts[50:60])
    print("SUCCESS: ANN pipeline works!")
    print(f"Predictions: {pred}")
except Exception as e:
    print(f"ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
