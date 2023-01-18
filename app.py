import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Below code is used so that image on streamlit will be wider and fit to screen
st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India Data Visualization')

selected_state = st.sidebar.selectbox('Select a State',list_of_states)

primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:

    st.text('Size represents -> Primary Parameter')
    st.text('Color represents -> Secondary Parameter')

    if selected_state == 'Overall India':
        # plot for India
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', zoom=3.3, size=primary, color=secondary, size_max=35, mapbox_style='carto-positron',width=1500, height=600, hover_name='District',color_continuous_scale='Jet')
        # use_container_width = this put graph at center in stream lit
        st.plotly_chart(fig,use_container_width=True)
    else:
        # plot for state
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=5.35, size=primary, color=secondary,
                                size_max=35, mapbox_style='carto-positron', width=1500, height=600, hover_name='District',color_continuous_scale='Jet')
        st.plotly_chart(fig, use_container_width=True)