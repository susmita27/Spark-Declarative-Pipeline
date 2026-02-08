# from pyspark import pipelines as dp
# from pyspark.sql.functions import *

# #create materialized views
# @dp.table(name="src_sales_stream")
# def src_sales_stream():
#     df=spark.readStream.table("workspace.source.sales")
#     df=df.withColumn("date_time",to_date(col("date_time"),"MM-dd-yyyy"))
#     return df

# #referring another materialized view
# @dp.table(name="enr_sales_stream")
# def enr_sales_stream():
#     df=dp.read_stream("src_sales_stream")
#     df=df.withColumn("revenue",col("revenue")*1.05)
#     return df

# @dp.table(name="cur_sales_stream")
# def cur_sales_stream():
#     df=dp.read_stream("enr_sales_stream")
#     df=df.groupBy("date_time").agg(sum("revenue").alias("total_revenue"))
#     return df
