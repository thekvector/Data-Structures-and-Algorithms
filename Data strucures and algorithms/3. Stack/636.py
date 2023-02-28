"""
On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.

"""

"""
Intuition:
Create a cache for all of the functions ordered 1 to n. Create a stack to hold the functions when they are being called. When a function is ended, pop from the stack and find the time it took for the function. Add that time into the cache. 
Remove that time from the cache of the top function id in the stack because it was not being used during the time the current function was being called."""

class Solution:
    def exclusiveTime(self, n: int, logs):
        stack = []
        sol = [0 for i in range(n)]
        for log in logs:
            id, check, pos = log.split(':')
            id = int(id)
            pos = int(pos)
            if check == 'start':
                stack.append((id, pos))
            else:
                id, start = stack.pop()
                time = pos-start + 1
                sol[id] += time
                if stack:
                    sol[stack[-1][0]] -= time
        return sol

s = Solution()
print(s.exclusiveTime(n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]))