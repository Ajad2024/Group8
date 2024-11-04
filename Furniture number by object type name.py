import ifcopenshell


ifc_file_path = "D:\\BIM\\CES_BLD_24_10_ARC.ifc"  

ifc_file = ifcopenshell.open(ifc_file_path)


furniture_items = ifc_file.by_type("IfcFurniture")


target_object_type = "Schreibtisch-Kombination-02 mit PC:Typ1"


specific_item_count = 0


for furniture in furniture_items:
    if getattr(furniture, 'ObjectType', '') == target_object_type:
        specific_item_count += 1


print(f"Total number of '{target_object_type}' items: {specific_item_count}")
