from sklearn.feature_selection import SelectKBest, RFE
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import f_classif, SelectFromModel
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data manipulation

#y = df[“Subtype_Selected”]
#X = df[All columns for genes]

brca_csv = pd.read_csv("cleaned_data/merged_brca.csv")
coad_csv = pd.read_csv("cleaned_data/merged_coad.csv")
prad_csv = pd.read_csv("cleaned_data/merged_prad.csv")

le = LabelEncoder()

y = brca_csv["Subtype_Selected"]
y = le.fit_transform(y)

X = brca_csv.drop(columns=["pan.samplesID", "Subtype_Selected"])
X = X.astype(float)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#missing scaling of data, need to understand how to do it.

#all methods will select k-best features (50)
selectors = {
    "Filter_SelectKBest": SelectKBest(score_func=f_classif, k=50),
    "Wrapper_RFE": RFE(estimator=LogisticRegression(max_iter=5000), n_features_to_select=50, step=1000),
    "Embedded_XGBoost": SelectFromModel(XGBClassifier(eval_metric="mlogloss"), max_features=50, threshold=-np.inf)
}



for name, selector in selectors.items():

    print(f"\nRunning: {name}")

    X_train_new = selector.fit_transform(X_train, y_train)
    X_test_new = selector.transform(X_test)
    
    print("Feature selection complete")
    print("Selected features:", X_train_new.shape[1])

    
    model = LogisticRegression().fit(X_train_new, y_train)

    
    pred = model.predict(X_test_new)

    #eval of performance:
    
    accuracy = accuracy_score(y_test, pred)
    f1 = f1_score(y_test, pred, average="weighted")
    

    print(name)
    
    print(f"Accuracy: {accuracy}")
    print(f"F1 score: {f1}")

    cm = confusion_matrix(y_test, pred)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)

    disp.plot(cmap="Blues")

    plt.title(f"Confusion Matrix - {name}")
    plt.show()
    

