import streamlit as st
import pandas as pd
from PIL import Image
imagen1 = Image.open ('logo2.jpg')

html = """
<div style = "background-color:black ; padding:10px">
<h2 style = "color:white; text-align:center; "> Demo 1</h2>
</div>
"""
st.markdown(html, unsafe_allow_html=True)
#Primeras líneas de código
st.title("Aplicación")

st.write("Mi primera aplicación")
#Parámetros a ingresarse
st.sidebar.title ("Parámetros")
x=st.sidebar.slider('Porcentajes', 0, 100, 30, 10)
st.sidebar.selectbox('Categoría', ('Alta', 'Media', 'Baja'))
check = st.checkbox('Visualizar gráfico', value=False)
if check == True:
	st.image(imagen1)
else:
	st.write("Marcar el checkbox")
from pandas import read_excel
df=pd.read_excel('Data2.xls', sheet_name='Hoja1')
st.write(df)
df2=df.describe()
st.write(df2)
filtro=df['Letras']== 'A'
df_filtro= df[filtro]
st.write(df_filtro)
# Visualización de datos
import altair as alt 	
i=x 
ly=list(range(-i,0))
ly=reversed(ly)
lx=[0]*i
lz=[0]*i
data_1={"Eje x":lx,
		"Eje y":ly,
		"Eje z":lz}
df1=pd.DataFrame(data_1)
st.write (df1)

import plotly.express as px
fig=px.line_3d(df1,x="Eje z", y="Eje x", z="Eje y")
st.write(fig)