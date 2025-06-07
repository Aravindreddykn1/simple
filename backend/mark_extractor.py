# backend/mark_extractor.py
import csv

def write_to_csv(data, filename="results/extracted_csv/output.csv"):
    with open(filename, mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "USN", "Subject", "IA1", "IA2", "IA3"])
        for row in data:
            writer.writerow(row)
