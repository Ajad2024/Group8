import ifcopenshell
from bonsai.bim.ifc import IfcStore

def count_furniture_per_storey():
    # Load the IFC file using IfcStore
    file = IfcStore.get_file()

    # Retrieve all building storeys from the IFC file
    storeys = file.by_type('IfcBuildingStorey')

    # Create a dictionary to store the count of furniture per storey
    furniture_count_per_storey = {}

    # Initialize furniture count for each storey
    for storey in storeys:
        storey_name = storey.Name if storey.Name else storey.GlobalId
        furniture_count_per_storey[storey_name] = 0

    # Initialize counter for furniture not assigned to any storey
    unassigned_furniture_count = 0

    # Loop through each IfcFurniture element
    for furniture in file.by_type('IfcFurniture'):
        assigned = False

        # Check if the furniture is contained within a building storey using IfcRelContainedInSpatialStructure
        if furniture.ContainedInStructure:
            for relation in furniture.ContainedInStructure:
                if relation.is_a("IfcRelContainedInSpatialStructure"):
                    relating_storey = relation.RelatingStructure
                    # If the relating structure is a building storey, increase the count
                    if relating_storey in storeys:
                        storey_name = relating_storey.Name if relating_storey.Name else relating_storey.GlobalId
                        furniture_count_per_storey[storey_name] += 1
                        assigned = True
                        break

        # If the furniture was not assigned to any storey, increase the unassigned count
        if not assigned:
            unassigned_furniture_count += 1

    # Return the dictionary with counts and unassigned furniture count
    return furniture_count_per_storey, unassigned_furniture_count

def print_furniture_count():
    # Call the function and retrieve counts
    furniture_count_per_storey, unassigned_furniture_count = count_furniture_per_storey()
    
    # Print the number of furniture items per storey
    for storey_name, count in furniture_count_per_storey.items():
        print(f"Number of furniture on {storey_name}: {count}")

    # Print the number of furniture items not assigned to any storey
    print(f"Number of furniture items not assigned to any storey: {unassigned_furniture_count}")

    # Print the total count for verification
    total_furniture_count = sum(furniture_count_per_storey.values()) + unassigned_furniture_count
    print(f"Total number of furniture items: {total_furniture_count} (should match 1633)")

# Example usage of the function to print the results
print_furniture_count()
