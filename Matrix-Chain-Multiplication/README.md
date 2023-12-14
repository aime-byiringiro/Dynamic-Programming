    # MATRIX-CHAIN-ORDER(P)
    1. let m[1:n, 1:n] and s[1:n-1,2:n] be new tables
       2. for i = i to n        // chain lenth 1 
       3.     m[i,i] = 0
       4. for l = 2 to n         // l is the chain  length 
       5.    for i = 1 to n-l+1  // chain being at Ai
       6.       j = i + l -1    // chain ends at Aj
       7.       m[i,j] = ∞ 
       8.       for k = i to j -1     // try Ai.k Ak+1:j
       9.           q = m[i,k] + m[k+1,j] + pi-1pkpj
       10.          if q < m[i,j]
       11.             m[i,j] = q   // remember this cost 
       12.             s[i,j] = k   // remember this index 
       13. return m and s
    
    # PRINT-OPTIMAL-PARENS(s,i,j)
    1. if i == j
       2.   print"A"i
       3. else print "("
       4.    PRINT-OPTIMAL-PARENS(s,i,s[i,j])
       5.    PRINT-OPTIMAL-PARENS(s,s[i,j]+1,j)
       6.    print")
    
    # Running time: O(n^3)