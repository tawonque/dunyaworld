import streamlit as st
import pandas as pd
import rasterio
from rasterio.crs import CRS
import geopandas as gp


def png_to_tiff(png_path, tiff_path, crs):
    """change a raster from png to tiff format"""
    with rasterio.open(png_path) as src:
        meta = src.meta.copy()

        meta.update({
            'driver': 'GTiff',
            'height': src.height,
            'width': src.width,
            'count': src.count,
            'crs': crs,
            'transform': src.transform
        })

    with rasterio.open(tiff_path, 'w', **meta) as dst:
        dst.write(src.read())

def get_raster_crs(raster_file: str) -> CRS:
    """get the CRS of a raster"""
    with rasterio.open(raster_file) as src:
        raster_crs = CRS.from_string(src.crs)

    return raster_crs

def create_points_df(points_list: tuple):
    """given a tuple of lat-long tuples, create a dataframe with columns named 'latitude' and 'longitude'"""
    points_df = pd.DataFrame({'latitude': [t[0] for t in points_list],
                              'longitude': [t[1] for t in points_list]})
    return points_df

def pandas_to_geodf(dataframe: pd.DataFrame):
    """change a pandas dataframe to a geodataframe"""
    gdf = gp.GeoDataFrame(
        dataframe, geometry=gp.points_from_xy(dataframe.longitude, dataframe.latitude), crs="EPSG:4326"
    )
    return gdf

def sample_from_raster(
    points: pd.DataFrame, raster: str, raster_crs: CRS
) -> Tuple[pd.DataFrame, list]:

    # Transform points DataFrame
    points = points.to_crs(raster_crs).copy()

    # Sample raster
    with rasterio.open(raster) as r:
        values = [r.sample([(p.x, p.y)])[0] for p in points.geometry]

    # Return DataFrame of values
    df = pd.DataFrame(values, columns=["value"])
    return df, values

######
crs = CRS.from_epsg(4326)

png_to_tiff('image.png', 'image.tif', crs)

points = ((42.546245, 1.601554), (23.424076, 53.847818),	(33.9391, 67.70995), (17.060816, -61.796428))