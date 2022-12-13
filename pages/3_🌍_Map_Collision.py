import streamlit as st
import pandas as pd
import numpy as np
from pydeck.types import String
import pydeck as pdk

st.title("Vehicle collisions")

# Read DataFrame
df = pd.read_csv('NYC.csv')

# Filter out the Nan from the selected columns: Longitude, latitute, borough
mask = (df['LATITUDE'].isna())|(df['LONGITUDE'].isna())|(df['BOROUGH'].isna())
df_ = df[~mask]
df_.reset_index(drop=True,inplace=True) # reset index
df_ = df_.rename(columns={'LATITUDE':'latitude','LONGITUDE':'longitude'}) #pydeck does not allow capital letters

# boroughs without NaN
dist = list(df_['BOROUGH'].unique())
dist.append('All')

selected_dist = st.selectbox(
    "Select a borough",
    dist
)

if selected_dist in dist[:-1]:
    df_acc = df_[(df_['BOROUGH']==selected_dist)]
    df_acc.reset_index(drop = True, inplace = True)
    mid = [np.average(df_acc['latitude']),np.average(df_acc['longitude'])]
    st.header(f'Accidentes para el distrito {selected_dist}')
else:
	df_acc = df_.copy()
	mid = [np.average(df_acc['latitude']),np.average(df_acc['longitude'])]
	st.header(f'Accidents in {selected_dist}')


pyd = pdk.Deck(map_style="mapbox://styles/mapbox/light-v9",
	           initial_view_state={
                    "latitude": mid[0],
                    "longitude": mid[1],
                    "zoom": 11,
                    "pitch": 50,
                },
                layers=[
                    pdk.Layer(
                        "HexagonLayer",
                        data=df_acc[['BOROUGH',"longitude", "latitude"]],
                        get_position=["longitude", "latitude"],
                        radius=100,
                        elevation_scale=4,
                        elevation_range=[0, 1000],
                        pickable=True,
                        extruded=True,
                    ),
                ])
st.pydeck_chart(pyd)
