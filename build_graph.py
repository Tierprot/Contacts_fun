
import numpy as np
import matplotlib.pyplot as plt

def build_plot(keks, name, min_dist=3, max_dist=13, resolution=100):
    x = []
    y = []
    c = []
    for i in keks:
        x.append(i[0])
        y.append(i[1])
        if i[2]>=max_dist:
           c.append(max_dist)
        elif i[2]<=min_dist:
           c.append(min_dist)
        else:
           c.append(i[2])
    plt.hexbin(x, y, c, gridsize=resolution, cmap=plt.cm.jet_r)
    plt.xlabel(name)
    plt.ylabel(name)
    plt.title("Contacts map")
    plt.colorbar().set_label('distance, A')
    plt.show()

