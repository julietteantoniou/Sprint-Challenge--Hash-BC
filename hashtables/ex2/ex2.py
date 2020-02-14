#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

# create pairs
# find starting point
# iterate through and find next ticket
# return results

    #source: destination
    for i in range(0, length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    #set first one to ticket with no destination, assuming that's the starting point????
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    for i in range(1, length):
        last_source = route[i-1]
        route[i] = hash_table_retrieve(hashtable, last_source)
    #slice off last element since it will always be NONE
    return route[:length -1]
