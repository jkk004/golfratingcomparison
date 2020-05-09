import matplotlib.pyplot as plt
from matplotlib import style

#copy and paste the data from main.py here, or you could always put the code from here to the main.py file. I just made it here to make the code simpler
plt.style.use("ggplot")
tot = []
rankings_int = []
rankings = [250, '43', '7', '81', '6', '195', '112', '129', '67', '149', '180', '108', '2', '49', '9', '110', '21', '113', '13']
front = ['Charles Howell III', 'Chris Smith', 'Chad Campbell', 'Joe Durant', 'Kenny Perry', 'Chris Smith', 'Cameron Beckman', 'Joe Durant', 'Jonathan Byrd', 'Charles Warren', 'Boo Weekley', 'Boo Weekley', 'Henrik Stenson', 'Henrik Stenson', 'Henrik Stenson', 'Lucas Glover', 'Kyle Stanley', 'Sam Ryder', 'Paul Casey']
years = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
tot = []
for i in range(19):
    tot.append(front[i] + " " + years[i])
for i in range(19): #convert str of number to int of number
   rankings_int.append(int(rankings[i]))
plt.barh(tot, rankings_int,color = 'k')
plt.xlabel("Money Leader Ranking (Lower The Better)")
plt.title("Best Ball Striker of the Year vs Actual Ranking")

plt.show()

