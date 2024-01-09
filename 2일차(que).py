# https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3

from collections import deque

def solution(priorities, location):
    answer = 0
    idx_deque = deque([(i, priority) for i, priority in enumerate(priorities)])

    while idx_deque:
        current_process = idx_deque.popleft()
        if any(current_process[1] < priority for _, priority in idx_deque):
            idx_deque.append(current_process)
        else:
            answer += 1
            if current_process[0] == location:
                return answer
