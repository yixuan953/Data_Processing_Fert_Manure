----------------------Code description---------------
The code of this folder is used to calculate global N and P manure input
1. Format_Trans_h52nc.py: Extract manure data from .h5 files and transform into .nc formats
2. Cal_Sum_N_Manure_total.py: Sum up the total N manure input (MA_surface + MA_deep) for each crop (.nc files)
3. Res_Trans_Downscale.py: Downscale N manure from 10 km to 0.5 degree
4. Cal_PN_ratio.py: Calculate PN ratio using the N, P content in manure data

6. Cal_Manure_P_input.py: Calculate the P manure input = NP ratio in manure * N manure input
7. Rename_Manure.py: Rename all of the .nc files for each crop type ("Manure_NP_1960-2020_' + [Crop name]")

----------------------Original dataset---------------
[N fertilization for each crop type] 
Unit: kg N ha-1（harvest area）y-1
Variables: 
    1 - MA_surface: manure input for harvest area without tillage applied
    2 - MA_deep: manure input for harvest area with tillage applied
Temporal scale: 1960-2020, annual
Spatial scale: global, 10km
Data format: .h5
Data source: Adalibieke, W., Cui, X., Cai, H., You, L., Zhou, F. (2023). Global crop-specific nitrogen fertilization dataset in 1961-2020. National Tibetan Plateau / Third Pole Environment Data Center. https://doi.org/10.11888/Terre.tpdc.300446. https://cstr.cn/18406.11.Terre.tpdc.300446.

[N content in manure production] 
Unit: -
Variable: N content in manure production
Temporal scale: Data collection period: 1994-2001, annul 1-year data
Spatial scale: Global, 0.5 degree
Data format: .tiff
Data source: Potter et al. (2010) https://cmr.earthdata.nasa.gov/search/concepts/C1000000001-SEDAC.html

[P content in manure production] 
Unit: -
Variable: P content in manure production
Temporal scale: Data collection period: 1994-2001, annul 1-year data
Spatial scale: Global, 0.5 degree
Data format: .tiff
Data source: Potter et al. (2010) https://cmr.earthdata.nasa.gov/search/concepts/C1000000002-SEDAC.html 

[Harvest area] 
Unit: 
Variable: 
Temporal scale: 
Spatial scale: 
Data format: .h5
Data source: 

----------------------Transformed data------------
[Manure N and P input] 
Unit: kg N ha-1（harvest area）y-1
Variables: 
    1 - N_manure 
    2 - P_manure
Temporal scale: 1960 - 2020, annual
Spatial scale: Global, 0.5 degree
Data format: .nc