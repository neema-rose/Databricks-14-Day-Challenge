# Databricks notebook source
# MAGIC %md
# MAGIC # **DAY 0**

# COMMAND ----------

!pip install kaggle

# COMMAND ----------

import os

os.environ["KAGGLE_USERNAME"] = "<your_kaggle_username>"
os.environ["KAGGLE_KEY"] = "<your_kaggle_api_key>"


print("Kaggle credentials configured")

# COMMAND ----------

spark.sql("""
          CREATE SCHEMA IF NOT EXISTS workspace.ecommerce
          """)

# COMMAND ----------

spark.sql("""
          CREATE VOLUME IF NOT EXISTS workspace.ecommerce.ecommerce_data
          """)

# COMMAND ----------

# MAGIC %sh
# MAGIC cd /Volumes/workspace/ecommerce/ecommerce_data
# MAGIC kaggle datasets download -d mkechinov/ecommerce-behavior-data-from-multi-category-store

# COMMAND ----------

# MAGIC %sh
# MAGIC cd /Volumes/workspace/ecommerce/ecommerce_data
# MAGIC unzip -o ecommerce-behavior-data-from-multi-category-store.zip
# MAGIC ls -lh

# COMMAND ----------

# MAGIC %sh
# MAGIC cd /Volumes/workspace/ecommerce/ecommerce_data
# MAGIC rm -f ecommerce-behavior-data-from-multi-category-store.zip
# MAGIC ls -lh

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

df_n = spark.read.csv("/Volumes/workspace/ecommerce/ecommerce_data/2019-Nov.csv")

# COMMAND ----------

df = spark.read.csv("/Volumes/workspace/ecommerce/ecommerce_data/2019-Oct.csv")

# COMMAND ----------

# Display dataset statistics and schema
print(f"October 2019 - Total Events:{df.count():,}")
print("\n"+"="*60)
print("SCHEMA:")
print("="*60)
df.printSchema()

# COMMAND ----------

#Display sample data
print("\n"+"="*60)
print("Sample data (first 5 rows):")
print("="*60)
df.show(5,truncate=False)
