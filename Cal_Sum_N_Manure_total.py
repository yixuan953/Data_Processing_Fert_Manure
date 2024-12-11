# This code is used to: Sum up the MA_deep and MA_surface --> Manure N

import xarray as xr
import netCDF4
from netCDF4 import Dataset
import os
import glob
import numpy as np

# Path for all the manure N input .nc file
folder_path = 'C:/Users/zhou111/OneDrive - Wageningen University & Research/2_Data/NP_Input/Processed_data/N_Manure_Input_Original'
# folder_path = 'C:/Users/zhou111/Desktop'
nc_files = glob.glob(os.path.join(folder_path, '*.nc'))

for nc_file_name in nc_files:    
    print(f"Processing .nc file: {nc_file_name}")
    
    # Open the file in append mode
    with Dataset(nc_file_name, mode='a') as nc_file:
        # Access the two variables
        var1 = nc_file.variables['N_manure_surface'][:]  
        var2 = nc_file.variables['N_manure_deep'][:]
        
        # Convert variables to numpy arrays and handle missing data
        var1_data = np.ma.filled(var1, 0)  # Replace masked values with 0
        var2_data = np.ma.filled(var2, 0)  # Replace masked values with 0

        summed_var_data = var1_data + var2_data
        summed_var_dim = nc_file.variables['N_manure_surface'].dimensions  # Use same dimensions
        summed_var = xr.DataArray(summed_var_data, name="N_manure_Total")
            
        if 'N_manure_Total' not in nc_file.variables:   
            nc_file.createVariable('N_manure_Total', var1.dtype, summed_var_dim)        
            
        nc_file.variables['N_manure_Total'][:] = summed_var
    
    print(f"Summed variable added and saved to: {nc_file_name}")