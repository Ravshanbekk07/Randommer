import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        endpoint = 'Finance/CryptoAddress/Types'
        url   = self.get_url()+endpoint
        headers ={
            'X-Api-Key' : api_key
        }
        response = requests.get(url=url,headers=headers)
        if response.status_code ==200:
            return response.json()
        return False



    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        endpoint = 'Finance/CryptoAddress'
        url   = self.get_url()+endpoint
        payload={
            'crypto_type':str
        }
        headers ={
            'X-Api-Key' : api_key
        }
        response = requests.get(url=url,headers=headers,params=payload)
        if response.status_code ==200:
            return response.json()
        return False

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        endpoint = 'Finance/Countries'
        url   = self.get_url()+endpoint
        
        headers ={
            'X-Api-Key' : api_key
        }
        response = requests.get(url=url,headers=headers)
        if response.status_code ==200:
            return response.json()
        return False

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        pass











fin =Finance()
TOKEN = 'c0410fcc5b554a67a6611b1c235849c6'
#print(fin.get_crypto_address_types(api_key=TOKEN))
#print(fin.get_crypto_address(api_key=TOKEN,crypto_type=str))
print(fin.get_countries(api_key=TOKEN))