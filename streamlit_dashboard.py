import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
import warnings

warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="AI Medical Chatbot - EDA Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# SIDEBAR CONFIGURATION
# ============================================================================

st.sidebar.markdown("# 📋 Navigation")
page = st.sidebar.radio("Select a page:", [
    "🏠 Home",
    "📊 Dataset Overview",
    "🔍 Data Quality",
    "📈 Statistical Analysis",
    "🏥 Medical Domain Analysis",
    "📝 NLP Analysis",
    "🎯 Key Findings",
    "🔧 Preprocessing Guide",
    "🤖 Model Recommendations"
])

st.sidebar.markdown("---")
st.sidebar.markdown("### 📁 Dataset Info")
st.sidebar.write("**File:** ai-medical-chatbot.csv")
st.sidebar.write("**Size:** 254.88 MB")
st.sidebar.write("**Status:** ✅ Ready for Analysis")

# ============================================================================
# LOAD DATA
# ============================================================================

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('ai-medical-chatbot.csv')
        return df
    except FileNotFoundError:
        st.error("❌ Dataset not found. Please ensure 'ai-medical-chatbot.csv' is in the current directory.")
        return None

df = load_data()

if df is None:
    st.stop()

# ============================================================================
# PAGE: HOME
# ============================================================================

if page == "🏠 Home":
    st.title("🏥 AI Medical Chatbot - EDA Dashboard")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="📦 Total Records", value=f"{df.shape[0]:,}")
    with col2:
        st.metric(label="🏷️ Features", value=df.shape[1])
    with col3:
        st.metric(label="💾 Dataset Size", value="254.88 MB")
    
    st.markdown("---")
    
    st.markdown("""
    ## Welcome to the EDA Dashboard 👋
    
    This comprehensive dashboard provides **Exploratory Data Analysis** for the AI Medical Chatbot dataset.
    Navigate using the sidebar to explore different aspects of the data.
    
    ### 📚 What's Included:
    
    ✅ **Dataset Overview** - Structure, shape, and composition  
    ✅ **Data Quality** - Missing values, duplicates, and integrity checks  
    ✅ **Statistical Analysis** - Descriptive statistics and distributions  
    ✅ **Medical Domain Analysis** - Disease/intent classification distribution  
    ✅ **NLP Analysis** - Text length, keywords, and vocabulary analysis  
    ✅ **Key Findings** - Summary of insights and recommendations  
    ✅ **Preprocessing Guide** - Step-by-step data preparation pipeline  
    ✅ **Model Recommendations** - Best practices for chatbot model training  
    
    ### 🎯 Quick Stats:
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    missing_pct = (df.isnull().sum().sum() / (df.shape[0] * df.shape[1])) * 100
    duplicates_pct = (df.duplicated().sum() / df.shape[0]) * 100
    text_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    with col1:
        st.metric("Data Completeness", f"{100 - missing_pct:.1f}%")
    with col2:
        st.metric("Unique Records", f"{(1 - duplicates_pct/100)*100:.1f}%")
    with col3:
        st.metric("Text Columns", len(text_cols))
    with col4:
        st.metric("Categorical Cols", len(df.select_dtypes(include=['object']).columns))

# ============================================================================
# PAGE: DATASET OVERVIEW
# ============================================================================

elif page == "📊 Dataset Overview":
    st.title("📊 Dataset Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Column Information")
        info_data = []
        for col in df.columns:
            info_data.append({
                "Column": col,
                "Type": str(df[col].dtype),
                "Non-Null": df[col].notna().sum(),
                "Null": df[col].isna().sum()
            })
        info_df = pd.DataFrame(info_data)
        st.dataframe(info_df, use_container_width=True)
    
    with col2:
        st.subheader("📈 Data Type Distribution")
        dtype_counts = df.dtypes.value_counts()
        fig, ax = plt.subplots(figsize=(8, 6))
        colors = plt.cm.Set3(np.linspace(0, 1, len(dtype_counts)))
        ax.pie(dtype_counts.values, labels=dtype_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
        ax.set_title('Data Type Distribution', fontsize=12, fontweight='bold')
        st.pyplot(fig)
    
    st.markdown("---")
    
    st.subheader("👀 First Few Rows")
    st.dataframe(df.head(5), use_container_width=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Rows", f"{df.shape[0]:,}")
    with col2:
        st.metric("Total Columns", df.shape[1])
    with col3:
        memory = df.memory_usage(deep=True).sum() / 1024**2
        st.metric("Memory Usage", f"{memory:.2f} MB")

# ============================================================================
# PAGE: DATA QUALITY
# ============================================================================

elif page == "🔍 Data Quality":
    st.title("🔍 Data Quality Assessment")
    
    col1, col2 = st.columns(2)
    
    # Missing Values
    with col1:
        st.subheader("❌ Missing Values")
        missing_data = df.isnull().sum()
        missing_pct = (missing_data / len(df)) * 100
        missing_summary = pd.DataFrame({
            'Column': missing_data.index,
            'Missing Count': missing_data.values,
            'Missing %': missing_pct.values
        })
        st.dataframe(missing_summary[missing_summary['Missing Count'] > 0], use_container_width=True)
        
        if missing_data.sum() == 0:
            st.success("✅ No missing values detected!")
    
    # Duplicates
    with col2:
        st.subheader("🔄 Duplicate Records")
        duplicate_count = df.duplicated().sum()
        duplicate_pct = (duplicate_count / len(df)) * 100
        st.metric("Duplicate Records", f"{duplicate_count:,} ({duplicate_pct:.2f}%)")
        if duplicate_count == 0:
            st.success("✅ No duplicate records found!")
        else:
            st.warning(f"⚠️ {duplicate_count:,} duplicate records detected")
    
    st.markdown("---")
    
    # Missing values visualization
    if missing_data.sum() > 0:
        st.subheader("📊 Missing Values by Column")
        fig, ax = plt.subplots(figsize=(12, 6))
        colors = ['#27ae60' if x == 0 else '#f39c12' if x < 5 else '#e74c3c' for x in missing_pct]
        ax.barh(missing_data.index, missing_data.values, color=colors)
        ax.set_xlabel('Count of Missing Values', fontweight='bold')
        ax.set_title('Missing Values Distribution', fontsize=12, fontweight='bold')
        st.pyplot(fig)
    
    st.markdown("---")
    
    st.subheader("📈 Data Quality Score")
    total_missing = missing_data.sum()
    missing_pct_total = (total_missing / (df.shape[0] * df.shape[1])) * 100
    completeness = 100 - missing_pct_total
    uniqueness = 100 - (duplicate_pct if duplicate_count > 0 else 0)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Data Completeness", f"{completeness:.2f}%")
    with col2:
        st.metric("Uniqueness Score", f"{uniqueness:.2f}%")
    with col3:
        overall_quality = (completeness + uniqueness) / 2
        st.metric("Overall Quality", f"{overall_quality:.2f}%")

# ============================================================================
# PAGE: STATISTICAL ANALYSIS
# ============================================================================

elif page == "📈 Statistical Analysis":
    st.title("📈 Statistical Analysis")
    
    # Numeric columns analysis
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if numeric_cols:
        st.subheader("📊 Numeric Columns Statistics")
        stats_df = df[numeric_cols].describe().T
        st.dataframe(stats_df, use_container_width=True)
        
        st.markdown("---")
        
        # Distribution plots
        st.subheader("📉 Distribution Plots")
        for col in numeric_cols[:4]:  # Limit to first 4 numeric columns
            col_name = col
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.hist(df[col].dropna(), bins=30, color='#3498db', edgecolor='black', alpha=0.7)
            ax.set_xlabel(col_name, fontweight='bold')
            ax.set_ylabel('Frequency', fontweight='bold')
            ax.set_title(f'Distribution of {col_name}', fontsize=12, fontweight='bold')
            st.pyplot(fig)
    else:
        st.info("ℹ️ No numeric columns found in dataset")
    
    # Text column statistics
    st.markdown("---")
    st.subheader("📝 Text Column Statistics")
    
    text_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    if text_cols:
        selected_col = st.selectbox("Select a text column:", text_cols)
        
        text_data = df[selected_col].fillna('').astype(str)
        char_lengths = text_data.str.len()
        word_counts = text_data.str.split().str.len()
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Mean Length (chars)", f"{char_lengths.mean():.0f}")
        with col2:
            st.metric("Median Length (chars)", f"{char_lengths.median():.0f}")
        with col3:
            st.metric("Mean Words", f"{word_counts.mean():.1f}")
        with col4:
            st.metric("Max Length", f"{char_lengths.max()}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.hist(char_lengths, bins=40, color='#3498db', edgecolor='black', alpha=0.7)
            ax.axvline(char_lengths.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {char_lengths.mean():.0f}')
            ax.set_xlabel('Character Length', fontweight='bold')
            ax.set_ylabel('Frequency', fontweight='bold')
            ax.set_title(f'Length Distribution - {selected_col}', fontsize=12, fontweight='bold')
            ax.legend()
            st.pyplot(fig)
        
        with col2:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.hist(word_counts, bins=40, color='#e74c3c', edgecolor='black', alpha=0.7)
            ax.axvline(word_counts.mean(), color='blue', linestyle='--', linewidth=2, label=f'Mean: {word_counts.mean():.1f}')
            ax.set_xlabel('Word Count', fontweight='bold')
            ax.set_ylabel('Frequency', fontweight='bold')
            ax.set_title(f'Word Count Distribution - {selected_col}', fontsize=12, fontweight='bold')
            ax.legend()
            st.pyplot(fig)

# ============================================================================
# PAGE: MEDICAL DOMAIN ANALYSIS
# ============================================================================

elif page == "🏥 Medical Domain Analysis":
    st.title("🏥 Medical Domain Analysis")
    
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    if categorical_cols:
        selected_col = st.selectbox("Select a categorical column:", categorical_cols)
        
        category_counts = df[selected_col].value_counts()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Total Categories", df[selected_col].nunique())
        with col2:
            imbalance_ratio = category_counts.max() / category_counts.min() if category_counts.min() > 0 else 0
            st.metric("Imbalance Ratio", f"{imbalance_ratio:.2f}:1")
        
        st.markdown("---")
        
        # Top categories
        st.subheader(f"🏷️ Top 15 {selected_col} Categories")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            top_15 = category_counts.head(15)
            display_df = pd.DataFrame({
                'Rank': range(1, len(top_15) + 1),
                'Category': [str(x)[:40] for x in top_15.index],
                'Count': top_15.values,
                'Percentage': (top_15.values / len(df) * 100).round(2)
            })
            st.dataframe(display_df, use_container_width=True)
        
        with col2:
            fig, ax = plt.subplots(figsize=(10, 8))
            colors = plt.cm.Set3(np.linspace(0, 1, len(top_15)))
            ax.barh(range(len(top_15)), top_15.values, color=colors, edgecolor='black')
            ax.set_yticks(range(len(top_15)))
            ax.set_yticklabels([str(x)[:30] for x in top_15.index], fontsize=9)
            ax.set_xlabel('Frequency', fontweight='bold')
            ax.set_title(f'Top 15 {selected_col} Distribution', fontsize=12, fontweight='bold')
            ax.invert_yaxis()
            st.pyplot(fig)
        
        st.markdown("---")
        
        # Category balance analysis
        st.subheader("⚖️ Category Balance Analysis")
        
        balance_status = "WELL-BALANCED" if imbalance_ratio < 2 else "MODERATELY IMBALANCED" if imbalance_ratio < 5 else "HIGHLY IMBALANCED"
        coverage = "EXCELLENT" if df[selected_col].nunique() > 50 else "GOOD" if df[selected_col].nunique() > 20 else "MODERATE"
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"""
            **Balance Status:** {balance_status}
            
            **Category Diversity:** {coverage}
            
            **Total Categories:** {df[selected_col].nunique()}
            
            **Avg samples/category:** {len(df) / df[selected_col].nunique():.0f}
            """)
        
        with col2:
            fig, ax = plt.subplots(figsize=(8, 6))
            data_to_plot = [category_counts.values]
            bp = ax.boxplot(data_to_plot, vert=True, patch_artist=True)
            bp['boxes'][0].set_facecolor('#3498db')
            ax.set_ylabel('Count', fontweight='bold')
            ax.set_title('Category Count Distribution', fontsize=12, fontweight='bold')
            ax.set_xticklabels([selected_col])
            st.pyplot(fig)
    else:
        st.info("ℹ️ No categorical columns found")

# ============================================================================
# PAGE: NLP ANALYSIS
# ============================================================================

elif page == "📝 NLP Analysis":
    st.title("📝 NLP & Text Analysis")
    
    text_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    if len(text_cols) >= 2:
        col1, col2 = st.columns(2)
        with col1:
            question_col = st.selectbox("Question/Query Column:", text_cols)
        with col2:
            answer_col = st.selectbox("Answer/Response Column:", text_cols, index=min(1, len(text_cols)-1))
        
        q_data = df[question_col].fillna('').astype(str)
        a_data = df[answer_col].fillna('').astype(str)
        
        q_lengths = q_data.str.len()
        q_words = q_data.str.split().str.len()
        a_lengths = a_data.str.len()
        a_words = a_data.str.split().str.len()
        
        st.markdown("---")
        
        st.subheader("📊 Q&A Length Comparison")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Avg Q Length", f"{q_lengths.mean():.0f}")
        with col2:
            st.metric("Avg A Length", f"{a_lengths.mean():.0f}")
        with col3:
            st.metric("Avg Q Words", f"{q_words.mean():.1f}")
        with col4:
            st.metric("Avg A Words", f"{a_words.mean():.1f}")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig, ax = plt.subplots(figsize=(10, 5))
            data_to_plot = [q_lengths, a_lengths]
            bp = ax.boxplot(data_to_plot, labels=['Questions', 'Answers'], patch_artist=True)
            bp['boxes'][0].set_facecolor('#3498db')
            bp['boxes'][1].set_facecolor('#e74c3c')
            ax.set_ylabel('Character Length', fontweight='bold')
            ax.set_title('Q&A Length Comparison', fontsize=12, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
            st.pyplot(fig)
        
        with col2:
            fig, ax = plt.subplots(figsize=(10, 5))
            data_to_plot = [q_words, a_words]
            bp = ax.boxplot(data_to_plot, labels=['Questions', 'Answers'], patch_artist=True)
            bp['boxes'][0].set_facecolor('#3498db')
            bp['boxes'][1].set_facecolor('#e74c3c')
            ax.set_ylabel('Word Count', fontweight='bold')
            ax.set_title('Q&A Word Count Comparison', fontsize=12, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
            st.pyplot(fig)
    else:
        st.info("ℹ️ Need at least 2 text columns for Q&A analysis")

# ============================================================================
# PAGE: KEY FINDINGS
# ============================================================================

elif page == "🎯 Key Findings":
    st.title("🎯 Key Findings & Recommendations")
    
    missing_pct_total = (df.isnull().sum().sum() / (df.shape[0] * df.shape[1])) * 100
    duplicate_pct = (df.duplicated().sum() / df.shape[0]) * 100
    completeness = 100 - missing_pct_total
    uniqueness = 100 - duplicate_pct
    overall_readiness = (completeness + uniqueness) / 2
    
    # Quality score
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Data Completeness", f"{completeness:.1f}%")
    with col2:
        st.metric("Uniqueness", f"{uniqueness:.1f}%")
    with col3:
        st.metric("Overall Readiness", f"{overall_readiness:.1f}%")
    
    st.markdown("---")
    
    readiness_status = "READY FOR PRODUCTION" if overall_readiness >= 85 else "READY FOR TRAINING" if overall_readiness >= 75 else "REQUIRES PREPROCESSING"
    
    st.subheader(f"📌 Overall Status: {readiness_status}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        ### Dataset Assessment
        
        ✅ **Total Records:** {df.shape[0]:,}  
        ✅ **Features:** {df.shape[1]}  
        ✅ **Memory:** {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB  
        
        ### Data Quality Summary
        
        - **Completeness Score:** {completeness:.1f}%
        - **Duplicate Records:** {duplicate_pct:.2f}%
        - **Missing Values:** {missing_pct_total:.2f}%
        
        ### Recommendation
        
        The dataset is **{readiness_status.lower()}**. 
        Proceed with model development while maintaining data quality checks.
        """)
    
    with col2:
        fig, ax = plt.subplots(figsize=(6, 6))
        readiness_text = f"{overall_readiness:.0f}%"
        colors_gauge = ['#27ae60'] if overall_readiness >= 85 else ['#f39c12'] if overall_readiness >= 75 else ['#e74c3c']
        
        circle = plt.Circle((0.5, 0.5), 0.4, color=colors_gauge[0], alpha=0.3)
        ax.add_patch(circle)
        ax.text(0.5, 0.5, readiness_text, ha='center', va='center', fontsize=40, fontweight='bold')
        ax.text(0.5, 0.15, readiness_status, ha='center', va='center', fontsize=10, fontweight='bold')
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        st.pyplot(fig)

# ============================================================================
# PAGE: PREPROCESSING GUIDE
# ============================================================================

elif page == "🔧 Preprocessing Guide":
    st.title("🔧 Data Preprocessing Guide")
    
    st.markdown("""
    ## Step-by-Step Preprocessing Pipeline
    
    ### Phase 1: Data Cleaning
    
    **1.1 Handle Missing Values**
    - Review missing value patterns
    - Apply appropriate imputation strategy
    - Drop or fill based on data type
    
    **1.2 Remove Duplicates**
    ```python
    df.drop_duplicates(inplace=True)
    ```
    
    **1.3 Text Normalization**
    - Convert to lowercase
    - Remove extra whitespace
    - Remove special characters
    
    ### Phase 2: Text Processing
    
    **2.1 Tokenization**
    - Break text into tokens
    - Use NLTK or spaCy
    
    **2.2 Stopword Removal**
    - Remove common words
    - Keep medical domain terms
    
    **2.3 Lemmatization**
    - Reduce words to base form
    - Improve vocabulary consistency
    
    ### Phase 3: Feature Engineering
    
    **3.1 Text Vectorization**
    - TF-IDF: Weighted term frequency
    - Word2Vec: Dense embeddings
    - BERT: Contextual embeddings
    
    **3.2 Feature Creation**
    - Text length features
    - Word count features
    - Category encoding
    
    ### Phase 4: Train/Test Split
    
    **4.1 Data Splitting**
    ```python
    from sklearn.model_selection import train_test_split
    train_data, test_data = train_test_split(
        df, test_size=0.2, random_state=42
    )
    ```
    
    **4.2 Stratified Sampling**
    - Maintain class distribution
    - Use for imbalanced data
    
    ### Code Example
    
    ```python
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    
    # Load data
    df = pd.read_csv('ai-medical-chatbot.csv')
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.dropna()
    
    # Split data
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    
    # Normalize numeric features
    scaler = StandardScaler()
    train_scaled = scaler.fit_transform(train)
    ```
    """)

# ============================================================================
# PAGE: MODEL RECOMMENDATIONS
# ============================================================================

elif page == "🤖 Model Recommendations":
    st.title("🤖 Model Architecture Recommendations")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "Intent Classification",
        "Q&A Matching",
        "Hyperparameters",
        "Deployment"
    ])
    
    with tab1:
        st.subheader("Intent Classification Models")
        
        models = [
            {
                "Name": "BERT + Classification Head",
                "Accuracy": "90-95%",
                "Training Time": "2-4 hours",
                "Framework": "Hugging Face",
                "Recommendation": "⭐⭐⭐⭐⭐ BEST FOR MEDICAL"
            },
            {
                "Name": "RoBERTa",
                "Accuracy": "92-96%",
                "Training Time": "3-5 hours",
                "Framework": "Hugging Face",
                "Recommendation": "⭐⭐⭐⭐⭐ HIGHLY RECOMMENDED"
            },
            {
                "Name": "DistilBERT",
                "Accuracy": "88-93%",
                "Training Time": "1-2 hours",
                "Framework": "Hugging Face",
                "Recommendation": "⭐⭐⭐⭐ FAST INFERENCE"
            },
            {
                "Name": "Random Forest (Baseline)",
                "Accuracy": "80-85%",
                "Training Time": "Minutes",
                "Framework": "Scikit-learn",
                "Recommendation": "⭐⭐⭐ FOR BASELINE"
            }
        ]
        
        models_df = pd.DataFrame(models)
        st.dataframe(models_df, use_container_width=True)
    
    with tab2:
        st.subheader("Q&A Matching & Retrieval Models")
        
        retrieval_models = [
            {
                "Name": "Bi-Encoder (Sentence-BERT)",
                "MRR Score": "0.85-0.92",
                "Speed": "Fast",
                "Use Case": "Semantic similarity search",
                "Status": "⭐⭐⭐⭐⭐ RECOMMENDED"
            },
            {
                "Name": "Cross-Encoder",
                "MRR Score": "0.90-0.95",
                "Speed": "Slower",
                "Use Case": "Ranking verification",
                "Status": "⭐⭐⭐⭐ FOR ACCURACY"
            },
            {
                "Name": "Dense Passage Retrieval",
                "MRR Score": "0.88-0.93",
                "Speed": "Fast",
                "Use Case": "Large corpus retrieval",
                "Status": "⭐⭐⭐⭐ FOR SCALE"
            }
        ]
        
        retrieval_df = pd.DataFrame(retrieval_models)
        st.dataframe(retrieval_df, use_container_width=True)
    
    with tab3:
        st.subheader("Recommended Hyperparameters")
        
        st.markdown("""
        ```python
        # Training Configuration
        learning_rate = 2e-5  # Start with this
        batch_size = 16       # Adjust based on GPU memory
        epochs = 10           # With early stopping
        optimizer = 'AdamW'   # Best for transformers
        warmup_steps = 500    # 10% of training
        weight_decay = 0.01   # L2 regularization
        dropout_rate = 0.1    # Prevent overfitting
        max_seq_length = 512  # BERT standard
        
        # Learning Rate Scheduler
        # Use: Linear decay with warmup
        # or: Cosine annealing
        ```
        """)
        
        st.markdown("---")
        
        st.subheader("📊 Evaluation Metrics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Classification Metrics:**
            - Accuracy
            - Precision / Recall
            - F1-Score
            - ROC-AUC
            - Confusion Matrix
            """)
        
        with col2:
            st.markdown("""
            **Retrieval Metrics:**
            - MRR (Mean Reciprocal Rank)
            - NDCG (Normalized Discounted Cumulative Gain)
            - MAP (Mean Average Precision)
            - Recall@k
            """)
    
    with tab4:
        st.subheader("🚀 Deployment Architecture")
        
        st.markdown("""
        ### Recommended Stack
        
        **Frontend:**
        - React/Vue.js for web UI
        - Mobile apps for iOS/Android
        
        **API Layer:**
        - FastAPI or Flask
        - Docker containerization
        - NGINX load balancing
        
        **Model Layer:**
        - Primary: BERT classifier
        - Secondary: Sentence-BERT retriever
        - Fallback: TF-IDF similarity
        
        **Data Layer:**
        - Vector database: FAISS / Pinecone
        - Cache: Redis
        - Logging: ELK Stack
        
        **Monitoring:**
        - Prometheus + Grafana
        - Sentry for error tracking
        - CloudWatch/ELK for logs
        """)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🏥 <b>AI Medical Chatbot - EDA Dashboard</b></p>
    <p>Professional Exploratory Data Analysis Report</p>
    <p><small>Generated January 2026 | Dataset: 254.88 MB | Records: {:,}</small></p>
</div>
""".format(df.shape[0]), unsafe_allow_html=True)
