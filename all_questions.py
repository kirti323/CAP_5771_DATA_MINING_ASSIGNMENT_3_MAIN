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
    answers["(a) explain"] = "Group A and B can be merged since the rightmost point of A and leftmost point of B has the smallest single link distance."

    # type: set
    answers["(b)"] = {'Group A', 'Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ".Group A and C can be merged since the rightmost point of A and farthest point of C has the smallest complete link distance."

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
    answers["(a) explain"] = "Cluster 4 has highest entropy due to more even distribution of categories."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 has low entropy due to the unequal distribution.The vast majority of its data points fall into a single category, making it highly homogeneous." 
    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Two diagonal entries are more blue and crisp than the other two, indicating that two clusters (B and C) have higher cohesion than the other two (A and D)."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The first and third rows correspond to clusters A and C. This is because the colors of the off-diagonal entries for these two rows are all different, indicating the different distances between clusters A (or C) and all other clusters (i.e., A is closest to C (blue off-diagonal), followed by B (green off-diagonal), and is the furthest from D (yellow off-diagonal); similar explanation for C). Row 2 corresponds to cluster B. Distances to A and C are the same (green off-diagonal), and the furthest distance from A is the red one. Row 4 corresponds to cluster D. Distances from A and C are the same (yellow off-diagonal), but the furthest distance from B is red off-diagonal."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Two diagonal entries are more blue and crisp compared to the other two,  indicating two clusters have better cohesion (B and C) than the other  two (A and D)"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "1. Rows with less crisp diagonal entries (rows 1 and 4) have all  different colors, indicating that all other clusters have different  distances from these clusters (e.g: Cluster A is the nearest to B,  followed by C and then D, no 2 clusters have same distance to cluster A).  2. Rows with more crisp diagonal entries have 2 same colors (other than  the diagonal), indicating that it has same distance to 2 clusters,  and is the furthest from 1 cluster (e.g: B’s distance to A and C is  similar, but is the furtherst from D)."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Two diagonal entries are more blue and crisp compared to the other two,  indicating two clusters have better cohesion (B and C) than the other  two (A and D)."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "All rows have two similar and 1 different colors off diagonals entries.  This indicates each cluster has two other clusters relatively closer  to it than the remaining 1 cluster (e.g: B is similarly close to A and  C compared to with D."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Diagonal entry is less crisp, meaning the cluster is less cohesive.  All off- diagonal entries have different colors, indicating all  other clusters have different distances from is (closest to B,  followed by C, and furthest from A)."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "Diagonal entry is more crisp, indicating the cluster is cohesive.  2/3 off-diagonal entries have the same color, indicating 2 other  clusters are closer to it (A and C, eventhough the off-diagonal  indicating distances with A is less crisp), and is the furthest  from 1 other cluster (D)."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Diagonal entry is more pronounced, indicating that the cluster is cohesive.  Two-thirds of the off-diagonal entries have the same color, indicating that two other clusters are closer to it (A and C, despite the fact that the off-diagonal indicating distances with A is less crisp), and it is the furthest from one other cluster (D)."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "The cluster is nearest to A, then to C, and farthest from B, and it's more tightly-knit, shown by the different colors for each distance"
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
    answers["(e) explain"] = "Letter grades are distinct categories that do not overlap (exclusive), each student receives only one grade per class (exclusive), and all students in the class will receive a grade (complete)."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN can work only for (b) because in (b) the points in the nose,  eyes, and mouth are much closer together than the points between  these areas, and DBSCAN could distinguish these areas. For (a),  the noise is much denser than the interest patterns, so the nose,  eyes, and mouth will be eliminated by DBSCAN."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means can work for (b) as long as the number of clusters  was set to 4, although the lower density points would also  be included. K-means does not work for (a)."

    # type: string
    answers["(c)"] = "Consider reciprocal of density as the next density and run DBSCAN on it."

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
