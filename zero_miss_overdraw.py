from PIL import Image
 


#850 fixes out edge


# m = []

				


# I had the same issue as Dwight, but to avoid the float cast just replaced the if statement with this one: 


# if(x*x+y*y < radius*radius + radius) also to get just the circle (ring) you can do this 


def draw_circle(centre_x, centre_y, radius):
    offset_y = 0
    offset_x = radius
    crit = 1 - radius
    while offset_y <= offset_x:
        pix[centre_x + offset_x, centre_y + offset_y] = (0,127,0)
        pix[centre_x + offset_y, centre_y + offset_x] = (0,127,0)
        pix[centre_x - offset_x, centre_y + offset_y] = (0,127,0)
        pix[centre_x - offset_y, centre_y + offset_x] = (0,127,0)
        pix[centre_x - offset_x, centre_y - offset_y] = (0,127,0)
        pix[centre_x - offset_y, centre_y - offset_x] = (0,127,0)
        pix[centre_x + offset_x, centre_y - offset_y] = (0,127,0)
        pix[centre_x + offset_y, centre_y - offset_x] = (0,127,0)
        offset_y = offset_y + 1
        if crit <= 0:
            crit = crit + 2 * offset_y + 1
        else:
            offset_x = offset_x - 1
            crit = crit + 2 * (offset_y - offset_x) + 1

def super_circle(centre_x, centre_y, radius):
	r = radius
	for x_orig in range(160):
		for y_orig in range(120):
			x = x_orig - 80
			y = 60 - y_orig
			
			if ( (x**2 + y**2 - r**2)**2 <= r**2 ):
					pix[x_orig,y_orig] = (0,pix[x_orig,y_orig][1],127)
		

def count_error():
	perfect = 0
	missed = 0
	extra = 0
	for x_orig in range(160):
		for y_orig in range(120):
			x = x_orig - 80
			y = 60 - y_orig
			if pix[x_orig,y_orig] == (0, 127, 127):
				perfect += 1
			elif pix[x_orig,y_orig] == (0, 127, 0):
				missed += 1
			elif pix[x_orig,y_orig] == (0, 0, 127):
				extra += 1
	# print("Perfect: " + str(perfect))
	# print("Missed: " + str(missed))
	# print("Extra: " + str(extra))
	return([perfect,missed,extra])
	
listx = []
for radii in range(59):
	img = Image.new('RGB', (160, 120), color = 'black')
	pix = img.load()
	pix[80,60] = 127

	draw_circle(80,60,radii + 1)
	super_circle(0,0,radii + 1)
	
	ret = count_error()
	img.save("circ_"+str(radii+1)+"-missed-"+str(ret[1])+"-extra-"+str(ret[2])+".png")
	listx.append(ret)

p = 0
e = 0
m = 0
for item in listx:
	p += item[0]
	m += item[1]
	e += item[2]

File_object2 = open("Perf-" + str(p) + "-Err-" + str(e) + "-Miss-"+ str(m) + ".txt","w")
#File_object2.write("\n".join(listx))


# x = 0
# y = radius;
# d = 1 - radius;
# deltaE = 3
# deltaSE = -2 * radius + 5

# pix[x+80,60-y] = (pix[x+80,60-y][0],pix[x+80,60-y][1],127)

# while(y > x):
	# if (d < 0): 
		# d += deltaE
		# deltaE += 2
		# deltaSE += 2
	# else:
		# d += deltaSE;
		# deltaE += 2
		# deltaSE += 4
		# y -= 1
	# print(str(x)+ "," + str(y))
	# x += 1
	# pix[x+80,60-y] = (pix[x+80,60-y][0],pix[x+80,60-y][1],127)
	
	
	
# f = 1 - radius
# ddf_x = 1
# ddf_y = -2 * radius
# x = 0
# y = radius
# self.set(x0, y0 + radius, colour)
# self.set(x0, y0 - radius, colour)
# self.set(x0 + radius, y0, colour)
# self.set(x0 - radius, y0, colour)

# while x < y:
	# if f >= 0: 
		# y -= 1
		# ddf_y += 2
		# f += ddf_y
	# x += 1
	# ddf_x += 2
	# f += ddf_x    
	# self.set(x0 + x, y0 + y, colour)
	# self.set(x0 - x, y0 + y, colour)
	# self.set(x0 + x, y0 - y, colour)
	# self.set(x0 - x, y0 - y, colour)
	# self.set(x0 + y, y0 + x, colour)
	# self.set(x0 - y, y0 + x, colour)
	# self.set(x0 + y, y0 - x, colour)
	# self.set(x0 - y, y0 - x, colour)





