# Databricks notebook source
# MAGIC %md
# MAGIC CREATE SOURCE TABLE

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE workspace.source.sales
# MAGIC (order_id INT,
# MAGIC product_id INT,
# MAGIC revenue FLOAT,
# MAGIC date_time DATE,
# MAGIC store_id INT
# MAGIC
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT  INTO workspace.source.sales
# MAGIC VALUES (1,1001,1000,'2021-01-01',1),
# MAGIC        (2,1002,2000,'2021-01-02',2),
# MAGIC        (3,1003,3000,'2021-01-03',3),
# MAGIC        (4,1004,4000,'2021-01-04',4);
# MAGIC      

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from workspace.source.sales

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT  INTO workspace.source.sales
# MAGIC VALUES (5,1001,1000,'2021-01-01',1),
# MAGIC        (6,1002,2000,'2021-01-02',2);
# MAGIC        
# MAGIC      

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM workspace.target.cur_sales_stream

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT  INTO workspace.source.sales
# MAGIC VALUES (7,1001,1000,'2021-01-01',1),
# MAGIC        (8,1002,2000,'2021-01-02',2);

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE workspace.source.sales_north
# MAGIC (order_id INT,
# MAGIC product_id INT,
# MAGIC revenue FLOAT,
# MAGIC date_time DATE,
# MAGIC store_id INT
# MAGIC
# MAGIC );
# MAGIC
# MAGIC INSERT  INTO workspace.source.sales_north
# MAGIC VALUES (1,1001,1000,'2021-01-01',1),
# MAGIC        (2,1002,2000,'2021-01-02',2),
# MAGIC        (3,1003,3000,'2021-01-03',3),
# MAGIC        (4,1004,4000,'2021-01-04',4);
# MAGIC
# MAGIC        

# COMMAND ----------

# MAGIC %sql
# MAGIC -- CREATE TABLE workspace.source.sales_south
# MAGIC -- (order_id INT,
# MAGIC -- product_id INT,
# MAGIC -- revenue FLOAT,
# MAGIC -- date_time DATE,
# MAGIC -- store_id INT
# MAGIC
# MAGIC -- );
# MAGIC
# MAGIC INSERT  INTO workspace.source.sales_south
# MAGIC VALUES (5,1001,1000,'2021-01-05',1),
# MAGIC        (6,1002,2000,'2021-01-06',2),
# MAGIC        (7,1003,3000,'2021-01-07',3),
# MAGIC        (8,1004,4000,'2021-01-08',4);