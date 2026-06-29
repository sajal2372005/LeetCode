class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        ans = [0]*n
        for log in logs:
            func_id, action, timestamp = log.split(':')
            func_id = int(func_id)
            timestamp = int(timestamp)
            if action == "start":
                stack.append([func_id,timestamp,0])
            else:
                parent_id,parent_time,child = stack.pop()
                result = timestamp - parent_time +1
                ans[func_id] += result - child
                if stack:
                    stack[-1][2] += result
        return ans