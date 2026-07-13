import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

# Get your key from https://fredaccount.stlouisfed.org/apikey
# and uncomment the following line filling in the key
#key = 'paste your key here'
fred = Fred(api_key = key)

import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap
truncblues = LinearSegmentedColormap.from_list(
    'truncblues', plt.colormaps['Blues'](range(32, 256)))

start_date = '1960-01-01'
end_date = '2025-01-01'

# https://fred.stlouisfed.org/series/CP 
profits = fred.get_series('CP', 
    frequency = 'a', # annual frequency
    aggregation_method = 'avg', # since data is annualized
    observation_start = start_date, 
    observation_end = end_date)

# https://fred.stlouisfed.org/series/W790RC1Q027SBEA
net_investment = fred.get_series('W790RC1Q027SBEA', 
    frequency = 'a', # annual frequency
    aggregation_method = 'avg', # since data is annualized
    observation_start = start_date, 
    observation_end = end_date)

# https://fred.stlouisfed.org/series/GDP 
gdp = fred.get_series('GDP', 
    frequency = 'a', # annual frequency
    aggregation_method = 'avg', # since data is annualized
    observation_start = start_date, 
    observation_end = end_date)

x = profits / gdp * 100
y =  net_investment / profits * 100

plt.figure(figsize=(6, 4))
plt.scatter(x, y, c = gdp.index.year.to_numpy(),
    edgecolors='none', cmap = truncblues, 
    s = 150, alpha = 0.66, zorder=3)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(True)
plt.gca().spines['right'].set_visible(True)

plt.ylabel("")
plt.xlabel('Corporate Profits (% of GDP)')
plt.gca().yaxis.tick_right()
plt.gca().yaxis.set_label_position("right")

plt.xticks([4, 6, 8, 10, 12])
plt.gca().spines['bottom'].set_bounds(4, 12)
plt.yticks([0, 20, 40, 60, 80, 100, 120])
plt.gca().spines['right'].set_bounds(0, 120)

plt.text(x=7.4, y=120, 
    s="Net Corporate Investment (% of Profit)", 
    fontsize=11, fontweight='normal', color='#333333')

alpha = 0.33

plt.annotate('1991', 
    xy=(x['1991-01-01'], y['1991-01-01']), xytext=(0,-10), 
    textcoords='offset points', 
    fontweight='bold', fontsize=9, alpha=alpha,
    ha='center', va='center', zorder=4)

plt.annotate('1966', 
    xy=(x['1966-01-01'], y['1966-01-01']), xytext=(0,8), 
    textcoords='offset points', 
    fontweight='bold', fontsize=9, alpha=alpha,
    ha='center', va='center', zorder=4)

plt.annotate('1962', 
    xy=(x['1962-01-01'], y['1962-01-01']), xytext=(-16, 0), 
    textcoords='offset points', 
    fontweight='bold', fontsize=9, alpha=alpha,
    ha='center', va='center', zorder=4)

plt.annotate('1986', 
    xy=(x['1986-01-01'], y['1986-01-01']), xytext=(16, 6), 
    textcoords='offset points', 
    fontweight='bold', fontsize=9, alpha=alpha,
    ha='center', va='center', zorder=4)

plt.annotate('2021', xy=(x['2021-01-01'], y['2021-01-01']), 
    xytext=(0,-10), textcoords='offset points', 
    fontweight='bold', fontsize=9, alpha=alpha,
    ha='center', va='center', zorder=4)


plt.annotate('2009', 
    xy=(x['2009-01-01'], y['2009-01-01']), xytext=(0, 8), 
    textcoords='offset points', 
    fontweight='bold', fontsize=9, alpha=alpha,
    ha='center', va='center', zorder=4)

plt.annotate('2025', 
    xy=(x['2025-01-01'], y['2025-01-01']), xytext=(-14, -9), 
    textcoords='offset points', 
    fontweight='bold', fontsize=9, alpha=alpha,
    ha='center', va='center', zorder=4)

plt.annotate('2008', 
    xy=(x['2008-01-01'], y['2008-01-01']), xytext=(-18,0), 
    textcoords='offset points', 
    fontweight='bold', fontsize=9, alpha=alpha,
    ha='center', va='center', zorder=4)

plt.annotate('2003', 
    xy=(x['2003-01-01'], y['2003-01-01']), xytext=(0,-10), 
    textcoords='offset points', 
    fontweight='bold', fontsize=9, alpha=alpha,
    ha='center', va='center', zorder=4)

plt.annotate('1979', 
    xy=(x['1979-01-01'], y['1979-01-01']), xytext=(0,8), 
    textcoords='offset points', 
    fontweight='bold', fontsize=9, alpha=alpha,
    ha='center', va='center', zorder=4)

plt.annotate('2000', 
    xy=(x['2000-01-01'], y['2000-01-01']), xytext=(-16,6), 
    textcoords='offset points', 
    fontweight='bold', fontsize=9, alpha=alpha,
    ha='center', va='center', zorder=4)

plt.text(x=0, y=-0.2, s='Data: St. Louis Fed | @sashamarcze', 
         fontsize=9, color='#777777', 
         ha='left', va='top', transform=plt.gca().transAxes)

plt.subplots_adjust(bottom=0.2)

plt.tight_layout()
plt.savefig('profit_vs_investment.png', 
    bbox_inches='tight', dpi=512)

plt.savefig('profit_vs_investment.svg', format='svg', 
    bbox_inches='tight', transparent=True)


