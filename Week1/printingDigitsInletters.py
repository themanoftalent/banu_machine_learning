class NoCevir:

    def __init__(self, name):
        self.name = name
        # print(f"{self.name} bey cevirdigi numaralar ")

    def cevirDijit(self):
        digits_mapping = {
            '0': 'zero', '1': 'one', '2': 'two', '3': 'three',
            '4': 'four', '5': 'five', '6': 'six',
            '7': 'seven', '8': 'eight', '9': 'nine'}

        output = ''
        for phone in mesaj:
            output = output + digits_mapping.get(phone, '!') + ' '
        return output

    def baski(self):
        print(f"{self.name} bey cevirdigi numaralar ")
        print(self.cevirDijit())


mesaj = input('Enter a phone number to be translated \n')
no1 = NoCevir('Cemil')
no2 = NoCevir('Ahmet')

# no1.name
# print(no1.cevirDijit())
# print()
no1.baski()
no2.baski()
