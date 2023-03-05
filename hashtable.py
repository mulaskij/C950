# HashTable class using chaining.

import csv


def load_table(filename):
    rows = []
    with open(filename) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=",")
        header = next(csvreader)
        for row in csvreader:
            if not row == " ":
                rows.append(row)
        print(header)
        print(rows)
    return rows


class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.

    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, item):
        # get the bucket list where this item will go.
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        # Update key if it already exists
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # If key doesn't exist insert item to end of bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

packages = load_table("WGUPS Package File.csv")
print(packages)