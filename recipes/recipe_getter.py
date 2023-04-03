import os
import requests

class RecipeGetter:

    def trending():
        api_url = f"https://{os.environ.get('CD_API_HOST', '')}/randomselection.php"
        headers = {
            "X-RapidAPI-Key": os.environ.get('API_KEY', ''),
	        "X-RapidAPI-Host": os.environ.get('CD_API_HOST', '')
        }
        response = requests.request("GET", api_url, headers=headers)
        return response.json()["drinks"]
    
    def popular():
        url = f"https://{os.environ.get('CD_API_HOST', '')}/popular.php"

        headers = {
	        "X-RapidAPI-Key": os.environ.get('API_KEY', ''),
	        "X-RapidAPI-Host": os.environ.get('CD_API_HOST', '')
        }

        response = requests.request("GET", url, headers=headers)
        return response.json()["drinks"]


    def new():
        url = f"https://{os.environ.get('CD_API_HOST', '')}/latest.php"

        headers = {
	        "X-RapidAPI-Key": os.environ.get('API_KEY', ''),
	        "X-RapidAPI-Host": os.environ.get('CD_API_HOST', '')
        }

        response = requests.request("GET", url, headers=headers)
        return response.json()["drinks"]
    
    def detail(db, drink_id):
        if db == 'cd':
            url = f"https://{os.environ.get('CD_API_HOST', '')}/lookup.php"
            headers = {
            	"X-RapidAPI-Key": os.environ.get('API_KEY', ''),
	            "X-RapidAPI-Host": os.environ.get('CD_API_HOST', '')
            }
            querystring = {"i": drink_id}

            response = requests.request("GET", url, headers=headers, params=querystring)
            response = response.json()["drinks"][0]

        elif db == 'dd':
            url = f"https://{os.environ.get('DD_API_HOST', '')}/v1/cocktails/{drink_id}"
            headers = {
	            "X-RapidAPI-Key": os.environ.get('API_KEY', ''),
	            "X-RapidAPI-Host": os.environ.get('DD_API_HOST', '')
            }
            response = requests.request("GET", url, headers=headers)
            response = response.json()
        else:
            #throw an error
            return None
        
        return response
    
    def bar_cocktails(ingredients):
        url = f"https://{os.environ.get('DD_API_HOST', '')}/v1/cocktails/ingredients"
        querystring = {
            "filters": ingredients,
            "type": "by_name"
        }
        headers = {
	        "X-RapidAPI-Key": os.environ.get('API_KEY', ''),
	        "X-RapidAPI-Host": os.environ.get('DD_API_HOST', '')
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()
    
    def simple_search_cocktails(query):
        url = f"https://{os.environ.get('DD_API_HOST', '')}/v1/cocktails/search"
        querystring = {
            "query": query
        }
        headers = {
	        "X-RapidAPI-Key": os.environ.get('API_KEY', ''),
	        "X-RapidAPI-Host": os.environ.get('DD_API_HOST', '')
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()