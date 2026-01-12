# 📘 Day 4 – Delta Lake Introduction

Today, I learned how to use **Delta Lake** in Databricks by converting a very large CSV file into Delta format and testing how Delta Lake protects data using features like **ACID transactions** and **schema enforcement**.

This project helped me understand how big companies store and manage large amounts of data safely.

---

## 📚 What is Delta Lake?

Delta Lake is a storage layer built on top of data lake files.  
It allows us to store data in a way that is:

- Reliable
- Consistent
- Easy to update
- Safe from corruption

Normally, when we store data as CSV or Parquet files, we do not get protection from:
- Wrong data types
- Broken writes
- Duplicate or partial files

Delta Lake solves these problems.

---

## 🔹 Important Concepts I Learned

### 1️⃣ ACID Transactions  
ACID means:
- **Atomicity** – All data is written or nothing is written  
- **Consistency** – Data always follows rules  
- **Isolation** – Multiple users can write safely  
- **Durability** – Once written, data is not lost  

Delta Lake uses a transaction log so that data is always safe.

---

### 2️⃣ Schema Enforcement  
Schema means the structure of the data (columns and data types).

Delta Lake does not allow:
- Missing columns
- Extra columns
- Wrong data types

This prevents bad data from entering the table.

---

### 3️⃣ Delta Tables  
A Delta table is not just a file.  
It is a combination of:
- Data files
- A transaction log that tracks all changes

This allows:
- Updates
- Deletes
- Version history (time travel)

---

### 4️⃣ Delta vs Parquet

| Feature | Parquet | Delta Lake |
|--------|--------|------------|
| ACID Transactions | ❌ No | ✅ Yes |
| Schema Enforcement | ❌ No | ✅ Yes |
| Update & Delete | ❌ Hard | ✅ Easy |
| Data Versioning | ❌ No | ✅ Yes |

---

## 🛠️ Tasks

#### Step 1 – Load CSV into Spark  
#### Step 2 – Convert CSV to Delta  
#### Step 3 – Created Delta table using SQL
#### Step 4 – Tested Schema Enforcement
#### Step 5 –Tested Duplicate Inserts

**Check corresponding jupyter notebook for complete detailed code**

### 🏷️ Tags & Mentions
@Databricks
@Codebasics
@indiandataclub 
#DatabricksWithIDC
