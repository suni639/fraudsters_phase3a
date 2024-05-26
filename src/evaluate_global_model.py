import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, average_precision_score

# Load the test set
df = pd.read_csv('global_test_set.csv') 
X_test = df.drop('Class', axis=1)
y_test = df['Class']

# Remove feature names from X_test
X_test = X_test.to_numpy()

# Load aggregated model parameters
aggregated_params = joblib.load('models/aggregated_model.pkl')

# Initialize and set the global model with aggregated parameters
global_model = LogisticRegression(solver='liblinear')

# Set model coefficients and intercepts if available
if 'coef_' in aggregated_params and 'intercept_' in aggregated_params:
    global_model.coef_ = np.array(aggregated_params['coef_'])
    global_model.intercept_ = np.array(aggregated_params['intercept_'])
    # Manually set the classes_
    global_model.classes_ = np.array([0, 1])  # Binary classification: 0 for non-fraudulent, 1 for fraudulent
else:
    raise ValueError("Aggregated parameters do not contain 'coef_' and 'intercept_' keys")

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
