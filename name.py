import requests
from randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        endpoint = 'Name'
        url = self.get_url()+endpoint
        payload = {
            'startingWords':'ra',
            'nameType':'firstname',
            'quantity':4
        }
        headers = {
            'X-Api-Key' : api_key
        }
        response = requests.get(url=url,params=payload,headers=headers)
        if response.status_code ==200:
            return response.json()
        return False
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        endpoint = 'Name/Suggestions'
        url = self.get_url()+endpoint
        payload = {
            'startingWords':'ra'
        }
        headers = {
            'X-Api-Key' : api_key
        }
        response = requests.get(url=url,params=payload,headers=headers)
        if response.status_code ==200:
            return response.json()
        return False
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        endpoint = 'Name/Cultures'
        url = self.get_url()+endpoint
        headers = {
            'X-Api-Key' : api_key
        }
        response = requests.get(url,headers=headers)
        if response.status_code ==200:
            return response.json()
        return False



TOKEN = 'c0410fcc5b554a67a6611b1c235849c6'
name = Name()
#print(name.get_name_suggestions(api_key=TOKEN,startingWords=str))
#print(name.get_name_cultures(api_key=TOKEN))
print(name.get_name(api_key=TOKEN,nameType=str,quantity=int))