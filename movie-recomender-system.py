import streamlit as st
import pickle
import pandas as pd
st.title('Movie Recommender System')

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
recommend_var = pickle.load(open('recommend_var.pkl','rb'))
option = st.selectbox(
    'How would you like to be contacted?',
    (movies['title'].values))

def recommend(movie):
  movie_index = movies[movies['title']==movie].index[0]
  movie_index_list = sorted(enumerate(recommend_var[movie_index]), reverse=True, key=lambda x:x[1])[1:6]
  return [(movies.iloc[i[0]].title, movies.iloc[i[0]].belongs_to_collection) for i in movie_index_list]
if st.button('Recommend'):
    # st.write(recommend(option))
    col1, col2, col3, col4, col5 = st.columns(5)
    l = recommend(option)
    with col1:
        st.text(l[0][0])
        st.image('https://image.tmdb.org/t/p/w500'+l[0][1])
    with col2:
        st.text(l[1][0])
        st.image('https://image.tmdb.org/t/p/w500'+l[1][1])
    with col3:
        st.text(l[2][0])
        st.image('https://image.tmdb.org/t/p/w500'+l[2][1])
    with col4:
        st.text(l[3][0])
        st.image('https://image.tmdb.org/t/p/w500'+l[3][1])
    with col5:
        st.text(l[4][0])
        st.image('https://image.tmdb.org/t/p/w500'+l[4][1])

