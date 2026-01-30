# Streamlit Cloud Deployment Guide

## ✅ Repository Status
- **GitHub URL**: https://github.com/00Muneer12/AI_Medical_Chatbot.git
- **Branch**: main
- **Main File**: streamlit_dashboard.py
- **Status**: Code successfully pushed to GitHub ✅

## 🚀 Deploy on Streamlit Cloud

### Option 1: Quick Deploy (Recommended)
1. Go to **https://share.streamlit.io/**
2. Click **"New app"** button (top-right)
3. Fill in the deployment form:
   - **Repository**: `https://github.com/00Muneer12/AI_Medical_Chatbot.git`
   - **Branch**: `main`
   - **Main file path**: `streamlit_dashboard.py`
4. Click **"Deploy"**
5. Wait 2-5 minutes for deployment to complete
6. Your app will be available at:
   ```
   https://share.streamlit.io/00Muneer12/AI_Medical_Chatbot
   ```

### Option 2: Deploy with GitHub Authentication
1. Visit https://share.streamlit.io/
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select your repository and branch from the dropdown
5. Click **"Deploy"**

## 📝 Important Notes

### Data File Handling
- The `ai-medical-chatbot.csv` file is **excluded from GitHub** because it's 254.88 MB
- The Streamlit Cloud app will show an informational message about the missing CSV
- **For local use**: Place the CSV file in the project directory
- **For Cloud deployment**: The dashboard code and all visualization logic is available

### Alternative: Upload CSV to Cloud
If you want the data available in the cloud:

**Option A: Use Streamlit Secrets**
```bash
# 1. Create secrets file locally
mkdir -p .streamlit
echo 'csv_url = "https://your-cloud-storage-url/ai-medical-chatbot.csv"' > .streamlit/secrets.toml

# 2. Update streamlit_dashboard.py to use the URL
# 3. Push to GitHub
# 4. Add secret to Streamlit Cloud dashboard
```

**Option B: Use External Cloud Storage**
- Upload CSV to Google Cloud Storage, AWS S3, or Dropbox
- Update the app to download from the cloud URL
- Add authentication tokens as Streamlit secrets

## ⚙️ Deployment Troubleshooting

| Issue | Solution |
|-------|----------|
| "Repository not found" | Check GitHub URL and ensure repo is public |
| "File not found" | Verify `streamlit_dashboard.py` is at root of repo |
| "CSV not loaded" | This is expected - see "Data File Handling" section |
| "App crashes during deploy" | Check `requirements.txt` - ensure all packages listed |
| "Slow load times" | Normal for first deployment (2-5 min), subsequent loads are faster |

## ✨ Features Available in Cloud
✅ All 9 dashboard pages
✅ Data visualizations (without CSV data)
✅ Interactive filtering and exploration
✅ Code and documentation access
✅ Real-time updates from GitHub

## 📊 Local vs Cloud

### Local Development
```bash
cd d:\EDA\AI_Medical_Chatbot
streamlit run streamlit_dashboard.py
# Access at http://localhost:8501
```

### Cloud Deployment
- Access via: https://share.streamlit.io/00Muneer12/AI_Medical_Chatbot
- Auto-updates when you push to GitHub
- No local CSV file needed for code sharing

## 🔄 Update Dashboard in Cloud
Simply push changes to GitHub:
```bash
git add .
git commit -m "Update dashboard"
git push origin main
```
Streamlit Cloud will auto-detect changes and redeploy within minutes.

## 📞 Support
- **Streamlit Docs**: https://docs.streamlit.io/
- **GitHub Issues**: Create issue in your repository
- **Community Forum**: https://discuss.streamlit.io/

---
**Created**: 2024
**Last Updated**: Configuration for GitHub + Streamlit Cloud
