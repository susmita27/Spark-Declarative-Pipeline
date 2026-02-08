from pyspark import pipelines as dp
from pyspark.sql.functions import *

#create empty stream table
dp.create_streaming_table("total_sales")

@dp.append_flow(target="total_sales")
def north_sales():
    df = spark.read.table("workspace.source.sales_north")
    return df

@dp.append_flow(target="total_sales")
def south_sales():
    df = spark.read.table("workspace.source.sales_south")
    return df