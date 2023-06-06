import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

from cycler import cycler
from mpl_toolkits.axes_grid1 import make_axes_locatable

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
mpl.rcParams["grid.alpha"] = 0.2
mpl.rcParams["legend.loc"] = "upper right"


def plot_bar(
    bar_names: list[str],
    bar_vals: list[float],
    title: t.Optional[str] = None,
    val_axis_label: t.Optional[str] = None,
    cat_axis_label: t.Optional[str] = None,
    save_path: t.Optional[str] = None,
    show: bool = True,
    bar_label: bool = False,
    figsize: tuple = None,
    int_vals: bool = True,
) -> None:
    """Draw and optionally show and save a bar chart."""
    if figsize:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig, ax = plt.subplots()
    x = np.arange(1, len(bar_names) + 1)
    bar = ax.bar(x, height=bar_vals, tick_label=bar_names, log=False)
    plt.xticks(rotation=30, ha="right")
    ax.ticklabel_format(useOffset=False, style="plain", axis="y")
    if int_vals:
        y_tick_fmt = lambda x: f"{int(x):,}"
    else:
        y_tick_fmt = lambda x: f"{float(x):.3f}"
    ax.set_yticks(ax.get_yticks()[:-1], [y_tick_fmt(x) for x in ax.get_yticks()[:-1]])
    if title:
        ax.set_title(title)
    if val_axis_label:
        ax.set_ylabel(val_axis_label)
    if cat_axis_label:
        ax.set_xlabel(cat_axis_label)
    if bar_label:
        if int_vals:
            ax.bar_label(bar, fmt="{:,.0f}")
        else:
            ax.bar_label(bar, fmt="{:,.3f}")
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
        ax.pie(
            slice_vals,
            labels=None,
            autopct=make_autopct(slice_vals),
            textprops={"color": "black"},
        )
        ax.legend(labels=slice_names, labelcolor="black")
    else:
        ax.pie(slice_vals, labels=slice_names, autopct=make_autopct(slice_vals))
    if title:
        ax.set_title(title)
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
        ax.hist(vals, alpha=0.8, bins=bins)
    else:
        ax.hist(vals, alpha=0.8)
    if title:
        ax.set_title(title)
    if y_label:
        ax.set_ylabel(y_label)
    if x_label:
        ax.set_xlabel(x_label)
    if save_path:
        plt.savefig(save_path, transparent=True, bbox_inches="tight")
    if show:
        plt.show()
    return None


# Taken straight from matplotlib docs: https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
def heatmap(
    data: np.ndarray,
    row_labels: list[str],
    col_labels: list[str],
    ax: mpl.axes.Axes = None,
    cbar_kw: dict = None,
    cbarlabel: str = "",
    **kwargs,
):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar, make its size consistent with imshow plot
    # Taken from: https://stackoverflow.com/a/18195921
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.3)
    cbar = plt.colorbar(im, cax=cax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")


    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1] + 1) - 0.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0] + 1) - 0.5, minor=True)
    ax.grid(which="minor", color="w", linestyle="-", linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


# Taken straight from matplotlib docs: https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
def annotate_heatmap(
    im,
    data=None,
    valfmt="{x:.2f}",
    textcolors=("black", "white"),
    threshold=None,
    **textkw,
):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max()) / 2.0

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center", verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = mpl.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts


def heatmap_from_df_cols(
    df: pd.DataFrame,
    col1: str,
    col2: str,
    top_k1: int,
    top_k2: int,
    heat_val_name: str,
    normalize: bool = True,
    title: t.Optional[str] = None,
    y_label: t.Optional[str] = None,
    x_label: t.Optional[str] = None,
    save_path: t.Optional[str] = None,
    show: bool = True,
    figsize: tuple = None,
):
    vals1 = list(df[col1].value_counts().keys())
    vals2 = list(df[col2].value_counts().keys())

    arr = np.zeros((len(vals1), len(vals2)))
    for idx, row in df.iterrows():
        try:
            row_idx = vals1.index(row[col1])
            col_idx = vals2.index(row[col2])
            arr[row_idx, col_idx] += 1
        except ValueError:
            pass

    if normalize:
        # Avoid division by zero
        eps = .0001
        sum_cols = arr.sum(axis=0)
        sum_cols[sum_cols==0] = eps
        arr = arr / sum_cols

    arr = arr[:top_k1, :top_k2]
    vals1 = vals1[:top_k1]
    vals2 = vals2[:top_k2]

    if figsize:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig, ax = plt.subplots()

    im, cbar = heatmap(
        arr, vals1, vals2, ax=ax, cmap="Purples", cbarlabel=heat_val_name
    )
    # texts = annotate_heatmap(im, valfmt="{x:.1f} t")

    if title:
        ax.set_title(title, pad=40)
    if y_label:
        ax.set_ylabel(y_label, loc="center", labelpad=30)
    if x_label:
        ax.xaxis.set_label_position('top')
        ax.set_xlabel(x_label, loc="center", labelpad=0)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, transparent=True, bbox_inches="tight")
    if show:
        plt.show()
    return None
