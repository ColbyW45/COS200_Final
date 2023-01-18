# Note: Variables "Area", "S1_Detail", "S2_Detail", "Max Height" are defined outside python runtime object

# Parametric Metal Plate Thing

import rhinoscriptsyntax as rs
import ghpythonlib.components as ghp
import random as r

# Create Empty Point List
points = []

SL = ghp.SegmentLengths(Area)

side_len1 = round(float(SL[2]))
side_len2 = round(float(SL[0]))
#print(side_len1, side_len2)

# Creating Point Array
for e in range(int(S2_Detail)+1):
    for i in range(int(S1_Detail)+1):
        points.append(rs.CreatePoint((side_len1/S1_Detail*i),side_len2/S2_Detail*e,0))

# Setting Base Thickness
rs.MoveObjects(points, ghp.UnitZ(10))

# Randomizing Heights
for point in points:
    rs.MoveObject(point, ghp.UnitZ(r.randint(2,Max_Height)))

# Determine U-Count
if S1_Detail > S2_Detail:
    a = S1_Detail
else:
    a = S2_Detail

UC = a + 1

# Create Top Surface
top_srf = ghp.SurfaceFromPoints(points, UC, True)

# Makeing Surface Object Solid
output = ghp.Extrude(top_srf, ghp.Negative(ghp.UnitZ(2)))