from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE

def train_local_models(client_data):
    local_models = []
    for data in client_data:
        X = data.drop('Class', axis=1)
        y = data['Class']
        sm = SMOTE(sampling_strategy='minority', random_state=42)
        X_resampled, y_resampled = sm.fit_resample(X, y)
        model = LogisticRegression(solver='liblinear')
        model.fit(X_resampled, y_resampled)
        local_models.append(model)
    return local_models

if __name__ == "__main__":
    from data_preparation import load_and_preprocess_data, split_data
    df = load_and_preprocess_data('creditcard.csv')
    client_data = split_data(df)
    local_models = train_local_models(client_data)
