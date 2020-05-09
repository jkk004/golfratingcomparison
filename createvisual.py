import matplotlib.pyplot as plt
from matplotlib import style

#copy and paste the data from main.py here, or you could always put the code from here to the main.py file. I just made it here to make the code simpler
plt.style.use("ggplot")
rankings = [3, 119, 184, 76, 19, 58, 22, 52, 13, 8, 80, 14, 124, 41, 39, 2, 10, 184, 65]
front = ['David Toms', 'Bernhard Langer', 'Brian Henninger', 'Brad Faxon', 'Ben Crane', 'Ben Crane', 'Tim Clark', 'Daniel Chopra', 'Brian Gay', 'Paul Casey', 'Charlie Wi', 'Luke Donald', 'Greg Chalmers', 'Graeme McDowell', 'Russell Henley', 'Jason Day', 'Brian Harman', 'Greg Chalmers', 'Graeme McDowell']
tot=['David Toms 2001', 'Bernhard Langer 2002', 'Brian Henninger 2003', 'Brad Faxon 2004', 'Ben Crane 2005', 'Ben Crane 2006', 'Tim Clark 2007', 'Daniel Chopra 2008', 'Brian Gay 2009', 'Paul Casey 2010', 'Charlie Wi 2011', 'Luke Donald 2012', 'Greg Chalmers 2013', 'Graeme McDowell 2014', 'Russell Henley 2015', 'Jason Day 2016', 'Brian Harman 2017', 'Greg Chalmers 2018', 'Graeme McDowell 2019']

plt.barh(tot, rankings,color = 'k')
plt.xlabel("Money Leader Ranking (Lower The Better)")
plt.title("Best Putter of the Year vs Actual Ranking")

plt.show()
