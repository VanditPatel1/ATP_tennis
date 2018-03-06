import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def save_plot(name, figure):

    ll = figure.get_figure()
    ll.savefig(name)

def x_y_plot(df, x, y, name):
    plot = df.plot(x=x, y=y)
    save_plot(name, plot)
