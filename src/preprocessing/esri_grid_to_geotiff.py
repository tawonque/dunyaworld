import gdal


def convert_grid_to_geotiff(grid_path, tiff_path):
    """
    Convert an ESRI Grid file to a GeoTIFF

    Parameters
    ----------
    grid_path : str
        Path to the ESRI Grid file
    tiff_path : str
        Desired path for the output GeoTIFF file
    """

    src_ds = gdal.Open(grid_path)

    # Get spatial reference from source
    src_srs = src_ds.GetSpatialRef()

    driver = gdal.GetDriverByName("GTiff")
    dst_ds = driver.CreateCopy(tiff_path, src_ds, 0, src_srs)

    # Set spatial reference on destination
    dst_ds.SetProjection(src_srs.ExportToWkt())

    src_ds = None
    dst_ds = None

    print(f"Converted {grid_path} to {tiff_path}")

# or...????
from osgeo import gdal
#Your arc/info grid file master folder....
inras = r'C:\test\whatcodtm'
#The path and name to your output tif
outras = r'C:\test\foo.tif'
ds = gdal.Translate(outras, inras)


#my_grid = "datasets/elevation.grid"
#my_tiff = "datasets/elevation.tif"

#convert_grid_to_geotiff(my_grid, my_tiff)