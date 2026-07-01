"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    data_path = Path(__file__).parent.parent / "files" / "input" / "news.csv"
    output_path = Path(__file__).parent.parent / "files" / "plots" / "news.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(data_path, sep=",", index_col=0)
    colors = {
        "Television": "#6f7471",
        "Newspaper": "#8f9690",
        "Internet": "#2b7ca7",
        "Radio": "#d5d9d6",
    }

    fig, ax = plt.subplots(figsize=(8, 6))

    for col in df.columns:
        color = colors[col]
        zorder = 2 if col == "Internet" else 1
        linewidth = 3.5 if col == "Internet" else 2.0

        ax.plot(
            df.index,
            df[col],
            color=color,
            linewidth=linewidth,
            zorder=zorder,
        )
        ax.scatter(
            [df.index[0], df.index[-1]],
            [df[col].iloc[0], df[col].iloc[-1]],
            color=color,
            s=55,
            zorder=zorder + 1,
        )

        ax.text(
            df.index[0] - 0.2,
            df[col].iloc[0],
            f"{col} {df[col].iloc[0]}%",
            color=color,
            ha="right",
            va="center",
            fontsize=11,
            fontweight="bold",
        )
        ax.text(
            df.index[-1] + 0.2,
            df[col].iloc[-1],
            f"{df[col].iloc[-1]}%",
            color=color,
            ha="left",
            va="center",
            fontsize=11,
            fontweight="bold",
        )

    ax.set_title("How people get their news", fontsize=20, pad=16)
    ax.set_xlim(df.index[0] - 0.45, df.index[-1] + 0.45)
    ax.set_ylim(10, 86)
    ax.set_xticks([2002, 2004, 2006, 2008, 2010])
    ax.set_yticks([])
    ax.tick_params(axis="x", labelsize=11, width=1, length=5, colors="#555555")
    ax.tick_params(axis="y", length=0)

    for spine in ["left", "right", "top"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#555555")
    ax.spines["bottom"].set_linewidth(1.2)

    for label in ax.get_xticklabels():
        label.set_fontweight("bold")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    return df

if __name__ == "__main__":
    df = pregunta_01()
    print(df.head())
