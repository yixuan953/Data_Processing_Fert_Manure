# This code is used to: Calculate P manure input based on N manure input and PN ratio

import xarray as xr
import netCDF4 as nc
from netCDF4 import Dataset
import os
import glob
import numpy as np

# Read the PN ratio
PNraito_path = 'C:/Users/zhou111/OneDrive - Wageningen University & Research/2_Data/NP_Input/Processed_data/PNratio.nc'
PNratio_data = xr.open_dataset(PNraito_path)
PNratio = PNratio_data['data'].values
# Expand dimensions and repeat along 'time' using NumPy
PNratio_transposed = PNratio.T 
PNratio_broadcasted = np.expand_dims(PNratio_transposed, axis=0)  # Add time dimension
PNratio_broadcasted = np.repeat(PNratio_broadcasted, 60, axis=0)  # Repeat along time dimension
PNratio_data.close()


# Path for all the manure N input .nc file
folder_path = 'C:/Users/zhou111/OneDrive - Wageningen University & Research/2_Data/NP_Input/Processed_data/P_Manure_Input'
nc_files = glob.glob(os.path.join(folder_path, '*.nc') )                          
                     
for nc_file_name in nc_files:
    
    with nc.Dataset(nc_file_name, mode='a') as nc_file:

         var_name0 = 'N_manure_total'
         var_name1 = 'N_manure'  
         var_name2 = 'P_manure' 
         
         time_dim = nc_file.dimensions['time']
         lon_dim = nc_file.dimensions['lon']
         lat_dim = nc_file.dimensions['lat']
         
         N_manure_data = nc_file.variables[var_name0]
         N_manure = N_manure_data[:].filled(np.nan)
         N_manure[N_manure == 0] = np.nan
         P_manure = N_manure * PNratio_broadcasted
         
         # Add N manure
         new_var1 = nc_file.createVariable(var_name1, 'f4', ('time', 'lon', 'lat'))
         new_var1[:] = N_manure  # Use slicing to assign the data
         new_var1.setncattr('description', 'Annual total manure nitrogen input')
         new_var1.setncattr('units', 'kg/ha harvest area')         
         
         # Add P manure
         new_var2 = nc_file.createVariable(var_name2, 'f4', ('time', 'lon', 'lat'))
         new_var2[:] = P_manure  # Use slicing to assign the data    
         new_var2.setncattr('description', 'Annual total manure phosphorus input')
         new_var2.setncattr('units', 'kg/ha harvest area')   
         

    print(f"P manure of {nc_file_name} has been calculated and added")           
         
         