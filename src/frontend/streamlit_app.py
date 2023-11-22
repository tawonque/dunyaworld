import streamlit as st
from typing import Tuple, DataFrame

import pandas as pd
import rasterio
from rasterio.crs import CRS


def get_raster_crs(raster_file: str) -> CRS:


# Code to get CRS

def sample_raster(
        points: DataFrame, raster: str, raster_crs: CRS
) -> Tuple[DataFrame, list]:


# Code to sample raster

st.title('Raster Sampling App')

# Upload CSV
points_df: DataFrame = st.file_uploader('Upload points')

# Upload raster
raster_file: str = st.file_uploader('Upload raster', type=['tif'])

if st.button('Sample'):
    raster_crs: CRS = get_raster_crs(raster_file)

    values_df: DataFrame
    values: list

    values_df, values = sample_raster(points_df, raster_file, raster_crs)

    st.write(values_df)