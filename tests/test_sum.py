# -*- coding: utf-8 -*-

import unittest

def sum(a, b):
    return a + b

# Implementación pendiente para resta (TDD)
def subtract(a, b):
    return a - b

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)

    def test_subtract(self):
        # TDD: este test fallará hasta que se implemente la función
        self.assertEqual(subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()