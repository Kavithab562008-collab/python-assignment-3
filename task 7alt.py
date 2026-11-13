def merge_pairwise(contacts):
    nums = [{normalise_number(p) for p in c["phones"] if normalise_number(p)} for c in contacts]
    parent = list(range(len(contacts)))          # union-find to group matching contacts
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for i in range(len(contacts)):
        for j in range(i + 1, len(contacts)):    # n(n-1)/2 comparisons
            if nums[i] & nums[j]:
                parent[find(j)] = find(i)
