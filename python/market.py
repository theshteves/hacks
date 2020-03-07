#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt

from matplotlib import style
style.use('fivethirtyeight')

import matplotlib.cm as cm
from matplotlib import colors
colour = colors.DivergingNorm(vmin=800, vcenter=1000, vmax=1200)


def randomwalk(dims=(256, 256), n=20, sigma=5, alpha=0.95, seed=1):
    """ A simple random walk with memory """

    r, c = dims
    gen = np.random.RandomState(seed)
    pos = gen.rand(2, n) * ((r,), (c,))
    old_delta = gen.randn(2, n) * sigma

    while True:
        delta = (1. - alpha) * gen.randn(2, n) * sigma + alpha * old_delta
        pos += delta
        for ii in range(n):
            if not (0. <= pos[0, ii] < r):
                pos[0, ii] = abs(pos[0, ii] % r)
            if not (0. <= pos[1, ii] < c):
                pos[1, ii] = abs(pos[1, ii] % c)
        old_delta = delta
        yield pos

TRADES = []
holding = 0

STONKS = 1000000
N = 1000
history = []
x, y = [0], [N]

#rw = randomwalk()
H_min, H_max = N * .8, N * 1.2
plt.ion() ## Note this correction

def buy(n=1):
    global N, TRADES, holding, STONKS
    print('BUY  {} @{}'.format(round(STONKS*.1), round(N)))
    plt.axhline(y=N, color='b', linestyle='-')

    #holding = min([10, holding + 1])
    TRADES.append((STONKS*.1, N))
    STONKS *= .9
    holding += 1

    
def sell(n=1):
    global N, TRADES, holding, STONKS
    if not TRADES:
        return

    shares, price = TRADES.pop(0)
    print('SELL {} @{}  => {}'.format(round(shares), round(N), round(STONKS)))
    plt.axhline(y=N, color='b', linestyle=':')

    #holding = max([0, holding - 1])
    #price = min(TRADES)
    #TRADES.remove(price)
    STONKS += shares + round(shares * (N - price) / price)
    holding -= 1


def press(event):
    global N
    if event.key == 'i':
        buy()

    if event.key == 'o':
        sell()

    if event.key == 'up':
        N += 20

    if event.key == 'down':
        N -= 20

fig = plt.figure()
buy() # Start with some skin in the game
for year in range(20):
    fig = plt.figure()
    fig.canvas.mpl_connect('key_press_event', press)

    for run in history:
        plt.plot(x, run, '_', color="brown")

    colour = colors.DivergingNorm(vmin=N*.8, vcenter=N, vmax=N*1.2)
    plt.axis([0, 365, 0, H_max + 200])
    x, y = [0], [N]
    plt.show()

    for day in range(1, 365):
        #temp_y = np.random.random();
        fun = np.random.normal(0, 40) #16.133) # Scaled from VTSAX st.dev
        N += fun

        '''
        if holding:
            STONKS += fun * (STONKS * holding / 10 / N)
        '''
        #temp_x, temp_y = next(rw)

        if STONKS < 0: # Bankruptcy hurts.
            plt.pause(5)
            fig.suptitle("SORRY! Try again next year.", fontsize=14, fontweight='bold')
            break

        x.append(day);
        y.append(N);

        plt.scatter(day, N, color="green" if fun > 0 else "red", marker="o") #norm=colour, cmap=cm.RdYlGn)
        fig.suptitle("ASSETS: {}, YOUR STONKS: {:,}".format(holding, round(STONKS)), fontsize=14, fontweight='bold')
        plt.show()
        plt.pause(.001) #Note this correction

    H_min, H_max = min([H_min, min(y)]), max([H_max, max(y)])
    plt.close(fig)
    plt.close()
    history.append(y)

print('TOTAL STONKS = {:,}'.format(round(N)))
