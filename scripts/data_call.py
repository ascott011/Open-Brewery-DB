import requests
import json
import os 

brewery_api_url = 'https://api.openbrewerydb.org/v1/breweries'

wanted_fields = ['id', 'name', 'brewery_type', 'city', 'state', 'postal_code', 'country']

def fetch_brewery_data():
    try:
        response = requests.get(brewery_api_url, )

        if response.status_code == 200:
            data = response.json()
            #checks to make sure data folder exist and makes it if not
            if not os.path.exists('../data'):
                os.makedirs('../data')

            with open('data/brewery_data.json', 'w') as file:
                json.dump(data, file, indent=2)
            
            print('Data retrieved successfully.')
    
        else: 
            print('Unable to retieve data. Error:', response.status_code)

    except requests.exceptions.RequestException as e:
        print('Error:', e)

fetch_brewery_data()