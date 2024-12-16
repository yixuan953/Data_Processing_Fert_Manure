# This code is used to resample PNratio.nc from 0.5 degree to 0.05 degree

import xarray as xr
import numpy as np
import netCDF4
from scipy.interpolate import griddata


# Load the NetCDF file
file_path = 'C:/Users/zhou111/OneDrive - Wageningen University & Research/2_Data/NP_Input/Processed_data/PNratio.nc'
ds = xr.open_dataset(file_path)

# Define the new latitude and longitude
lon_new = np.arange(-180,180,0.05)
lat_new = np.arange(90,-90,-0.05)

# Create a mesh grid
lon_grid, lat_grid = np.meshgrid(lon_new, lat_new)

# Extract the original lat, lon, and variable
lat = ds['latitude'].values  
lon = ds['longitude'].values
PNratio = ds['data'].values  

# If lat and lon are 1D arrays, mesh them for interpolation
# Create meshgrid for the original lat/lon (if needed for the dataset)
lon_original, lat_original = np.meshgrid(lon, lat)

# Flatten the original lat/lon and PNratio data for interpolation
points = np.vstack([lon_original.flatten(), lat_original.flatten()]).T
values = PNratio.flatten()

# Perform interpolation
new_data = griddata(points, values, (lon_grid, lat_grid), method='linear')
# Create the new dataset with lat_new and lon_new
new_ds = ds.interp(latitude=lat_new, longitude=lon_new, method="linear")

new_ds.to_netcdf('C:/Users/zhou111/OneDrive - Wageningen University & Research/2_Data/NP_Input/Processed_data/PNratio_5_arc_min.nc')