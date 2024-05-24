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
- Set up a simple blockchain.
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
