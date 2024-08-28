# Customer Segmentation Using K-Means Clustering

## Overview

This Streamlit application demonstrates customer segmentation using the K-means clustering algorithm. The app uses a synthetic dataset that simulates customer behavior based on various features such as annual income, spending score, and age. The goal is to segment customers into distinct groups, which can help businesses target different customer segments with tailored marketing strategies.

## Features

- **Data Input:** Synthetic dataset with customer information.
- **User Input:** Adjustable number of clusters for the K-means algorithm.
- **Data Display:** View the clustered data and cluster centers.
- **Visualization:** Scatter plot visualization of customer segments based on selected features.
- **Summary and Insights:** Business insights and potential applications of the results.

## Dependencies
- **Streamlit**
- **pandas**
- **numpy**
- **scikit-learn**
- **matplotlib**

# Usage
Once the app is running (`streamlit run customer_segmentator.py`), you can adjust the number of clusters using the sidebar slider. The app will automatically re-cluster the data and update the visualizations and insights based on the selected number of clusters.

# Example Use Cases
- Retail Industry: Segmenting customers based on their purchasing power and spending behavior.
- Banking Sector: Identifying customer segments for personalized financial products.
- Marketing: Targeting customer segments with tailored promotional strategies.

# Cluster Analysis and Conclusions
As an example, for k=3, the K-means clustering results in the following customer segments:

| Cluster | Average Age | Average Annual Income ($k) | Average Spending Score |
|---------|-----------|----------------------|------------------------|
| **0**   | ~ 43      | ~ 50                 | ~ 42.9                 |
| **1**   | ~ 57      | ~ 102                | ~ 66.9                 |
| **2**   | ~ 29      | ~ 124                | ~ 40.4                 |

**Some insights from the results:**
- Cluster 0: Middle-aged, moderate income and spending. Ideal for mid-tier products.
- Cluster 1: Older, high income, high spenders. Best for premium offerings.
- Cluster 2: Younger, high income, conservative spenders. Focus on upselling with exclusive offers.

# Deploy the App on Streamlit Cloud:

- Go to Streamlit Cloud (https://share.streamlit.io/)
- Log in with your GitHub account.
- Select "New app" and link it to your GitHub repository.
- Choose the branch and the main file (customer_segmentator.py).
- Click "Deploy" to make the app publicly accessible.