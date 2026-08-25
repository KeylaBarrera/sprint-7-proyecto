import pandas as pd
import plotly.graph_objects as go
import streamlit as st


vehicles = pd.read_csv('vehicles_us.csv')

st.header('Anuncio de ventas de coches')

hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=vehicles['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: precio vs kilometraje')
    fig = go.Figure(data=[go.Scatter(
        x=vehicles['odometer'],
        y=vehicles['price'],
        mode='markers'
    )])
    fig.update_layout(title_text='Precio vs Kilometraje',
                      xaxis_title='Kilometraje', yaxis_title='Precio')
    st.plotly_chart(fig, use_container_width=True)
