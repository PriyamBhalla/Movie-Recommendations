import streamlit as st
import pickle
import requests

def fetch_posters(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=9d25a33202ae19b8ef58a3ddc61692eb&language=en-US".format(
          movie_id)
     data = requests.get(url)
     data = data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
     return full_path

def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_movies=[]
     recommended_movies_posters=[]
     for i in movies_list:
          movie_id=movies.iloc[i[0]].movie_id
          recommended_movies_posters.append(fetch_posters(movie_id))
          recommended_movies.append(movies.iloc[i[0]].title)
     return recommended_movies,recommended_movies_posters

st.title('Movie Recommender System')
movies=pickle.load(open('movies.pkl','rb'))
movies_list=movies['title'].values


similarity=pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox(
     'How would you like to be contacted?',
movies_list)


st.write('You selected:', selected_movie_name)

if st.button('Recommend'):
     recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
     col1, col2, col3, col4, col5 = st.columns(5)
     with col1:
          st.text(recommended_movie_names[0])
          st.image(recommended_movie_posters[0])
     with col2:
          st.text(recommended_movie_names[1])
          st.image(recommended_movie_posters[1])
     with col3:
          st.text(recommended_movie_names[2])
          st.image(recommended_movie_posters[2])
     with col4:
          st.text(recommended_movie_names[3])
          st.image(recommended_movie_posters[3])
     with col5:
          st.text(recommended_movie_names[4])
          st.image(recommended_movie_posters[4])


