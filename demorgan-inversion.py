import re

"""
De Morgan's Laws allow us to transform a single 3-CNF clause into a different form
3-CNF clauses are all (a | b | c) where a, b, and c are all a variable either negated or not negated.

(a | b | c) -> (~(~a & ~b) | c)
-> ~(~a & ~(~(~b & ~c)))
-> ~(~a & (~b & ~c))
-> ~(~a & ~b & ~c)

So therefore each clause is equivalent to ~(~a & ~b & ~c)

Additionally, we can follow the same steps with any number of conjunctions of clauses:
c1 & c2 & c3 & c4...

(c1 & c2 & c3...) == ~(~c1 | ~c2 | ~c3...)

and since each x_n clause has already has a convenient negated form (~a & ~b & ~c), we can 
convert a CNF into something like

   (x1 | ~x2 |  x3) &  (x1 | ~x2 | ~x3) & (~x1 | ~x2 |  x3) & (~x1 | ~x2 | ~x3) ->

~((~x1 &  x2 & ~x3) | (~x1 &  x2 &  x3) |  (x1 &  x2 & ~x3) |  (x1 &  x2 &  x3))

Therefore, any regex that encodes the term 

(~x1 & x2 & ~x3) | (~x1 & x2 & x3) | (x1 & x2 & ~x3) | (x1 & x2 & x3)

will fail to match any satisfying arrangements of values!




We can construct this regex using a bunch of lookaheads relatively easily.

If we have v variables, the solution is in the format [tf]{v}.

This ensures that there aren't too many or two few variables. 

Then, we can construct each clause by having three lookaheads

Each of these lookaheads can be constructed for a variable x_n by repeating the . (any char) 
n - 1 times, and then putting t or f depending on whether the variable is negated or not



For example, a single SAT clause that has the standard format of [-2, 4, 3] would be made as follows:
First, invert each of the terms since we're working in our De Morgan transformation of the CNF form
So we get [2, -4, 3]
Then we can construct our lookaheads: 

In this case, the first term is a non-negated 2, so we can make it into the lookahead (?=.t)
The next one becomes (?=...f)
Finally, the third term becomes (?=..t)

Appending these all together gives us our equivalent of an AND operator
(?=.t)(?=...f)(?=..t)

And if this is our only clause, we could finish right here by appending our variable count and anchors, giving us:
^(?=.t)(?=...f)(?=..t)[tf]{4}$

This is our first regex SAT test!
"""