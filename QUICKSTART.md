# 🚀 Quick Start Guide

## Installation & Setup (5 minutes)

### Option 1: Automated Setup (Recommended)

```bash
# Run the setup script
python setup.py

# This will:
# ✅ Check Python version
# ✅ Install all dependencies
# ✅ Download NLTK data
# ✅ Verify dataset files
```

### Option 2: Manual Setup

```bash
# 1. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download NLTK data
python -m nltk.downloader stopwords punkt averaged_perceptron_tagger
```

---

## 🎯 Launch the Dashboard (1 minute)

```bash
streamlit run streamlit_dashboard.py
```

✅ **Dashboard opens at:** http://localhost:8501

### Dashboard Navigation

| Section | What You'll See |
|---------|-----------------|
| 🏠 Home | Quick stats & overview |
| 📊 Dataset Overview | Columns, types, structure |
| 🔍 Data Quality | Missing values, duplicates |
| 📈 Statistical Analysis | Distributions, statistics |
| 🏥 Medical Domain | Disease/intent categories |
| 📝 NLP Analysis | Text patterns, keywords |
| 🎯 Key Findings | Overall assessment |
| 🔧 Preprocessing | Data pipeline guide |
| 🤖 Model Recommendations | Best practices |

---

## 📓 View Detailed Analysis (Optional)

```bash
# Option 1: Jupyter Notebook
jupyter notebook Professional_EDA_Report.ipynb

# Option 2: JupyterLab
jupyter lab Professional_EDA_Report.ipynb

# Option 3: Export to HTML
jupyter nbconvert --to html Professional_EDA_Report.ipynb
```

---

## 📊 What's in the Dashboard?

### Data Quality Metrics
- ✅ Missing values analysis
- ✅ Duplicate detection
- ✅ Data completeness score
- ✅ Overall quality assessment

### Statistical Insights
- 📈 Distribution analysis
- 📊 Summary statistics
- 📉 Trend visualization
- 🔍 Outlier detection

### Medical Domain Analysis
- 🏥 Disease/Intent categories
- ⚖️ Category balance
- 📊 Domain coverage
- 🎯 Imbalance assessment

### NLP Insights
- 📝 Question/Answer analysis
- 📚 Text length patterns
- 🔤 Keyword extraction
- 📖 Vocabulary diversity

### Model Readiness
- ✅ Training readiness score
- 📋 Preprocessing checklist
- 🤖 Model recommendations
- 🚀 Deployment guidelines

---

## 🔧 Common Tasks

### Export Data to CSV
```python
import pandas as pd

df = pd.read_csv('ai-medical-chatbot.csv')

# Clean data
df = df.drop_duplicates()
df = df.dropna()

# Save
df.to_csv('ai-medical-chatbot-cleaned.csv', index=False)
```

### Analyze Specific Column
```python
import pandas as pd

df = pd.read_csv('ai-medical-chatbot.csv')

# Get column info
print(f"Unique values: {df['column_name'].nunique()}")
print(f"Most common: {df['column_name'].value_counts().head()}")
print(f"Missing: {df['column_name'].isna().sum()}")
```

### Generate Preprocessing Code
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv('ai-medical-chatbot.csv')

# Train/test split (80/20)
train, test = train_test_split(df, test_size=0.2, random_state=42)

# Stratified split by category
train, test = train_test_split(
    df, test_size=0.2, 
    stratify=df['category'],  # Balance categories
    random_state=42
)

# Scale numeric features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(train.select_dtypes(include=['number']))
```

---

## 📚 Key Statistics to Check

After launching the dashboard, verify:

| Metric | Expected Value | Status |
|--------|---|---|
| Data Completeness | > 95% | ✅ |
| Duplicate Records | < 1% | ✅ |
| Missing Values | < 5% | ✅ |
| Text Columns | ≥ 2 | ✅ |
| Unique Categories | > 10 | ✅ |

---

## 🐛 Troubleshooting

### Dashboard won't start?
```bash
# Clear Streamlit cache
streamlit cache clear

# Try different port
streamlit run streamlit_dashboard.py --server.port 8502
```

### Data not loading?
```python
# Check if file exists and is accessible
import os
print(os.path.exists('ai-medical-chatbot.csv'))
print(os.path.getsize('ai-medical-chatbot.csv') / 1024**2)  # Size in MB
```

### Dependencies not installing?
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Try installing individually
pip install pandas numpy matplotlib seaborn streamlit
```

---

## 📖 Documentation

- **README.md** - Full project documentation
- **requirements.txt** - All dependencies
- **Professional_EDA_Report.ipynb** - Detailed analysis notebook
- **streamlit_dashboard.py** - Dashboard source code

---

## 🚀 Next Steps

1. ✅ **Explore the Dashboard** - Get familiar with your data
2. ✅ **Review Key Findings** - Check data quality metrics
3. ✅ **Run Preprocessing** - Clean and prepare data
4. ✅ **Train Models** - Follow model recommendations
5. ✅ **Deploy Chatbot** - Follow deployment guide

---

## 💡 Tips

- **First Time?** → Start with the Home page
- **Need Stats?** → Check Dataset Overview
- **Data Issues?** → Go to Data Quality section
- **Training Models?** → See Model Recommendations
- **Ready for Deployment?** → Check Key Findings

---

## ⏱️ Time Estimates

| Task | Time |
|------|------|
| Setup | 5 min |
| Dashboard Exploration | 10-15 min |
| Full Dashboard Review | 30-45 min |
| Notebook Analysis | 1-2 hours |
| Data Preprocessing | 2-4 hours |
| Model Training | 4-8 hours |

---

## 📞 Need Help?

1. Check README.md for detailed documentation
2. Review the Jupyter notebook for examples
3. Check Streamlit documentation: https://docs.streamlit.io
4. NLTK documentation: https://www.nltk.org

---

**Ready? Let's go! 🎉**

```bash
streamlit run streamlit_dashboard.py
```

Your dashboard awaits at **http://localhost:8501** 🚀
