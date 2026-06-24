class Solution(object):
    def findDegrees(self, matrix):
        Output = []
        for i in range (len(matrix)):
            count = 0
            for j in range (len(matrix[i])):
                if(matrix[i][j]==1):
                    count = count +1
            Output.append(count)
        return Output
        
        
        