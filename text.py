import requests
from randommer import Randommer


class Text(Randommer):
    def generate_LoremIpsum(self, api_key: str, loremType: str, type: str, number: int) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            loremType (str): loremType (normal or bussines)
            type (str): type (words or paragraphs)
            number (int): number

        Returns:
            str: Lorem text
        '''
        endpoint = 'Text/LoremIpsum'
        url   = self.get_url()+endpoint
        payload = {
            'LoremType':'normal',
            'type':'words',
            'number':20
        }
        headers ={
            'X-Api-Key' : api_key
        }
        response = requests.get(url=url,headers=headers,params=payload)
        if response.status_code ==200:
            return response.json()
        return False
    
    def generate_password(self, api_key: str, length: int, hasDigits: bool, hasUppercase: bool, hasSpecial: bool) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            length (int): lenth of password
            hasDigits (bool): hasDigits
            hasUppercase (bool): hasUppercase
            hasSpecial (bool): hasSpecial

        Returns:
            str: pasword
        '''
        endpoint = 'Text/Password'
        url = self.get_url()+endpoint
        headers = {
            'X-Api-Key' : api_key
        }
        payload = {
            'length':12,
            'hasDigits':True,
            'hasUppercase':True,
            'hasSpecial':True
        }
        response = requests.get(url,params=payload,headers=headers)
        if response.status_code==200:
            return response.json()
        return False


TOKEN = 'c0410fcc5b554a67a6611b1c235849c6'
text = Text()
#print(text.generate_LoremIpsum(api_key=TOKEN,loremType=str,type=str,number=int))
print(text.generate_password(api_key=TOKEN,length = int,hasDigits=bool,hasSpecial=bool,hasUppercase=bool))
