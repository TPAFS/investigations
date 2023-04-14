import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

from cycler import cycler

import typing as t

plt.style.use("ggplot")
mpl.rcParams["axes.prop_cycle"] = cycler(
    color=[
        "#8f5e77",
        "#62aebf",
        "#E24A33",
        "#467821",
        "#348ABD",
        "#7A68A6",
        "#A60628",
        "#CF4457",
        "#188487",
        "tab:orange",
    ]
)

COLOR = "#969696"
mpl.rcParams["text.color"] = COLOR
mpl.rcParams["axes.labelcolor"] = COLOR
mpl.rcParams["axes.titlepad"] = 20 
mpl.rcParams["xtick.color"] = COLOR
mpl.rcParams["ytick.color"] = COLOR
mpl.rcParams["grid.alpha"] = .2
mpl.rcParams["legend.loc"] = "lower right"


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
        ax.set_title(title, pad=20)
    if val_axis_label:
        ax.set_ylabel(val_axis_label)
    if cat_axis_label:
        ax.set_xlabel(cat_axis_label)
    if save_path:
        plt.savefig(save_path, transparent=True, bbox_inches="tight")
    if show:
        plt.show()
    return None


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return "{p:.2f}%\n({v:d})".format(p=pct, v=val)

    return my_autopct


def plot_pie(
    slice_names: list[str],
    slice_vals: list[float],
    title: t.Optional[str] = None,
    save_path: t.Optional[str] = None,
    show: bool = True,
    legend: bool = True,
) -> None:
    """Drawn and optionally show and save a pie chart."""
    fig, ax = plt.subplots(figsize=(10, 10))
    if legend:
        ax.pie(slice_vals, labels=None, autopct=make_autopct(slice_vals), textprops={'color':"black"})
        ax.legend(labels=slice_names, labelcolor="black")
    else:
        ax.pie(slice_vals, labels=slice_names, autopct=make_autopct(slice_vals))
    if title:
        ax.set_title(title, pad=20)
    if save_path:
        plt.savefig(save_path, transparent=True, bbox_inches="tight")
    if show:
        plt.show()
    return None


def plot_hist(
    vals: list[float],
    bins: t.Optional[list[float]] = None,
    title: t.Optional[str] = None,
    y_label: t.Optional[str] = None,
    x_label: t.Optional[str] = None,
    save_path: t.Optional[str] = None,
    show: bool = True,
) -> None:
    """Draw and optionally show and save a histogram."""
    fig, ax = plt.subplots()
    if bins is not None:
        ax.hist(vals, alpha=0.8, bins=np.linspace(0, 0.5, 11))
    else:
        ax.hist(vals, alpha=0.8)
    if title:
        ax.set_title(title, pad=20)
    if y_label:
        ax.set_ylabel(y_label)
    if x_label:
        ax.set_xlabel(x_label)
    if save_path:
        plt.savefig(save_path, transparent=True, bbox_inches="tight")
    if show:
        plt.show()
    return None
