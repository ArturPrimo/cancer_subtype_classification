import pandas as pd

# BRCA

# --- Load the expression matrix (genes as rows, samples as columns) ---
expr_brca = pd.read_csv('data/tcga_brca.csv', index_col=0)
# Now: rows = genes (ENSG...), columns = sample IDs (TCGA-...)

# Transpose so samples become rows
expr_T_brca = expr_brca.T.reset_index()
expr_T_brca = expr_T_brca.rename(columns={'index': 'pan.samplesID'})
# Now: rows = samples, columns = pan.samplesID + gene names

# --- Load the metadata (samples as rows) ---
meta_brca = pd.read_csv('data/cancer_subtypes.csv')
meta_brca = meta_brca[['pan.samplesID', 'Subtype_Selected']]
# Already has pan.samplesID as a column

# --- Merge on sample ID ---
merged_brca = pd.merge(meta_brca, expr_T_brca, on='pan.samplesID', how='inner')

merged_brca.to_csv('cleaned_data/merged_brca.csv', index=False)
print(f"Done! Shape: {merged_brca.shape}")

# COAD

# --- Load and transpose expression matrix ---
expr_coad = pd.read_csv('data/tcga_coad.csv', index_col=0)
expr_T_coad = expr_coad.T.reset_index().rename(columns={'index': 'pan.samplesID'})

# --- Load metadata ---
meta_coad = pd.read_csv('data/cancer_subtypes.csv')
meta_coad = meta_coad[['pan.samplesID', 'Subtype_Selected']]

# --- Add short ID and merge ---
meta_coad['short_id'] = meta_coad['pan.samplesID'].str[:12]
expr_T_coad['short_id'] = expr_T_coad['pan.samplesID'].str[:12]
merged_coad = pd.merge(meta_coad, expr_T_coad, on='short_id', how='inner')

# --- Clean up: drop redundant columns, reorder ---
merged_coad = merged_coad.drop(columns=['pan.samplesID_x', 'short_id'])
merged_coad = merged_coad.rename(columns={'pan.samplesID_y': 'pan.samplesID'})

# --- Save ---
merged_coad.to_csv('cleaned_data/merged_coad.csv', index=False)
print(f"Done! Shape: {merged_coad.shape}")

# PRAD

# --- Load and transpose expression matrix ---
expr_prad = pd.read_csv('data/tcga_prad.csv', index_col=0)
expr_T_prad = expr_prad.T.reset_index().rename(columns={'index': 'pan.samplesID'})

# --- Load metadata ---
meta_prad = pd.read_csv('data/cancer_subtypes.csv')
meta_prad = meta_prad[['pan.samplesID', 'Subtype_Selected']]

# --- Add short ID and merge ---
meta_prad['short_id'] = meta_prad['pan.samplesID'].str[:12]
expr_T_prad['short_id'] = expr_T_prad['pan.samplesID'].str[:12]
merged_prad = pd.merge(meta_prad, expr_T_prad, on='short_id', how='inner')

# --- Clean up: drop redundant columns, reorder ---
merged_prad = merged_prad.drop(columns=['pan.samplesID_x', 'short_id'])
merged_prad = merged_prad.rename(columns={'pan.samplesID_y': 'pan.samplesID'})

# --- Save ---
merged_prad.to_csv('cleaned_data/merged_prad.csv', index=False)
print(f"Done! Shape: {merged_prad.shape}")