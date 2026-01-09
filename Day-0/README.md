# Day 0 – Databricks Environment Setup

This folder contains the complete setup work for **Day 0** of the **Databricks 14-Day Challenge by Indian Data Club**.

The goal of Day 0 was to prepare a working Databricks environment with real data so that all future analytics and Spark tasks can run smoothly.

---

## 🎯 Objective

Set up Databricks, connect Kaggle, and load a real ecommerce dataset into the Lakehouse.

---

## 🛠 What I completed

Using Databricks Community Edition, I performed the following:

- Installed Kaggle inside Databricks  
- Configured Kaggle API authentication  
- Created a Databricks schema and volume  
- Downloaded a real ecommerce dataset from Kaggle  
- Extracted and stored the data in Databricks  
- Loaded the dataset using Spark  
- Verified row counts and schema  

The dataset used:
**E-commerce Behavior Data from a Multi-Category Store**

---

## 📂 What is in this folder

| File | Purpose |
|------|--------|
| `Day 0 Databricks 14 Day AI Challenge.py.py` | All commands used to configure Kaggle, create volumes, download data, and load it into Spark |

---

## ✅ Verification

The setup was validated by:

- Successfully loading `2019-Oct.csv` and `2019-Nov.csv`
- Running `count()` on the dataset
- Printing the Spark schema
- Displaying sample rows

This confirms the Lakehouse environment is ready for analysis.

---

## 📌 Challenge Submission

#DatabricksWithIDC  
@Databricks  
@Codebasics  
@indiandataclub  
