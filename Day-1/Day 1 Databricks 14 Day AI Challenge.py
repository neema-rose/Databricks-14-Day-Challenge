# Databricks notebook source
# MAGIC %md
# MAGIC ## **DAY 1**

# COMMAND ----------

# Create Simple DataFrame
data = [("iPhone", 999), ("Samsung", 799), ("MacBook", 1299)]
df = spark.createDataFrame(data, ["product", "price"])
df.show()

# Filter expensive products
df.filter(df.price > 1000).show()