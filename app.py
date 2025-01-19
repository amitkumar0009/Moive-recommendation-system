import streamlit as st
import pickle
import pandas as pd
st.title('Movie Recommended System')


with open('model/movies.pkl','rb') as file:
    movies=pickle.load(file)

with open('model/similarity.pkl','rb') as file:
    similarity=pickle.load(file)

def recommend(movie):
  movie_index= movies[movies['title']==movie].index[0]

  difference=similarity[movie_index]

  movies_list=sorted(list(enumerate(difference)),reverse=True,key=lambda x: x[1])[1:6]
  for i in movies_list:
    st.write(movies.iloc[i[0]].title)
movie_name=st.text_input("Enter the movie name ")
movie_name=movie_name.lower()
if st.button('Recommend movie'):
    check=(movies['title']==movie_name).sum()
    if check==0:
        st.write("Movies Not Found !!!")

    else : 
        recommend(movie_name)