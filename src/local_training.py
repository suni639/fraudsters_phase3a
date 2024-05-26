import logging
import pandas as pd
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE # type: ignore
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, average_precision_score
from sklearn.model_selection import cross_val_score, StratifiedKFold
import joblib

# Set up logging
logging.basicConfig(level=logging.INFO)

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model using various metrics.
    
    Parameters:
    model: The trained model to evaluate.
    X_test (pd.DataFrame): The test features.
    y_test (pd.Series): The test labels.
    
    Returns:
    dict: A dictionary containing evaluation metrics.
    """
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    
    evaluation_metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1_score': f1_score(y_test, y_pred),
        'roc_auc': roc_auc_score(y_test, y_proba),
        'average_precision': average_precision_score(y_test, y_proba)
    }
    
    return evaluation_metrics

def train_local_models(client_data):
    """
    Train local models on each client's data and evaluate them.
    
    Parameters:
    client_data (list of tuples): A list where each element is a tuple containing the train and test dataframes for a client.
    
    Returns:
    list: A list of tuples containing the trained models, their parameters, and their evaluation metrics.
    """
    local_models = []
    for i, (train_data, test_data) in enumerate(client_data):
        X_train = train_data.drop('Class', axis=1)
        y_train = train_data['Class']
        X_test = test_data.drop('Class', axis=1)
        y_test = test_data['Class']
        
        # Oversampling the minority class using SMOTE
        sm = SMOTE(sampling_strategy='minority', random_state=42)
        X_resampled, y_resampled = sm.fit_resample(X_train, y_train)
        
        # Cross-validation setup
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        
        # Training the logistic regression model
        model = LogisticRegression(solver='liblinear')
        
        # Perform cross-validation
        cv_scores = cross_val_score(model, X_resampled, y_resampled, cv=skf, scoring='roc_auc')
        logging.info(f"Client {i+1} Cross-validation ROC AUC scores: {cv_scores}")
        logging.info(f"Client {i+1} Mean CV ROC AUC: {cv_scores.mean()}")
        
        # Fit the model on the entire training data
        model.fit(X_resampled, y_resampled)
        
        # Evaluate the model
        evaluation_metrics = evaluate_model(model, X_test, y_test)
        logging.info(f"Client {i+1} Model Evaluation:\n{evaluation_metrics}")
        
        # Save model parameters
        model_params = {
            'coef_': model.coef_.tolist(),  # Ensure coefficients are saved
            'intercept_': model.intercept_.tolist(),  # Ensure intercepts are saved
            'C': model.C,
            'class_weight': model.class_weight,
            'dual': model.dual,
            'fit_intercept': model.fit_intercept,
            'intercept_scaling': model.intercept_scaling,
            'l1_ratio': model.l1_ratio,
            'max_iter': model.max_iter,
            'multi_class': model.multi_class,
            'n_jobs': model.n_jobs,
            'penalty': model.penalty,
            'random_state': model.random_state,
            'solver': model.solver,
            'tol': model.tol,
            'verbose': model.verbose,
            'warm_start': model.warm_start
        }
        
        local_models.append((model, model_params, evaluation_metrics))
        logging.info(f"Model {i+1} trained on client data.")
    
    return local_models

if __name__ == "__main__":
    try:
        # Load the preprocessed and split data
        client_data = []
        for i in range(5):  # Adjust the range based on the number of clients
            train_df = pd.read_csv(f'client_{i+1}_train.csv')
            test_df = pd.read_csv(f'client_{i+1}_test.csv')
            client_data.append((train_df, test_df))
        
        # Train local models
        local_models = train_local_models(client_data)
        logging.info("Local models trained and evaluated successfully.")
        
        # Save the trained models and their parameters
        for idx, (model, model_params, _) in enumerate(local_models):
            joblib_file = f"client_{idx+1}_model.pkl"
            joblib.dump(model_params, joblib_file)
            logging.info(f"Model parameters saved to {joblib_file}")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
