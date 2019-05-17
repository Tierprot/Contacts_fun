
import numpy as np
import matplotlib.pyplot as plt

def build_plot(keks):
    x = []
    y = []
    c = []
    for i in keks:
        x.append(i[0])
        y.append(i[1])
        c.append(i[2])
    plt.hexbin(x, y, c)
    plt.show()

