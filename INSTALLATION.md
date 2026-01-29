# ✅ Installation & Verification Checklist

## Pre-Installation Checklist

- [ ] Python 3.9+ installed
- [ ] pip package manager available
- [ ] Git installed (for version control)
- [ ] 1 GB free disk space (for dependencies)
- [ ] Internet connection (for package downloads)
- [ ] Terminal/PowerShell access

## Installation Steps

### Step 1: Verify Python Installation
```bash
python --version
# Expected: Python 3.9.x or higher
```

### Step 2: Navigate to Project Directory
```bash
cd "d:\EDA\AI_Medical_Chatbot"
```

### Step 3: Create Virtual Environment (Recommended)
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
# Option A: Automated setup
python setup.py

# Option B: Manual installation
pip install -r requirements.txt
```

### Step 5: Download NLTK Data
```bash
python -m nltk.downloader stopwords punkt averaged_perceptron_tagger
```

## Post-Installation Verification

### ✅ Check Package Installation
```bash
pip list | findstr "streamlit pandas numpy matplotlib"
```

**Expected Output:**
```
matplotlib       3.6.x
matplotlib-core 3.6.x
numpy            1.23.x
pandas           1.5.x
streamlit        1.15.x
```

### ✅ Verify File Structure
```bash
# All these files should exist:
dir
  ✅ streamlit_dashboard.py
  ✅ Professional_EDA_Report.ipynb
  ✅ requirements.txt
  ✅ README.md
  ✅ QUICKSTART.md
  ✅ setup.py
  ✅ ARCHITECTURE.md
  ✅ PROJECT_SUMMARY.md
  ✅ ai-medical-chatbot.csv
  ✅ .gitignore
```

### ✅ Test Imports
```bash
python -c "import streamlit; print('✅ Streamlit:', streamlit.__version__)"
python -c "import pandas; print('✅ Pandas:', pandas.__version__)"
python -c "import numpy; print('✅ NumPy:', numpy.__version__)"
python -c "import matplotlib; print('✅ Matplotlib:', matplotlib.__version__)"
python -c "import seaborn; print('✅ Seaborn loaded')"
python -c "import nltk; print('✅ NLTK loaded')"
```

## Dashboard Launch

### Quick Start
```bash
streamlit run streamlit_dashboard.py
```

### Expected Output:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://[YOUR_IP]:8501

  For better performance, install Watchdog.

  Ready to receive client connections
```

## Browser Access

1. **Automatic:** Browser opens automatically
2. **Manual:** Open http://localhost:8501 in your browser
3. **Network:** Access from other machines using your IP + :8501

## Troubleshooting

### Issue: "streamlit command not found"
```bash
# Solution: Full path to streamlit
python -m streamlit run streamlit_dashboard.py
```

### Issue: "ModuleNotFoundError"
```bash
# Solution: Reinstall requirements
pip install --upgrade -r requirements.txt
```

### Issue: "Port 8501 already in use"
```bash
# Solution: Use different port
streamlit run streamlit_dashboard.py --server.port 8502
```

### Issue: "CSV file not found"
```bash
# Solution: Verify file exists in current directory
# Expected: d:\EDA\AI_Medical_Chatbot\ai-medical-chatbot.csv
```

### Issue: "Out of memory"
```bash
# Solution: Close other applications
# The dataset is 254.88 MB, needs ~1 GB RAM with dependencies
```

## First-Time User Guide

### When You First Run the Dashboard:

1. **Loading Screen**
   - Wait for data to load (30-60 seconds)
   - You'll see "Running" in bottom right
   - Don't close the terminal

2. **Home Page**
   - Review quick statistics
   - Check dataset info
   - Read welcome message

3. **Dataset Overview**
   - Explore columns and types
   - View sample data
   - Check memory usage

4. **Data Quality Page**
   - Verify no critical issues
   - Review missing values
   - Check duplicates

5. **Medical Domain Analysis**
   - Select categorical column
   - Review category distribution
   - Check balance metrics

6. **Key Findings**
   - Review overall readiness score
   - Read recommendations
   - Plan next steps

## Performance Expectations

| Task | Time | Notes |
|------|------|-------|
| Data Loading | 30-60 sec | First time, then cached |
| Page Switch | 1-2 sec | Instant after first load |
| Visualization | 1-3 sec | Depends on chart complexity |
| Full Report | 2-5 min | All pages rendered |

## Memory Usage

```
Component              Memory
─────────────────────────────
DataFrame (CSV)        200-300 MB
Streamlit Cache        50-100 MB
Visualizations         10-20 MB
Pandas/NumPy Ops       50-100 MB
─────────────────────────────
Total Runtime          400-600 MB
```

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.9 | 3.10+ |
| RAM | 2 GB | 4 GB+ |
| Storage | 1 GB | 2 GB |
| Disk I/O | Standard | SSD |
| Network | Not needed | N/A |

## Verify Dashboard Works

### Test 1: Navigation
- [ ] Click through all sidebar pages
- [ ] Each page loads without errors
- [ ] All metrics display correctly

### Test 2: Visualizations
- [ ] Charts render properly
- [ ] Colors display correctly
- [ ] No distorted text

### Test 3: Data Display
- [ ] Tables show all data
- [ ] Numbers format correctly
- [ ] Percentages calculate right

### Test 4: Interactivity
- [ ] Dropdowns work (if present)
- [ ] Filters respond
- [ ] No UI lag

## Verification Script

```bash
# Run this to verify everything
python -c "
import sys
print('Python:', sys.version)
print()
print('Testing imports...')
try:
    import streamlit; print('✅ Streamlit')
except: print('❌ Streamlit')
try:
    import pandas; print('✅ Pandas')
except: print('❌ Pandas')
try:
    import numpy; print('✅ NumPy')
except: print('❌ NumPy')
try:
    import matplotlib; print('✅ Matplotlib')
except: print('❌ Matplotlib')
try:
    import seaborn; print('✅ Seaborn')
except: print('❌ Seaborn')
try:
    import nltk; print('✅ NLTK')
except: print('❌ NLTK')
try:
    import sklearn; print('✅ Scikit-learn')
except: print('❌ Scikit-learn')
print()
print('All checks complete!')
"
```

## Common Issues & Solutions

### Issue 1: Slow Performance
**Symptoms:** Dashboard responds slowly
**Solutions:**
1. Close other applications
2. Increase available RAM
3. Use SSD for better I/O
4. Clear browser cache

### Issue 2: Data Not Loading
**Symptoms:** Error about CSV file
**Solutions:**
1. Verify file exists in directory
2. Check file isn't corrupted
3. Ensure read permissions
4. Try with full path

### Issue 3: Missing Dependencies
**Symptoms:** Import errors
**Solutions:**
1. Reinstall requirements: `pip install -r requirements.txt`
2. Use virtual environment
3. Check Python version
4. Update pip: `python -m pip install --upgrade pip`

### Issue 4: Port Already in Use
**Symptoms:** "Port 8501 is already in use"
**Solutions:**
1. Kill existing process
2. Use different port: `--server.port 8502`
3. Wait a few minutes and retry
4. Restart terminal/IDE

## Success Indicators

✅ **Installation is successful when:**
- [ ] `python setup.py` runs without errors
- [ ] `pip list` shows all required packages
- [ ] All test imports work
- [ ] `streamlit run streamlit_dashboard.py` launches
- [ ] Browser opens to localhost:8501
- [ ] Dashboard displays data correctly
- [ ] All navigation pages work
- [ ] No error messages in terminal

## Next Steps After Verification

1. ✅ **Explore the Dashboard**
   - Visit each page
   - Review all metrics
   - Take screenshots if needed

2. ✅ **Review Documentation**
   - Read README.md
   - Check ARCHITECTURE.md
   - Review QUICKSTART.md

3. ✅ **Plan Data Processing**
   - Use preprocessing guide
   - Implement data cleaning
   - Engineer features

4. ✅ **Model Development**
   - Follow model recommendations
   - Set up training environment
   - Fine-tune models

5. ✅ **Deployment**
   - Containerize application
   - Set up API server
   - Deploy to production

## Support Resources

| Resource | Purpose | Link |
|----------|---------|------|
| README.md | Full documentation | Local file |
| QUICKSTART.md | Quick setup | Local file |
| ARCHITECTURE.md | System design | Local file |
| Streamlit Docs | Framework help | streamlit.io |
| Pandas Docs | Data processing | pandas.pydata.org |
| NLTK Book | NLP learning | nltk.org/book |

## Validation Checklist

### Pre-Run Checklist
- [ ] Python 3.9+ verified
- [ ] Virtual env activated
- [ ] All packages installed
- [ ] CSV file present
- [ ] Directory correct

### Post-Run Checklist
- [ ] Dashboard loads
- [ ] No error messages
- [ ] Data displays correctly
- [ ] Navigation works
- [ ] Metrics show values

### Functionality Checklist
- [ ] Home page loads
- [ ] Dataset overview works
- [ ] Data quality shows metrics
- [ ] Statistics calculate
- [ ] Medical analysis works
- [ ] NLP analysis works
- [ ] Key findings display
- [ ] Preprocessing guide shows
- [ ] Model recommendations show

## Performance Tuning (Optional)

### For Better Performance:
```bash
# Use faster dataframe operations
# Consider using polars instead of pandas
pip install polars

# Enable Streamlit fast reruns
# Already configured in dashboard
```

### For Production:
```bash
# Install production dependencies
pip install gunicorn
pip install nginx

# Create requirements-prod.txt
# with only essential packages
```

## Maintenance

### Regular Tasks:
- [ ] Update packages monthly: `pip install --upgrade -r requirements.txt`
- [ ] Clear cache: `streamlit cache clear`
- [ ] Backup data: Copy CSV to backup location
- [ ] Check disk space: Ensure > 500 MB free

### As Needed:
- [ ] Add new columns to analysis
- [ ] Update documentation
- [ ] Add new visualizations
- [ ] Optimize code

---

**Installation Complete!** 🎉

Your AI Medical Chatbot EDA Dashboard is ready to use.

For questions or issues, refer to the documentation files in the project directory.

Happy analyzing! 📊
