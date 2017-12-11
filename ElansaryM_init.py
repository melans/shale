import ElansaryM_inc
db="https://raw.githubusercontent.com/melans/shale/master/shaledata.csv"

dataset = ElansaryM_inc.pandas.read_csv(db, sep=',', header=1)

classifiers_names = [
    "Nearest Neighbors",
    "Linear SVM",
    "RBF SVM",
    "Poly SVM",
    "Sigmoid SVM",
    "Gaussian Process",
    "Decision Tree",
    "Regrission Tree",
    "Random Forest",
    "Neural Net",
    "AdaBoost",
    "Naive Bayes",
]

classifiers_ = [
    ElansaryM_inc.KNeighborsClassifier(),
    ElansaryM_inc.SVC(kernel="linear"),
    ElansaryM_inc.SVC(kernel="rbf"),
    ElansaryM_inc.SVC(kernel="poly"),
    ElansaryM_inc.SVC(kernel="sigmoid"),
    ElansaryM_inc.GaussianProcessClassifier(),
    ElansaryM_inc.DecisionTreeClassifier(),
    ElansaryM_inc.DecisionTreeRegressor(),
    ElansaryM_inc.RandomForestClassifier(),
    ElansaryM_inc.MLPClassifier(),
    ElansaryM_inc.AdaBoostClassifier(),
    ElansaryM_inc.GaussianNB(),
]

reg_metrics_names_ = [
    "Explained variance regression score function",
    "Mean absolute error regression loss",
    "Mean squared error regression loss",
    "Mean squared logarithmic error regression loss",
    "Median absolute error regression loss",
    "R^2 (coefficient of determination) regression score function.",
]

reg_metrics_ = [
    ElansaryM_inc.explained_variance_score,
    ElansaryM_inc.mean_absolute_error,
    ElansaryM_inc.mean_squared_error,
    ElansaryM_inc.mean_squared_log_error,
    ElansaryM_inc.median_absolute_error,
    ElansaryM_inc.r2_score,
]

cls_metrics_names_ = [
    "Accuracy Score",
    "Matthews correlation coefficient (MCC)",
    "Jaccard similarity coefficient",
    "Cohen's kappa",

    # "Logistic Loss or Cross-Entropy Loss",
    # "Precision Score",
    # "F1 Score",
    # "F-beta Score",
    # "Recall Score",
]

cls_metrics_ = [
    ElansaryM_inc.accuracy_score,
    ElansaryM_inc.matthews_corrcoef,
    ElansaryM_inc.jaccard_similarity_score,
    ElansaryM_inc.cohen_kappa_score,

    # ElansaryM_inc.log_loss(ytst,predictions,eps=1e-15),
    # ElansaryM_inc.precision_score(ytst,predictions,average='weighted'),
    # ElansaryM_inc.f1_score(ytst,predictions,average='weighted'),
    # ElansaryM_inc.fbeta_score(ytst,predictions,average='weighted'),
    # ElansaryM_inc.recall_score(ytst,predictions,average='weighted'),
]

outputs_ = [
    29,
    30,
    # 31,
    # 32,
    # 33,
    # 34,
    # 35,
    # 36,
]

outputs_names_ = [
    "30 Day Cum Gas (MCF)",
    "30 Day Cum Condensate (bbls)",
    # "90 Day Cum Gas (MCF)",
    # "90 Day Cum Condensate (bbls)",
    # "120 Day Cum Gas (MCF)",
    # "120 Day Cum Condensate (bbls)",
    # "180 Day Cum Gas (MCF)",
    # "180 Day Cum Condensate (bbls)",
]
