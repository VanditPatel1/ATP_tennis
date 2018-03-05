import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def save_plot(name, figure):

    ll = figure.get_figure()
    ll.savefig(name)
