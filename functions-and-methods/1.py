def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# error: foo isn't defined outside of function

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# bar. Assignment on line 12 creates a new variable local
# to the function. This is variable shadowing.
# foo on line 12 shadows the var on line 1.