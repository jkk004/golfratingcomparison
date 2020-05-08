import requests

#code to get data

gro = []
year = []
off = []


def stats(plug):
    link = "https://www.pgatour.com/content/pgatour/stats/stat.02428.y20" + plug +".html"
    f = requests.get(link)
    loc = f.text.index("players/player")
    check = ""
    tally = 0
    for i in range(loc,loc + 2000):
        if f.text[i] == "<" and tally >= 1:
            break
        if f.text[i].isupper():
            tally += 1
        if tally >= 1:
            check += f.text[i]
    return check
def stats1(plug):
    link = "https://www.pgatour.com/content/pgatour/stats/stat.109.y20" + plug +".html"
    f = requests.get(link)
    loc = f.text.index(gro[int(plug)-1])
    check1 = ""
    tally = 0
    for i in range(loc-180,loc):
        if f.text[i] == "<" and tally >= 1:
            break
        if f.text[i].isdigit():
            tally += 1
        if tally >= 1:
            check1 += f.text[i]
    return check1
for i in range(1,20):
    if i < 10:
        plug = "0" + str(i)
        hey = stats(plug)
        gro.append(hey)
        year.append("20" + plug)
        hey1 = stats1(plug)
        off.append(hey1)
    else:
        plug = str(i)
        hey = stats(plug)
        gro.append(hey)
        year.append("20" + str(i))
        hey1 = stats1(plug)
        off.append(hey1)
total = []
ranking_int = []
for i in range(19):
    total.append(gro[i] + " " + year[i])
for i in range(19):
    ranking_int.append(int(year[i]))
print(gro,total, year, ranking, ranking_int, off)