# License Classification and Identification

A machine learning system for multi-class software license classification and identification with real integration to industry-standard tools (ScanCode, FOSSology, ML models).

## Overview

This project implements a production-ready license classifier that:
- Analyzes license texts and categorizes them into four classes: Permissive, Copyleft, Proprietary, Public Domain
- Integrates with real tools: ScanCode CLI, FOSSology REST API, custom ML model
- Provides graceful fallbacks when tools are unavailable
- Benchmarks performance across all three integration methods
- Achieves 88% accuracy with ensemble methods

## Project Structure

```
ML_Project/
├── main.ipynb           # Main analysis notebook (all code)
├── license_data/        # Training dataset (1000+ licenses with labels)
└── README.md            # This file
```

## Quick Start

### Prerequisites
- Python 3.9+
- Jupyter Notebook
- Dependencies: scikit-learn, pandas, numpy, nltk, requests

### Installation

```bash
# Clone repository
git clone https://github.com/yosseer/License-Classification-and-Identification
cd ML_Project

# Install dependencies
pip install -r requirements.txt

# (Optional) Install real tools
pip install scancode-toolkit  # For real ScanCode integration
docker pull fossology/fossology  # For FOSSology integration
```

### Running the Notebook

```bash
jupyter notebook main.ipynb
```

Execute cells in order:
1. Cells 1-15: Data loading and preprocessing
2. Cells 16-20: Model training and evaluation (60+ ML models)
3. Cells 21-30: Real tool integrations and benchmarking
4. Cells 31-33: Comparative analysis and results

## Features

### Multi-Class License Classification
- Permissive: MIT, Apache, BSD, ISC, etc.
- Copyleft: GPL, AGPL, LGPL, EPL, etc.
- Proprietary: Commercial, Closed-source, Evaluation licenses
- Public Domain: Unlicense, CC0, Public Domain Dedication

### Three Integration Methods

1. **ScanCode Integration**
   - Real CLI subprocess calls with 30-second timeout
   - Falls back to pattern matching if unavailable
   - Accuracy: 75%+

2. **FOSSology Integration**
   - Real REST API calls to FOSSology server
   - Docker deployment ready
   - Falls back to pattern matching
   - Accuracy: 82%+

3. **ML Model Integration**
   - TF-IDF vectorization with RidgeClassifier
   - Trained on 1000+ SPDX licenses
   - Direct prediction on new texts
   - Accuracy: 88%

### Model Zoo
60+ trained models including:
- Naive Bayes variants (MultinomialNB, ComplementNB)
- Linear classifiers (LogisticRegression, RidgeClassifier, SGDClassifier)
- Distance-based (KNN with various parameters)
- Neural networks (MLPClassifier with multiple architectures)
- SVM (LinearSVC with different regularizations)
- Ensemble voting classifier

### Performance Metrics
- Accuracy scores on test set
- Precision, Recall, F1-Score (weighted)
- Per-class confusion matrices
- Comparative performance tables

## Data

The `license_data/` directory contains 1000+ SPDX license files extracted from:
- SPDX License List: https://spdx.org/licenses/
- Real-world open-source projects
- Commercial software

Files are categorized by license ID (e.g., MIT.txt, GPL-3.0-only.txt) and preprocessed with:
- Stopword removal
- Lemmatization
- Special character removal
- Lowercase conversion

## Notebook Structure

### Phase 1: Data Preparation (Cells 1-7)
- Load all license files from license_data/
- Extract text and category labels
- Analyze class distribution

### Phase 2: Text Preprocessing (Cell 8)
- NLTK stopword removal
- Lemmatization
- Special character and number removal
- Word count analysis

### Phase 3: Model Zoo Creation (Cells 9-13)
- Define 60+ classifier configurations
- Different feature extraction methods (TF-IDF, n-grams)
- Various hyperparameters
- Train and evaluate all models

### Phase 4: Best Model Selection (Cells 14-16)
- Display top 5 best performers
- Identify fastest models
- Select best by accuracy/F1-score
- Visualize results

### Phase 5: Real Tool Integration (Cells 17-19)
- Initialize ScanCode integration
- Initialize FOSSology integration
- Verify installations and connectivity

### Phase 6: System Validation (Cell 20)
- Test each tool with sample license
- Verify fallback behavior
- Check error handling

### Phase 7: Batch Predictions (Cell 21)
- Generate real predictions on test set
- Compare predictions from all three tools
- Track agreement and disagreement

### Phase 8: Metrics and Analysis (Cells 22-30)
- Calculate comprehensive metrics
- Create confusion matrices
- Generate comparison tables
- Visualize performance differences
- Analyze per-class performance
- Create final assessment

### Phase 9: Advanced Analysis (Cells 31-33)
- Edge case evaluation
- Tool agreement analysis
- Hybrid ensemble voting
- Final recommendations

## Configuration

### Environment Variables (Optional)

```bash
# FOSSology server configuration
export FOSSOLOGY_SERVER="http://localhost"
export FOSSOLOGY_TOKEN="your-api-token"

# Or set in notebook cell before running integrations
```

### Timeout Settings

Default timeouts (in ScanCodeIntegration class):
- ScanCode subprocess: 30 seconds
- FOSSology API: 30 seconds
- Pattern matching: <1 second (used by default for batch mode)

## Output Examples

All outputs are displayed in the notebook:
- Model training results table
- Top 20 models bar chart
- Confusion matrices for each tool
- Side-by-side performance comparison
- Per-class analysis tables
- Error rate analysis

## Accuracy Results

On test set (160 samples from 4 categories):
- Best ML Model: 88% accuracy
- FOSSology: 82% accuracy (with real API)
- ScanCode: 75% accuracy (with fallback patterns)
- Ensemble voting: 90% accuracy

## Troubleshooting

### ScanCode timeouts
- Timeout is normal for large files
- System uses fast pattern matching by default
- Enable real CLI integration separately if needed

### FOSSology connection fails
- Check Docker container status: `docker ps | grep fossology`
- Verify token validity
- Start fresh container: `docker run -d --name fossology -p 80:80 fossology/fossology`

### Low accuracy on custom licenses
- Model trained on SPDX licenses only
- Consider retraining on domain-specific data
- Use ensemble voting for better results

## License

This project is for educational and research purposes. See individual license files in license_data/ for SPDX license information.

## Author

Created as part of ML-based license identification research project.
