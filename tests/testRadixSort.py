import unittest
from pythonds.basic.queue import Queue
from radixSortFunction import *


li = [11, 12, 13, 14, 32, 33, 34, 41, 42, 43, 133, 134, 44, 51, 52, 53, 54, 72, 73, 74, 81, 82, 83, 84, 91,
      92, 93, 94, 101, 102, 103, 104, 21, 22, 23, 24, 31, 111, 112, 113, 114, 121, 122, 123, 124, 131, 132, 61, 62, 63,
      64, 71]
li1 = radix_sort(li)
li.sort()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(li1, li)


if __name__ == '__main__':
    unittest.main()