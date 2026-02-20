import math

def cosineSimilarity(M, a, b, I):
    dot = 0
    normA = 0
    normB = 0

    for i in range(0, I):
        dot = dot + M[a][i] * M[b][i]
        normA = normA + M[a][i] * M[a][i]
        normB = normB + M[b][i] * M[b][i]

    if normA == 0 or normB == 0:
        return 0

    return dot / (math.sqrt(normA) * math.sqrt(normB))


def consineSimilarity(M, a, b, I):
    return cosineSimilarity(M, a, b, I)


def findTopK(M, User, friends, nbUser, I, K):
    list = []

    for sUser in range(0, nbUser):
        if sUser != User and sUser not in friends[User]:
            s = consineSimilarity(M, User, sUser, I)
            list.append((sUser, s))

    list.sort(key=lambda x: x[1], reverse=True)
    return list[:K]


def collaborativeFiltering(M, User, topK, I):
    list = []

    for i in range(0, I):
        if M[User][i] == 0:
            sum = 0
            count = 0

            for (sUser, sim) in topK:
                if M[sUser][i] > 0:
                    sum = sum + M[sUser][i]
                    count = count + 1

            if count > 0:
                predicted = sum / count
                list.append((i, predicted))

    list.sort(key=lambda x: x[1], reverse=True)
    return list


def recommendationByCommonInterests(M, User, friends, nbUser, I, K):
    topK = findTopK(M, User, friends, nbUser, I, K)
    
    if len(topK) == 0 or topK[0][1] == 0:
        return [], []

    collaborativeFiltering_result = collaborativeFiltering(M, User, topK, I)
    return topK, collaborativeFiltering_result


# ------------------------------------------------------------------------------------------
#                                                 Test 
# ------------------------------------------------------------------------------------------------


def test_1_normal():
    print("------------------------ TEST 1 (Normal case) ----------------------------------------")

    print("""
                [Description]
                This is a non-edge test case.
                We consider one target user 0 and four other users: 1, 2, 3, 4.
                There are 6 interests in total.
                We suppose 2 is next most similar, 3 is 0's friend
    """)

    
    interests = ["Music", "Sports", "Tech", "Fashion", "Travel", "Food"]

    
    M = [
        [10,   0,    8,   0,     5,    0],  
        [ 9,   0,    7,   1,     4,    6], 
        [ 6,   2,    8,   0,     5,    1], 
        [10,   0,    8,   0,     5,    9],  
        [ 0,  10,    1,   8,     0,    0],  
    ]

    User = 0
    nbUser = 5
    I = 6
    K = 2

    friends = [set() for _ in range(nbUser)]
    friends[0].add(3)  

    
    print(f"Interests: {interests}")
    for u in range(nbUser):
        print(f"User {u}: {M[u]}")

    print("")  
   
    for v in range(1, nbUser):
        sim = cosineSimilarity(M, 0, v, I)
        print(f"Similarity(User0, User{v}) = {sim:.4f}")

    print("") 

  
    topK, rec = recommendationByCommonInterests(M, User, friends, nbUser, I, K)

    
    if len(topK) > 0:
        best_interest_index = rec[0][0]
        most_similar_user = topK[0][0]
        print(f"TopK most similar (not friends): User{most_similar_user}")
    else:
        print("There is sth wrong")

    
    if len(rec) > 0:
        best_interest_name = interests[best_interest_index]
        print(f"The most recommended interest is: {best_interest_name}")
        
    else:
        print("There is sth wrong")

    print("")  










def test_2_K_zero():
    print("------------------------------ TEST 2 ( K = 0) --------------------------------")


    interests = ["Music", "Sports", "Tech", "Fashion", "Travel", "Food"]

    M = [
        [10,   0,    8,   0,     5,    0],
        [ 9,   0,    7,   1,     4,    6],
        [ 6,   2,    8,   0,     5,    1],
        [10,   0,    8,   0,     5,    9],
        [ 0,  10,    1,   8,     0,    0],
    ]

    User = 0
    nbUser = 5
    I = 6
    K = 0

    friends = [set() for _ in range(nbUser)]
    friends[0].add(3)

    print(f"Interests: {interests}")
    for u in range(nbUser):
        print(f"User {u}: {M[u]}")

    print("")

    for v in range(1, nbUser):
        sim = cosineSimilarity(M, 0, v, I)
        print(f"Similarity(User0, User{v}) = {sim:.4f}")

    print("")

    topK, rec = recommendationByCommonInterests(M, User, friends, nbUser, I, K)

    if len(topK) > 0:
        most_similar_user = topK[0][0]
        print(f"TopK most similar (not friend): User{most_similar_user}")
    else:
        print("TopK most similar (not friend) null")

    if len(rec) > 0:
        best_interest_index = rec[0][0]
        best_interest_name = interests[best_interest_index]
        print(f"The most recommended interest is: {best_interest_name}")
    else:
        print("The most recommended interest is null")

    print("")  










def test_3_all_candidates_are_friends():
    print("--------------------- TEST 3 (All candidates are friends) ------------------------")


    interests = ["Music", "Sports", "Tech", "Fashion", "Travel", "Food"]

    M = [
        [10,   0,    8,   0,     5,    0],
        [ 9,   0,    7,   1,     4,    6],
        [ 6,   2,    8,   0,     5,    1],
        [10,   0,    8,   0,     5,    9],
        [ 0,  10,    1,   8,     0,    0],
    ]

    User = 0
    nbUser = 5
    I = 6
    K = 2

    friends = [set() for _ in range(nbUser)]
    friends[0].add(1)
    friends[0].add(2)
    friends[0].add(3)
    friends[0].add(4)

    print(f"Interests: {interests}")
    for u in range(nbUser):
        print(f"User {u}: {M[u]}")

    print("")

    for v in range(1, nbUser):
        sim = cosineSimilarity(M, 0, v, I)
        print(f"Similarity(User0, User{v}) = {sim:.4f}")

    print("")

    topK, rec = recommendationByCommonInterests(M, User, friends, nbUser, I, K)

    if len(topK) > 0:
        most_similar_user = topK[0][0]
        print(f"TopK most similar (not friends): User{most_similar_user}")
    else:
        print("TopK most similar (not friends) is null")

    if len(rec) > 0:
        best_interest_index = rec[0][0]
        best_interest_name = interests[best_interest_index]
        print(f"The most recommended interest is: {best_interest_name}")
    else:
        print("The most recommended interest is null")

    print("")      











def test_4_user0_all_zero():
    print("------------------------- TEST 4 : User0 interests are all 0  --------------------------")



    interests = ["Music", "Sports", "Tech", "Fashion", "Travel", "Food"]

    M = [
        [ 0,   0,    0,   0,     0,    0],
        [ 9,   0,    7,   1,     4,    6],
        [ 6,   2,    8,   0,     5,    1],
        [10,   0,    8,   0,     5,    9],
        [ 0,  10,    1,   8,     0,    0],
    ]

    User = 0
    nbUser = 5
    I = 6
    K = 2

    friends = [set() for _ in range(nbUser)]
    friends[0].add(3)

    print(f"Interests: {interests}")
    for u in range(nbUser):
        print(f"User {u}: {M[u]}")

    print("")

    for v in range(1, nbUser):
        sim = cosineSimilarity(M, 0, v, I)
        print(f"Similarity(User0, User{v}) = {sim:.4f}")

    print("")

    topK, rec = recommendationByCommonInterests(M, User, friends, nbUser, I, K)

    if len(topK) > 0:
        most_similar_user = topK[0][0]
        print(f"TopK most similar (not friends): User{most_similar_user}")
    else:
        print("TopK most similar (not friends) is null")

    if len(rec) > 0:
        best_interest_index = rec[0][0]
        best_interest_name = interests[best_interest_index]
        print(f"The most recommended interest is: {best_interest_name}")
    else:
        print("The most recommended interest is null")


    print("")  

   










def test_5_user0_all_rated():
    print("--------------------TEST 5 : User0 has already rated all interests-------------------")

    interests = ["Music", "Sports", "Tech", "Fashion", "Travel", "Food"]

    M = [
        [ 1,   2,    3,   4,     5,    6],
        [ 9,   0,    7,   1,     4,    6],
        [ 6,   2,    8,   0,     5,    1],
        [10,   0,    8,   0,     5,    9],
        [ 0,  10,    1,   8,     0,    0],
    ]

    User = 0
    nbUser = 5
    I = 6
    K = 2

    friends = [set() for _ in range(nbUser)]
    friends[0].add(3)

    print(f"Interests: {interests}")
    for u in range(nbUser):
        print(f"User {u}: {M[u]}")

    print("")

    for v in range(1, nbUser):
        sim = cosineSimilarity(M, 0, v, I)
        print(f"Similarity(User0, User{v}) = {sim:.4f}")

    print("")

    topK, rec = recommendationByCommonInterests(M, User, friends, nbUser, I, K)

    if len(topK) > 0:
        most_similar_user = topK[0][0]
        print(f"TopK most similar (not friends): User{most_similar_user}")
    else:
        print("TopK most similar (not friends) is null")

    if len(rec) > 0:
        best_interest_index = rec[0][0]
        best_interest_name = interests[best_interest_index]
        print(f"The most recommended interest is: {best_interest_name}")
    else:
        print("The most recommended interest is null")

    print("")






if __name__ == "__main__":
    test_1_normal()
    test_2_K_zero()
    test_3_all_candidates_are_friends()
    test_4_user0_all_zero()
    test_5_user0_all_rated()