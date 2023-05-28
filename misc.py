import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        endpoint = 'Misc/Cultures'
        url   = self.get_url()+endpoint
        headers ={
            'X-Api-Key' : api_key
        }
        response = requests.get(url=url,headers=headers)
        if response.status_code ==200:
            return response.json()
        return False
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        endpoint = 'Misc/Random-Address'
        url   = self.get_url()+endpoint
        payload = {
            'number':2,
            'culture':'en'
        }
        headers ={
            'X-Api-Key' : api_key
        }
        response = requests.get(url=url,headers=headers,params=payload)
        if response.status_code ==200:
            return response.json()
        return False

misc =Misc()
TOKEN = 'c0410fcc5b554a67a6611b1c235849c6'
#print(misc.get_cultures(api_key=TOKEN))
print(misc.get_random_address(api_key=TOKEN,number=int,culture='en'))










