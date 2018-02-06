
# coding: utf-8

# In[4]:

N = 1
X = 1
PNX = (3/4) ** 5
PN = (1/4) ** 15
NFactorial = range(16, 21)
for i in NFactorial:
    N *= i
XFactorial = range(1, 6)
for j in XFactorial:
    X *= j
Probability = ((N/X)*(PNX)*(PN))
print (Probability)

