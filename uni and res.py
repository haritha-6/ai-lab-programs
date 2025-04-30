def unify(x, y, s={}):
    if s is None:
        return None
    elif x == y:
        return s
    elif isinstance(x, str) and x.islower():
        return unify_var(x, y, s)
    elif isinstance(y, str) and y.islower():
        return unify_var(y, x, s)
    elif isinstance(x, tuple) and isinstance(y, tuple):
        return unify(x[1:], y[1:], unify(x[0], y[0], s))
    else:
        return None

def unify_var(var, x, s):
    if var in s:
        return unify(s[var], x, s)
    elif x in s:
        return unify(var, s[x], s)
    else:
        s2 = s.copy()
        s2[var] = x
        return s2

x = ('f', 'x', ('g', 'y'))
y = ('f', 'a', ('g', 'b'))
result = unify(x, y)
print("Unification result:", result)

def resolve(clause1, clause2):
    resolvents = []
    for literal in clause1:
        if ('~' + literal) in clause2:
            new_clause = list(set(clause1 + clause2))
            new_clause.remove(literal)
            new_clause.remove('~' + literal)
            resolvents.append(new_clause)
        elif literal.startswith('~') and literal[1:] in clause2:
            new_clause = list(set(clause1 + clause2))
            new_clause.remove(literal)
            new_clause.remove(literal[1:])
            resolvents.append(new_clause)
    return resolvents

c1 = ['A', 'B']
c2 = ['~B', 'C']
res = resolve(c1, c2)
print("Resolvents:", res)
