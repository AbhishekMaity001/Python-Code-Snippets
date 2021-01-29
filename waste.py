import numpy as np
mat = np.arange(16).reshape(4,4)
print(mat)
upper = []
lower = []
for i in range(len(mat)) :
    for j in range(len(mat)) :
        if i !=j:
            # print(mat[i][j])
            if i < j :
                upper.append(mat[i][j])
            else :
                lower.append(mat[i][j])

print('-'*70)

print(upper)
upper.sort(reverse=True)
print(upper)
print(lower)
lower.sort(reverse=True)
print(lower)
ctr=0
ctr1=0
for i in range(len(mat)) :
    for j in range(len(mat)) :
        if i !=j:

            if i < j :
                mat[i][j] = upper[ctr]
                ctr+=1
            else :
                mat[i][j] = lower[ctr1]
                ctr1 += 1

print('-'*70)
print(mat)
print(mat.shape)







