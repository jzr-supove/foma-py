# foma-py
Python bindings for Foma

This is a foma interface implemented in Python. Requires libfoma installed.

## Installation

From PyPI:

    pip install foma

From source:

    git clone https://github.com/GooDeeJaY/foma-py.git
    cd foma-py
    python -m pip install .

## Basic usage

```python3
from foma import FST

fst = FST.load("path_to_model")

fst.apply_up("example")
fst.apply_down("example")
```

## Other modules:

### attapply

This is a stand-alone Python utility for reading AT\&T files and applying transductions.  Useful for minimizing dependencies. Also supports weighted transducers, in which case `apply()` returns output strings in least-cost order.

*TODO: Add basic usage*

### phonrule

This is a simple helper tool for debugging foma-scripts that are sequences of phonological rules meant to apply in a certain order.
It assumes a grammar is written as a sequence of define-statements and ordered rewrite-rules combined with a chain-statement (simulating composition of the rules). It then passes words from STDIN through the sequence of transducers and prints a decorated output to STDOUT where rules that fire are shown between brackets.

<!--
Example:

```
# myscript.foma
def  ARule a -> b || c _ d; # Rule one
def  BRule b -> c ||   _ d; # Rule two
chain ARule, BRule
```

We can now run the following, passing the word `cad` through the two transducers and tracing the rule actions:

```
$echo "cad" | python phonrule.py myscript.foma
```

and the output is

```
cad[ARule|Rule one]cbd[BRule|Rule two]ccd
```
-->

*TODO: Add basic usage*

### foma2js

This is a port of `foma/contrib/foma2js.perl` to Python 3. Get the help using `foma2js.py -h`. Everything else like in the original program.

*TODO: Add basic usage*

---

Forked from [mhulden/foma/python](https://github.com/mhulden/foma/tree/master/foma/python)
