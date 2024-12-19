import csv

def process_csv(filename):
    
    try:
        with open(filename, 'r', encoding='utf-8') as file: 
            reader = csv.DictReader(file)  
            data = list(reader)  

           
            for row in data:
                for key, value in row.items():
                    print(f"{key} → {value}")

            return data  

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while processing the CSV file: {e}")
        return None


def csv_min(data, column):
  
    try:
        return min(float(row[column]) for row in data)
    except (ValueError, KeyError):
        print("Error: Invalid column or data type.")
        return None


def csv_max(data, column):
    
    try:
        return max(float(row[column]) for row in data)
    except (ValueError, KeyError):
        print("Error: Invalid column or data type.")
        return None


def csv_sum(data, column):
    
    try:
        return sum(float(row[column]) for row in data)
    except (ValueError, KeyError):
        print("Error: Invalid column or data type.")
        return None


def csv_average(data, column):
    
    try:
        values = [float(row[column]) for row in data]
        return sum(values) / len(values) if values else None
    except (ValueError, KeyError):
        print("Error: Invalid column or data type.")
        return None



csv_data = process_csv("6.csv")
if csv_data:
    min_val = csv_min(csv_data, 'column_name') 
    max_val = csv_max(csv_data, 'column_name')
    sum_val = csv_sum(csv_data, 'column_name')
    avg_val = csv_average(csv_data, 'column_name')

    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    print(f"Sum: {sum_val}")
    print(f"Average: {avg_val}")