# import sys
# from collections import deque

# N = int(sys.stdin.readline())
# q = deque()

# for _ in range(N):
#     command = list(map(int, sys.stdin.readline().split()))
    
#     if command[0] == 1:
#         q.appendleft(command[1])
    
#     elif command[0] == 2:
#         q.append(command[1])
    
#     elif command[0] == 3:
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q.popleft())
    
#     elif command[0] == 4:
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q.pop())

#     elif command[0] == 5:
#         print(len(q))
    
#     elif command[0] == 6:
#         if len(q) == 0:
#             print(1)
#         else:
#             print(0)
    
#     elif command[0] == 7:
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q[0])
    
#     elif command[0] == 8:
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q[-1])


#################코드 리팩토링#################

'''
파이썬 라이브러리 사용하지 않고 문제풀이
'''
        
import sys

class Deque:
    def __init__(self):
        self.MAX_SIZE = 100000
        self.deq = [0] * self.MAX_SIZE
        self.front = 0
        self.rear = 0

    # command 1
    def add_front(self, x):
        self.front = (self.front - 1 + self.MAX_SIZE) % self.MAX_SIZE
        self.deq[self.front] = x
    
    # command 2
    def add_rear(self, x):
        self.deq[self.rear] = x
        self.rear = (self.rear + 1) % self.MAX_SIZE
    
    # command 3
    def del_front(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.deq[self.front])
            self.front = (self.front + 1) % self.MAX_SIZE

    # command 4
    def del_rear(self):
        if self.is_empty():
            print(-1)
        else:
            self.rear = (self.rear - 1 + self.MAX_SIZE) % self.MAX_SIZE
            print(self.deq[self.rear])
    
    # command 5
    def get_count(self):
        print((self.rear - self.front + self.MAX_SIZE) % self.MAX_SIZE)

    # command 6
    def is_empty(self):
        return self.rear == self.front
    
    # command 7
    def get_front(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.deq[self.front])
    
    # command 8
    def get_rear(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.deq[(self.rear - 1 + self.MAX_SIZE) % self.MAX_SIZE])

def main():
    dq = Deque()
    N = int(sys.stdin.readline())

    for _ in range(N):
        command = list(map(int, sys.stdin.readline().split()))

        if command[0] == 1:
            dq.add_front(command[1])
        
        elif command[0] == 2:
            dq.add_rear(command[1])
        
        elif command[0] == 3:
            dq.del_front()
        
        elif command[0] == 4:
            dq.del_rear()
        
        elif command[0] == 5:
            dq.get_count()
        
        elif command[0] == 6:
            if dq.is_empty() == True:
                print(1)
            else:
                print(0)
        
        elif command[0] == 7:
            dq.get_front()
        
        elif command[0] == 8:
            dq.get_rear()
        
if __name__ == '__main__':
    main()