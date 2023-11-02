"""
Very simple test code to confirm functions
get_age() & is_vintage() are working
"""
from prac_06.guitar import Guitar

my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.4)
print(my_guitar)
print(f"Gibson L-5 CES get_age()    - expected 101.  Got {my_guitar.get_age()}")
print(f"Gibson L-5 CES is_vintage() - expected True. Got {my_guitar.is_vintage()}")
