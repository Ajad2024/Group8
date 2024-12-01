import ifcopenshell
import pandas as pd

# Path IFC file
ifc_file_path = r"D:\BIM\CES_BLD_24_10_ARC.ifc"

# Output Excel path
output_excel_path = r"D:\BIM\ifcspace_data_sorted.xlsx"


try:
    ifc_file = ifcopenshell.open(ifc_file_path)
    print(f"Successfully loaded IFC file: {ifc_file_path}")
except Exception as e:
    print(f"Failed to load IFC file: {e}")
    exit()

# Extract IfcSpace
spaces = ifc_file.by_type("IfcSpace")
print(f"Found {len(spaces)} IfcSpace elements in the IFC file.")

# call level
def get_space_level(space):
    try:
        for rel in space.Decomposes:
            if rel.is_a("IfcRelAggregates") and rel.RelatingObject.is_a("IfcBuildingStorey"):
                return rel.RelatingObject.Name  # Return the level name
    except AttributeError:
        return "Not Defined"
    return "Not Defined"

#  Excel
data = []
for space in spaces:
    space_data = {
        "GlobalId": space.GlobalId,
        "LongName": getattr(space, "LongName", "Not Defined"),
        "Level": get_space_level(space),
    }
    data.append(space_data)

#  DataFrame
df = pd.DataFrame(data)

# Sort 
df = df.sort_values(by=["LongName", "Level"], ascending=[True, True])

# Save 
try:
    df.to_excel(output_excel_path, index=False)
    print(f"Data saved to Excel file: {output_excel_path}")
except Exception as e:
    print(f"Failed to save Excel file: {e}")
