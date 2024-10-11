## BIManalyst Group8
## Use case: Space Management
We have chosen the Use Case “Space management” with special emphasis on a gross floor areas. Planning gross floor areas in the early stages of a project is essential for several reasons, as it directly impacts the overall design, functionality, cost, and success of the development. With this information the stakeholder might decide whether or not to proceed with a project and see how profitable it might be.
The claim
To efficiently allocate and manage the available gross floor area (GFA) while ensuring optimal utilization of furniture in a given space. The goal is to maximize productivity, ensure regulatory compliance, and maintain a comfortable and functional environment. The claim of gross floor area (GFA) and furniture management relies on comprehensive data from floor plans, furniture inventories, space utilization metrics, regulatory requirements, and cost factors. 


## Bim Purpose and what does our script try to identify?
BIM allows for more precise planning, visualization, and management of building spaces by offering a highly detailed, data model of the building.  We wanted to dive into the organizational area’s aspects of the IFC-file. By doing this we want to make a use case for the architects, stakeholders and engineers, planning provides an early opportunity for value engineering—optimizing costs without sacrificing quality. By understanding the GFA early, the team can explore alternative design or material choices that reduce costs while maintaining functionality and aesthetics and they can be access to all the important areas information in the IFC.  The idea is that the Use Case will provide simple and understandable floor areas details, dimensions and the furniture occupancy. Contractors can have the information that helps in managing costs by allowing developers to adjust designs based on budget constraints. In large-scale projects, proper GFA planning allows developers to break the project into manageable phases. This ensures that each phase is aligned with market demand and that construction can proceed without interruptions. 

## How does our script address this problem?
Our plan is to make a script in order to analyze the gross floor’s areas and office areas, as well as identifying furniture areas, in this case desks in any project by using IFCOpenShell. Our current script focuses on GFA and desks in order to areas. By calculating these areas/occupancy the contractor can decide and analyze if the space is optimized or if he wants to change the offices spaces and their configuration. The script defines a condition which can later be changed by the operator. Originally this condition says that if the recess is smaller than 0.5m^2 it should be drilled after hardening. As the assignment goes on, this script will develop and look at much more aspects of the IFC file.

## What IFC concepts have we used in our scripts?
We have mainly focused on IfcObjectDefinition and IfcPropertyDefinition in order to extract the values for the different elements in the model. This is done in order to define which objects we want to analyze and use their properties to satisfy our use case.
 
## What disciplinary analysis does it require?
In our project we are focused on gross floor areas, and work offices areas optimization. We are interested in design elements, architectural elements and space definitions. So, with this use case we will take some advantages on our future as a Architectural Engineering students. n.

## What use cases must be done before we can start our use case?
All site analysis, as well as structural analysis, must be defined and pre-designed. For good space management, there is also need that lightning analyzes is determined, to define the workplaces and the best spaces with lighting, as well the energy use case with regards to ventilation.

## What is the input data for our use case?
Space Utilization Data, Employee or User Data and Inventory Data.

## What other use cases are waiting for ours to be completed?
DesignReviewing, Build and operate.

<<<<<<< HEAD
![diagram](https://github.com/user-attachments/assets/fee9b707-b160-4ce1-8003-27b01b9902d4)
