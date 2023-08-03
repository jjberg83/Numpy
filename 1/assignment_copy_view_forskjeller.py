import numpy as np

theOriginal = np.array([1,2,3,4])
theAssignment = theOriginal
theCopy = theOriginal.copy()
theView = theOriginal.view()

theAssignment[1] = 22
theCopy[2] = 33
theView[3] = 44

print(id(theOriginal), "theOriginal", theOriginal)
print(id(theAssignment), "theAssignment", theAssignment)
print(id(theCopy), "theCopy", theCopy)
print(id(theView), "theView", theView)