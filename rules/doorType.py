import ifcopenshell

def checkRule(model):
    things = model.by_type('IfcDoorType')

    result  ="Number of Total Door Types",len(things)

    return result
