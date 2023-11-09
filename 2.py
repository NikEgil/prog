import matplotlib.pyplot as plt
import numpy as np

mas = np.ones((1,5))
print(mas)
a= np.array([1,2,3,4,5])

mas=np.append(mas,[a],axis=0)
print(mas)
print(np.sum(mas,axis=0))    
