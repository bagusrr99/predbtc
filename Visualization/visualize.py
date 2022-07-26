from matplotlib.transforms import Bbox
import mpld3 

import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
fig = plt.figure(figsize = (18,8))



#Plots 1

plt.subplot(2,2,1)

with open('csvVisualize.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append(row[2])
        
        
plt.bar(x, y, color = 'g', width = 0.25, label = "CO2EMISSIONS")
plt.xlabel('ENGINESIZE')
plt.ylabel('Fuel Consumption')
plt.title('CO2 Emission Result')
plt.legend()

#Plot 2


plt.subplot(2,2,2)


plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Consumption Data")
  
plt.xticks(rotation = 25)
plt.xlabel('Engine Size')
plt.ylabel('Consumption')
plt.title('Consumption Report ')
plt.grid()
plt.legend()


#Plot3

# plt.subplot(2,2,3)

# with open('csvVisualize.csv', 'r') as csvfile:
#     lines = csv.reader(csvfile, delimiter = ',')
#     for row in lines:
#         x.append(row[0])
#         y.append(row[1])


  
# plt.pie(y,labels = x,autopct = '%.2f%%')
# plt.title('Emission Pie Chart')
# plt.grid()










# plt.show()

plt.savefig('CO2EMISSIONS.png', bbox_inches="tight")




html_str = mpld3.fig_to_html(fig)
Html_file= open("index.html","w")
Html_file.write(html_str)
Html_file.close()