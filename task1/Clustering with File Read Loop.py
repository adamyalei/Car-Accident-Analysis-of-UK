#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN 
from sklearn import metrics 
from sklearn.datasets.samples_generator import make_blobs 
from sklearn.preprocessing import StandardScaler 
from sklearn import datasets
import os
import gmaps
import gmaps.datasets

gmaps.configure(api_key='AIzaSyAsnB1GH9bSBUq7w4KO5CDuaJBi8io8X7A')
filepath= r"/Users/testing/Desktop/project/blocks"
col_names = ['Latitude','Longitude']
locations=pd.DataFrame(columns = col_names)
files = []

    
def findFiles(filepath):
    for filename in os.listdir(filepath):
        if filename.endswith(".csv"):
            files.append(os.path.join(filepath, filename))
            #print(os.path.join(filepath, filename))
            continue
        else:
            continue
        
def dbscan():
    global locations
    for file in files:
        dataread = pd.read_csv(file, usecols = ['Longitude','Latitude'], error_bad_lines = False)
        print('--reading--', file, dataread.empty)
        if dataread.empty:
            continue
        #datainput = dataread[['Longitude','Latitude']]
        
        db = DBSCAN(eps=0.1, min_samples=80).fit(dataread)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        print('--clusters--', n_clusters_)
        n_noise_ = list(labels).count(-1)
        print('--------')
        unique_labels = set(labels)
        for k in unique_labels:
            if k == -1:
                continue
            #print('--Test--', k)
            class_member_mask = (labels == k)
            xy = np.array(dataread[class_member_mask & core_samples_mask])
            temp=pd.DataFrame({'Latitude':xy[:,1], 'Longitude':xy[:,0]})
            locations=locations.append(temp)
            xy = np.array(dataread[class_member_mask & ~core_samples_mask])
            temp=pd.DataFrame({'Latitude':xy[:,1], 'Longitude':xy[:,0]})
            locations=locations.append(temp)

def showMap(locations):
    london_coordinates = (51.50, 0.12)
    gmaps.figure(center=london_coordinates, zoom_level=12)
    gmaps.figure(map_type='HYBRID')
    fig = gmaps.figure()
    print('---')
    print(locations)
    heatmap_layer = gmaps.heatmap_layer(locations)
    fig.add_layer(heatmap_layer)
    fig

findFiles(filepath)
if len(files) == 0:
    print('No files in the given directory')
dbscan()
#showMap(locations)
london_coordinates = (51.50, 0.12)
gmaps.figure(center=london_coordinates, zoom_level=10)
gmaps.figure(map_type='HYBRID')
fig = gmaps.figure()
print('---')
print(locations)
heatmap_layer = gmaps.heatmap_layer(locations)
fig.add_layer(heatmap_layer)
fig


# In[ ]:





# In[ ]:




