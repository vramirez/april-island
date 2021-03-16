import requests

def getGeoPost(lon, lat):
    URL = 'http://api.postcodes.io/postcodes?lon=%f&lat=%f'
    response = requests.get(URL%(float(lon),float(lat)))
    if (response.status_code == 200):
        result = response.json()['result']
        if ( result is not None):
            #Geo location found
            return  result
    return None