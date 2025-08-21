import requests

url = 'https://api.openbrewerydb.org/v1/breweries'

def get_data():
    try:
        response = requests.get(url)  # Fixed this line

        if response.status_code == 200:
            data = response.json()
            return data
        
        else:
            print('Error:', response.status_code)

    except requests.exceptions.RequestException as e:
        print('Error:', e)

if __name__ == "__main__":
    data = get_data()
    print(data)
