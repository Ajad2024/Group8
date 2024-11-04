
import ifcopenshell


file_path = r"D:\BIM\CES_BLD_24_10_ARC.ifc"
ifc_file = ifcopenshell.open(file_path)


slab_object_type_to_find = "Geschossdecke:331001, Floor, 100mm"


slab_areas = []


for slab in ifc_file.by_type("IfcSlab"):
   
    if getattr(slab, "ObjectType", "") == slab_object_type_to_find:
       
        area = None
        for rel in slab.IsDefinedBy:
            if rel.is_a("IfcRelDefinesByProperties"):
                prop_set = rel.RelatingPropertyDefinition
                if prop_set.is_a("IfcElementQuantity"):
                    for quantity in prop_set.Quantities:
                        if quantity.is_a("IfcQuantityArea"):
                            area = quantity.AreaValue
                            break
      
        if area:
            slab_areas.append(area)
        else:
            slab_areas.append("Area not defined")


print(f"Areas of '{slab_object_type_to_find}' slabs:")
for i, area in enumerate(slab_areas, start=1):
    print(f"Slab {i}: {area} m²")
