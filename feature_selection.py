from sklearn.feature_selection import SelectKBest, RFE
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import f_classif, SelectFromModel
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split


#y = df[“Subtype_Selected”]
#X = df[All columns for genes]



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#missing scaling of data, need to understand how to do it.


methods = {
    "Filter_SelectKBest": SelectKBest(score_func=f_classif, k=5),
    "Wrapper_RFE": RFE(estimator=LogisticRegression(), n_features_to_select=5),
    "Embedded_XGBoost": SelectFromModel(XGBClassifier(), threshold="median")
}

results = {}

for name, selector in methods.items():
    X_train_new = selector.fit_transform(X_train, y_train)
    X_test_new = selector.transform(X_test)
    
    #eval of performance:
    model = LogisticRegression().fit(X_train_new, y_train)
    score = model.score(X_test_new, y_test)

    results[name] = {"Accuracy": score, "Features": X_train_new.shape[1]}