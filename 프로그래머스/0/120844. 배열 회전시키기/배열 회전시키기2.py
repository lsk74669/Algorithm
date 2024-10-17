from collections import deque

def solution(numbers, direction):
    q = deque(numbers)
    
    if direction == 'right':
        q.appendleft(q.pop())
    else:
        q.append(q.popleft())
    return list(q)
