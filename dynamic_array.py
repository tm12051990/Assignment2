# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """resizes internal array to new capacity"""

        if new_capacity < self._size or new_capacity <= 0:

            return

        new_data = StaticArray(new_capacity) #Initializes a new StaticArray that can hold new_capacity elements.

        for i in range(self._size): #Loop that iterates over each element in the old array to copy the values to new array.

            new_data[i] = self._data[i] #Makes the copy

        self._data = new_data #Updates the internal array to reflect the new resized array.

        self._capacity = new_capacity #Updates the internal capacity to reflect the new capacity.

    def append(self, value: object) -> None:
        """Appends new value to the end of the array"""

        if self._size == self._capacity: #If capacity is reached, doubles the capacity.

            self.resize(2 * self._capacity)

        self._data[self._size] = value #Sets the value to the next available position.

        self._size += 1 #increments the size by 1 since a new element is added.

    def insert_at_index(self, index: int, value: object) -> None:
        """Inserts a new element at a given index in the array"""

        if index < 0 or index > self._size: #Parameters for Dynamic Array Exception.

            raise DynamicArrayException

        if self._size == self._capacity: #If capacity is reached, doubles the capacity.

            self.resize(2 * self._capacity)

        for i in range(self._size - 1, index - 1, -1): #Loop for shifting all elements, from the desired index, to the right.

            self._data[i+1] = self._data[i] #Copies elements from the desired index, one index to the right.

        self._data[index] = value #Places the new value at the desired index

        self._size += 1 #Increase size of the array by 1 to account for the new value.

    def remove_at_index(self, index: int) -> None:
        """Removes an element at a given index and adjusts capacity if below a certain threshold"""

        if index < 0 or index >= self._size: #Parameters for Dynamic Array Exception.

            raise DynamicArrayException

        if self._size < self._capacity / 4 and self._capacity > 10: #Check if the capacity needs to be reduced.

            if 2 * self._size > 10: #Conditional statement for resize, resizing cannot reduce the capacity to less than 10 elements.

                new_capacity = 2 * self._size #doubles the current capacity.

                self.resize(new_capacity)

            else: #If the the adjusted capacity will be less than 10, sets the capacity to 10.

                new_capacity = 10

                self.resize(new_capacity)

            if new_capacity < self._capacity:

                self.resize(new_capacity)


        if index == self._size - 1: #Provides O(1) functionality, if index to be removed is the last element in the array, no shifting needs to occur.

            self._size -= 1

            return

        for i in range(index, self._size - 1): #Loop to remove elements at a desired index.

            self._data[i] = self._data[i+1] #Shifts each element to the left after removing the element.

        self._size -= 1 #Decreases size of the array by 1.

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """Slices a portion of an existing array with given parameters, then copies those elements into a new array."""

        if start_index < 0 or start_index >= self._size: #Raise exception if the start_index is invalid.

            raise DynamicArrayException

        if size < 0 or start_index + size > self._size: #Raise exception if the size is invalid or the sliced elements are invalid.

            raise DynamicArrayException

        sliced_array = DynamicArray() #Initializes new array to copy the sliced elements

        for i in range(start_index, start_index + size): #For loops that slices from the given index, up to the size indicated.

            sliced_array.append(self._data[i]) #Copies those elements into the new array.

        return sliced_array

    def map(self, map_func) -> "DynamicArray":
        """Defines a map function that maps each element to a given function, then copies their output into a new array"""

        mapped_array = DynamicArray() #Initializes new array

        for i in range(self._size): #Loop that applies the map function to each element in the array

            mapped_array.append(map_func(self._data[i])) #Copies those elements into a new array

        return mapped_array

    def filter(self, filter_func) -> "DynamicArray":
        """Defines a function that filters elements from an exisiting array then copies the filtered elements into a new array"""

        filtered_array = DynamicArray() #Initializes the new array

        for i in range(self._size): #Loop that applies the filter paraments and copies them to a new array, if those elements are found.

            if filter_func(self._data[i]): #Boolean

                filtered_array.append(self._data[i])

        return filtered_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """Defines a function that applies the reduce funtion to all elements in an array, then returns the accumulated result"""

        if self._size == 0: #If the dynamic array is empty or the initializer is None, returns none, otherwise begins the loop.

            if initializer is None:

                return None

            return initializer

        if initializer is None: #Sets accumulator if initializer parameter is not provided.

            accumulator = self._data[0]

            start_index = 1

        else: #If initializer is provided, sets it to the accumulator

            accumulator = initializer

            start_index = 0

        for i in range(start_index, self._size): #Loops through the array, applying the function to all elements.

            accumulator = reduce_func(accumulator, self._data[i])

        return accumulator






def chunk(arr: DynamicArray) -> "DynamicArray":
    """defines a function that takes an array and splits them into smaller sub arrays of equal size"""

    chunked_array = DynamicArray()

    if arr.length() == 0:

        return chunked_array

    current_chunk = DynamicArray()
    current_chunk.append(arr[0])

    for i in range(1, arr.length()):

        if arr[i] >= arr[i-1]:

            current_chunk.append(arr[i])

        else:

            chunked_array.append(current_chunk)

            current_chunk = DynamicArray()
            current_chunk.append(arr[i])

    chunked_array.append(current_chunk)

    return chunked_array



def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    def print_chunked_da(arr: DynamicArray):
        if len(str(arr)) <= 100:
            print(arr)
        else:
            print(f"DYN_ARR Size/Cap: {arr.length()}/{arr.get_capacity()}")
            print('[\n' + ',\n'.join(f'\t{chunk}' for chunk in arr) + '\n]')

    print("\n# chunk example 1")
    test_cases = [
        [10, 20, 30, 30, 5, 10, 1, 2, 3, 4],
        ['App', 'Async', 'Cloud', 'Data', 'Deploy',
         'C', 'Java', 'Python', 'Git', 'GitHub',
         'Class', 'Method', 'Heap']
    ]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# chunk example 2")
    test_cases = [[], [261], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# find_mode example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
