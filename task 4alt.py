# (a) nested loops : O(n * m) time, O(1) extra space
common = []
for a in A:
    for b in B:
        if a == b:
            common.append(a); break
 
# (b) sort both lists and walk through them together : O(n log n + m log m) time
def common_sorted(A, B):
    A, B = sorted(A), sorted(B)
    i = j = 0; out = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]: out.append(A[i]); i += 1; j += 1
        elif A[i] < B[j]: i += 1
        else: j += 1
    return out
