rates = '160.0,,,'
usd = 160.0

def pkr_to_usd(pkr):
    with open('forex.csv','r') as fx:
        rates = fx.readline()
        usd = float(rates.split(',')[0])
    return int(pkr/usd)
