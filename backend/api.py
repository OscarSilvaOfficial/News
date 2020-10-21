import requests

def getApiResponse():
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=f2d97d0896ec4a74aea2ddc10e3c27a1')
    response = requests.get(url)
    return response.json()