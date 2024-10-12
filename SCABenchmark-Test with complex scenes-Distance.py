Expression_list=["regions","geometrical shapes"]
Expression=Expression_list[1] # choose the "expression" dimension

polygon=[]
polygon.append("(0,0)")
# Point 1-7
polygon.append("(17,9)")
polygon.append("(22,10)")
polygon.append("(24,8)")
polygon.append("(25,3)")
polygon.append("(28,8)")
polygon.append("(61,4)")
polygon.append("(63,8)")
# Line 8-12
polygon.append("(19,9), (21,7), (24,6), (28,6)")
polygon.append("(36,6), (38,5), (41,2)")
polygon.append("(39,15), (41,15), (42,14)")
polygon.append("(47,1), (48,4), (48,6)")
polygon.append("(61,9), (65,7), (66,8)")
# Polygon 13-18
polygon.append("(3,26), (6,24), (10,24), (11,26), (9,31), (6,32), (4,30), (3,26)")
polygon.append("(6,23), (12,23), (14,26), (8,29), (6,23)")
polygon.append("(5,40), (8,38), (10,40), (9,48), (6,46), (4,43), (5,40)")
polygon.append("(11,41), (12,39), (15,41), (14,46), (11,47), (10,45), (11,41)")
polygon.append("(17,37), (18,38), (24,36), (31,35), (30,32), (27,31), (22,30), (19,33), (17,37)")
polygon.append("(25,36), (28,37), (31,37), (35,36), (36,34), (32,33), (28,33), (25,36)")
# Polygon 19-24
polygon.append("(19,26), (20,24), (22,23), (25,25), (26,27), (22,28), (19,26)")
polygon.append("(18,26), (19,23), (22,21), (26,20), (28,23), (27,26), (26,27), (21,28), (18,26)")
polygon.append("(18,15), (20,12), (26,11), (28,12), (27,13), (25,13), (25,15), (27,15), (28,16), (27,18), (25,19), (24,17), (22,17), (22,18), (20,19), (19,18), (18,15)")
polygon.append("(16,6), (16,5), (19,4), (25,4), (24,5), (18,6), (17,7), (16,6)")
polygon.append("(34,27), (32,24), (33,23), (34,23), (35,24), (34,27)")
polygon.append("(30,26), (31,21), (37,20), (38,23), (36,29), (33,28), (30,26)")
# Polygon 25-30
polygon.append("(36,14), (41,12), (45,12), (45,14), (43,16), (40,17), (37,16), (36,14)")
polygon.append("(35,4), (36,2), (38,2), (39,3), (37,5), (36,5), (35,4)")
polygon.append("(38,37), (39,35), (43,34), (50,34), (52,37), (50,37), (49,35), (43,36), (41,37), (39,39), (38,37)")
polygon.append("(40,40), (43,37), (48,36), (49,38), (48,39), (49,40), (48,41), (41,43), (40,40)")
polygon.append("(45,21), (47,20), (48,22), (46,22), (45,21)")
polygon.append("(44,21), (45,20), (48,19), (50,20), (49,23), (46,24), (45,23), (44,21)")
# Polygon 31-36
polygon.append("(44,3), (45,2), (48,1), (49,3), (47,5), (45,4), (44,3)")
polygon.append("(52,24), (53,22), (54,21), (56,22), (56,25), (53,25), (52,24)")
polygon.append("(57,22), (58,21), (61,21), (62,23), (61,25), (57,25), (57,22)")
polygon.append("(50,17), (50,16), (52,14), (54,14), (56,16), (56,18), (52,19), (50,17)")
polygon.append("(54,17), (54,15), (58,13), (60,14), (61,15), (58,18), (56,18), (54,17)")
polygon.append("(57,3), (61,1), (62,2), (60,4), (58,4), (57,3)")

distance_test=[]
description_g1="polygon x: "
description_g2="polygon y: "
description_p1="point x: "
description_p2="point y: "
description_l1="line x: "
description_l2="line y: "

# Distance test scenes
distance_test.append(description_g1 + polygon[32] + "; " + description_g2 + polygon[33])
distance_test.append(description_g1 + polygon[21] + "; " + description_g2 + polygon[35])
distance_test.append(description_g1 + polygon[27] + "; " + description_g2 + polygon[28])
distance_test.append(description_g1 + polygon[30] + "; " + description_g2 + polygon[29])
distance_test.append(description_g1 + polygon[1] + "; " + description_g2 + polygon[8])
distance_test.append(description_g1 + polygon[3] + "; " + description_p2 + polygon[8])
distance_test.append(description_p1 + polygon[6] + "; " + description_p2 + polygon[36])
distance_test.append(description_l1 + polygon[1] + "; " + description_g2 + polygon[5])
distance_test.append(description_l1 + polygon[8] + "; " + description_l2 + polygon[9])
distance_test.append(description_p1 + polygon[4] + "; " + description_g2 + polygon[25])

# The definition of distance relation
relation_dis=f""" 
Qualitatively describe the relation by delimiting the distance range.
    (1) Close(x,y): The length of the distance from x to y is [0,10].
    (2) Medium(x,y): The length of the distance from x to y is (11,30].
    (3) Far(x,y): The length of the distance from x to y is (30,+∞).
"""

def get_completion(prompt):
    # Connect to your LLM to get the response.
    response="LLM Response"
    return response

for i in range(10):
    coordinate=distance_test[i]
    prompt = f"""
    Your task is to determine the distance relation between two closed {Expression} given below in the same coordinate system.
    The three kind of distance relations will be delimited with ``` tag.
    ```{relation_dis}```.
    The two {Expression} are points or lines or polygons that will be given their position by coordinates: {coordinate}.
    Points are given a coordinate. Lines and polygons are given the coordinates of each vertex in order, where the polygon will eventually return to the first coordinate, drawing the closed figure.
    """
    response = get_completion(prompt)