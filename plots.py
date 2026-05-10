import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


results_df = pd.read_csv("data/feature_selection_results.csv")

datasets = results_df["Dataset"].unique()

selectors = results_df["Selector"].unique()

x = np.arange(len(datasets))
bar_width = 0.25

#acc bar plot

for i, selector in enumerate(selectors):

    selector_data = results_df[
        results_df["Selector"] == selector
    ]

    plt.bar(
        x + i * bar_width,
        selector_data["Accuracy"],
        width=bar_width,
        label=selector
    )

plt.xticks(
    x + bar_width,
    datasets
)

plt.ylabel("Accuracy")
plt.xlabel("Dataset")
plt.title("Feature Selection Accuracy Comparison")
plt.legend()
plt.show()

#runtime bar plot

for i, selector in enumerate(selectors):

    selector_data = results_df[
        results_df["Selector"] == selector
    ]

    plt.bar(
        x + i * bar_width,
        selector_data["Runtime_Seconds"],
        width=bar_width,
        label=selector
    )

plt.xticks(
    x + bar_width,
    datasets
)

plt.ylabel("Runtime (Seconds)")
plt.yscale("log")
plt.xlabel("Dataset")
plt.title("Feature Selection Runtime Comparison")
plt.legend()
plt.show()