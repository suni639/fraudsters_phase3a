from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, average_precision_score

# Load test set
X_test = df.drop('Class', axis=1)
y_test = df['Class']

# Assuming aggregated_params are used to set the global model
global_model = LogisticRegression()
global_model.coef_ = aggregated_params

# Evaluate global model
y_pred = global_model.predict(X_test)
y_prob = global_model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)
auprc = average_precision_score(y_test, y_prob)

results = {
    'Accuracy': accuracy,
    'Precision': precision,
    'Recall': recall,
    'F1 Score': f1,
    'ROC AUC Score': roc_auc,
    'AUPRC': auprc
}

if __name__ == "__main__":
    for metric, value in results.items():
        print(f'{metric}: {value}')
