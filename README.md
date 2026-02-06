# 🛡️ Amharic Fake News Detection System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-15-000000?style=for-the-badge&logo=next.js&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

A comprehensive machine learning system for detecting fake news in **Amharic (አማርኛ)** text, featuring specialized text preprocessing for Ethiopic script, multiple classification models, a FastAPI backend, and a modern Next.js web interface.

[Live Demo](https://fake-news-detector-snowy.vercel.app/) • [Report](./Fake%20News%20Detection%20Report.pdf)

</div>

---

## � Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Model Performance](#-model-performance)
- [Data Pipeline](#-data-pipeline)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Technology Stack](#-technology-stack)
- [Dataset](#-dataset)
- [Contributing](#-contributing)
- [References](#-references)

---

## 🎯 Overview

The spread of misinformation in Amharic-language social media poses significant challenges to Ethiopian and global Amharic-speaking communities. This project addresses this challenge by providing an end-to-end solution for detecting fake news in Amharic text using classical machine learning techniques.

### Key Highlights

- **Language-Specific Preprocessing**: Custom normalization rules for Ethiopic script (Fidel) handling phonologically similar characters
- **Multi-Model Ensemble**: Four trained classifiers providing diverse predictions with confidence scores
- **Production-Ready API**: RESTful API with CORS support for seamless integration
- **Interactive Web Interface**: Modern, responsive UI with real-time analysis and visualization

---

## ✨ Features

### 🔤 Amharic Text Preprocessing

- **Character Normalization**: Unifies phonologically equivalent Ethiopic characters (e.g., ሀ/ሐ/ሓ/ኀ → ሀ)
- **Noise Removal**: Eliminates URLs, HTML tags, English text, emojis, and special characters
- **Geez Number Handling**: Removes traditional Ethiopic numerals (፩፪፫...)
- **Text Cleaning**: Handles elongated words, extra whitespace, and leading/trailing spaces

### 🤖 Machine Learning Models

| Model                   | Description                                |
| ----------------------- | ------------------------------------------ |
| **Logistic Regression** | Linear classifier, best overall accuracy   |
| **Decision Tree**       | Rule-based classifier for interpretability |
| **Random Forest**       | Ensemble of decision trees for robustness  |
| **Gradient Boosting**   | Sequential ensemble for high performance   |

### 🌐 Web Application

- **Real-time Analysis**: Instant fake news detection with confidence visualization
- **Model Selection**: Switch between different classifiers to compare predictions
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Visual Feedback**: Pie chart visualization of prediction confidence

---

## � Project Structure

```
fake_news_detection/
├── app/
│   ├── api/                          # Backend REST API
│   │   ├── assets/                   # Trained model files (.pkl)
│   │   │   ├── LR_model.pkl         # Logistic Regression
│   │   │   ├── DT_model.pkl         # Decision Tree
│   │   │   ├── RF_model.pkl         # Random Forest
│   │   │   ├── GB_model.pkl         # Gradient Boosting
│   │   │   └── vectorizer.pkl       # TF-IDF Vectorizer
│   │   ├── internal/
│   │   │   ├── models.py            # Model loading & prediction logic
│   │   │   └── preprocess.py        # Text preprocessing for API
│   │   ├── schemas/
│   │   │   └── request.py           # Pydantic request models
│   │   ├── main.py                  # FastAPI application entry point
│   │   └── requirements.txt         # Python dependencies
│   │
│   └── web/                          # Frontend Application
│       ├── src/
│       │   ├── app/                 # Next.js app router pages
│       │   ├── components/          # React components
│       │   │   ├── analysis.tsx     # Results visualization
│       │   │   ├── header.tsx       # App header
│       │   │   └── ui/              # UI components (shadcn/ui)
│       │   ├── hooks/               # Custom React hooks
│       │   └── lib/                 # Utility functions
│       ├── package.json
│       └── tailwind.config.ts
│
├── data/
│   ├── raw/
│   │   └── data.xlsx                # Original labeled dataset
│   └── processed/
│       └── processed_data.csv       # Cleaned and preprocessed data
│
├── notebooks/
│   ├── data_preprocess.ipynb        # Data cleaning and profiling
│   └── model_training.ipynb         # Model training and evaluation
│
├── src/
│   └── preprocess.py                # Core preprocessing module
│
├── Fake News Detection Report.pdf   # Project documentation
└── README.md
```

---

## 📊 Model Performance

All models were trained on an 80/20 train-test split using TF-IDF vectorization.

### Classification Results

| Model                   | Accuracy  | Precision | Recall | F1-Score |
| ----------------------- | --------- | --------- | ------ | -------- |
| **Logistic Regression** | **93.5%** | 0.94      | 0.94   | 0.94     |
| Random Forest           | 91.5%     | 0.91      | 0.91   | 0.91     |
| Gradient Boosting       | ~91%      | 0.91      | 0.91   | 0.91     |
| Decision Tree           | 87.6%     | 0.88      | 0.88   | 0.88     |

> **Note**: Logistic Regression achieves the best performance, making it the recommended default model for production use.

### Feature Engineering

- **TF-IDF Vectorization**: Converts preprocessed Amharic text into numerical features
- **Vocabulary Size**: Trained on 8,631 samples with dynamic vocabulary

---

## 🔄 Data Pipeline

### 1. Data Profiling (Before Preprocessing)

The raw data contains various noise elements that are identified and removed:

| Issue                | Count   |
| -------------------- | ------- |
| URLs                 | 1,294   |
| English words/digits | 135,414 |
| Special characters   | 205,193 |
| Extra spaces         | 17,345  |
| Emojis               | 1,686   |
| HTML tags            | 110     |

### 2. Preprocessing Steps

```
Raw Text → URL Removal → HTML Tag Removal → English/Number Removal
        → Geez Number Removal → Special Character Removal → Emoji Removal
        → Elongation Normalization → Ethiopic Character Normalization
        → Whitespace Normalization → Clean Text
```

### 3. Character Normalization Examples

| Input Characters | Normalized To |
| ---------------- | ------------- |
| ሐ, ሃ, ኻ, ሓ, ኀ, ኃ | ሀ             |
| ሠ, ሡ, ሢ...       | ሰ, ሱ, ሲ...    |
| ኣ, ዐ, ዓ          | አ             |
| ጸ, ጹ, ጺ...       | ፀ, ፁ, ፂ...    |

---

## 🚀 Installation

### Prerequisites

- Python 3.9+
- Node.js 18+
- npm or yarn

### Backend Setup

```bash
# Navigate to API directory
cd app/api

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the API server
uvicorn main:app --reload --port 8000
```

### Frontend Setup

```bash
# Navigate to web directory
cd app/web

# Install dependencies
npm install

# Start development server
npm run dev
```

The web application will be available at `http://localhost:3000`

---

## 💻 Usage

### Web Interface

1. Navigate to the web application
2. Paste or type Amharic news text in the input area
3. Click **"Verify"** to analyze the text
4. View results with confidence scores
5. Switch between models using the dropdown to compare predictions

### Python API

```python
import requests

# API endpoint
url = "http://localhost:8000/detect-news"

# Amharic news text to analyze
payload = {
    "text": "የእርስዎ አማርኛ ዜና ጽሁፍ እዚህ ያስገቡ"
}

# Make request
response = requests.post(url, json=payload)
result = response.json()

print(result)
# {
#     "prediction": {
#         "logistic_regression": "Real",
#         "decision_tree": "Real",
#         "random_forest": "Real",
#         "gradient_boosting": "Real"
#     },
#     "probabilities": {
#         "logistic_regression": 0.923,
#         "decision_tree": 0.871,
#         "random_forest": 0.912,
#         "gradient_boosting": 0.908
#     }
# }
```

---

## 📡 API Reference

### Detect Fake News

```http
POST /detect-news
```

#### Request Body

| Parameter | Type     | Description                             |
| --------- | -------- | --------------------------------------- |
| `text`    | `string` | **Required**. Amharic news article text |

#### Response

```json
{
  "prediction": {
    "logistic_regression": "Real" | "Fake",
    "decision_tree": "Real" | "Fake",
    "random_forest": "Real" | "Fake",
    "gradient_boosting": "Real" | "Fake"
  },
  "probabilities": {
    "logistic_regression": 0.0-1.0,
    "decision_tree": 0.0-1.0,
    "random_forest": 0.0-1.0,
    "gradient_boosting": 0.0-1.0
  }
}
```

#### Example cURL

```bash
curl -X POST "http://localhost:8000/detect-news" \
  -H "Content-Type: application/json" \
  -d '{"text": "መንግስት አዲስ ሕግ አውጥቷል"}'
```

---

## 🛠️ Technology Stack

### Backend

| Technology       | Purpose                                       |
| ---------------- | --------------------------------------------- |
| **FastAPI**      | High-performance REST API framework           |
| **scikit-learn** | Machine learning model training and inference |
| **Pandas**       | Data manipulation and preprocessing           |
| **Pydantic**     | Request/response validation                   |
| **Uvicorn**      | ASGI server                                   |

### Frontend

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| **Next.js 15**   | React framework with App Router |
| **React 19**     | UI component library            |
| **Tailwind CSS** | Utility-first styling           |
| **Recharts**     | Data visualization (pie charts) |
| **shadcn/ui**    | Pre-built accessible components |
| **Lucide Icons** | Icon library                    |

### Data Science

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| **TF-IDF Vectorizer** | Text feature extraction   |
| **Jupyter Notebooks** | Exploratory data analysis |
| **Matplotlib**        | Data visualization        |

---

## 📚 Dataset

### Source

The dataset is sourced from research by **Membere Hailu** (2022):

> "Amharic Fake News Detection on Social Media Using Pretrained Language Model"

[Dataset Repository](https://github.com/MenbereHailu/Amharic_Fake_News_Detection_On_Social_Media-_Using_Pretrained-_Language_Model)

### Statistics

| Metric        | Value                  |
| ------------- | ---------------------- |
| Total Samples | 8,631                  |
| Training Set  | 6,904 (80%)            |
| Test Set      | 1,727 (20%)            |
| Classes       | 2 (Real, Fake)         |
| Class Balance | Approximately balanced |

### Label Distribution

- **Fake News (0)**: ~50% of samples
- **Real News (1)**: ~50% of samples

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Areas for Improvement

- [ ] Add transformer-based models (AmBERT, XLM-RoBERTa)
- [ ] Implement real-time social media integration
- [ ] Add explainability features (LIME, SHAP)
- [ ] Expand dataset with more recent news articles
- [ ] Add multilingual support for other Ethiopian languages

---

## 📖 References

1. Hailu, M. (2022). _Amharic Fake News Detection on Social Media Using Pretrained Language Model_. [GitHub Repository](https://github.com/MenbereHailu/Amharic_Fake_News_Detection_On_Social_Media-_Using_Pretrained-_Language_Model)

2. [FastAPI Documentation](https://fastapi.tiangolo.com/)

3. [scikit-learn Documentation](https://scikit-learn.org/)

4. [Next.js Documentation](https://nextjs.org/docs)

---

## 📄 License

This project is for educational and research purposes. Please cite the original dataset source when using this work.

---

<div align="center">

**Built with ❤️ for the Amharic-speaking community**

_Software Engineering - AI Stream | NLP Final Project_

</div>
