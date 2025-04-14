import requests

def ipTracker(ip):
    url = f"https://jsonmock.hackerrank.com/api/ip?ip={ip}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return "No Result Found"
    
    data = response.json()
    
    # Check if data list is not empty
    if data['data']:
        return data['data'][0]['country']
    else:
        return "No Result Found"