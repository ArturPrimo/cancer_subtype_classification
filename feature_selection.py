from sklearn.feature_selection import SelectKBest, RFE
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import f_classif, SelectFromModel
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, ConfusionMatrixDisplay, roc_auc_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

#data manipulation

#y = df[“Subtype_Selected”]
#X = df[All columns for genes]

brca_csv = pd.read_csv("cleaned_data/merged_brca.csv")
coad_csv = pd.read_csv("cleaned_data/merged_coad.csv")
prad_csv = pd.read_csv("cleaned_data/merged_prad.csv")


datasets = {
    "BRCA": brca_csv,
    "COAD": coad_csv,
    "PRAD": prad_csv
}

all_results = []

#used for turning categories into numeric vals:
le = LabelEncoder()

#all methods will select k-best features (50)
selectors = {
    "Filter_SelectKBest": SelectKBest(score_func=f_classif, k=50),
    "Wrapper_RFE": RFE(estimator=LogisticRegression(max_iter=5000), n_features_to_select=50, step=1000),
    "Embedded_XGBoost": SelectFromModel(XGBClassifier(eval_metric="mlogloss"), max_features=50, threshold=-np.inf)
}


for dataset_name, dataset in datasets.items():

    print(f"Working with dataset: {dataset}")

    y = dataset["Subtype_Selected"]
    y = le.fit_transform(y)
    all_class_ids = np.arange(len(le.classes_))

    X = dataset.drop(columns=["pan.samplesID", "Subtype_Selected"])
    X = X.astype(float)

    #stratify is used to avoid missing subtype classes.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y) 

    for name, selector in selectors.items():

        print(f"\nRunning: {name}")

        start_time = time.time()

        X_train_new = selector.fit_transform(X_train, y_train)
        X_test_new = selector.transform(X_test)
        
        print("Feature selection complete")
        print("Selected features:", X_train_new.shape[1])

        
        model = LogisticRegression(max_iter=5000).fit(X_train_new, y_train)

        
        pred = model.predict(X_test_new)
        proba = model.predict_proba(X_test_new)
        selected_genes = X.columns[selector.get_support()].tolist()

        #eval of performance:
        accuracy = accuracy_score(y_test, pred)
        f1 = f1_score(y_test, pred, average="weighted")
        auroc = roc_auc_score(y_test, proba, multi_class="ovr", average="weighted", labels=all_class_ids)
        
        

        runtime = time.time() - start_time

        print(name)
        
        print(f"Accuracy: {accuracy}")
        print(f"F1 score: {f1}")
        print(f"Runtime: {runtime} sec")
        print(f"AUROC: {auroc}")
        print(f"Selected genes for {name}:")
        print(selected_genes)

        cm = confusion_matrix(y_test, pred, labels=all_class_ids)

        
        
        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm,
            display_labels=le.classes_
        )



        disp.plot(cmap="Blues")

        plt.title(f"Confusion Matrix - {name}")
        plt.xticks(rotation=45)
        plt.show()

        all_results.append({
            "Dataset": dataset_name,
            "Selector": name,
            "Accuracy": accuracy,
            "F1_Score": f1,
            "AUROC": auroc,
            "Selected_Features": X_train_new.shape[1],
            "Runtime_Seconds": runtime,
            "Selected_Genes": ";".join(selected_genes),
        })
        

results_df = pd.DataFrame(all_results)

results_df.to_csv("data/feature_selection_results.csv", index=False)


