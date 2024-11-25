from itertools import combinations

# Simulated healthcare data
data = [
    ["diabetes", "hypertension", "heart_disease"],
    ["diabetes", "obesity"],
    ["hypertension", "cholesterol", "diabetes"],
    ["heart_disease", "diabetes"],
    ["obesity", "hypertension"],
    ["hypertension", "cholesterol"],
    ["cholesterol", "diabetes"],
    ["heart_disease", "hypertension", "cholesterol"],
    ["obesity", "diabetes", "hypertension"],
    ["diabetes", "obesity", "cholesterol"],
    ["obesity", "hypertension", "heart_disease"],
    ["heart_disease", "cholesterol"],
]

# Minimum support threshold
min_support = 0.2  # 20%

# Generate all possible combinations of items
def generate_combinations(data, k):
    combinations_list = []
    for transaction in data:
        combinations_list.extend(list(combinations(transaction, k)))
    return combinations_list

# Count the support for each combination
def calculate_support(data, itemsets):
    support_count = {}
    for itemset in itemsets:
        support_count[itemset] = sum([1 for transaction in data if set(itemset).issubset(transaction)])
    return {item: count for item, count in support_count.items() if count / len(data) >= min_support}

# Apriori algorithm
def apriori(data, min_support):
    k = 1
    frequent_itemsets = {}
    while True:
        combinations_list = generate_combinations(data, k)
        support_count = calculate_support(data, combinations_list)
        if not support_count:
            break
        frequent_itemsets.update(support_count)
        k += 1
    return frequent_itemsets

# Run Apriori
frequent_itemsets = apriori(data, min_support)

# Display results
print("Frequent Itemsets (EPDA Simulation):")
for itemset, count in frequent_itemsets.items():
    print(f"{itemset}: {count}")