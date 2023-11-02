import os
import loguru
import hotrecharge
import random
import json
import requests
from decouple import config

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(ROOT_DIR, '.env')
logger = loguru.logger

CUSTOM_MESSAGE = os.getenv('CUSTOM_MESSAGE')

class Client():
    def __init__(self, access_code, access_password):
        self.session = requests.Session()
        self.session.headers={
            'x-access-code': access_code,
            'x-access-password': access_password,
            'x-agent-reference': f"airtym-{str(random.randint(0,10000000))}",
            "content-type": 'application/json',
            "cache-control": "no-cache",
        }
        

    def __str__(self):
        return f'{self.access_code}'  
                
    def reset_reference(self):
        self.session.headers['x-agent-reference'] = f'aitym-{str(random.randint(0,100))}{str(random.randint(0,10000))}'


    def get_evds(self)->object:
        evds = self.self.api.getEVDs()
        return evds
    
    def get_wallet_balance(self)->object:
        self.reset_reference()
        self.reset_reference()
        url = 'https://ssl.hot.co.zw/api/v1/agents/wallet-balance'
        
        response = self.session.get(url)
       
        return response.json()['WalletBalance']
    
    def get_data_bundles(self)->object:
        self.reset_reference()
        url ='https://ssl.hot.co.zw/api/v1/agents/get-data-bundles-all'
        response = self.session.get(url)
       
        return response
            
    def recharge_data_bundles(self, data_bundle_code:str,recipient_phone_number:str)->object:
        self.reset_reference()
        custom_message = f'Your account has been topped with {data_bundle_code} data bundle .\n Thank you for doing business with Airtym.com'
        headers = {
            'x-access-password': self.access_password,
            'x-access-code': self.access_code
        }
        recharge_data_bundle_response = self.api.dataBundleRecharge(product_code=data_bundle_code, number=recipient_phone_number, mesg=custom_message, headers=headers)
        return recharge_data_bundle_response

    def recharge_airtime(self, amount:int, recipient_phone_number:str)->object:
        self.reset_reference()
        url = "https://ssl.hot.co.zw/api/v1/agents/recharge-pinless"
        custom_message = f'Your account has been topped with {amount} RTGS .\n Thank you for doing business with Airtym.com'
        body ={"amount": amount,"targetMobile": recipient_phone_number,"CustomerSMS":custom_message}
        
        response = self.session.post(url, json=body)
        return response.json()
    
    def buy_bundle(self,product_code,recipient):
        self.reset_reference()
        url = "https://ssl.hot.co.zw/api/v1/agents/recharge-data"
        custom_message = f'The account {recipient} has been topped.\n Thank you for doing business with Airtym.com'
        body ={"ProductCode": product_code,"targetMobile":recipient }
        
        response = self.session.post(url, json=body)
        return response.json()
    
        
        
    def recharge_zesa(self, meter_number:str, amount:int)->object:
         #zesa logic here
        return None