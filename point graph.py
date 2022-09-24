import matplotlib.pyplot as plt
import csv
  
Names = []
Values = []
  
with open('book2.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        Names.append(row[1])
        Values.append(row[0])
  
plt.scatter(Names, Values, color = 'g',s = 100)
plt.xticks(rotation = 25)
plt.xlabel('sales')
plt.ylabel('collections')
plt.title('top 10 collections', fontsize = 20)
  
plt.show()
