# Note: Variables "Surface", "Detail" are defined outside python runtime object

# Weave Generator

import rhinoscriptsyntax as rs
import ghpythonlib.components as ghp
import random as r

moveScale = 3

# Creating Point Array
DS = ghp.DivideSurface(Surface,Detail,Detail)
points = DS[0]
normals = DS[1]

# Point set 1 - White
movedPts1 = []
for i in range(len(points)):
    if i % 2 == 0:
        movedPts1.append((ghp.Move(points[i],((normals[i])*moveScale)))[0])
    
    if i % 2 == 1:
        movedPts1.append((ghp.Move(points[i],(-1*(normals[i])*moveScale)))[0])

# Point set 2 - Black
movedPts2 = []
for i in range(len(points)):
    if i % 2 == 1:
        movedPts2.append((ghp.Move(points[i],((normals[i])*moveScale)))[0])
    
    if i % 2 == 0:
        movedPts2.append((ghp.Move(points[i],(-1*(normals[i])*moveScale)))[0])

# Spline set 1
a = 0
splineOut1 = []
for e in range(Detail+1):
    temp_list = []
    
    for i in range(Detail+1):
        temp_list.append(movedPts1[i+(Detail*a)+e])
    
    a += 1
    splineOut1.append((ghp.Interpolate(temp_list,3,False,0))[0])

# Spline set 2
a = 0
splineOut2 = []
for e in range(Detail+1):
    temp_list = []
    
    for i in range(Detail+1):
        temp_list.append(movedPts2[(i*(Detail+1))+e])
    
    a += 1
    splineOut2.append((ghp.Interpolate(temp_list,3,False,0))[0])

# Pipes
splines = ghp.Merge(splineOut1,splineOut2)
Output = ghp.Pipe(splines,2,True)