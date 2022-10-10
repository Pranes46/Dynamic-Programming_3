class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)  
        
        for i in range(1,n):  #to access the row
            for j in range(n):  # to access the column
                if j ==0:   #if the j is in 0th index we are doing double check
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j+1])
                    
                elif j == n-1:  #if the j is n-1 column we are doing double check again
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j-1])  #we are taking the minimum and we are adding it to the index
                      #if j is not in both 0th index and n-1 column we are doing triple check
                else:
                     matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j-1],matrix[i-1][j+1]) #we are taking the minimum and we are adding it to the index
                        
                        
        return(min(matrix[-1]))  #returning min from the last 
                    
                    
                    