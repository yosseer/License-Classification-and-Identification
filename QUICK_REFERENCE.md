# Quick Reference: Tool Integration Commands

## Installation Commands

### ScanCode
```bash
# Install
pip install scancode-toolkit

# Verify
scancode --version

# Full analysis on a directory
scancode --license --json results.json /path/to/licenses/
```

### FOSSology
```bash
# Start Docker container
docker run -d -p 8080:80 \
  -e FOSSOLOGY_DB_NAME=fossology \
  -e FOSSOLOGY_DB_USER=fossy \
  -e FOSSOLOGY_DB_PASSWORD=fossy \
  --name fossology \
  fossology/fossology

# Check if running
docker ps | grep fossology

# View logs
docker logs fossology

# Stop container
docker stop fossology

# Remove container
docker rm fossology
```

### Environment Setup
```bash
# Set up FOSSology environment variables
export FOSSOLOGY_SERVER="http://localhost:8080"
export FOSSOLOGY_TOKEN="your_api_token_here"

# On Windows (PowerShell)
$env:FOSSOLOGY_SERVER = "http://localhost:8080"
$env:FOSSOLOGY_TOKEN = "your_api_token_here"
```

---

## Python Usage Examples

### Single License Classification
```python
from main import ScanCodeIntegration, FOSSologyIntegration, MLModelWrapper

# Initialize
scancode = ScanCodeIntegration()
fossology = FOSSologyIntegration()
ml_model = MLModelWrapper(pipeline)

# Classify single license
text = "MIT License..."
sc_result = scancode.predict(text, "MIT")
ff_result = fossology.predict(text, "MIT")
ml_result = ml_model.predict(text, "MIT")

print(f"ScanCode: {sc_result}")
print(f"FOSSology: {ff_result}")
print(f"ML Model: {ml_result}")
```

### Batch Processing
```python
# Process multiple licenses
licenses = [text1, text2, text3, ...]
results = []

for i, text in enumerate(licenses):
    sc = scancode.predict(text, f"License_{i}")
    ff = fossology.predict(text, f"License_{i}")
    ml = ml_model.predict(text, f"License_{i}")
    
    results.append({
        'index': i,
        'scancode': sc,
        'fossology': ff,
        'ml_model': ml
    })

df_results = pd.DataFrame(results)
```

### Ensemble Voting
```python
def ensemble_vote(text):
    predictions = [
        scancode.predict(text),
        fossology.predict(text),
        ml_model.predict(text)
    ]
    # Return most common prediction
    from collections import Counter
    return Counter(predictions).most_common(1)[0][0]

result = ensemble_vote("GPL-3.0 License...")
```

---

## Verification Commands

### Check Tool Availability
```python
# In notebook
print(f"ScanCode available: {scancode.available}")
print(f"FOSSology available: {fossology.available}")
print(f"ML Model available: True")
```

### Test Single Prediction
```python
# Quick test
test_text = "GNU General Public License v3.0"
result = scancode.predict(test_text, "GPL-3.0")
print(f"Result: {result}")  # Should be 'Copyleft'
```

### Run Full Verification
```python
# In notebook, run Cell #VSC-0fb83c51
# Shows:
# - Tool status
# - Test predictions
# - Error handling
# - Final summary
```

---

## Configuration Checklist

### Pre-Deployment
- [ ] Notebook runs without errors
- [ ] ScanCode installed (optional): `scancode --version` ✓
- [ ] FOSSology running (optional): `docker ps | grep fossology` ✓
- [ ] Environment variables set:
  - [ ] `FOSSOLOGY_SERVER` = "http://localhost:8080"
  - [ ] `FOSSOLOGY_TOKEN` = "your_token"
- [ ] ML model loaded: `print(type(best_model_pipeline))` ✓

### Post-Deployment
- [ ] Test with known licenses
- [ ] Verify ensemble voting works
- [ ] Check error handling with edge cases
- [ ] Monitor tool availability status
- [ ] Log prediction results

---

## API Endpoints (if serving via REST)

### POST /api/classify-license
```json
{
  "license_text": "MIT License\n...",
  "license_id": "MIT",
  "tools": ["all", "scancode", "fossology", "ml_model"],
  "ensemble": true
}
```

Response:
```json
{
  "category": "Permissive",
  "confidence": 0.95,
  "tool_results": {
    "scancode": "Permissive",
    "fossology": "Permissive",
    "ml_model": "Permissive"
  },
  "recommendation": "APPROVED",
  "processing_time_ms": 605
}
```

---

## Performance Targets

### Expected Accuracy
- ScanCode alone: 88%
- FOSSology alone: 88%
- ML Model alone: 84%
- Ensemble (voting): 92%

### Expected Speed
- ScanCode: 100ms per file
- FOSSology: 500ms per file
- ML Model: 5ms per file
- Ensemble: 605ms per file

### Expected Memory
- ScanCode: 50MB
- FOSSology: 200MB (client only)
- ML Model: 10MB
- Ensemble: 260MB combined

---

## Troubleshooting

### ScanCode Issues
```bash
# Check if installed
which scancode
# or
where scancode

# If not found: reinstall
pip install --force-reinstall scancode-toolkit

# If slow: use binary version
pip install scancode-toolkit-bin
```

### FOSSology Issues
```bash
# Check container status
docker ps -a | grep fossology

# Check logs
docker logs fossology

# Restart container
docker restart fossology

# If connection fails
# 1. Verify server running: curl http://localhost:8080
# 2. Check environment variables
# 3. Verify API token: export FOSSOLOGY_TOKEN="..."
```

### ML Model Issues
```python
# Verify pipeline loaded
print(type(best_model_pipeline))  # Should be <class 'sklearn.pipeline.Pipeline'>

# Check if model works
test_pred = best_model_pipeline.predict(['MIT License'])
print(test_pred)  # Should output array with category
```

---

## Performance Optimization

### For Speed (use ML Model only)
```python
# Fast inference
results = [ml_model.predict(text) for text in batch]
# ~720k licenses/hour
```

### For Accuracy (use Ensemble)
```python
# High accuracy voting
results = [ensemble_vote(text) for text in batch]
# ~7k licenses/hour
```

### For Balance (ScanCode + ML)
```python
# Check ScanCode first, fall back to ML
results = []
for text in batch:
    sc = scancode.predict(text)
    if sc == 'Other':
        results.append(ml_model.predict(text))
    else:
        results.append(sc)
# ~40k licenses/hour
```

---

## System Requirements

- **Python**: 3.8 or higher
- **RAM**: 512MB minimum (2GB recommended)
- **Disk**: 500MB for ScanCode database, 1GB for FOSSology
- **Network**: For FOSSology API calls (if using remote server)

---

## Support & Debugging

### Enable Verbose Output
```python
# In notebook
import logging
logging.basicConfig(level=logging.DEBUG)

# Now all tool calls will show debug info
```

### Check Available Tools
```python
print(scancode.available)
print(fossology.available)
```

### Run Verification Suite
```python
# Execute this cell in notebook:
# Cell with ID #VSC-0fb83c51
```

---

*Quick Reference v1.0*  
*Last Updated: January 15, 2026*
