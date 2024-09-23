import ifcopenshell

from .rules import windowRule
from .rules import doorRule
from .rules import doorType


model = ifcopenshell.open("D:/Autumn/41934/L2/CES_BLD_24_06_ARC.ifc")

windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)
