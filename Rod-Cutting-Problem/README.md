# Given a rod length n inches adn a table of prices pi for i = 1,2,3...n, determine teh maximum revenue rn obtainable by cutting up the rod adn selling the pieces.
    # CUT-ROD (p,n)
    1. if n == 0
       2.    return 0
       3. q = - ∞ 
       4. for i = 1 to n
       5.    q = max {q,p[i] + CUT-ROD(p,n-i)}
       6. return q

    # MEMOIZED-CUT-ROD(p,n)
    1. let r[0:n] be new array 
       2. for i = 0 to n
       3.   r[i] = -∞
       4. return MEMOIZED-CUT-ROD-AUX(p,n,r)

    # MEMOIZED-CUT-ROD-AUX(p,n,r)
    1. if r[n] ≥ 0 // already have a solution for length n?
       2.    return r[n]
       3. if n == 0
       4.   q = 0
       5. else q = - ∞
       6.   for i = 1 to n // i is the position of the first cut
       7.         q = max{q,p[i] + MEMOIZED-CUT-ROD-AUX(p,n-i,r)}
       8. r[n] = q
       9. return q

    # BUTTON-UP-CUT-ROD(p,n)
    1. Let r[0,n] be a new array   // will remember solution values in r
       2. r[0] = 0
       3. for j = 1 to n // for increasing rod length j 
       4.    q = - ∞
       5.    for i = 1 to j // i is the position of the first cut 
       6.      q = max{q,p[i] + r[j-i]}
       7.     r[j] = q  // remember the solution value fo length j
       8. return r[n]


