import xml.etree.ElementTree as ET

# Charger le fichier XML
tree = ET.parse('python/python_to_BD/test.drawio.xml')
root = tree.getroot()

# Parcourir les cellules pour trouver les entités
for cell in root.findall(".//mxCell[@value]"):
    table_name = cell.get("value")
    print(f"-- Table {table_name}")
    print(f"CREATE TABLE {table_name} (id INT PRIMARY KEY);")