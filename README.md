1. BIManalyst Group 08 
2. Focus Area Architecture-Doors
3. Checked- Number Of Doors on the whole project and also the How many types of doors are present on the Building.

4. Inside the report named CES_BLD_24_06_ARC-There was no clear Number about Total door and also not mention the Door types.
   But we tried to figure out the number of these two things and we run the below script for find out the IfcDoor and IfcDoorType.
5. Script-1 -Number of total Doors

import ifcopenshell

from bonsai.bim.ifc import IfcStore

file = IfcStore.get_file()

things = file.by_type('IfcDoor')

print("Number of Total Door",len(things))

Result- Number of Total Door 664

Script-2 -Number of total Doors Type

import ifcopenshell

from bonsai.bim.ifc import IfcStore

file = IfcStore.get_file()

things = file.by_type('IfcDoor')

print("Number of Total Door",len(things)) 

Result- Number of Total Door Type 33

Our Script find out the number of Doors and Doors Type Which 

were named as IfcDoor and IfcDoorType only.