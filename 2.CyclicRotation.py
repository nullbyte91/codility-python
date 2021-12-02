def solution(A, K):
    len_a = len(A)
    new_array = [0] * len_a
    for index in range(len_a):
        new_index = (index + K) % len_a
        new_array[new_index] = A[index]
    return new_array