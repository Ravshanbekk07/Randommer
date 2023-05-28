import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        endpoint = 'Phone/Generate'
        url = self.get_url()+endpoint
        headers = {
             'X-Api-Key' : api_key
        }    
        payload = {
            'CountryCode':'uz',
            'Quantity':5
        }
        response = requests.get(url,params=payload,headers=headers)
        if response.status_code ==200:
            return response.json()
        return False
    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        pass
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        endpoint = 'Phone/Validate'
        url = self.get_url()+endpoint
        headers = {
             'X-Api-Key' : api_key
        }    
        payload = {
            'telephone':'+998934526621',
            'CountryCode':'99'
        }
        response = requests.get(url,params=payload,headers=headers)
        if response.status_code ==200:
            return response.json()
        return False
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        endpoint = 'Phone/Countries'
        url = self.get_url()+endpoint
        headers = {
             'X-Api-Key' : api_key
        }    
        
        response = requests.get(url,headers=headers)
        if response.status_code ==200:
            return response.json()
        return False




TOKEN = 'c0410fcc5b554a67a6611b1c235849c6'
phone = Phone()
#print(phone.is_valid(api_key=TOKEN,telephone=str,CountryCode=str))
#print(phone.get_countries(api_key=TOKEN))
print(phone.generate(api_key=TOKEN,CountryCode=str,Quantity=int))
