# Databricks notebook source
!pip install kaggle

# COMMAND ----------

import os

os.environ['KAGGLE_USERNAME']="YOUR_USERNAME"
os.environ['KAGGLE_KEY']="YOUR_API_KEY"

print("Kaggle credantials configured")

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

# Load data
events = spark.read.csv("/Volumes/workspace/ecommerce/ecommerce_data/2019-Nov.csv", header=True, inferSchema=True)
display(events)

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Basic operations**

# COMMAND ----------

events.select("event_type", "category_code", "price").show(10)

# COMMAND ----------

events.filter("price > 100").count()

# COMMAND ----------

events.groupBy("event_type").count().show()

# COMMAND ----------

top_brands = events.groupBy("brand").count().orderBy("count", ascending=False).limit(5)
display(top_brands)

# COMMAND ----------

