import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    scaler = StandardScaler()
    df['scaled_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
    df['scaled_time'] = scaler.fit_transform(df['Time'].values.reshape(-1, 1))
    df.drop(['Amount', 'Time'], axis=1, inplace=True)
    df.insert(0, 'scaled_amount', df.pop('scaled_amount'))
    df.insert(1, 'scaled_time', df.pop('scaled_time'))
    return df

def split_data(df, num_clients=5):
    client_data = []
    df_fraud = df[df['Class'] == 1]
    df_non_fraud = df[df['Class'] == 0]
    for _ in range(num_clients):
        fraud_sample = df_fraud.sample(frac=1/num_clients, random_state=42)
        non_fraud_sample = df_non_fraud.sample(frac=1/num_clients, random_state=42)
        client_data.append(pd.concat([fraud_sample, non_fraud_sample]))
    return client_data

if __name__ == "__main__":
    df = load_and_preprocess_data('creditcard.csv')
    client_data = split_data(df)
