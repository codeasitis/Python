# Queue
from collections import deque
num_list=deque([2,4,6,8])
num_list.append(10)
num_list.append(12)
print(num_list)
print(num_list.popleft())
print(num_list.popleft())