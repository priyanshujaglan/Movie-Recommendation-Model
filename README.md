# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using Python, Scikit-learn, and Streamlit. The application recommends movies similar to a user's selected movie by analyzing genres, keywords, cast, director, and movie metadata.

## 🚀 Features

* Recommend Top 5 similar movies instantly
* Content-Based Filtering using Cosine Similarity
* Interactive Streamlit Web Application
* Movie Posters, Ratings & Release Dates using TMDB API
* Cast Information and Movie Overview
* Modern and User-Friendly Interface

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* CountVectorizer
* Cosine Similarity
* TMDB API

## 📂 Dataset

This project uses the TMDB 5000 Movies Dataset containing movie metadata such as genres, keywords, cast, crew, and plot overviews.

## ⚙️ How It Works

1. Movie metadata is combined into a single feature set.
2. CountVectorizer converts text data into numerical vectors.
3. Cosine Similarity measures similarity between movies.
4. The system recommends the Top 5 most similar movies.
5. TMDB API fetches movie posters and additional details.

## 📁 Project Structure

```bash
Movie-Recommendation-Model/
│
├── main.py
├── movies.pkl
├── similarity.pkl
├── Netflix Recommendation model.ipynb
├── requirements.txt
├── README.md
└── Images/
```

## ▶️ Run Locally

### Clone Repository

```bash
git clone https://github.com/priyanshujaglan/Movie-Recommendation-Model.git
cd Movie-Recommendation-Model
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run main.py
```

## 📸 Application Features

* AI-powered movie recommendations
* Movie posters and ratings
* Cast details
* Movie overviews
* Responsive Streamlit UI

## 👨‍💻 Author

**Priyanshu Jaglan**

B.Tech CSE (AI)

GitHub: https://github.com/priyanshujaglan
