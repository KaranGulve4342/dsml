# 10. Write a program to do the following: You have given a collection of 8
# points. P1=[2, 10] P2=[2, 5] P3=[8, 4] P4=[5, 8] P5=[7,5] P6=[6, 4] P7=[1, 2]
# P8=[4, 9]. Perform the k-mean clustering with initial centroids as m1=P1
# =Cluster#1=C1 and m2=P4=cluster#2=C2, m3=P7 =Cluster#3=C3. Answer
# the following 1] Which cluster does P6 belong to? 2] What is the
# population of a cluster around m3? 3] What is the updated value of m1,
# m2, m3?

import numpy as np

points = np.array([
    [2, 10],
    [2, 5],
    [8, 4],
    [5, 8],
    [7, 5],
    [6, 4],
    [1, 2],
    [4, 9]
])

m1 = points[0]
m2 = points[3]
m3 = points[6]

def euclidean_distance(point,centroid):
    return np.sqrt(np.sum((point-centroid)**2))

def k_mean(points,m1,m2,m3,max_iteration=10):
    for iteration in range(max_iteration):
        clusters = {1:[],2:[],3:[]}
        for point in points:
            dist1 = euclidean_distance(point,m1)
            dist2 = euclidean_distance(point,m2)
            dist3 = euclidean_distance(point,m3)
            if dist1<dist2 and dist1<dist3 :
                clusters[1].append(point)
            elif dist2<dist3:
                clusters[2].append(point)
            else:
                clusters[3].append(point)
        new_m1 = np.mean(clusters[1],axis=0) if clusters[1] else m1
        new_m2 = np.mean(clusters[2],axis=0) if clusters[2] else m2
        new_m3 = np.mean(clusters[3],axis=0) if clusters[3] else m3

        if np.allclose(new_m1,m1) and np.allclose(new_m2,m2) and np.allclose(new_m3,m3):
            break
        m1,m2,m3 = new_m1,new_m2,new_m3

        return clusters,m1,m2,m3

clusters,updated_m1,updated_m2,updated_m3 = k_mean(points,m1,m2,m3,15)

p6_cluster = None
p6 = points[5]

for clusters_id,clusters_points in clusters.items():
    for point in clusters_points:
        if np.array_equal(p6,point):
            p6_cluster  = clusters_id
            break
        if p6_cluster:
            break

# Question 2: What is the population of the cluster around m3?
print(f"1] P6 belongs to Cluster: {p6_cluster}")
population_m3 = len(clusters[3])
print(f"2] Population of Cluster 3 (around m3): {population_m3}")

# Question 3: What are the updated values of m1, m2, m3?
print(f"3] Updated values:\n   m1: {updated_m1}\n   m2: {updated_m2}\n   m3: {updated_m3}")
