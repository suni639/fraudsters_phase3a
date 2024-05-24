# FraudBusters: A Federated Learning Odyssey with Blockchain and Zero Knowledge Proofs

## Project Overview
This project explores advanced techniques to enhance credit card fraud detection. By leveraging the Credit Card Fraud Detection dataset, the aim is to compare the performance, complexity, and computational intensity of centralized machine learning models versus decentralized federated learning (using logistic regression). The federated learning phase of the project is then extended into two additional phases that investigate the benefits of integrating blockchain and zero knowledge proofs.

## Objectives
- To implement and evaluate a centralized logistic regression baseline for fraud detection.
- To distribute logistic regression training across multiple clients using federated learning.
- To secure model updates in federated learning with blockchain technology.
- To enhance privacy in federated learning with zero knowledge proofs.
- To analyze and compare the accuracy, complexity, and computational intensity of each approach.

## Phases
### Phase 1: Centralized Model using Logistic Regression
**Overview:** Understand the underlying data, and implement a centralized baseline logistic regression model to detect fraudulent transactions.
<br>

**High-level actions:**
- Load and preprocess the dataset.
- Carry out exploratory data analysis.
- Train a logistic regression model.
- Evaluate and document the model's performance.

### Phase 2: Federated Learning using Logistic Regression
**Overview:** Implement federated learning to distribute model training across multiple clients. This simulates multiple clients (i.e. other financial institutions in this case) collaboratively training a machine learning model without sharing their sensitive data. This approach enhances data privacy while leveraging the collective knowledge from multiple sources. 
<br>

**High-level actions:**
- Split the dataset into multiple subsets for different clients.
- Implement federated learning using the Federated Averaging (FedAvg) algorithm.
- Aggregate model updates from clients.
- Evaluate the global model's performance.

### Phase 3A: Federated Logistic Regression with Blockchain
**Overview:**  Federated learning allows multiple parties to collaboratively train a machine learning model without sharing their data. Blockchain can enhance federated learning by providing a decentralized and immutable ledger for tracking contributions, ensuring data integrity, and facilitating secure model aggregation.
<br>

**High-level actions:**
- Set up a local blockchain using Ganache.
- Log model updates from each client on the blockchain.
- Aggregate updates securely.
- Evaluate the global model's performance.

### Phase 3B: Federated Logistic Regression using Zero Knowledge Proofs
**Overview:** Use zero knowledge proofs to enhance privacy in federated learning. In this phase, a federated machine learning model developed similar to that in Phase 2. Integrating zero-knowledge proofs with machine learning is also known as ZKML. 
<br>

ZKML allows for the secure and private verification of ML model computations. Essentially, ZKML enables one party to prove that a computation was performed correctly on private data without revealing the data itself or the details of the computation.
<br>

**High-level actions:**
- Implement ZKPs using PyZPK or similar libraries.
- Verify model updates without revealing data.
- Aggregate verified updates.
- Evaluate the global model's performance.

## Dataset Description
**Dataset:** Credit Card Fraud Detection
- **Source:** [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **Description:** 
    - The dataset contains transactions made by credit cards in September 2013 by European cardholders.
    - This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.
    - It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, the original features and more background information about the data are not provided. 
    - Features `V1, V2, … V28` are the principal components obtained with PCA, the only features which have not been transformed with PCA are `Time` and `Amount`.
- **Features:** 
  - `Time` Number of seconds elapsed between this transaction and the first transaction in the dataset.
  - `V1-V28`: Principal components obtained with PCA.
  - `Amount`: Transaction amount.
  - `Class`: 1 for fraudulent transactions, 0 otherwise.
- **Descriptive Statistics:** 
  - Total transactions: 284,807
  - Fraudulent transactions: 492
  - Non-fraudulent transactions: 284,315

## Overview of Technology Concepts
### Logistic Regression
Logistic regression is a statistical method for binary classification. It is chosen for its simplicity and efficiency, making it suitable for implementation on a laptop with limited computational power.

### Federated Learning
 Federated learning enables multiple clients to train a model collaboratively without sharing raw data. This enhances data privacy and security.

### Blockchain
 Blockchain technology provides a secure, decentralized ledger for logging model updates. Integrating blockchain with federated learning ensures the integrity and immutability of model updates.

### Zero Knowledge Proofs (ZKPs)
 ZKPs allow one party to prove to another that a statement is true without revealing any information beyond the validity of the statement. In federated learning, ZKPs enhance privacy by verifying model updates without exposing data.

### Zero Knowledge Machine Learning (ZKML)
ZKML combines zero-knowledge proofs (ZKPs) with machine learning (ML) to allow for the secure and private verification of ML model computations. Essentially, ZKML enables one party to prove that a computation was performed correctly on private data without revealing the data itself or the details of the computation.

# Overview of Phase 3A (Federated Learning with Blockchain)

## Focus of This Phase
The objective of this phase is to implement a federated learning framework where model updates from clients are submitted to a blockchain. The blockchain ensures the integrity and transparency of the updates before they are aggregated to form a global model.

## Benefits of Using Blockchain with Federated Learning
1. **Data Integrity**: Blockchain ensures that the data (model updates) cannot be tampered with once recorded.
2. **Transparency**: All updates are logged on the blockchain, providing a transparent record of contributions.
3. **Security**: Blockchain secures the transmission and storage of updates.
4. **Decentralized Trust**: Trust is established without relying on a central authority.
5. **Immutability**: Once recorded, the updates cannot be altered, ensuring the reliability of the process.

## Explanation of New Technologies
### Truffle
A development framework for Ethereum that makes it easier to manage and deploy smart contracts.

### Ganache
A personal blockchain for Ethereum development that allows you to deploy contracts, develop applications, and run tests.

## Placeholders for Relevant Diagrams/Pics
- Diagram of the federated learning process with blockchain integration.
- Screenshot of the deployed smart contract on Ganache.

## Detailed Execution Process / Steps

### 1. Setting Up the Blockchain
- Create and deploy a smart contract using Truffle and Ganache.

### 2. Data Preparation
- Load and preprocess the dataset.
- Split the data into multiple clients.

### 3. Local Model Training
- Train local models with SMOTE for handling class imbalance.

### 4. Submit Model Updates to Blockchain
- Submit model updates to the blockchain.

### 5. Aggregate Models from Blockchain
- Aggregate the model updates retrieved from the blockchain.

### 6. Evaluate Global Model
- Evaluate the performance of the global model using various metrics.

# Step-by-Step Guide to Execute Phase 3A

## Prerequisites
1. **Docker**: Ensure Docker Desktop is installed and running.
2. **Ganache**: Install and run Ganache.

## 1. Setting Up Ganache
1. **Start Ganache**:
    - Open Ganache and create a new workspace.
    - Ensure the settings match the network configuration in `truffle-config.js` (host: `127.0.0.1`, port: `7545`).

## 2. Setting Up Docker Environment
1. **Create Dockerfile**:
    ```Dockerfile
    # Use an official Python runtime as a parent image
    FROM python:3.8-slim

    # Set the working directory in the container
    WORKDIR /usr/src/app

    # Copy the current directory contents into the container at /usr/src/app
    COPY . .

    # Install any needed packages specified in requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt

    # Install npm dependencies
    RUN apt-get update && apt-get install -y npm && npm install

    # Make port 8545 available to the world outside this container
    EXPOSE 8545

    # Define environment variable
    ENV PYTHONUNBUFFERED=1

    # Run the data preparation script first
    CMD ["python", "src/data_preparation.py"]
    ```

2. **Create requirements.txt**:
    ```plaintext
    pandas==1.2.4
    scikit-learn==0.24.2
    imbalanced-learn==0.7.0
    web3==5.20.0
    requests==2.25.1
    ```

3. **Build the Docker Image**:
    ```powershell
    docker build -t fraudbusters_phase3a .
    ```

4. **Run the Docker Container**:
    ```powershell
    docker run -it --rm --name fraudbusters_container fraudbusters_phase3a
    ```

## 3. Deploy Smart Contract
1. **Navigate to Project Directory**:
    ```powershell
    cd phase3a-federated_learning_with_blockchain
    ```

2. **Compile the Smart Contract**:
    ```powershell
    truffle compile
    ```

3. **Migrate the Smart Contract**:
    ```powershell
    truffle migrate --network development
    ```

## 4. Running the Project Scripts
1. **Access the Running Container**:
    ```powershell
    docker exec -it fraudbusters_container /bin/bash
    ```

2. **Run the Local Training Script**:
    ```bash
    python src/local_training.py
    ```

3. **Submit Model Updates**:
    ```bash
    python src/submit_updates.py
    ```

4. **Aggregate Models**:
    ```bash
    python src/aggregate_models.py
    ```

5. **Evaluate Global Model**:
    ```bash
    python src/evaluate_global_model.py
    ```

## Summary
This setup includes starting Ganache, configuring Docker, and running all necessary scripts to execute Phase 3A. Each script must be run in order, starting with `data_preparation.py` to ensure the data is ready for processing. Follow this guide to successfully execute Phase 3A of your project.
