# SABER-GeoJSON-Feature-Layer.py
SABER data for this dataset is outputted through GeoJSON and then converted into a Feature Service to be consumed through ArcGIS Online using the ArcGIS API for Python. You will need an ArcGIS Online or ArcGIS Enterprise account to process the code as a feature service.

To automate the process through Windows Task Schduler you will need to format the action to real to "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" and the Add Argument option will direct to where you have your script running. For testing purposes, I added it to my local drive: "C:\Python Test\New Code\SABER\SABER GeoJSON Feature Layer.py" on an hour interval.

The script is dependent on ArcGIS Python Library but you can add the necessary libraries through the python console if you do not have access to Pro.

Here is the Python Code for you to download and host on your machine. I also attached the ArcGIS API for https://developers.arcgis.com/python/sample-notebooks/overwriting-feature-layers/

Here is the Feature Service Overview for the current SABER GeoJSON feed that Jim provided as well: https://azdema.maps.arcgis.com/home/item.html?id=424e7373554d4e0e9497f744269f4756#overview

Any comments or questions can be directed to here:
Eric Shreve, GIS Analyst Arizona Department of Emergency & Military Affairs (DEMA)
5636 East McDowell Road, Phoenix, AZ 85008
(w) (602) 464-6344| eric.shreve@azdema.gov | dema.az.gov
