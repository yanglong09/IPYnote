
# coding: utf-8

# In[ ]:

from mpl_toolkits.basemap import Basemap, cm
# requires netcdf4-python (netcdf4-python.googlecode.com)
from netCDF4 import Dataset as NetCDFFile
import numpy as np
import matplotlib.pyplot as plt

# plot rainfall from NWS using special precipitation
# colormap used by the NWS, and included in basemap.

nc1 = NetCDFFile('C:/Anaconda/0DATA/current0.nc')
nc2 = NetCDFFile('C:/Anaconda/0DATA/future0.nc')

pr_TT = nc1.variables['TT']
po_TT = nc2.variables['TT']

pr_data = pr_TT[:]
pr_data = pr_data[0,3,:,:]

po_data = po_TT[:]
po_data = po_data[0,3,:,:]

newdata = po_data-pr_data

latcorners = nc1.variables['CLAT'][:]
loncorners = nc1.variables['CLONG'][:]

fig, axes = plt.subplots(nrows=1, ncols=3)
ax1, ax2, ax3= axes.ravel()

map_ax = Basemap(ax = ax1,llcrnrlon=110.79,llcrnrlat=35.2,urcrnrlon=121.1,urcrnrlat=43.1,resolution='i',projection='tmerc',lon_0=115.4,lat_0=39.272)
map_ax.readshapefile('C:\0=research\Research\4=BJ WRF analysis\RADAR_analysis\shape\plain-borderline.shx','attribute', drawbounds=True)
map_ax.drawcoastlines()
map_ax.drawlsmask()
map_ax.drawcountries()
# draw parallels.
parallels = np.arange(0.,90,5.)
map_ax.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
# draw meridians
meridians = np.arange(110.,120.,5.)
map_ax.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
ny = pr_data.shape[0]; nx = pr_data.shape[1]
lons, lats = map_ax.makegrid(nx, ny) # get lat/lons of ny by nx evenly space grid.
x, y = map_ax(lons, lats) # compute map proj coordinates.
# draw filled contours.
clevs = [210,225,230,235,240,245,250,255,260,265,270]
cs = map_ax.contourf(x,y,pr_data,clevs,cmap='RdBu_r')
# add colorbar.
cbar = map_ax.colorbar(cs,location='bottom',pad="5%")
cbar.set_label('K')
ax1.set_title('Current')

map_ax2 = Basemap(ax = ax2,llcrnrlon=110.79,llcrnrlat=35.2,urcrnrlon=121.1,urcrnrlat=43.1,resolution='i',projection='tmerc',lon_0=115.4,lat_0=39.272)
map_ax2.drawcoastlines()
map_ax2.drawlsmask()
map_ax2.drawcountries()
# draw parallels.
map_ax2.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
# draw meridiann
map_ax2.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
# draw filled contours.
clevs = [210,222,224,235,240,245,250,255,260,265,270]
cs = map_ax2.contourf(x,y,po_data,clevs,cmap='RdBu_r')
# add colorbar.
cbar = map_ax2.colorbar(cs,location='bottom',pad="5%")
cbar.set_label('K')
ax2.set_title('Future')

map_ax = Basemap(ax = ax3,llcrnrlon=110.79,llcrnrlat=35.2,urcrnrlon=121.1,urcrnrlat=43.1,resolution='i',projection='tmerc',lon_0=115.4,lat_0=39.272)
map_ax.drawcoastlines()
map_ax.drawlsmask()
map_ax.drawcountries()
# draw parallels.
parallels = np.arange(0.,90,5.)
map_ax.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
# draw meridians
meridians = np.arange(110.,120.,5.)
map_ax.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
ny = pr_data.shape[0]; nx = pr_data.shape[1]
lons, lats = map_ax.makegrid(nx, ny) # get lat/lons of ny by nx evenly space grid.
x, y = map_ax(lons, lats) # compute map proj coordinates.
# draw filled contours.
clevs = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
# clevs = [210,225,230,235,240,245,250,255,260,265,270]
cs = map_ax.contourf(x,y,newdata,clevs,cmap='RdBu_r')
# add colorbar.
cbar = map_ax.colorbar(cs,location='bottom',pad="5%")
cbar.set_label('K')
ax3.set_title('Future-Current(pres=950 hpa)')

plt.show()


# In[ ]:



