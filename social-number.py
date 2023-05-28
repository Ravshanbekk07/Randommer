import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        endpoint = 'SocialNumber'
        url   = self.get_url()+endpoint
        headers ={
            'X-Api-Key' : api_key
        }
        response = requests.get(url=url,headers=headers)
        if response.status_code ==200:
            return response.json()
        return False
    


TOKEN = 'c0410fcc5b554a67a6611b1c235849c6'
social = SocialNumber()
print(social.get_SocialNumber(api_key=TOKEN)) 