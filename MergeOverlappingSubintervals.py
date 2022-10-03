class Solution:
    def merge(self, inte: List[List[int]]) -> List[List[int]]:
        inte.sort()
        res=[inte[0]]
        
        for start,end in inte[1:]:
            if start > res[-1][1]:
                res.append([start,end])
            elif end >res[-1][1]:
                res[-1][1]=end
        return res