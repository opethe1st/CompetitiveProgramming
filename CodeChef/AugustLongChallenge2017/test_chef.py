from unittest import main, TestCase

class RainbowTest(TestCase):
    def test_nextNum(self):
        self.assertEqual(nextNum(2, True), 3)
        self.assertEqual(nextNum(2, False), 1)
        self.assertEqual(nextNum(7, False), 6)
        self.assertEqual(nextNum(7, True), 6)
    def test_single_array(self):
        arr = [1]
        self.assertFalse(isRainbow(arr))

    def test_negative_elements(self):
        arr = [1, -2, -4]
        self.assertFalse(isRainbow(arr))

    def test_basic(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
        self.assertTrue(isRainbow(arr))

    def test_element_occurs_zero_times(self):
        arr = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1]
        self.assertFalse(isRainbow(arr))

    def test_basic_random(self):
        arr = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 6, 5, 4, 4, 4, 4, 3, 2, 1]
        self.assertEqual(arr, arr[::-1])
        self.assertTrue(isRainbow(arr))


if __name__ == "__main__":
    main()