# importing the required module 
import matplotlib.pyplot as plt 
  
x = []

# TODO: get this from an API...
x.append([22,15,30,23,26,24,31,16]) # dabqu
x.append([33,19,24,31,31,21,22,26]) # taka nome
x.append([6,37,12,16,9,23,31,14]) # dragon4563
x.append([38,33,23,26,47,26,33,31]) # LasvO
x.append([42,32,57,35,33,46,75,50]) # Mookie

names = ["dabqu", "Taka Nome", "Dragon4563", "LasvO", "Mookie"]

y =  range(1,9)
for i in range(len(x)):
    plt.plot(y, x[i], label = names[i])
  
plt.xlabel('Last 8 Games')
plt.ylabel('Headshot%')
plt.title('Valorant Statistics')
plt.legend()
plt.show()