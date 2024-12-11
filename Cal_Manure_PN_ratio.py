import rasterio
import numpy as np

# Load the TIFF files
Ncontent_tiff = '/lustre/nobackup/WUR/ESG/zhou111/Data/Raw/Nutri/Fertilization/Manure_Ncontent/nmanure_global.tif'
Pcontent_tiff = '/lustre/nobackup/WUR/ESG/zhou111/Data/Raw/Nutri/Fertilization/Manure_Pcontent/pmanure_global.tif'

with rasterio.open(Ncontent_tiff) as src1, rasterio.open(Pcontent_tiff) as src2:
    # Print the data information of P and N content in manure to ensure they have the same coordinates
    print("Metadata of Ncontent:", src1.meta)
    print("Metadata of Pcontent:", src2.meta)

    # Read data as arrays
    Ncontent = src1.read(1)  # First band
    Pcontent = src2.read(1)  # First band

    # Calculate the PN ratios
    PNratio = Pcontent/Ncontent

output_file = '/lustre/nobackup/WUR/ESG/zhou111/Data/Processed/Fertilization/PNratio.tif'
with rasterio.open(Ncontent_tiff) as src1:
    meta = src1.meta.copy()
# Update metadata if necessary
meta.update(dtype=rasterio.float32)
with rasterio.open(output_file, 'w', **meta) as dst:
    dst.write(PNratio.astype(rasterio.float32), 1)
print(f"Result saved to {output_file}")