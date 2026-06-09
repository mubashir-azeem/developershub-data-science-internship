# Task 2 - Customer Segmentation Using Unsupervised Learning (Mall Customers Dataset)

## Objective

The objective of this task is to segment customers into distinct groups based on their demographic characteristics and spending behavior. The project uses K-Means Clustering to identify customer segments and PCA (Principal Component Analysis) to visualize the clusters. Marketing strategies are then proposed for each customer segment.

---

# Dataset Information

Dataset Used:

* Mall Customers Dataset

Features:

* CustomerID
* Gender
* Age
* Annual Income (k$)
* Spending Score (1-100)

Target Variable:

* No target variable (Unsupervised Learning)

Total Records:

* 200 rows
* 5 columns

---

# Technologies Used

* Python
* Google Colab
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn

---

# Steps Performed

## 1. Data Loading

* Loaded the Mall Customers dataset
* Displayed dataset structure using:

  * `.shape`
  * `.head()`
  * `.info()`
  * `.describe()`

## 2. Data Inspection

* Checked dataset information
* Verified missing values
* Generated statistical summary
* Examined customer demographics

## 3. Exploratory Data Analysis (EDA)

Created:

* Gender Distribution
* Age Distribution
* Annual Income Distribution
* Spending Score Distribution
* Correlation Heatmap

## 4. Feature Selection

Selected important customer attributes:

* Age
* Annual Income (k$)
* Spending Score (1-100)

Excluded:

* CustomerID

Reason:

* CustomerID is only an identifier and does not represent customer behavior.

## 5. Feature Scaling

* Applied StandardScaler
* Standardized all selected features
* Prepared data for clustering

## 6. Finding Optimal Number of Clusters

### Elbow Method

* Calculated WCSS values for K = 1 to K = 10
* Generated Elbow Method graph
* Identified optimal number of clusters

Selected:

* K = 5

Reason:

* The elbow point appeared at K = 5 where additional clusters provided only minor improvements.

## 7. Customer Segmentation Using K-Means

* Applied K-Means Clustering
* Created 5 customer segments
* Assigned cluster labels to each customer

## 8. Dimensionality Reduction (PCA)

* Applied Principal Component Analysis (PCA)
* Reduced dataset from 3 dimensions to 2 dimensions
* Generated cluster visualization

## 9. Cluster Analysis

Analyzed average values for:

* Age
* Annual Income
* Spending Score

Identified customer groups with different spending behaviors and purchasing power.

## 10. Marketing Strategy Development

Developed targeted marketing strategies for each customer segment based on:

* Income level
* Spending habits
* Age characteristics

---

# Cluster Summary

## Cluster 0

* Older customers
* Low income
* Low spending score

Strategy:

* Budget offers
* Discount campaigns
* Seasonal promotions

## Cluster 1

* Younger customers
* Moderate income
* High spending behavior

Strategy:

* Social media marketing
* Loyalty rewards
* Personalized recommendations

## Cluster 2

* High income
* High spending score

Strategy:

* Premium memberships
* VIP programs
* Exclusive product launches

## Cluster 3

* High income
* Low spending score

Strategy:

* Personalized promotions
* Targeted offers
* Customer engagement campaigns

## Cluster 4

* Older customers
* Average income
* Moderate spending score

Strategy:

* Cashback programs
* Membership discounts
* Product recommendation campaigns

---

# Key Observations

* Customer spending behavior varies significantly across segments.
* Annual income alone does not determine spending habits.
* Younger customers generally show higher spending scores.
* Five distinct customer groups were successfully identified.
* PCA visualization confirmed clear separation between most customer segments.
* Customer segmentation enables more effective and personalized marketing strategies.

---

# Conclusion

The Mall Customers dataset was successfully analyzed using unsupervised machine learning techniques. K-Means Clustering identified five meaningful customer segments based on age, annual income, and spending score. The Elbow Method helped determine the optimal number of clusters, while PCA enabled effective visualization of customer groups. The identified customer segments provide valuable business insights and can help organizations create targeted marketing campaigns, improve customer engagement, and increase revenue through data-driven decision-making.

---

# Output Visualizations

## Exploratory Data Analysis

* Gender Distribution
* Age Distribution
* Annual Income Distribution
* Spending Score Distribution
* Correlation Heatmap

## Clustering

* Elbow Method Graph
* PCA Cluster Visualization

## Customer Analysis

* Cluster Summary Table
* Customer Segment Analysis

---

# Author

Mubashir Azeem Abbasi
