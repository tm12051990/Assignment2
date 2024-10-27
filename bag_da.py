# Name: Tony Miglets
# OSU Email: migletst@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2
# Due Date: 28 OCT 2024
# Description: ADT Implementation and Dynamic Array HW


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """Defines an add functionality to add a value to the bag"""
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """Defines a function to remove a value from the bag and decrement the array accordingly"""
        for i in range(self._da.length()): #For loop that checks if the current element is equal to the provided value
            if self._da[i] == value:
                for j in range(i, self._da.length()-1):
                    self._da[j] = self._da[j+1]
                self._da._size -= 1 #Decrements the array size
                return True
        return False

    def count(self, value: object) -> int:
        """Defines a function that counts the number of same elements in the bag, then returns the count"""
        accumulator = 0

        for i in range(self._da.length()): #For loop that checks if each element is equal to the provided value.
            if self._da[i] == value:
                accumulator += 1
        return accumulator

    def clear(self) -> None:
        """Clears all elements in the bag"""
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """Defines a function that checks if two bags are equal in both length and elements, then returns a boolean"""
        if self._da.length() != second_bag._da.length():
            return False

        for i in range(self._da.length()): #For loop that checks each element in the index has a match in the second bag.
            current_value = self._da[i]
            self_count = self.count(current_value)
            second_bag_count = second_bag.count(current_value)
            if self_count != second_bag_count:
                return False
        else:
            return True

    def __iter__(self):
        """Creates an iterator to iterate over the array"""
        self._index = 0
        return self

    def __next__(self):
        """Allows the iterator to move to the next element in the array and stops when there are no more indices"""
        if self._index < self._da.length(): #Advances iterator if end of the array hasn't been reached.
            current_value = self._da[self._index]
            self._index += 1
            return current_value
        else:
            raise StopIteration


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
