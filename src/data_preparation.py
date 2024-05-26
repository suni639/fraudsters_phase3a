import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def load_and_preprocess_data(file_path):
    """
    Load data from a CSV file and preprocess it by scaling certain columns.
    
    Parameters:
    file_path (str): The path to the CSV file containing the data.
    
    Returns:
    pd.DataFrame: The preprocessed data.
    """
    try:
        df = pd.read_csv(file_path)
        logging.info("Data loaded successfully.")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error reading the file: {e}")
        raise

    # Standardizing the 'Amount' and 'Time' columns
    scaler = StandardScaler()
    df['scaled_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
    df['scaled_time'] = scaler.fit_transform(df['Time'].values.reshape(-1, 1))
    df.drop(['Amount', 'Time'], axis=1, inplace=True)
    
    # Reordering columns
    df.insert(0, 'scaled_amount', df.pop('scaled_amount'))
    df.insert(1, 'scaled_time', df.pop('scaled_time'))

    logging.info("Data preprocessing completed.")
    return df

def split_data(df, num_clients=5, test_size=0.2):
    """
    Split the data into subsets for each client, ensuring balanced classes, and further split into train and test sets.
    
    Parameters:
    df (pd.DataFrame): The preprocessed data.
    num_clients (int): The number of clients to split the data for.
    test_size (float): The proportion of the dataset to include in the global test split.
    
    Returns:
    tuple: A tuple containing the global test set and a list where each element is a tuple containing the train and test dataframes for a client.
    """
    # Create a global test set
    train_df, global_test_df = train_test_split(df, test_size=test_size, stratify=df['Class'], random_state=42)
    logging.info(f"Global test set prepared: {len(global_test_df)} samples.")

    client_data = []
    df_fraud = train_df[train_df['Class'] == 1]
    df_non_fraud = train_df[train_df['Class'] == 0]

    for i in range(num_clients):
        fraud_sample = df_fraud.sample(frac=1/num_clients, random_state=42 + i)
        non_fraud_sample = df_non_fraud.sample(frac=1/num_clients, random_state=42 + i)
        
        client_df = pd.concat([fraud_sample, non_fraud_sample]).sample(frac=1, random_state=42).reset_index(drop=True)
        
        train_client_df, test_client_df = train_test_split(client_df, test_size=test_size, stratify=client_df['Class'], random_state=42)
        
        client_data.append((train_client_df, test_client_df))

        logging.info(f"Client {i+1} data prepared: {len(fraud_sample)} fraud samples, {len(non_fraud_sample)} non-fraud samples. Train size: {len(train_client_df)}, Test size: {len(test_client_df)}")
    
    return global_test_df, client_data

if __name__ == "__main__":
    try:
        df = load_and_preprocess_data('creditcard.csv')
        global_test_df, client_data = split_data(df)
        
        # Save the preprocessed data
        df.to_csv('preprocessed_creditcard.csv', index=False)
        global_test_df.to_csv('global_test_set.csv', index=False)
        for i, (train_df, test_df) in enumerate(client_data):
            train_df.to_csv(f'client_{i+1}_train.csv', index=False)
            test_df.to_csv(f'client_{i+1}_test.csv', index=False)
        
        logging.info("Data split among clients and global test set prepared and saved successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
