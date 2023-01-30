import matplotlib.pyplot as plt
import numpy as np

def plot_bar(bar_names: list[str], bar_vals: list[float],
             title = None, val_axis_label=None, cat_axis_label= None,
             save_path: str=None, show=True):
    """Draw and optionally show and save a bar chart via matplotlib.
    """
    fig, ax = plt.subplots()
    x = np.arange(1, len(bar_names) + 1)
    ax.bar(x, height=bar_vals, tick_label=bar_names, log=False)
    plt.xticks(rotation=30, ha="right")
    if title:
        ax.set_title(title)
    if val_axis_label:
        ax.set_ylabel(val_axis_label)
    if cat_axis_label:
        ax.set_xlabel(cat_axis_label)
    if save_path:
        plt.savefig(save_path)
    if show:
        plt.show()
    return None