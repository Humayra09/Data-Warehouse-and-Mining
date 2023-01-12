import numpy as np
import math
dataset = [[185, 72], [170, 56], [168, 60], [179, 68], [182, 72], [188, 77],
           [180, 71], [180, 70], [183, 84], [180, 88], [180, 67], [177, 76]]


k = 2
cluster1 = []
cluster2 = []

centroid1 = [185, 72]
centroid2 = [170, 56]
iteration = 0


def kmeans():
    global centroid1, centroid2, centroid3, cluster1, cluster2, cluster3, iteration
    iteration = iteration + 1
    print("\nIteration ", iteration)

    for i in range(0, len(dataset)):
        a = abs(math.sqrt(
            (pow(centroid1[0] - dataset[i][0], 2)) + (pow(centroid1[-1] - dataset[i][-1], 2))))
        b = abs(math.sqrt(
            (pow(centroid2[0] - dataset[i][0], 2)) + (pow(centroid2[-1] - dataset[i][-1], 2))))
        print(a, b)

        if a > b:
            cluster2.append(dataset[i])
        else:
            cluster1.append(dataset[i])

        print(cluster1, cluster2)

    listx1 = []
    listy1 = []

    for x, y in cluster1:
        listx1.append(x)
        listy1.append(y)
    x1, y1 = listx1, listy1

    listx2 = []
    listy2 = []
    for x, y in cluster2:
        listx2.append(x)
        listy2.append(y)

    x2, y2 = listx2, listy2

    valx1 = sum(x1)/len(x1)
    valy1 = sum(y1)/len(y1)

    valx2 = sum(x2)/len(x2)
    valy2 = sum(y2)/len(y2)

    tup1 = (float("{:.2f}".format(valx1)), float("{:.2f}".format(valy1)))
    tup2 = (float("{:.2f}".format(valx2)), float("{:.2f}".format(valy2)))

    print("\nThe mean centroids are \n", tup1, "\n", tup2)

    if tup1 == centroid1 and tup2 == centroid2:
        print("\nClusters have been formed")
    else:
        centroid1 = tup1
        centroid2 = tup2

        cluster1 = []
        cluster2 = []

        kmeans()


kmeans()
