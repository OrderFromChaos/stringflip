# stringflip

https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

Why do I use the method I use on vks_algebra? Well, you could read the string forward and flip them individually as you go, but I came upon an insight that helped make it significantly faster:

I'm rewriting the string a lot of unnecessary times; what if my strings are a million long?

Let's say my flip operation adds an operator notation, like a.transpose in linear algebra. Then, a problem solution would look like this:

((A)(B))

(A.T*B.T)

(A.T*B.T).T

Interestingly, the "string flip" problem follows the same algebraic rules as transpose: (AB).T = B.T + A.T.

This made me realize that I could solve the problem as an abstract algebra problem _first_, and then actually do the string flipping at the end.

To do this, you need to 1) tokenize the string (I use the pyparsing library to do this), 2) define your algebraic computations (I create a Substr class and a function to do this), and 3) combine your final Substr results (I use __add__() and reduce() to do this).

You can see this solution in vks_algebra.py.
