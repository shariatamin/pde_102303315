from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("IrisDataProcessing") \
    .master("local[*]") \
    .getOrCreate()

# Read the Iris CSV file
df = spark.read.csv("Iris.csv", header=True, inferSchema=True)

# Show the first few rows (like checking the data)
df.show(5)

# Example: Calculate average sepal length by species
avg_df = df.groupBy("Species").avg("SepalLengthCm")

# Show the results
avg_df.show()

# Stop Spark session
spark.stop()
