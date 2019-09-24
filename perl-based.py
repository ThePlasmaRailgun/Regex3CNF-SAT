import re

# Simple encoding of 3-CNF sat
# (x1 | ~x2 | x3) & (x1 | ~x2 | ~x3) & (~x1 | ~x2 | x3) & (~x1 | ~x2 | ~x3)
sat_problem = [[1, -2, 3], [1, -2, -3], [-1, -2, 3], [-1, -2, -3]]

# Unsatisfiable SAT problem
# sat_problem = [[1, 1, 1], [-1, -1, -1]]

num_vars = max(
    [abs(x) for clause in sat_problem for x in clause]
)

num_clauses = len(sat_problem)

satis_string = (num_vars * 'x') + ';' + (num_clauses * 'x,')
regex = '^' + num_vars * '(x?)' + '.*;' + ''.join(
    '(?:' + '|'.join(
        '\\' + (str(-x) + 'x' if x < 0 else str(x))
        for x in clause) + '),'
    for clause in sat_problem)

print(regex)
print(re.match(regex, satis_string).groups())
