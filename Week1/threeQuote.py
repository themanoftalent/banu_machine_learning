friday_song = """
It's Friday, Friday
Gotta get down on Friday
Everybody's lookin' forward to the weekend, weekend
Friday, Friday
Gettin' down on Friday
Everybody's lookin' forward to the weekend

Partyin', partyin' (Yeah)
Partyin', partyin' (Yeah)
Fun, fun, fun, fun
Lookin' forward to the weekend

It's Friday, Friday
Gotta get down on Friday
Everybody's lookin' forward to the weekend, weekend
Friday, Friday
Gettin' down on Friday
Everybody's lookin' forward to the weekend
"""
# print(friday_song)
count = 1
for line in friday_song.splitlines():
    print(line)
    count += 1
    if count == 5:
        break
    else:
        continue

    # print("#######################")
