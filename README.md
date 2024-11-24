# FP-Growth and Apriori Algorithm Analysis

This project improves frequent pattern mining for healthcare data by optimizing the EPDA algorithm using the FP-Growth algorithm and Apache Spark. The implementation focuses on memory efficiency and real-time processing to handle large datasets effectively.

---

## Abstract

Frequent pattern mining is essential for analyzing healthcare data to identify co-occurring conditions. Traditional algorithms like EPDA and Apriori are inefficient in memory usage and speed. This project addresses these challenges by:
- Using the FP-Growth algorithm to reduce memory usage.
- Leveraging Apache Spark for real-time data processing.

---

## Requirements and Setup

### Dependencies

Ensure the following are installed:

- **Python**: Version 3.8 or above
- **Apache Spark**: For distributed computing
- **Python Libraries**:
  - PySpark
  - Pandas
  - Numpy

### Installation

Follow these steps to install the dependencies:

1. **Python Installation**: Ensure you have Python 3.8 or later installed. You can download it from the [official Python website](https://www.python.org/downloads/).
2. **Install Apache Spark**:
   - Download and install Apache Spark from [Apache Spark Download](https://spark.apache.org/downloads.html).
   - Set the `SPARK_HOME` environment variable to point to the Spark installation directory.
   - Add Spark's `bin` directory to your system's `PATH`.
   - Verify the installation by running:
     ```bash
     spark-shell
     ```
3. **Install Python Libraries**:
   Install the required libraries using pip:
   ```bash
   pip install pyspark pandas numpy
   ```

---

## Execution Steps

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/techy21/Fp-Growth-and-Apriori-Algorithm-Analysis.git
cd Fp-Growth-and-Apriori-Algorithm-Analysis
```

### Step 2: Prepare the Dataset

- Ensure your dataset is placed in the `data/` directory (create the directory if it doesn’t exist).
- Confirm that the dataset adheres to the specified format.
- If necessary, update the dataset path in the `fp_growth.py` script.

### Step 3: Run the FP-Growth Script

Run the script to analyze the data:

```bash
python fp_growth.py
```

---

## Outputs

1. **Frequent Itemsets**: Patterns that frequently co-occur in the dataset.
   - *Example*: `{diabetes, hypertension}` appears 15 times.
2. **Association Rules**: Relationships between conditions.
   - *Example*: `diabetes -> hypertension (confidence: 80%)`.
3. **Predictions**: Suggested co-occurring conditions based on identified patterns.
   - *Example*: A patient with `heart_disease` may also have `obesity`.

---

## Contributions

- **Umer Abdul Khaliq**
- **Gurpreet Singh**
- **Bilal Tariq**
- **Saif Ali**

---

## License

This project is licensed under the MIT License.
