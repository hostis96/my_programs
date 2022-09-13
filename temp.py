# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':25})
x = np.arange(0, 10, 1)
y1 = 0.05 * x**2
y2 = 0.1 * x

my_ticks = x+4

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x, y1, 'g-')
ax1.set_xticks(x)
ax1.set_xticklabels(my_ticks, rotation=90)
ax1.set_ylim(0, max(y1))
ax2.plot(x, y2, 'b-')
ax2.set_ylim(0, max(y1))

ax1.set_xlabel('X data')
ax1.set_ylabel(r'$\Gamma_{\mu\nu}$ $[M_\odot]$')
ax2.set_ylabel('Y2 data', color='b')

plt.tight_layout()

plt.savefig('figura01.png', dpi=100)

plt.show()

# x = np.genfromtxt('path', usecols=0, unpack=True, skip_header=1)

# my_ticks = np.genfromtxt('path', usecols=1, unpack=True, skip_header=1)

# y1 = np.genfromtxt('path', usecols=3, unpack=True, skip_header=1)
# y2 = np.genfromtxt('path', usecols=4, unpack=True, skip_header=1)
