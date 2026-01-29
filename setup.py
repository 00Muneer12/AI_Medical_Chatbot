#!/usr/bin/env python
"""
Setup script for AI Medical Chatbot EDA Dashboard
Helps with initial configuration and dependency installation
"""

import subprocess
import sys
import os
from pathlib import Path

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")

def check_python_version():
    """Check if Python version is 3.9 or higher"""
    print_header("Checking Python Version")
    
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("❌ ERROR: Python 3.9+ required")
        sys.exit(1)
    
    print("✅ Python version is compatible")
    return True

def install_requirements():
    """Install required packages"""
    print_header("Installing Dependencies")
    
    try:
        print("📦 Installing packages from requirements.txt...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "-r", "requirements.txt"
        ])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def download_nltk_data():
    """Download required NLTK data"""
    print_header("Downloading NLTK Data")
    
    try:
        import nltk
        
        print("📥 Downloading stopwords...")
        nltk.download('stopwords')
        
        print("📥 Downloading punkt...")
        nltk.download('punkt')
        
        print("📥 Downloading averaged_perceptron_tagger...")
        nltk.download('averaged_perceptron_tagger')
        
        print("✅ NLTK data downloaded successfully")
    except Exception as e:
        print(f"⚠️  Warning: Could not download NLTK data: {e}")
        print("   You can download it manually later using:")
        print("   python -m nltk.downloader stopwords punkt averaged_perceptron_tagger")

def verify_data_file():
    """Verify dataset file exists"""
    print_header("Verifying Dataset")
    
    csv_path = Path('ai-medical-chatbot.csv')
    
    if csv_path.exists():
        size_mb = csv_path.stat().st_size / (1024 * 1024)
        print(f"✅ Dataset found: {csv_path.name}")
        print(f"   Size: {size_mb:.2f} MB")
        return True
    else:
        print(f"⚠️  Dataset not found: {csv_path}")
        print("   Please ensure 'ai-medical-chatbot.csv' is in the current directory")
        return False

def verify_notebooks():
    """Verify notebook files exist"""
    print_header("Verifying Notebook Files")
    
    notebook_path = Path('Professional_EDA_Report.ipynb')
    
    if notebook_path.exists():
        print(f"✅ Notebook found: {notebook_path.name}")
        return True
    else:
        print(f"⚠️  Notebook not found: {notebook_path}")
        return False

def main():
    """Main setup function"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  🏥 AI Medical Chatbot - EDA Dashboard Setup".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "="*68 + "╝")
    
    # Step 1: Check Python version
    check_python_version()
    
    # Step 2: Verify files
    verify_data_file()
    verify_notebooks()
    
    # Step 3: Install requirements
    try:
        install_requirements()
    except KeyboardInterrupt:
        print("\n❌ Installation cancelled")
        sys.exit(1)
    
    # Step 4: Download NLTK data
    download_nltk_data()
    
    # Final summary
    print_header("Setup Complete!")
    
    print("✅ All setup steps completed successfully!\n")
    print("📊 Next Steps:\n")
    print("   1. Launch the Streamlit Dashboard:")
    print("      streamlit run streamlit_dashboard.py\n")
    print("   2. View the Jupyter Notebook:")
    print("      jupyter notebook Professional_EDA_Report.ipynb\n")
    print("   3. Read the documentation:")
    print("      - README.md for overview")
    print("      - requirements.txt for dependencies\n")
    print("🌐 Dashboard URL (after running):")
    print("   http://localhost:8501\n")
    print("="*70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during setup: {e}")
        sys.exit(1)
