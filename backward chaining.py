def backward_chaining(fact, rules, goal):
    if goal in fact:
        return True
    for rule in rules:
        if rule[0] == goal:
            if all(backward_chaining(fact, rules, condition) for condition in rule[1]):
                fact.append(goal)
                return True
    return False

facts = ['A', 'B']
rules = [('C', ['A', 'B']),('D', ['C'])]

goal = 'D'
result = backward_chaining(facts, rules, goal)
print(f"Goal {goal} can be proved: {result}")

