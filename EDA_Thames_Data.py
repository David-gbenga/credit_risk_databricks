# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM `hive_metastore`.`default`.`thames1_water_collections_sample`;

# COMMAND ----------

# MAGIC %md
# MAGIC #EDA & RISK SEGMENTATION
# MAGIC Exploratory Data Analysis (EDA) and risk segmentation was carried out to understand the patterns , relationship between features and re-create the data into meaningful groups. This helps to understand how likely each group is to fall into arrears or default. A key metric here is the bad/default rate – the percentage of customers in a segment who become seriously delinquent or written off.
# MAGIC
# MAGIC - By analysing bad/default rates across variables like dpd (days past due), arrears_amount, income_band, vulnerability_flag, tariff_type, bill_cycle, etc., I will be able to :
# MAGIC
# MAGIC - See how risk increases with dpd and arrears size
# MAGIC
# MAGIC - Identify affordability issues in certain income bands or vulnerable customers
# MAGIC
# MAGIC - Spot whether specific tariffs or billing cycles are linked to higher arrears
# MAGIC
# MAGIC - Build risk tiers/segments (e.g. low/medium/high risk) to target collections actions more effectively
# MAGIC
# MAGIC - This is crucial because it turns raw data into actionable strategy: you know which groups need early support, tailored contact, or policy changes—and which groups can be managed with lighter-touch, cost-effective treatments.

# COMMAND ----------


#Load data 
df = spark.read.table("default.thames1_water_collections_sample")
display(df)


# COMMAND ----------

#show distinct delinquency_bucket
display(df.select('delinquency_bucket').distinct())

