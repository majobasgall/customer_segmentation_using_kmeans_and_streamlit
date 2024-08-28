import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="📊",
    layout="wide",
)

# Title and Description
st.title("Customer Segmentation Using K-Means Clustering")
st.markdown(
    """
    This application demonstrates customer segmentation using K-means clustering. 
    We use a synthetic dataset that simulates customer behavior based on various features such as 
    annual income, spending score, and age.
    """
)

# Sidebar for user input
st.sidebar.header("Input Parameters")

# Function to load the dataset
@st.cache_data
def load_data():
    # Synthetic dataset creation
    np.random.seed(42)
    data = pd.DataFrame({
        'Age': np.random.randint(18, 70, 200),
        'Annual Income (k$)': np.random.randint(15, 150, 200),
        'Spending Score (1-100)': np.random.randint(1, 100, 200)
    })
    return data

# Load data
data = load_data()

# Sidebar slider for number of clusters
n_clusters = st.sidebar.slider("Number of clusters", min_value=2, max_value=10, value=3)

# Standardize data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
data['Cluster'] = kmeans.fit_predict(data_scaled)

# Display the data table with cluster information
st.subheader("Clustered Data")
st.dataframe(data)

# Plot the clusters
st.subheader("Cluster Visualization")
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(data['Annual Income (k$)'], data['Spending Score (1-100)'], c=data['Cluster'], cmap='viridis')
ax.set_xlabel("Annual Income (k$)")
ax.set_ylabel("Spending Score (1-100)")
ax.set_title("Customer Segments")
plt.colorbar(scatter, ax=ax)
st.pyplot(fig)

# Display cluster centers
st.subheader("Cluster Centers")
centers = scaler.inverse_transform(kmeans.cluster_centers_)
st.write(pd.DataFrame(centers, columns=data.columns[:-1]))

# Summary and Insights
st.subheader("Summary and Insights")
st.markdown(
    """
    - **Cluster Analysis:** The clustering results segment customers into distinct groups based on their 
    spending habits and income levels. This information can be used to target different customer segments 
    with tailored marketing strategies.
    - **Business Applications:** Retailers and service providers can leverage such insights to improve customer 
    satisfaction, increase sales, and optimize marketing efforts.
    """
)

# Footer
st.markdown(
    """
    **Note:** This is a synthetic dataset used for demonstration purposes.
    """
)
