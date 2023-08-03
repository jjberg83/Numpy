import numpy as np

theOriginal = np.array([1,2,3,4])
theAssignment = theOriginal
theCopy = theOriginal.copy()
theView = theOriginal.view()

theAssignment[1] = 22
theCopy[2] = 33
theView[3] = 44

print(id(theOriginal), "theOriginal", theOriginal, "base:", theOriginal.base)
print(id(theAssignment), "theAssignment", theAssignment, "base:", theAssignment.base)
print(id(theCopy), "theCopy", theCopy, "base:", theCopy.base)
print(id(theView), "theView", theView, "base:", theView.base)