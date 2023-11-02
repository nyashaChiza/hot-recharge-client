import loguru
from client import Client
from decouple import config
import os

logger = loguru.logger
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(ROOT_DIR, '.env')

recipient_number = '0787442594'
#example call to client method

access_code=config('ACC_EMAIL_ADDRESS')
access_password=config('ACC_PASSWORD')
reference=config('REFERENCES')

client = Client(access_code=access_code, access_password=access_password)
balance = client.get_wallet_balance()
logger.success(f'wallet balance:{balance}')

response = client.recharge_airtime(20,recipient_number )
logger.success(f'Recharge status:{response}')


data_bundles = client.get_data_bundles()
logger.success(data_bundles.json())


purchase_bundle = client.buy_bundle('WPWB18', recipient_number )
logger.success(purchase_bundle)