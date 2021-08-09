#IMPORT LIBRARIES
from app import *

print("Performing some checks...")

assert does_it_fit(4,[2,0,0]) == True

assert does_it_fit(150,[10,5,0]) == False

assert does_it_fit(2000,[1,0,0]) == False

print("All systems go!")