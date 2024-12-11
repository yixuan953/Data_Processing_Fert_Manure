# This code is used to downscale N_manure_input from 10 km to 0.5 degree

import xarray as xr
import netCDF4 as nc
from netCDF4 import Dataset
import scipy.interpolate as interp
import os
import glob
import numpy as np

# Path for all the manure N input .nc file
folder_path = 'C:/Users/zhou111/OneDrive - Wageningen University & Research/2_Data/NP_Input/Processed_data/N_Manure_Input'
# folder_path = 'C:/Users/zhou111/Desktop/N_Manure_Input'
output_path = 'C:/Users/zhou111/Desktop'
nc_files = glob.glob(os.path.join(folder_path, '*.nc'))

scale_factor = 6

for nc_file_name in nc_files:    
    print(f"Processing .nc file: {nc_file_name}")    

    # Open the NetCDF file
    ds = xr.open_dataset(nc_file_name)
    
    # Variable to upscale
    var_name = 'N_manure_Total'    

    # Block averaging for upscaling
    data = ds[var_name]

    # Reshape data to group blocks of 6x6
    data_reshaped = data.values.reshape(
        (data.shape[0], 
         data.shape[1] // scale_factor, 
         scale_factor, 
         data.shape[2] // scale_factor, 
         scale_factor)
    )
    
    # Average over blocks of 6x6
    data_upscaled = data_reshaped.mean(axis=(2, 4))

    # Define new latitude and longitude based on upscaled shape
    lon_new = np.linspace(-180 + 0.5, 180 - 0.5, data_upscaled.shape[1], endpoint=True)
    lat_new = np.linspace(90 - 0.5, -90 + 0.5, data_upscaled.shape[2], endpoint=True)
    
    ds.close()
     
    new_nc_file_name = os.path.join(output_path, nc_file_name)
    with xr.Dataset() as ds_new:
        ds_new['lon'] = ('lon', lon_new)
        ds_new['lat'] = ('lat', lat_new)
        ds_new['N_manure_total'] = (('time', 'lon', 'lat'), data_upscaled)
        ds_new.to_netcdf(new_nc_file_name)

    print(f"Upscaled data saved to {new_nc_file_name}")    

        