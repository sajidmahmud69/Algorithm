# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

def combinationSum (candidates, target):
   res = [] 

   def dfs (i, cur, total):
       """
       params:
        i: which candidates we are allowed to choose
        cur: list of values we have added so far [could have duplicates]
             to the current combination
        total: sum of all elements in cur
       """
       if total == target:
           res.append (cur.copy())          # don't append cur because we need to pass cur recursively and we don't want to mutate cur while doing that
           return 
       
       if i >= len (candidates) or total > target:
           return 
        
       cur.append (candidates[i])
       dfs (i, cur, total + candidates[i])
    
       cur.pop ()
       dfs (i+1, cur, total)



   dfs (0, [], 0)
   return res


# Test Code
print (combinationSum ([2, 3, 5], 5))
