def solution(array, commands):
    result = []
    
    for command in commands:
        i, j, k = command
        sliced = sorted(array[i-1:j])
        result.append(sliced[k-1])
    
    return result