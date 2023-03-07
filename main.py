from package import *
from hashtable import *

my_hash = ChainingHashTable()
x = load_package("WGUPS Package File.csv")
for package in x:
    my_hash.insert(package, x[package])

print(my_hash.search(40))





