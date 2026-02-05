import os
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import ApiCreds, BalanceAllowanceParams, AssetType

# Load Credentials
api_key = os.getenv('POLY_API_KEY')
api_secret = os.getenv('POLY_SECRET')
passphrase = os.getenv('POLY_PASSPHRASE')
p_key = os.getenv('PRIVATE_KEY').strip()
funder = os.getenv('FUNDER_ADDRESS').strip()

creds = ApiCreds(api_key=api_key, api_secret=api_secret, api_passphrase=passphrase)

# signature_type=1 is REQUIRED for Email/Magic users to see their balance
client = ClobClient(
    host='https://clob.polymarket.com', 
    key=p_key, 
    chain_id=137, 
    creds=creds, 
    funder=funder,
    signature_type=1 
)

try:
    resp = client.get_balance_allowance(BalanceAllowanceParams(asset_type=AssetType.COLLATERAL))
    print(f"\n💰 [SUCCESS] Empire Funds: ${resp.get('balance')} USDC.e")
except Exception as e:
    print(f"❌ API Error: {e}")
