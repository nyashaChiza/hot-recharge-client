import os
import loguru
import hotrecharge
from dotenv import load_dotenv

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(ROOT_DIR, '.env')
logger = loguru.logger
load_dotenv(dotenv_path)
CUSTOM_MESSAGE = os.getenv('CUSTOM_MESSAGE')

class Client():

    access_code=os.getenv('ACC_EMAIL_ADDRESS')
    access_password=os.getenv('ACC_PASSWORD')
    reference=os.getenv('REFERENCES')
    
    config = hotrecharge.HRAuthConfig(
            access_code=access_code, 
            access_password=access_password,
            reference=reference
        )

    def __str__(self):
        return f'{self.access_code}'  
                
    def __init__(self, **kwargs):
        self.access_code = kwargs.get('access_code', self.access_code)
        self.access_password = kwargs.get('access_password', self.access_password)
        self.reference = kwargs.get('reference', self.reference)
        self.api = hotrecharge.HotRecharge(self.config, return_model=True)

    def get_evds(self)->object:
        evds = self.self.api.getEVDs()
        return evds
    
    def get_wallet_balance(self)->object:
        wallet_balance = self.api.walletBalance()
        return wallet_balance
    
    def get_data_bundles(self)->object:
        data_bundles = self.api.getDataBundles()
        return data_bundles
            
    def recharge_data_bundles(self, data_bundle_code:str,recipient_phone_number:str)->object:
        custom_message = f'Your account has been topped with {data_bundle_code} data bundle .\n Thank you for doing business with Airtym.com'
        recharge_data_bundle_response = self.api.dataBundleRecharge(product_code=data_bundle_code, number=recipient_phone_number, mesg=custom_message)
        return recharge_data_bundle_response

    def recharge_airtime_response(self, airtime_amount:int, recipient_phone_number:str)->object:
        custom_message = f'Your account has been topped with {airtime_amount} RTGS .\n Thank you for doing business with Airtym.com'
        response = self.api.rechargePinless(amount=airtime_amount, number=recipient_phone_number, mesg=custom_message)
        return response
    
    
    def recharge_zesa(self, meter_number:str, amount:int)->object:
         #zesa logic here
        return None         