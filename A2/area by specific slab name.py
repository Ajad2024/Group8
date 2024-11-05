 import bpy

target_name = "IfcSlab/Geschossdecke:331001, Floor, 100mm:2445465"
total_area = 0.0

for obj in bpy.context.scene.objects:
    if obj.name == target_name:
        if obj.type == 'MESH':
            slab_area = sum([face.area for face in obj.data.polygons])
            total_area += slab_area
            print(f"Area of IfcSlab '{obj.name}': {slab_area:.2f} square meters")

print("\nTotal area of the specific IfcSlab:", total_area, "square meters")

