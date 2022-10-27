def for_dongusu(iterable, sayi_tut):
    iterator = iter(iterable)

    sonuc = []
    while True:
        try:
            item = next(iterator)
            sonuc.append(sayi_tut(item))
        except StopIteration:
            return sonuc


list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(for_dongusu(list_numbers, lambda x: x ** 2))
