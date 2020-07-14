
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_entry(self, key, value):
        new_entry = HashTableEntry(key, value)
        if self.head == None:
            self.head = new_entry
        else:
            if self.head.key == key:
                self.head.value = value
            else:
                cur_prev = self.head
                cur = self.head.next
                while cur_prev.next is not None:
                    if cur.key == key:
                        cur.value = value
                new_entry.next = self.head
                self.head = new_entry




    def remove_entry(self, key):
        cur = self.head
        cur_next = self.head.next
        if self.head.key == key:
            self.head = self.head.next
            cur.next = None
            return cur
        while cur.next is not None:
            if cur_next.key == key:
                cur.next = cur_next.next
                cur_next = None
                return cur.next
            else:
                cur = cur.next
                cur_next = cur_next.next

    def find(self, key):
        if self.head == None:
            return None
        cur = self.head
        while cur.next == None:
            if cur.key == key:
                return cur.value
            else:
                cur = cur.next
        return None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.data = [0] * capacity
        self.capacity = capacity
        self.entries = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.data)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        factor = (self.capacity - self.entries) /2
        return factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        if self.data[slot] == 0:
            self.entries += 1
            new_list = LinkedList()
            new_list.add_entry(key, value)
            self.data[slot] = new_list

        else:
            self.entries += 1
            self.data[slot].add_entry(key, value)



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        self.entries -= 1
        self.data[slot].remove_entry(key)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        # if self.data[slot] == 0:
        #     return None
        # else:
        return self.data[slot].find(key)


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_arr = self.data
        self.capacity = new_capacity
        self.data = [0] * new_capacity
        for list in old_arr:
            cur = list.head
            if cur.next == None:
                self.put(cur.key, cur.value)
            else:
                while cur.next is not None:
                    self.put(cur.key, cur.value)
                    cur = cur.next




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 9):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 9):
        print(ht.get(f"line_{i}"))

    print("")
