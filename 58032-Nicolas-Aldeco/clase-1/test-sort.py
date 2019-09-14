import unittest
from sorting import Sort


class TestSorting(unittest.TestCase):

    def setUp(self):
        self.ls = Sort()
        self.lista_mixed = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
        self.lista_ordenada = [0, 5, 9, 16, 21, 36, 40, 66, 71, 73]
        self.lista3 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        self.listan = [0, 5, 9, 16, 21, -36, -40, 66, 71, 73]
        self.lista_ordenadan = [-40, -36, 0, 5, 9, 16, 21, 66, 71, 73]
# Bubble Sort Testing

    def test_BubbleSort_comun(self):    # 1
        ans = self.ls.bubblesort(self.lista_mixed)
        self.assertEqual(ans, self.lista_ordenada)

    def test_BubbleSort_ordenada(self):    # 2
        ans = self.ls.bubblesort(self.lista_ordenada)
        self.assertEqual(ans, self.lista_ordenada)

    def test_BubbleSort_todos_numeros_iguales(self):    # 3
        ans = self.ls.bubblesort(self.lista3)
        self.assertEqual(ans, self.lista3)

    def test_BubbleSort_con_numeros_negativos(self):    # 4
        ans = self.ls.bubblesort(self.listan)
        self.assertEqual(ans, self.lista_ordenadan)

# Insertion Sort Testing
    def test_InsertionSort_comun(self):    # 5
        ans = self.ls.insertionsort(self.lista_mixed)
        self.assertEqual(ans, self.lista_ordenada)

    def test_InsetionSort_ordenada(self):    # 6
        ans = self.ls.insertionsort(self.lista_ordenada)
        self.assertEqual(ans, self.lista_ordenada)

    def test_InsertionSort_todos_numeros_iguales(self):    # 7
        ans = self.ls.insertionsort(self.lista3)
        self.assertEqual(ans, self.lista3)

    def test_InsetionSort_con_numeros_negativos(self):    # 8
        ans = self.ls.insertionsort(self.listan)
        self.assertEqual(ans, self.lista_ordenadan)

# Marge Sort Testing
    def test_MergeSort_comun(self):     # 9
        ans = self.ls.mergesort(self.lista_mixed)
        self.assertEqual(ans, self.lista_ordenada)

    def test_MergeSort_ordenada(self):     # 10
        ans = self.ls.mergesort(self.lista_ordenada)
        self.assertEqual(ans, self.lista_ordenada)

    def test_MergeSort_todos_numeros_iguales(self):     # 11
        ans = self.ls.mergesort(self.lista3)
        self.assertEqual(ans, self.lista3)

    def test_MergeSort_con_numeros_negativos(self):     # 12
        ans = self.ls.mergesort(self.listan)
        self.assertEqual(ans, self.lista_ordenadan)


if __name__ == "__main__":
    unittest.main()
