
from pywallet import wallet
import sys


fd=open("bip39.txt")
for n in  fd.read().split('\n'):
    #seed="coyote range brand rubber sister monster property opera gift fiscal "+n+" raw"
    seed="tube silk brisk can emerge expose road area under clip rough "+n
    print(seed)
    w = wallet.create_wallet(network="BTC", seed=seed, children=1)
    if sys.argv[1]==w.get('address'):
        print('seed found !!!:',w.get('seed'))
        break
