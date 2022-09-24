import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('book1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[2])
        y.append(row[0])
  
plt.bar(x, y, color = 'b', width = 0.72, label = "sales")
plt.xlabel('buyers')
plt.ylabel('collections')
plt.title('bar graph report')
plt.legend()
plt.show()