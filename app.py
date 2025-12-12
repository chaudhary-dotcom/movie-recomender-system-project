import pickle
import streamlit as st
import requests
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=bc057d1781cd468eebec479e505241a4'.format(movie_id))
    data = response.json()
    poster_path = data.get('poster_path')

    if poster_path:
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    else:
        return None
    
# Normal recomendation 
def recommended(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movie_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movie_poster

# Genra based recomendation 
def recommend_by_genra(selected_genra):
    filtered = movies[movies['genres'].apply(lambda x: selected_genra in x)]

    filtered = filtered.head(5)

    names = filtered['title'].values
    posters = [fetch_poster(mid) for mid in filtered['movies_id'].values]
    return names, posters

# load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recomender System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values 
)

if st.button('Recommend'):
    names, posters = recommended(selected_movie_name)

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            st.image(posters[i])