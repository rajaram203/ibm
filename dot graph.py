import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('book2.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[2])
        y.append(row[0])
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "sales")
  
plt.xticks(rotation = 25)
plt.xlabel('sales')
plt.ylabel('collections')
plt.title('top 10 collections', fontsize = 20)
plt.grid()
plt.legend()
plt.show()