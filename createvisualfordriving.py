import matplotlib.pyplot as plt
from matplotlib import style

#copy and paste the data from main.py here, or you could always put the code from here to the main.py file. I just made it here to make the code simpler
plt.style.use("ggplot")
rankings = [61, 112, 250, 99, 170, 90, 55, 58, 127, 51, 62, 5, 173, 2, 5, 27, 39, 14, 64]
front = ['John Daly', 'John Daly', 'Hank Kuehne', 'Hank Kuehne', 'Scott Hend', 'Bubba Watson', 'Bubba Watson', 'Bubba Watson', 'Robert Garrigus', 'Robert Garrigus', 'J.B. Holmes', 'Bubba Watson', 'Luke List', 'Bubba Watson', 'Dustin Johnson', 'J.B. Holmes', 'Rory McIlroy', 'Rory McIlroy', 'Cameron Champ']
years = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
tot = []
for i in range(19):
    tot.append(front[i] + " " + years[i])

plt.barh(tot, rankings,color = 'k')
plt.xlabel("Money Leader Ranking (Lower The Better)")
plt.title("Best Driver of the Year vs Actual Ranking")

plt.show()

