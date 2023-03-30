import numpy as np 
import pandas as pd 
import plotly.express as px 
import streamlit as st 

data=pd.read_csv('players transfer.csv') 

st.write('Author:@AhmedEssam')

st.title('Player Transfer')

col1 ,col2 = st.columns(2)

with col1 :
    fig1=px.bar(data,x='Position',y='Goals',color='Age',width=500, height=400)
    st.plotly_chart(fig1)


with col2:
    fig2=px.scatter(data,x='Position' , y='Markey Value In Millions(£)',size='Assists',
           color='Yellow Cards',width=500, height=400)
    st.plotly_chart(fig2)    


with col1:
    fig3=px.pie(data, values='Assists' , names='Position',
       color_discrete_sequence=px.colors.sequential.RdBu, width=500, height=400)
    st.plotly_chart(fig3)


with col2:
    fig4=px.pie(data, values='Goals' , names='Position',width=500, height=400)
    st.plotly_chart(fig4)


with col1:
    fig5=px.bar(data ,x='Age' ,y='Goals',width=500, height=400) 
    st.plotly_chart(fig5) 



with col2:
    fig6=px.scatter(data,x='Age' , y='Markey Value In Millions(£)',size='Goals',
           color='Red Cards',width=500, height=400)
    st.plotly_chart(fig6)



with col1:
    fig7=px.bar(data , x='Age',y='Number Of Substitute Out',color='Red Cards',width=500, height=400)
    st.plotly_chart(fig7)




with col2:
    fig8=px.box(data,x='Position',y='Assists', color='Red Cards',width=500, height=400)
    st.plotly_chart(fig8)

