# Amharic Fake News Detection System

A comprehensive machine learning solution designed to detect fake news in Amharic text. This project integrates a robust data preprocessing pipeline, a Scikit-learn classification model, a FastAPI backend, and a Next.js web frontend.

## 🚀 Features

- **Amharic Text Preprocessing**: Specialized normalization and cleaning for Amharic script (Fidel), including character unification, removal of Geez numbers, and noise filtering.
- **Machine Learning Model**: Classification model trained to distinguish between real and fake news.
- **REST API**: High-performance API built with FastAPI to serve predictions.
- **Web Interface**: Modern, responsive user interface built with Next.js for easy interaction.
- **Data Profiling**: Tools to analyze text data distribution and quality.

## 📂 Project Structure

```bash
fake_news_detection/
├── app/
│   ├── api/                 # Backend API (FastAPI)
│   │   ├── internal/        # Model loading and inference logic
│   │   ├── schemas/         # Pydantic models for request/response
│   │   ├── main.py          # API entry point
│   │   └── requirements.txt # Python dependencies
│   └── web/                 # Frontend Application (Next.js)
├── notebooks/               # Jupyter notebooks for EDA and training
│   ├── data_preprocess.ipynb
│   └── model_training.ipynb
├── src/                     # Core data processing logic
│   └── preprocess.py        # Amharic normalization class
└── README.md
