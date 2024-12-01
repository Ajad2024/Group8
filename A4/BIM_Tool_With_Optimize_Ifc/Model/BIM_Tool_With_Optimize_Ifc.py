import ifcopenshell
import csv
import os

# Path to IFC file
ifc_file_path = "D:\\BIM\\CES_BLD_24_10_ARC.ifc"

# Define requirements
AREA_REQUIREMENTS = {
    "MEETING ROOM": 2.5,   # m² per person
    "OFFICE": 8.0,
    "STUDENT": 3.0,
    "Toilet": 5.0,         # Fixed area
    "PRINTING": 3.0,
    "STAIRCASE": 34.0, 
    "AUDITORIUM": 100      # Fixed area
}

# output path
export_dir = "C:\\Users\\ajads\\Desktop\\A-3-4\\One code if the ifc is with areas"
output_file = os.path.join(export_dir, "space_requirements_Result.csv")

def calculate_geometry_area(space):
    """
    Calculate area from geometric representations if available.
    """
    if hasattr(space, "Representation"):
        representation = space.Representation
        for rep in representation.Representations:
            if rep.RepresentationType == "SweptSolid":
                for item in rep.Items:
                    if item.is_a("IfcExtrudedAreaSolid"):
                        profile = item.SweptArea
                        if profile.is_a("IfcRectangleProfileDef"):
                            return (profile.XDim * profile.YDim) / 1_000_000  # Convert mm² to m²
    return None

def get_space_level(space):
    """
    Retrieve the level (IfcBuildingStorey) of a space.
    """
    try:
        for rel in space.Decomposes:
            if rel.is_a("IfcRelAggregates") and rel.RelatingObject.is_a("IfcBuildingStorey"):
                return rel.RelatingObject.Name  
    except AttributeError:
        return "Not Defined"
    return "Not Defined"

def extract_spaces_from_ifc(ifc_file):
    """
    Extract space information from the IFC file using both properties and geometry.
    """
    spaces = []
    for space in ifc_file.by_type("IfcSpace"):
        space_name = getattr(space, 'LongName', '') or getattr(space, 'Name', 'Unnamed Space')
        space_type = getattr(space, 'ObjectType', 'Undefined')
        level = get_space_level(space)
        
        # Extract area -properties/geometry
        gross_area = None
        if hasattr(space, "IsDefinedBy"):
            for rel in space.IsDefinedBy:
                if hasattr(rel, "RelatingPropertyDefinition") and hasattr(rel.RelatingPropertyDefinition, "HasProperties"):
                    for prop in rel.RelatingPropertyDefinition.HasProperties:
                        if prop.Name == "GrossFloorArea":
                            gross_area = float(prop.NominalValue.wrappedValue) / 1_000_000  # Convert mm² to m²
        
        if gross_area is None or gross_area == 0:
            gross_area = calculate_geometry_area(space) or 0
        
        # Result
        status = "Fail"
        comment = "Required area not met"
        
        # Validate  requirements
        for room_type, area_per_person in AREA_REQUIREMENTS.items():
            if room_type in space_name:
                required_area = area_per_person
                if room_type in ["Toilet", "PRINTING", "AUDITORIUM", "STAIRCASE"]:
                    if gross_area >= required_area:
                        status = "Pass"
                        comment = f"Meets fixed area requirement (available: {gross_area} m²)"
                    else:
                        comment = (
                            f"Required fixed area for {room_type} is {required_area} m², "
                            f"but the available area is {gross_area} m²."
                        )
                else:
                    # area logic
                    try:
                        num_people = int(space_name.split()[-1].replace('P', ''))
                        required_area = num_people * area_per_person
                        if gross_area >= required_area:
                            status = "Pass"
                            comment = f"Meets requirements (available: {gross_area} m²)"
                        else:
                            comment = (
                                f"Required area for {num_people}P in {room_type} is {required_area} m², "
                                f"but the available area is {gross_area} m²."
                            )
                    except ValueError:
                        comment = "Invalid format for number of people."
                break
        
        spaces.append({
            'Space Name': space_name,
            'Space Type': space_type,
            'Level': level,
            'Gross Area (m²)': gross_area,
            'Status': status,
            'Comment': comment
        })
    return spaces

def main():
    try:
        ifc_file = ifcopenshell.open(ifc_file_path)
    except Exception as e:
        print(f"Failed to open IFC file: {e}")
        return
    
    spaces = extract_spaces_from_ifc(ifc_file)
    print(f"Extracted {len(spaces)} spaces from the IFC file.")
    
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Space Name', 'Space Type', 'Level', 'Gross Area (m²)', 'Status', 'Comment']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(spaces)
        print(f"Space requirements exported to {output_file}.")
    except Exception as e:
        print(f"Failed to export CSV file: {e}")

if __name__ == "__main__":
    main()
