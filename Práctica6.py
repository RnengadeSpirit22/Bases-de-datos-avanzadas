import pandas as pd
import os
import xml.etree.ElementTree as ET

input_file_path = "C:/Users/LENOVO P50/Documents/Escuela/BDA/sales_data.csv"

df = pd.read_csv(input_file_path, encoding='ISO-8859-1')

df_filtered = df.dropna(subset=['STATE'])

output_folder = "C:/Users/LENOVO P50/Documents/Escuela/BDA"
os.makedirs(output_folder, exist_ok=True)
output_file_path = os.path.join(output_folder, 'sales_data_filtered.xml')

root = ET.Element('SalesData')

for _, row in df_filtered.iterrows():
    entry = ET.SubElement(root, 'Entry')
    for col in df_filtered.columns:
        element = ET.SubElement(entry, col)
        element.text = str(row[col])

tree = ET.ElementTree(root)
tree.write(output_file_path, encoding='utf-8', xml_declaration=True)

print(f"El archivo XML ha sido guardado en: {output_file_path}")
