 # Longest-common-subsequence

    # LCS-LENGTHY(X,Y,m,n)
    1. let b[1:m,1:n] and c[0:m,0:n] be new tables
       2. for i = 1 to m 
       3.    c [i,0] = 0
       4. for j = to to n
       5.     c[0,j] = 0
       6. for i = 1 to m   // compute table entries in row-major order
       7.    for j = 1 to m 
       8.     if xi = yi
       9.       c[i,j] = c[i-1, j-1] + 1
       10.      b[i,j] = "↖︎"
       11.    elseif c[i-1,j] ≥ c[i,j-1]
       12.       c[i,j] = c[i-1,j]
       13.       b[i,j] = "↑"
       14.    els c[i,j] = c[i,j-1]
       15.       b[i,j] = "←"
       16. return c and b
    
    # PRINT-LCS(b,X,i,j)
    1. if i == 0 or j == 0
       2.    return   // the LCS has length 0
       3. if b[i,j] == "↖︎"
       4.    PRINT-LCS9(b,X,i-1,j-1)
       5.    print xi     // same as yi
       6. elseif b [i,j] == "↑"
       7.    PRINT-LCS(b,X,i-1,j)
       8. else PRINT-LCS(b,X,i,j-1)

# Running time: O(m+n) time.