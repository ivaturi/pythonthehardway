# Study drills

# Why does Python include 'object' in class definitions?

"""
This is the 'new-style' definition of a class in Python.
This was introduced in PEP 252 and PEP 253, see [1], [2], and [3].

Basically, this model is intended to unify the 'class' and 'type' concepts.
In the old-style (classic) classes, instances of classes had a different class
and type. (the type was 'instance',and the class was whatever they were instances of)

In the new-style classes, a new-style class is basically a user-defined type. This allows
us to extend built-in types by simply specifying them as the parent class. (or simply
'object', if no other parent class is required)

[1] https://www.python.org/dev/peps/pep-0252/
[2] https://www.python.org/dev/peps/pep-0253/
[3] https://docs.python.org/release/2.2.3/whatsnew/sect-rellinks.html
"""
