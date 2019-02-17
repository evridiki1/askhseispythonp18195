def max_subarray(A):
     max_ending_here = A[0]
     startOld = start = end = max_so_far = 0
     for i, x in (zip (range (1, len (A)), A[1:])):
        max_ending_here_old = max_ending_here
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        if max_ending_here < 0:
              start = i + 1
        elif max_ending_here != max_ending_here_old:
             startOld = start
             end = i
     newarr=[]
     for i in range(startOld,end+1):
        newarr.append(A[i])

     result = str(max_so_far)
     result = result + ': '
     result = result + str(newarr)
     return result 
     
