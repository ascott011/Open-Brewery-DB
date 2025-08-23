import requests

# this file is to see what fields there are so I don't grab everything 

url = 'https://api.openbrewerydb.org/v1/breweries'

def get_wanted_fields():
    try:
        response = requests.get(url) 

        if response.status_code == 200:
            data = response.json()
            #get the keys from the first item in the list
            if isinstance(data, list) and len(data) > 0:
                first_item = data[0]
                keys = list(first_item.keys())
                print("Keys:", keys)
        else:
            print('Call failed. Error:', response.status_code)

    except requests.exceptions.RequestException as e:
        print('Error:', e)

    finally:
        print('Keys retrieved successfully.')       

if __name__ == "__main__":
    fields = get_wanted_fields()
    print(fields)
    