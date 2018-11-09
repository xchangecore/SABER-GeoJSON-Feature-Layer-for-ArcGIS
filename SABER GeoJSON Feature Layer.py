
# coding: utf-8

# In[15]:


import urllib.request, json
from arcgis.gis import GIS


# In[16]:


gis = GIS("https://www.arcgis.com", "YOUR AGOL USERNAME HERE", "YOUR AGOL PASSWORD HERE")
print("Logged in as " + str(gis.properties.user.username))


# In[17]:


with urllib.request.urlopen("https://app.spotonresponse.com/openfeeds/saberopen.json") as url:
    data = json.loads(url.read().decode())


# In[18]:


import os


# In[19]:


os.chdir('C:/test')


# In[20]:


#name your geojson file to whatever you want. Just make sure it has the geojson extension here.
#The data is written to the file highimpactdata.geojson in the test folder.
with open('SABER.geojson', 'w') as f:
    json.dump(data, f)


# In[21]:


SABER_json_file='C:/test/SABER.geojson'


# In[22]:


#item id of the feature layer in AGOL Organization
SABER_featureLayer_item = gis.content.get('Enter Feature Layer ID Here')


# In[23]:


from arcgis.features import FeatureLayerCollection
SABER_incidents_flayer_collection = FeatureLayerCollection.fromitem(SABER_featureLayer_item)


# In[24]:


from arcgis.features import FeatureLayer
SABER_incidents_flayer = FeatureLayer.fromitem(SABER_featureLayer_item, layer_id=0)


# In[25]:


#get the count of the features in the geojson
json_data = open(SABER_json_file)
data2 = json.load(json_data)
print(len(data2['features']))


# In[26]:


#if there are features then overwrite the layer with the new data. If no features then truncate the database.
if len(data2['features'])>0:
    SABER_incidents_flayer_collection.manager.overwrite(SABER_json_file)
else:
    SABER_incidents_flayer.manager.truncate()

