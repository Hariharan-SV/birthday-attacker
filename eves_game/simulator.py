"""
create a hash table of size k
our own hash function
create k+1 users
for k+1 users easy collision

check hashed password in a loop and get the user details
use that original password and login to that user and exploit details

use that probablity to observe collision

hash table should be of dynamic size
show that as collision occurs at some size

create a table (defaultdict : user and passwd)
add a new user into dict with passwd as key and user in a list
hashfn = modn
"""
from pprint import pprint

from eves_game.resources.hash import HashTable

if __name__ == '__main__':
    h = HashTable(5)
    users = {
        'hari': 0,
        'krish': 0

    }
    v = h.add("hari")
    users['hari'] = v
    v = h.add("krishnan")
    users['krish'] = v
    pprint(users)
    h.print_data()
