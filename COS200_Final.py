# Variables "Area", "S1_Detail", "S2_Detail", "Max Height" are defined outside object

import rhinoscriptsyntax as rs
import ghpythonlib.components as ghp
import random as r
import Rhino

# Create Empty Point List
points = []
#points = ghp.Populate2D(Area, Detail, 1)
#cornerPoints = ghp.ControlPolygon(Area)[1]

SL = ghp.SegmentLengths(Area)

side_len1 = round(float(SL[0]))
side_len2 = round(float(SL[2]))
#print(side_len1, side_len2)

#side_len1/S1_Detail

# Creating Point Array
for e in range(int(S2_Detail)+1):
    for i in range(int(S1_Detail)+1):
        points.append(rs.CreatePoint((side_len1/S1_Detail*i),side_len2/S2_Detail*e,0))

#points.append(rs.CreatePoint(1,1,1))
#pList = ghp.Merge(points, cornerPoints)

# Setting Base Thickness
rs.MoveObjects(points, ghp.UnitZ(5))

# Randomizing Heights
for point in points:
    rs.MoveObject(point, ghp.UnitZ(r.randint(5,10)))

# Proper U-Count
UC = 10

surface = ghp.SurfaceFromPoints(points, UC, True)