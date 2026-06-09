import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Superstore Business Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------
# Load Dataset
# -----------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")
    return df

df = load_data()

# -----------------------------------
# Data Cleaning
# -----------------------------------
df.drop_duplicates(inplace=True)

# -----------------------------------
# Sidebar Filters
# -----------------------------------
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

subcategory = st.sidebar.multiselect(
    "Sub-Category",
    options=df["Sub-Category"].unique(),
    default=df["Sub-Category"].unique()
)

# -----------------------------------
# Apply Filters
# -----------------------------------
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Sub-Category"].isin(subcategory))
]

# -----------------------------------
# Dashboard Title
# -----------------------------------
st.title("📊 Superstore Business Dashboard")
st.markdown("Interactive Analysis of Sales, Profit and Customer Performance")

# -----------------------------------
# KPIs
# -----------------------------------
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df.shape[0]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sales",
    f"${total_sales:,.2f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

col3.metric(
    "Total Orders",
    f"{total_orders:,}"
)

st.divider()

# -----------------------------------
# Sales by Category
# -----------------------------------
sales_category = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    sales_category,
    x="Category",
    y="Sales",
    title="Sales by Category",
    text_auto=True
)

# -----------------------------------
# Profit by Category
# -----------------------------------
profit_category = (
    filtered_df.groupby("Category")["Profit"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    profit_category,
    values="Profit",
    names="Category",
    title="Profit Distribution by Category"
)

col4, col5 = st.columns(2)

with col4:
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------------
# Top 5 Customers by Sales
# -----------------------------------
top_customers = (
    filtered_df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

fig3 = px.bar(
    top_customers,
    x="Sales",
    y="Customer Name",
    orientation="h",
    title="Top 5 Customers by Sales",
    text_auto=True
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------------
# Region-wise Sales
# -----------------------------------
region_sales = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig4 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Region-wise Sales"
)

st.plotly_chart(fig4, use_container_width=True)

# -----------------------------------
# Segment-wise Sales
# -----------------------------------
segment_sales = (
    filtered_df.groupby("Segment")["Sales"]
    .sum()
    .reset_index()
)

fig5 = px.bar(
    segment_sales,
    x="Segment",
    y="Sales",
    title="Sales by Segment",
    text_auto=True
)

st.plotly_chart(fig5, use_container_width=True)

# -----------------------------------
# Data Preview
# -----------------------------------
st.subheader("Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)