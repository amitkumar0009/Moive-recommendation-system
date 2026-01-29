# 🎬 Movie Recommendation System

A **content-based movie recommendation system** trained on the **TMDB dataset** that generates personalized movie suggestions using **cosine similarity**. The system analyzes movie metadata to recommend similar movies and is deployed with an interactive **Streamlit** web interface.

## Introduction
This project implements a real-world **content-based filtering** approach for movie recommendation. Instead of relying on user ratings, the system recommends movies by measuring similarity between movie features such as genres, keywords, and overview. The recommendations are fast, explainable, and suitable for practical deployment.

## Features
- Content-based movie recommendations using **cosine similarity**
- Trained on the **TMDB (The Movie Database) dataset**
- Utilizes movie metadata for similarity computation
- Generates personalized recommendations based on selected movies
- Interactive and user-friendly **Streamlit** web application
- Efficient handling and preprocessing of real-world datasets

## Technologies Used
- **Python**
- **Pandas, NumPy** for data preprocessing
- **Scikit-learn** for cosine similarity computation
- **Streamlit** for frontend and deployment
- **Jupyter Notebook** for model development and experimentation

## How It Works
1. Load and preprocess the TMDB movie dataset  
2. Clean and combine relevant movie features (genres, keywords, overview, cast, crew)  
3. Convert text features into numerical vectors  
4. Compute similarity scores using **cosine similarity**  
5. Recommend top-N similar movies based on similarity ranking  
6. Display recommendations instantly via Streamlit UI  

## Demo
🔗 Live Application:  
https://moive-recommendation-system-smy43bvhchmmbuemx3pr8y.streamlit.app/

## Future Enhancements
- Hybrid recommendation system (content-based + collaborative)
- User preference learning and feedback loop
- Improved feature engineering using embeddings
- Support for larger datasets and multilingual content

