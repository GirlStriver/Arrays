class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      
        for row in range(len(matrix)):
            if matrix[row][0] > target:
                break
            if matrix[row][-1] < target:
                 continue
        
            l,r=0,len(matrix[row])-1
            
            while r >= l:
                mid=(r + l) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    r=mid - 1
                else:
                    l=mid + 1
            return False
                    
                    
                
                
                

               