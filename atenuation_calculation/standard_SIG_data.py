from osgeo import gdal
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import elevation

# mask the NaN values

filename = "./dem-uni.tif"
gdal_data = gdal.Open(filename)
gdal_band = gdal_data.GetRasterBand(1)
nodataval = gdal_band.GetNoDataValue()

# convert to a numpy array
data_array = gdal_data.ReadAsArray().astype(np.float)
data_array

# replace missing values if necessary
if np.any(data_array == nodataval):
    data_array[data_array == nodataval] = np.nan


##
## Visualize Data with Matplotlib

#Plot out data with Matplotlib's 'contour'
fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111)
plt.contour(data_array, cmap = "viridis",
            levels = list(range(0, 5000, 100)))
plt.title("Elevation UNI's Hill")
cbar = plt.colorbar()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
