#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length < 2:
        return None

    for i in range(length):
        hash_table_insert(ht, weights[i], i)
        key = limit - weights[i]
        if hash_table_retrieve(ht, key):
            if hash_table_retrieve(ht, weights[i]) is not hash_table_retrieve(ht, key):
                if hash_table_retrieve(ht, weights[i]) >= hash_table_retrieve(ht, key):
                    return hash_table_retrieve(ht, weights[i]), hash_table_retrieve(ht, key)
                else:
                    return hash_table_retrieve(ht, key), hash_table_retrieve(ht, weights[i])
        
            if hash_table_retrieve(ht, weights[i]) is hash_table_retrieve(ht, key):
                return (1, 0)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
