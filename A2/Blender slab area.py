import bpy

total_area = 0.0

for obj in bpy.context.scene.objects:
    if "IfcSlab" in obj.name:
        if obj.type == 'MESH':
            slab_area = sum([face.area for face in obj.data.polygons])
            total_area += slab_area
            print(f"Area of IfcSlab '{obj.name}': {slab_area:.2f} square meters")

print("Total area of all IfcSlab elements:", total_area, "square meters")
