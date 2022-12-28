import requests

class ApiConnection:

    def __init__(self,pokemon_name) :
        self.url =f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    def makeRequest(self):
        response= requests.get(self.url)
        print(response)
        print(response.status_code)
        json_response=response.json()
        #print(json_response["abilities"])
        for item in json_response["stats"]:
            print(item["base_stat"],item["stat"]["name"])
        

api_connection=ApiConnection("charizard")
api_connection.makeRequest()       