import ifcopenshell
from collections import defaultdict

# Path to your IFC file
ifc_file_path = "D:\\BIM\\CES_BLD_24_10_ARC.ifc"

# Open the IFC file
ifc_file = ifcopenshell.open(ifc_file_path)

if ifc_file:
    
    space_count_dict = defaultdict(int)

    # Retrieve all IfcSpace
    spaces = ifc_file.by_type("IfcSpace")

    # count
    for space in spaces:
        long_name = getattr(space, 'LongName', '').strip()  # get 
        space_count_dict[long_name] += 1  # Count for each name

    # Print 
    for long_name, count in space_count_dict.items():
        if long_name:  
            print(f"{long_name}: {count}")
        else:
            print(f"Unnamed Space: {count}")
else:
    print(f"Error: Unable to load the IFC file at '{ifc_file_path}'")
