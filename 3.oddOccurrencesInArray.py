def solution(A):
    len_a = len(A)
    Dict = {}
    for index in range(len_a):
        if A[index] in Dict:
            del Dict[A[index]]
        else:
            Dict[A[index]] = 1
    for key in Dict.keys():
        return key