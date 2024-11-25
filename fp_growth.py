import time
import psutil
from pyspark.ml.fpm import FPGrowth
from pyspark.sql import SparkSession
from pyspark.sql.functions import split
from prettytable import PrettyTable

# Monitor memory usage
def memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / (1024 * 1024)  # Convert to MB

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("FP-Growth Healthcare Data") \
    .getOrCreate()

# Load large dataset
df = spark.read.csv("large_healthcare_dataset.csv", header=True)

# Ensure items are properly split into arrays
df = df.withColumn("items", split(df["items"], ", "))

# Measure time and memory usage
start_time = time.time()
initial_memory = memory_usage()

# Run FP-Growth
fpGrowth = FPGrowth(itemsCol="items", minSupport=0.01, minConfidence=0.1)
model = fpGrowth.fit(df)

end_time = time.time()
final_memory = memory_usage()

# PrettyTable for Frequent Itemsets
print("Frequent Itemsets (FP-Growth):")
freq_table = PrettyTable()
freq_table.field_names = ["Frequent Itemsets", "Frequency"]
for row in model.freqItemsets.limit(30).collect():  # Limit to first 30 results
    freq_table.add_row([", ".join(row["items"]), row["freq"]])
print(freq_table)

# PrettyTable for Association Rules
print("\nAssociation Rules:")
assoc_table = PrettyTable()
assoc_table.field_names = ["Antecedent", "Consequent", "Confidence", "Lift", "Support"]
for row in model.associationRules.limit(30).collect():  # Limit to first 30 results
    assoc_table.add_row([
        ", ".join(row["antecedent"]),
        ", ".join(row["consequent"]),
        row["confidence"],
        row["lift"],
        row["support"]
    ])
print(assoc_table)

# PrettyTable for Predictions
print("\nPredictions:")
predictions_table = PrettyTable()
predictions_table.field_names = ["ID", "Items", "Prediction"]
for row in model.transform(df).select("id", "items", "prediction").limit(30).collect():  # Limit to first 30 results
    predictions_table.add_row([
        row["id"],
        ", ".join(row["items"]),
        ", ".join(row["prediction"]) if row["prediction"] else "[]"
    ])
print(predictions_table)

# Output memory usage and execution time
print(f"\nExecution Time (FP-Growth): {end_time - start_time:.4f} seconds")
print(f"Memory Usage (FP-Growth): {final_memory - initial_memory:.4f} MB")
