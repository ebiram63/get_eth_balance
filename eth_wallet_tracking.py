
from requests import get
import matplotlib

Api_KEY = "G148JSYICQDVTKHG7XRFSQT8YZ8QR147QP"
address = "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae"
BASE_URL  = "https://api.etherscan.io/api"
ETHER_VALUE = 10 ** 18



'''https://api.etherscan.io/api
   ?module=account
   &action=balance
   &address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
   &tag=latest
   &apikey=YourApiKeyToken'''
   
   


def make_api_url(module, action, address, **kwargs):
    #kwargs ={"tag": "latest", "x":"2" }
    url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={Api_KEY}"   
    
    for key, value in kwargs.items():
        url += f"&{key}={value}"
        
    return url    
        
def get_account_balance(address):        
    get_balance_url = make_api_url("account", "balance", address, tag="latest", x="2")
    #print(get_balance_url)
    response = get(get_balance_url)
    data = response.json()
    value = int(data["result"]) / ETHER_VALUE
    return value

eth = get_account_balance(address)
print(eth)