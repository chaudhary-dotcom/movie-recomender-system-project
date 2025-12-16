# Movie Recommender System (Streamlit)
#### A content-based movie recomended system built using Python, Streamlit, and cosine similarity. The app recommends movies similar to selected movie and displays their posters using the TMDB API.

## Features
#### 1. Select a movie list from dropdown list
#### 2. Get Top 5 similar movie recommendations
#### 3. Fetches and displays movie posters using TMDB API
#### 4. Fast and lightweight Streamlit web app

## How It Works ?
#### 1. Movie data is preprocessed and stored in movies_dict.pkl
#### 2. A cosine similarity matrix is computed and saved as similarity.pkl
#### 3. When a user selects a movie:
######   A. The similarity scores are retrived
###### B. Top 5 most similar movies are selected
###### C. Posters are fetched using TMDB API

## Dataset
#### 1. movie_id
#### 2. title
#### 3. Tags/metadata used for similarity calculation

## Future Improvements
#### 1. Add movie rating and genres
#### 2. Improve UI with cards and animations
#### 3. Add collaborative filtering
#### 4. Add search instead of dropdown
