## BIManalyst Group8

## Focus Area Architecture-Doors

## Checked- Number Of Doors on the whole project and also the How many types of doors are present on the Building.

## Inside the report named CES_BLD_24_06_ARC-There was no clear Number about Total door and also not mention How many types of Door being used. But we tried to figure out the number of these two things and we run the below script for find out the Door and Door Types.
 
## Script-1 -Number of total Doors

import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()
things = file.by_type('IfcDoor')
print("Number of Total Doors",len(things))

### Result- Number of Total Doors 664

## Script-2 -Number of total Door Types

import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()
things = file.by_type('IfcDoorType')
print("Number of Total Door Types",len(things)) 

### Result- Number of Total Door Types 33


## Our Script find out the number of Doors and Doors Type Which  were named as IfcDoor and IfcDoorType only.
