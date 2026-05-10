import pandas as pd
import matplotlib.pyplot as plt

results_df = pd.read_csv("data/feature_selection_results.csv")

brca_df = results_df[results_df["Dataset"] == "BRCA"]

gene_sets = {}

for _, row in brca_df.iterrows():

    selector = row["Selector"]

    genes = set(row["Selected_Genes"].split(";"))

    gene_sets[selector] = genes


def jaccard_similarity(set1, set2):

    intersection = len(set1.intersection(set2))

    union = len(set1.union(set2))

    return intersection / union

selectors = list(gene_sets.keys())

similarity_matrix = pd.DataFrame(
    index=selectors,
    columns=selectors
)

for s1 in selectors:
    for s2 in selectors:

        similarity = jaccard_similarity(
            gene_sets[s1],
            gene_sets[s2]
        )

        similarity_matrix.loc[s1, s2] = similarity

similarity_matrix = similarity_matrix.astype(float)



plt.imshow(similarity_matrix, cmap="Blues")

plt.colorbar(label="Jaccard Similarity")

plt.xticks(
    range(len(selectors)),
    selectors,
    rotation=45
)

plt.yticks(
    range(len(selectors)),
    selectors
)

plt.title("Feature Selection Similarity Matrix - BRCA")

plt.show()