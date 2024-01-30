vector1 = [1,2,3,4]
vector2 = [4,5,6,7]

def dot_product(vector1, vector2):
    dot_vector = 0
    for i in range(len(vector1)):
        dot_vector = vector1[i] * vector2[i] + dot_vector
    return dot_vector

print(dot_product(vector1,vector2))