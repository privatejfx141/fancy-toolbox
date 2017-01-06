import unittest
from containers import *

class TestContainer(unittest.TestCase):

    def test_01_empty_new_container(self):
        container = Container()
        result = (container.size(), container.is_empty())
        expect = (0, True)
        self.assertEqual(result, expect, 'Container should be empty.')

    def test_02_container_edit(self):
        container = Container()
        container._set_list(['A', 'B', 1, 2, None])
        container._put(container._peek(1))
        container._get(1)
        container._put('New')

        result = container._get_list()
        expect = ['A', 1, 2, None, 'B', 'New']
        self.assertEqual(result, expect, 'Container should be changed.')


class TestBucket(unittest.TestCase):

    def test_01_filled_bucket(self):
        bucket = Bucket()
        bucket.put('~')

        result = (bucket.peek(), bucket.size(), bucket.is_empty())
        expect = ('~', 1, False)
        self.assertEqual(result, expect, 'Bucket should have one item.')


class TestStack(unittest.TestCase):
    pass


class TestQueue(unittest.TestCase):
    pass


if(__name__ == "__main__"):
    unittest.main(exit=False)
