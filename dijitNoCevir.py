def digiConvert(msg):
    words = msg.split(' ')
    dijitNumara = {
        '1': 'Bir',
        '2': 'iki',
        '3': 'Üc'
    }

    sonuc = ''
    for word in msg:
        sonuc += dijitNumara.get(word, 'Böyle bir sonuç yok') + ' '
    return sonuc


msg = input('Enter number = ')
print(digiConvert(msg))



############################

##### more
# def djitCevir(mesaj):
#     # words = mesaj.split(' ')
#     dijitNumara = {
#         '1': 'Bir',
#         '2': 'iki',
#         '3': 'Üc'
#     }
#     sonuc = ''
#     for word in mesaj:
#         sonuc += dijitNumara.get(word, 'Böyle bir sonuç yok') + ''
#         return sonuc
#
#
# mesaj = input('Numara gir : ')
# print(djitCevir(mesaj))


# mesaj = input('Numara gir : ')
# words = mesaj.split(' ')
# dijitNumara = {
#     '1': 'Bir',
#     '2': 'iki',
#     '3': 'Üc'
# }
# sonuc = ''
# for word in mesaj:
#     sonuc += dijitNumara.get(word, 'Böyle bir sonuç yok') + ' '
# print(sonuc)
