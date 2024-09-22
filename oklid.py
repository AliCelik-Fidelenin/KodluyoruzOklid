import math

# Function that calculates Euclidean distance

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Identifying points in 2D space
points = [(1, 2), (3, 4), (6, 8), (5, 1)]

# Calculation of distances between all points
distances = []

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Finding the minimum distance
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")