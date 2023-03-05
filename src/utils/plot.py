import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

from cycler import cycler

import typing as t

plt.style.use('ggplot')
mpl.rcParams['axes.prop_cycle'] = cycler(color=['#8f5e77', '#62aebf', '#E24A33', '#467821', '#348ABD', '#7A68A6', '#A60628', '#CF4457', '#188487', 'tab:orange'])

def plot_bar(
    bar_names: list[str],
    bar_vals: list[float],
    title: t.Optional[str] = None,
    val_axis_label: t.Optional[str] = None,
    cat_axis_label: t.Optional[str] = None,
    save_path: t.Optional[str] = None,
    show: bool = True,
) -> None:
    """Draw and optionally show and save a bar chart."""
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


def plot_pie(
    slice_names: list[str],
    slice_vals: list[float],
    title: t.Optional[str] = None,
    save_path: t.Optional[str] = None,
    show: bool = True,
) -> None:
    """Drawn and optionally show and save a pie chart."""
    fig, ax = plt.subplots()
    ax.pie(slice_vals, labels=slice_names)
    if title:
        ax.set_title(title)
    if save_path:
        plt.savefig(save_path)
    if show:
        plt.show()
    return None  