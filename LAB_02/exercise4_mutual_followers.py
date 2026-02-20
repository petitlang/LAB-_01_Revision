# FOLLOW
def follow(FM, follower, followee):
    FM[follower - 1][followee - 1] = True

# UNFOLLOW
def unfollow(FM, follower, followee):
    FM[follower - 1][followee - 1] = False

# IS_FOLLOWING
def is_following(FM, follower, followee):
    return FM[follower - 1][followee - 1]

# GET_FOLLOWERS
def get_followers(FM, user, N):
    followers = []
    for i in range(1, N + 1):
        if FM[i - 1][user - 1] is True:
            followers.append(i)
    return followers

# GET_FOLLOWING
def get_following(FM, user, N):
    following = []
    for j in range(1, N + 1):
        if FM[user - 1][j - 1] is True:
            following.append(j)
    return following

# MUTUAL_FOLLOWS
def mutual_follows(FM, N):
    pairs = []
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if FM[i - 1][j - 1] is True and FM[j - 1][i - 1] is True:
                pairs.append((i, j))
    return pairs

# INFLUENCE_SCORE
def influence_score(FM, user, N):
    followers_count = 0
    following_count = 0

    for i in range(1, N + 1):
        if FM[i - 1][user - 1] is True:
            followers_count += 1

    for j in range(1, N + 1):
        if FM[user - 1][j - 1] is True:
            following_count += 1

    return (followers_count + following_count) / N


# Edge Case Test Sets (Exercise 4)

# situation 1: N=1 (single user, no edges) 
N1 = 1
FM1 = [[False]]

# situation 2: N=2, no one follows anyone 
N2 = 2
FM2 = [
    [False, False],
    [False, False],
]

# situation 3: N=2, one-direction follow only (no mutual) 
N3 = 2
FM3 = [
    [False, True],   # 1 -> 2
    [False, False],
]

# situation 4: N=2, mutual follow 
N4 = 2
FM4 = [
    [False, True],   # 1 -> 2
    [True,  False],  # 2 -> 1
]

# situation 5: self-follow present (diagonal True) 
# (Some systems forbid this; this case checks behavior if it exists)
N5 = 3
FM5 = [
    [True,  False, False],  # 1 -> 1
    [False, False, False],
    [False, False, False],
]

# situation 6: one user follows everyone else (star-out) 
N6 = 4
FM6 = [
    [False, True,  True,  True],   # 1 -> 2,3,4
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False],
]

# situation 7: everyone follows one user (star-in) 
N7 = 4
FM7 = [
    [False, False, False, True],   # 1 -> 4
    [False, False, False, True],   # 2 -> 4
    [False, False, False, True],   # 3 -> 4
    [False, False, False, False],
]

# situation 8: fully connected except self (dense graph) 
N8 = 4
FM8 = [
    [False, True,  True,  True],
    [True,  False, True,  True],
    [True,  True,  False, True],
    [True,  True,  True,  False],
]

# situation 9: mixed graph (multiple mutual pairs + isolated node) 
N9 = 5
FM9 = [
    [False, True,  False, False, False],  # 1 -> 2
    [True,  False, True,  False, False],  # 2 -> 1,3
    [False, False, False, True,  False],  # 3 -> 4
    [False, False, True,  False, False],  # 4 -> 3  (mutual with 3)
    [False, False, False, False, False],  # 5 isolated
]

# situation 10: boundary users only (tests index edges: 1 and N) 
N10 = 5
FM10 = [
    [False, False, False, False, True],   # 1 -> 5
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [True,  False, False, False, False],  # 5 -> 1 (mutual with 1)
]

cases = [
    ("Situation 1", FM1, N1),
    ("Situation 2", FM2, N2),
    ("Situation 3", FM3, N3),
    ("Situation 4", FM4, N4),
    ("Situation 5", FM5, N5),
    ("Situation 6", FM6, N6),
    ("Situation 7", FM7, N7),
    ("Situation 8", FM8, N8),
    ("Situation 9", FM9, N9),
    ("Situation 10", FM10, N10),
]

for name, FM, N in cases:
    print(f"\n--- {name} ---")
    print("Mutual follows:", mutual_follows(FM, N))

    # pick a few representative users: 1, middle (if exists), N
    users_to_check = {1, N}
    if N >= 3:
        users_to_check.add((N + 1) // 2)

    for u in sorted(users_to_check):
        print(f"User {u} followers:", get_followers(FM, u, N))
        print(f"User {u} following:", get_following(FM, u, N))
        print(f"User {u} influence:", influence_score(FM, u, N))