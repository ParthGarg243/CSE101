x0,y0=float(input('Enter x coordinate: ')),float(input('Enter y coordinate: '))
x1,y1=x0,y0
print('Initial Coordinates of the vehicle are: ('+str(x0)+','+str(y0)+')')
print()
dist_input=float(input('Enter Distance: '))
distance=0

while dist_input>0:
    distance+=dist_input
    if dist_input<=25:
        y1+=dist_input      #north   
    elif (dist_input>=26) and (dist_input<=50):
        y1-=dist_input      #south
    elif (dist_input>=51) and (dist_input<=75):
        x1+=dist_input      #east
    elif dist_input>=76:
        x1-=dist_input      #west
    dist_input=int(input('Enter Distance: '))

print()
print('Final Coordinates of the vehicle are: ('+str(x1)+','+str(y1)+')')
print('Total Distance Traveled:',distance)
displacement=(((x1-x0)**2)+((y1-y0)**2))**0.5
print('Distance between Initial and Final points:',round(displacement,2))