import loguru
from HTTPclient.ht_client import Client
from dotenv import load_dotenv
import os

logger = loguru.logger
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(ROOT_DIR, '.env')
load_dotenv(dotenv_path)


access_code=os.getenv('ACC_EMAIL_ADDRESS')
access_password=os.getenv('ACC_PASSWORD')
reference=os.getenv('REFERENCES')


client = Client(access_code=access_code, access_password=access_password, reference=reference)
balance = client.get_wallet_balance()
logger.info(f'Wallet balance is {balance}')