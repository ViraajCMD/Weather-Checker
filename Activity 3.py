weather = (1,0,0,0,1,1,0)

sunny = 0
rainy = 0

for i in range(0,7):
    if(weather[1] == 0):
        rainy+=1
    else:
        sunny+=1

if (sunny>rainy):

    print("The weather is going to be good today!")

else:

    print("\nThe weather is going to be good!")