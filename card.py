import requests
from randommer import Randommer


class Card(Randommer):
    def get_card(self, api_key: str, type=None) -> dict:
        '''get card from randommer
        
        Args:
            api_key (str): api key
            type (str): card type

        Returns:
            dict: card data
        '''
        endpoint = 'Card'
        url = self.get_url()+endpoint
        payload = {
            'type':type
        }
        headers = {
            'X-Api-Key': api_key
        }
        response = requests.get(url,params=payload,headers=headers)
        if response.status_code == 200:
            return response.json()
        return False

        

    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        endpoint = 'Card/Types'
        url = self.get_url()+endpoint

        headers ={
            'X-Api-Key':api_key
        }
        response =requests.get(url,headers=headers)
        if response.status_code ==200:
            return response.json()
        return False
    

TOKEN =  'c0410fcc5b554a67a6611b1c235849c6'

card = Card()
print(card.get_card(api_key=TOKEN,type = 'Visa'))
print(card.get_card_types(api_key=TOKEN))