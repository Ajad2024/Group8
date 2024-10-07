import ifcopenshell

def checkRule(model):
    things = model.by_type('IfcDoor')

    result  =f"Number of Total Door: {len(things)}"

    return result
    