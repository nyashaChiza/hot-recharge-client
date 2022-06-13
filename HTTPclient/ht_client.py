import hotrecharge
from dotenv import load_dotenv
import os
import loguru

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(ROOT_DIR, '.env')
logger = loguru.logger
load_dotenv(dotenv_path)
custom_message = os.getenv('CUSTOM_MESSAGE')

class Client():

    access_code=os.getenv('ACC_EMAIL_ADDRESS')
    access_password=os.getenv('ACC_PASSWORD')
    reference=os.getenv('REFERENCES')
    
    def __init__(self, **kwargs):
        self.access_code = kwargs.get('access_code', self.access_code)
        self.access_password = kwargs.get('access_password', self.access_password)
        self.reference = kwargs.get('reference', self.reference)

    def get_evds(self)->object:
        config = hotrecharge.HRAuthConfig(
            access_code=self.access_code, 
            access_password=self.access_password,
            reference=self.reference
        )
        api = hotrecharge.HotRecharge(config, return_model=True)
        evds = api.getEVDs()
        return evds
    
    def get_wallet_balance(self)->object:
        config = hotrecharge.HRAuthConfig(
            access_code=self.access_code, 
            access_password=self.access_password,
            reference=self.reference
        )
        api = hotrecharge.HotRecharge(config, return_model=True)
        wallet_balance = api.walletBalance()
        return wallet_balance
    
    def get_data_bundles(self)->object:
        config = hotrecharge.HRAuthConfig(
            access_code=self.access_code,
            access_password=self.access_password,
            reference=self.reference
        )
        api = hotrecharge.HotRecharge(config, return_model=True)
        data_bundles = api.getDataBundles()
        return data_bundles
            
    def recharge_data_bundles(self, data_bundle_code,recipient_phone_number)->object:
        config = hotrecharge.HRAuthConfig(
            access_code=self.access_code,
            access_password=self.access_password,
            reference=self.reference
        )
        api = hotrecharge.HotRecharge(config, return_model=True)
        custom_message = f'Your account has been topped with {data_bundle_code} data bundle .\n Thank you for doing business with Airtym.com'
        recharge_data_bundle_response = api.dataBundleRecharge(product_code=data_bundle_code, number=recipient_phone_number, mesg=custom_message)
        return recharge_data_bundle_response


    def recharge_airtime_response(self, airtime_amount, recipient_phone_number)->object:
        config = hotrecharge.HRAuthConfig(
            access_code=self.access_code,
            access_password=self.access_password,
            reference=self.reference
        )
        api = hotrecharge.HotRecharge(config, return_model=True)
        custom_message = f'Your account has been topped with {airtime_amount} RTGS .\n Thank you for doing business with Airtym.com'
        response = api.rechargePinless(amount=airtime_amount, number=recipient_phone_number, mesg=custom_message)
        return response
    
    def recharge_zesa(self, meter_number, amount)->object:
        config = hotrecharge.HRAuthConfig(
            access_code=self.access_code,
            access_password=self.access_password,
            reference=self.reference
        )
        api = hotrecharge.HotRecharge(config, return_model=True)
        #zesa logic here
        return None         