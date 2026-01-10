# Day 2 – Spark DataFrames & Transformations

This folder contains my work for **Day 2** of the Databricks 14-Day Challenge by Indian Data Club.

The goal of Day 2 was to understand how Apache Spark processes data and how Spark DataFrames are used for analytics in Databricks.

---

## 📚 What I Learned

- Spark architecture: driver, executors, and DAG (Directed Acyclic Graph)  
- Difference between DataFrames and RDDs  
- Lazy evaluation in Spark (transformations vs actions)  
- Databricks notebook magic commands such as `%python`, `%sql`, and `%fs`  

---

## 🎯 Objective

Work with a real ecommerce dataset and perform basic Spark DataFrame operations.

---

## 🛠 What I did

Using PySpark in Databricks, I:

- Downloaded the ecommerce dataset from Kaggle  
- Loaded `2019-Nov.csv` into a Spark DataFrame  
- Selected important columns like event type, category, and price  
- Filtered records based on price  
- Grouped events by event type  
- Found the top brands based on activity  

These steps demonstrate how Spark performs distributed data processing.

---

## 📂 Files in this folder

| File | Purpose |
|------|--------|
| `Day 2 Databricks 14 Day AI Challenge.py` | PySpark code for loading data and performing Spark transformations |

---

## 📌 Challenge Submission

#DatabricksWithIDC  
@Databricks  
@Codebasics  
@indiandataclub  

