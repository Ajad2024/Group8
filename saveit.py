import ifcopenshell

from bonsai.bim.ifc import IfcStore

file = IfcStore.get_file()

things = file.by_type('IfcDoor')

print("Number of Total Doors",len(things))