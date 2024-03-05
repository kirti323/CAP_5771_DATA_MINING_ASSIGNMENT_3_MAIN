# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative hierarchical clustering creates clusters gradually by merging or splitting them according to distance measures. K-means clustering assigns points to the closest cluster center, which can bias the results if there are outliers."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means clustering can give different outcomes due to random starting points, while Agglomerative hierarchical clustering consistently gives the same result because it follows a set process."
    
    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "K-means is faster and uses less memory than agglomerative hierarchical clustering, making it a very efficient clustering method. However, other algorithms like the leader algorithm also exist."
    
    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "Splitting into two clusters reduces errors by having two centers, which shortens the distance to the nearest center."
    
    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Sum of squared errors (SSE) shows how tight clusters are: lower SSE means tighter clusters, and vice versa."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "For k-means, the sum of squares between (SSB) indicates how separate the clusters are: higher SSB means more separation, and the opposite is also true."
    
    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "In k-means, making clusters tighter (cohesion) doesn't automatically mean they're more spread out (separation)."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "In k-means, the total sum of squares (TSS) is the sum of SSE and SSB, and remains constant throughout the clustering process."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] ="SSB measures how far apart clusters are, and SSE shows how tight a cluster is. So, as clusters get tighter (more cohesive), SSE goes down and SSB goes up."
    
    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The figure shows that clusters are too distant from the centroid to pull points from others."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The figure indicates that because the shaded areas are near each other, the clusters will include points from both areas."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The centroid at 12.5 is too distant from all points, leaving all other clusters empty."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "(R^2)*4"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*((a*a) + (b*b) + (c*c))"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "4*((R^2) + ((R/2)^2))"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Since A and B each have 100 points at equal distances, one centroid will move towards A. The right side of B, with two-thirds of it, will have two centroids. Circle C, with 100,000 points and equally close to B, will definitely attract a centroid because of its stronger pull, even if it didn't initially. The even distribution of points in A and B means they should each get a centroid due to their similar attraction."
    
    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The centroid will remain at A because of its points and no stronger pull elsewhere. C's strong pull will draw one centroid from B, so each of the three circles will end up with one centroid each."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Since A and B are near each other and far from C, their points will go to A's centroid. C's points will split between two centroids, each getting 50,000 points. With A and B having equal points, their centroid will shift between them. The centroids in C will spread out a bit but remain in C, each holding half the points."
    
    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group A', 'Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "A and B can be combined because the nearest point in A to the nearest point in B has the shortest distance between them."

    # type: set
    answers["(b)"] = {'Group A', 'Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "A and C can be joined because the farthest point in A to the farthest point in C is the shortest distance for a complete link."
    
    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'B', 'C', 'E', 'F', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(a) boundary"] = {'D', 'G'}

    # type: set
    answers["(a) noise"] = {'A', 'H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','D','E','F','G'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'I', 'G', 'J', 'E', 'M', 'B', 'L', 'F', 'D', 'C'}

    # type: set
    answers["(c)-a boundary"] = {'A', 'H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'G', 'I', 'H', 'J', 'E', 'M', 'B', 'D', 'F', 'L', 'C'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 is most mixed, with an even spread of categories, giving it the highest entropy."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 has low entropy because most of its points are in one category, making it very uniform." 
    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Two diagonal entries are bluer and clearer, showing that clusters B and C are tighter than A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The first and third rows match clusters A and C because their off-diagonal colors vary, showing different distances to all other clusters. A is closest to C, then B, and farthest from D; C follows a similar pattern. The second row is for cluster B, equidistant to A and C (green), with the greatest distance being red. The fourth row is for D, equally far from A and C (yellow), with the farthest distance from B shown in red."
    
    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Two diagonal entries are bluer and clearer than the others, showing that clusters B and C are tighter than A and D."
    
    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "1. Rows 1 and 4, with fuzzier diagonals, show different colors, meaning each cluster is a unique distance away (e.g., Cluster A is closest to B, then C, and farthest from D, with no two clusters at the same distance from A). 2. Rows with clearer diagonals show two identical colors (aside from the diagonal), indicating equal distance to two clusters and the greatest distance from another (e.g., B is equally distant from A and C but farthest from D)."
    
    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Two diagonal entries are bluer and sharper, showing clusters B and C are tighter than A and D."
    
    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "All rows show two similar and one different off-diagonal colors, meaning each cluster is closer to two others and farther from one (e.g., B is equally close to A and C, but farther from D)."
    
    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "A less sharp diagonal entry means the cluster is not very tight. Different colors in off-diagonal entries show varying distances to other clusters (nearest to B, then C, and farthest from A)."
    
    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "A sharper diagonal entry shows the cluster is tight. Two out of three off-diagonal entries matching in color mean it's closer to two clusters (A and C, despite fuzzier lines with A) and farthest from another (D)."
    
    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "A clearer diagonal entry suggests the cluster is cohesive. Two of the off-diagonal entries being the same color means it's closer to two clusters (A and C, even if the line with A is less clear) and farthest from another (D)."
    
    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "The cluster is closest to A, next closest to C, and farthest from B, with its tightness indicated by the varying colors for each distance."
    
    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['Hierarchical', 'Partial', 'Overlapping']

    # type: list
    answers["(b)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: list
    answers["(c)"] = ['Partitional', 'fuzzy', 'complete']


    # type: list
    answers["(d)"] = ['Hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(e)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Letter grades are unique, non-overlapping categories, with each student getting one grade per class, ensuring every student gets a grade."
    
    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN suits (b) since the points in the nose, eyes, and mouth are closer together, allowing it to identify these areas. In (a), dense noise overpowers the patterns, causing DBSCAN to miss the nose, eyes, and mouth."
    
    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means fits (b) if set to 4 clusters, including sparse points, but fails for (a)."
    
    # type: string
    answers["(c)"] = "Use the inverse of density as the new density measure for running DBSCAN."
    
    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
