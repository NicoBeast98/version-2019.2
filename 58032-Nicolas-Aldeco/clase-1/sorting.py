class Sort():

    def bubblesort(self, lista):
        n = len(lista)
        for i in range(1, n):
            for j in range(n-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    def insertionsort(self, listx):
        n = len(listx)
        i = 0
        for i in range(i, n):
            vol = listx[i]
            j = i
            while j > 0 and listx[j-1] > vol:
                listx[j] = listx[j-1]
                j -= 1
            listx[j] = vol
        return listx

    def mergesort(self, lista):
        if len(lista) <= 1:
            return lista
        middle = int(len(lista) / 2)
        left = lista[:middle]
        right = lista[middle:]
        left = self.mergesort(left)
        right = self.mergesort(right)
        return self.merge(left, right)

    def merge(self, listA, listB):
        new_list = []
        a = 0
        b = 0
        while a < len(listA) and b < len(listB):
            if listA[a] < listB[b]:
                new_list.append(listA[a])
                a += 1
            else:
                new_list.append(listB[b])
                b += 1
        while a < len(listA):
            new_list.append(listA[a])
            a += 1
        while b < len(listB):
            new_list.append(listB[b])
            b += 1
        return new_list
