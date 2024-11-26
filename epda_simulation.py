import time
import psutil
import csv
from itertools import combinations
from prettytable import PrettyTable

# Monitor memory usage
def memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / (1024 * 1024)  # Convert to MB

# Simulated EPDA algorithm
def epda_algorithm(transactions, min_support):
    # Count single items
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1

    # Generate combinations for higher-order itemsets
    for transaction in transactions:
        for r in range(2, len(transaction) + 1):  # Generate itemsets of size 2 and higher
            for combo in combinations(transaction, r):
                combo = tuple(sorted(combo))  # Sort to avoid duplicates
                item_counts[combo] = item_counts.get(combo, 0) + 1

    # Filter by min_support
    frequent_itemsets = {item: count for item, count in item_counts.items() if count / len(transactions) >= min_support}
    return frequent_itemsets

# Load dataset from CSV
def load_dataset(file_path):
    transactions = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            transactions.append(row[1].split(", "))  # Assuming the second column contains the items
    return transactions

# Load the dataset
file_path = "large_healthcare_dataset.csv"  # Make sure this matches the file used for FP-Growth
transactions = load_dataset(file_path)

# Measure execution time and memory usage
start_time = time.time()
initial_memory = memory_usage()

# Run EPDA
frequent_itemsets = epda_algorithm(transactions, min_support=0.01)  # Adjust min_support as needed

end_time = time.time()
final_memory = memory_usage()

# Display frequent itemsets in table format
table = PrettyTable()
table.field_names = ["Frequent Itemsets", "Frequency"]
for item, freq in sorted(frequent_itemsets.items(), key=lambda x: (-len(x[0]) if isinstance(x[0], tuple) else 1, -x[1]))[:20]:
    table.add_row([", ".join(item) if isinstance(item, tuple) else item, freq])
print(table)

# Display execution time and memory usage
print(f"\nExecution Time (EPDA): {end_time - start_time:.4f} seconds")
print(f"Memory Usage (EPDA): {final_memory - initial_memory:.4f} MB")
