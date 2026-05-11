import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


results_df = pd.read_csv("data/feature_selection_results.csv")

datasets = results_df["Dataset"].unique()

selectors = results_df["Selector"].unique()

x = np.arange(len(selectors))
bar_width = 0.25

#acc bar plot

for i, dataset in enumerate(datasets):

    dataset_data = results_df[
        results_df["Dataset"] == dataset
    ]

    bars = plt.bar(
        x + i * bar_width,
        dataset_data["Accuracy"],
        width=bar_width,
        label=dataset
    )

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{height:.3f}",
            ha='center',
            va='bottom',
            fontsize=8
        )

plt.xticks(
    x + bar_width,
    selectors
)

plt.ylabel("Accuracy")
plt.xlabel("Method")
plt.title("Feature Selection Accuracy Comparison")
plt.legend()
plt.show()

#runtime bar plot

for i, dataset in enumerate(datasets):

    dataset_data = results_df[
        results_df["Dataset"] == dataset
    ]

    bars = plt.bar(
        x + i * bar_width,
        dataset_data["Runtime_Seconds"],
        width=bar_width,
        label=dataset
    )

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{height:.1f}",
            ha='center',
            va='bottom',
            fontsize=8
        )

plt.xticks(
    x + bar_width,
    selectors
)

plt.ylabel("Runtime (Seconds)")
plt.yscale("log")
plt.xlabel("Method")
plt.title("Feature Selection Runtime Comparison")
plt.legend()
plt.show()

#auroc bar plot

for i, dataset in enumerate(datasets):

    dataset_data = results_df[
        results_df["Dataset"] == dataset
    ]

    bars = plt.bar(
        x + i * bar_width,
        dataset_data["AUROC"],
        width=bar_width,
        label=dataset
    )

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{height:.3f}",
            ha='center',
            va='bottom',
            fontsize=8
        )

plt.xticks(
    x + bar_width,
    selectors
)

plt.ylabel("AUROC")
plt.xlabel("Method")
plt.title("Feature Selection AUROC Comparison")
plt.legend()
plt.show()



#f1 bar plot

for i, dataset in enumerate(datasets):

    dataset_data = results_df[
        results_df["Dataset"] == dataset
    ]

    bars = plt.bar(
        x + i * bar_width,
        dataset_data["F1_Score"],
        width=bar_width,
        label=dataset
    )

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{height:.3f}",
            ha='center',
            va='bottom',
            fontsize=8
        )

plt.xticks(
    x + bar_width,
    selectors
)

plt.ylabel("F1 Score")
plt.xlabel("Method")
plt.title("Feature Selection F1 Score Comparison")
plt.legend()
plt.show()