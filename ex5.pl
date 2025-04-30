% Simple Prolog Program to define family relations

% Facts
father(john, mary).
father(john, james).
mother(susan, mary).
mother(susan, james).

% Rules
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

% Query Example: Who is Mary’s parent?
