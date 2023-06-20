import random, time, requests, json, decimal
from web3 import Web3, HTTPProvider
from eth_account import Account
import json

ZksRPC = 'https://mainnet.optimism.io/'
web3 = Web3(HTTPProvider(ZksRPC))

def randomSleep(intervalMin, intervalMax):
    sTime = random.randint(intervalMin, intervalMax)
    print('karat兔子--随机间隔--等待...', sTime)
    time.sleep(sTime)

def karat_process(walletAddress, private_key,mynonce):
    print(f'karat兔子 开始执行, walletAddress={walletAddress}')
    try:
        karat_mint(walletAddress, private_key, random.randint(0, 150),mynonce)
    except Exception as ex:
        print(ex)
    finally:
        randomSleep(0, 1)

def signature(pkey):
    address = Account.from_key(pkey).address
    url = 'https://api.opw.today/api/bnb/eligibility/claim'
    postData = {
        
            "address": address,
        
    }
    signResponse = requests.post(url, json=postData)
    signResponse = signResponse.text
    # signResponse = json.dumps(signResponse)
    s = eval(signResponse)
    nonce = s['data']['nonce']
    sig = s['data']['signature']
    return nonce,sig

# keys = ''''''
# pkey = keys.split(f'\n')
# print(pkey)
# karat_mint()
p = '0x'
def mintNFT(pkey):
    nonce , sig = signature(pkey)
    print('获取到NONCE=='+str(nonce))
    print('获取到N签名=='+sig)
    address = Account.from_key(pkey).address
    print('获取到地址=='+address)
    abi= '''[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint128","name":"nonce","type":"uint128"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"address","name":"referrer","type":"address"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"Claim","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"INIT_CLAIM","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_ADDRESSES","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_REFER_TOKEN","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_TOKEN","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"_claimedUser","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"_usedNonce","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"canClaimAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"canGetReferReward","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint128","name":"nonce","type":"uint128"},{"internalType":"bytes","name":"signature","type":"bytes"},{"internalType":"address","name":"referrer","type":"address"}],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claimedCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimedPercentage","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimedSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getInfoView","outputs":[{"components":[{"internalType":"uint256","name":"maxToken","type":"uint256"},{"internalType":"uint256","name":"initClaim","type":"uint256"},{"internalType":"uint256","name":"currentClaim","type":"uint256"},{"internalType":"bool","name":"claimed","type":"bool"},{"internalType":"uint256","name":"inviteRewards","type":"uint256"},{"internalType":"uint256","name":"inviteUsers","type":"uint256"},{"internalType":"uint256","name":"claimedSupply","type":"uint256"},{"internalType":"uint256","name":"claimedCount","type":"uint256"}],"internalType":"struct OWDistributionPool.InfoView","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token_","type":"address"},{"internalType":"uint256","name":"startTime_","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"inviteRewards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"inviteUsers","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint128","name":"nonce","type":"uint128"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"isValidSignature","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"referReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"val","type":"address"}],"name":"setSigner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"signer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"startTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'''
    abi = json.loads(abi)
    合约地址='0x61d08d20Ed2112693D5a29AE2362869C1AC56239'
    contract = web3.eth.contract(address=合约地址, abi=abi)
    params = {
        "from": address,
        'gasPrice': web3.toWei(0.1, 'gwei'),
        'value': 0,
        "nonce": web3.eth.getTransactionCount(web3.toChecksumAddress(address)),  # 获取交易序号
        'chainId': web3.eth.chain_id,
        'gas': 1000000,
    }
    data=contract.functions.claim(nonce,sig,address).buildTransaction(params)
    signed_txn = web3.eth.account.signTransaction(data, private_key=pkey)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    result = web3.eth.wait_for_transaction_receipt(tx_hash.hex(), timeout=120, poll_latency=5)
    print(result)
if __name__ == '__main__':
    print('刘小鸽特别开发，感谢贡献，联系微信：lucus9939')
    # loginKey = input('请输入社区密码:')
    # authUrl = 'https://toolsforyou.cn/authUsers.php?method=bnx&dateLimit=230305&loginKey='+loginKey
    # authRes = requests.get(authUrl).text
    # print(authRes == 'ok')
    # if authRes == 'ok' :
    #     print(authRes)
    #     print('验证通过！')
    #     time.sleep(3)
    # else:
    #     print(authRes)
    #     print('验证失败！联系管理员：Lucus9939')
    #     time.sleep(5)
    #     os._exit()
    pk = input('请输入私钥按回车：')
    mintNFT(pk)