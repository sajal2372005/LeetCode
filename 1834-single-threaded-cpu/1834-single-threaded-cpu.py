import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        memory = []
        
        indexed_tasks = []
        for i in range(len(tasks)):
            indexed_tasks.append([tasks[i][0], tasks[i][1], i])
        indexed_tasks.sort(key=lambda x: x[0])
        
        if len(tasks) != 0:
            current_time = min(task[0] for task in tasks)
        
        task_ptr = 0
        
        while len(ans) < len(tasks):
            while task_ptr < len(indexed_tasks) and indexed_tasks[task_ptr][0] <= current_time:
                heapq.heappush(memory, (indexed_tasks[task_ptr][1], indexed_tasks[task_ptr][2]))
                task_ptr += 1
            
            
            if len(memory) > 0:
                processing_time, original_index = heapq.heappop(memory)
                
                ans.append(original_index)
                current_time += processing_time
            else:
                if task_ptr < len(indexed_tasks):
                    current_time = indexed_tasks[task_ptr][0]
        return ans
                    



        