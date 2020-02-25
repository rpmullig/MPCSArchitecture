# Robert Mulligan : CPU Cache Emulator

## Run Instructions

### Must run Python 3.6 or greater and llist library 

Run program with a `python3.6 cache-sim.py <flags> <setting>`

If an library/module error occurs, make sure the llist module is in the library and setup for python3.6. You may need to 
run a command like `pip install llist` or `pip3 install llist`. The library may not correspond to the right python package, 
 so run this command then `python3.6 -m pip install llist`.


## Abstract
CPU emulator capable of modeling a simplified memory hierarchy in python programming language.

1. Block placement: Where can a block be placed in cache?

2. Block identification: How is a block found if it is in cache?

3. Block replacement: Which block should be replaced on a miss?

4. Write strategy: What happens on a write?


