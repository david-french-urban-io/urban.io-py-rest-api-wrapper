import api_wrappers
import os

#declare api credentials, recommended to load these from environemnt variables
EMAIL = os.environ["X_USER_EMAIL"] #replace with your email address
API_TOKEN  = os.environ["X_USER_TOKEN"] #replace with your api token

#create instance of the API class
api = api_wrappers.PublicRESTEndpoints(
    email= EMAIL, 
    token=API_TOKEN
)

#get the datastreams location external ID available in the platform
response_dict = api.get_datastreams_by_location_ext("zw-8cKVAFIAZTtguGMzwKw")

#get the list of datastreams from the response
datastreams = response_dict['datastreams']

#loop through the datastreams any print some metadata
for ds in datastreams:
    ds_external_id = ds['external_id']
    device_id = ds['hardware_device_id']
    device_position = ds['labels']['position']
    print(f"Position: {device_position}, External ID of Datastream: {ds_external_id}, Device ID:{device_id}")

#get the 10 last readings for a datastream...
readings = api.get_datastream_readings(
    datastream_id= "eOKcvW61BGzLx6KfNaivbg", 
    params={"size":"10"}
)

print(readings)



