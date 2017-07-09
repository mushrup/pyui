from zipline.api import order, record, symbol
from matplotlib import style
from sys import argv

style.use('ggplot')
print(str(argv))
file = open('pink_orange.txt','r')
pink,orange = str(file.readline()).split()
file.close()
def initialize(context):
    print(pink)
    print(orange)
    context.sab = symbol(pink)
    context.stx = symbol(orange)

def handle_data(context, data):
    # Save values for later inspection
    price_sab = data.history(context.sab, "price", bar_count=30, frequency="1d")
    pct_change_sab = (price_sab.ix[-1] - price_sab.ix[0]) / price_sab.ix[0]
    price_stx = data.history(context.stx, "price", bar_count=30, frequency="1d")
    pct_change_stx = (price_stx.ix[-1] - price_stx.ix[0]) / price_stx.ix[0]
    record(SAB=pct_change_sab,
           STX=pct_change_stx)

def analyze(context=None, results=None): 
    import matplotlib.pyplot as plt
    fig, (ax1) = plt.subplots(num=None, figsize=(10, 5), dpi=80, facecolor='w', edgecolor='k')
    fig.set_size_inches(10, 5)
    ax1.plot(results.STX, lw=2,  color="#EAA2AD", label=pink)
    ax1.plot(results.SAB, lw=2,  color='#72A07E', label=orange)
    ax1.fill_between(results.STX.index, results.STX, color="#E5A4C1", alpha=0.5)
    ax1.set_ylabel('Price percentage change')
    plt.legend()
    plt.show()