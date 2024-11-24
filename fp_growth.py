from pyspark.ml.fpm import FPGrowth
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("FrequentPatternMining") \
    .getOrCreate()
 
# Load expanded healthcare transactional data
data = spark.createDataFrame([
    (0, ["diabetes", "hypertension", "heart_disease"]),
    (1, ["diabetes", "obesity"]),
    (2, ["hypertension", "cholesterol", "diabetes"]),
    (3, ["heart_disease", "diabetes"]),
    (4, ["obesity", "hypertension"]),
    (5, ["hypertension", "cholesterol"]),
    (6, ["cholesterol", "diabetes"]),
    (7, ["heart_disease", "hypertension", "cholesterol"]),
    (8, ["obesity", "diabetes", "hypertension"]),
    (9, ["diabetes", "obesity", "cholesterol"]),
    (10, ["obesity", "hypertension", "heart_disease"]),
    (11, ["heart_disease", "cholesterol"]),
    (12, ["hypertension", "obesity", "heart_disease"]),
    (13, ["cholesterol", "heart_disease"]),
    (14, ["obesity", "heart_disease"]),
    (15, ["diabetes", "cholesterol", "heart_disease"]),
    (16, ["diabetes", "obesity", "cholesterol", "heart_disease"]),
], ["id", "items"])

# Adjust FP-Growth parameters for larger datasets
# Lower minSupport and minConfidence to capture more patterns
fpGrowth = FPGrowth(itemsCol="items", minSupport=0.2, minConfidence=0.1)
model = fpGrowth.fit(data)

# Display frequent itemsets
print("Frequent Itemsets:")
model.freqItemsets.show(truncate=False)

# Display association rules
print("Association Rules:")
model.associationRules.show(truncate=False)

# Predict patterns on new data
print("Predictions:")
predictions = model.transform(data)
predictions.show(truncate=False)
