from PIL import Image
import math

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
	for x_orig in range(80):
		for y_orig in range(x_orig):
			x = x_orig - 80
			y = 60 - y_orig
			try:
				result1 = y - round(math.sqrt(r*r-x*x))
				result2 = x - round(math.sqrt(r*r-y*y))
				result3 = y - round(-math.sqrt(r*r-x*x))
				result4 = x - round(-math.sqrt(r*r-y*y))
				
				resultdiag1 = y + 1 - round(math.sqrt(r*r-(x+1)*(x+1)))
				resultdiag2 = y - 1 - round(math.sqrt(r*r-(x-1)*(x-1)))
				resultbelow = y - 1 - round(math.sqrt(r*r-x*x))
				resultbelowdiag1 = y - round(math.sqrt(r*r-(x+1)*(x+1)))
				resultbelowdiag2 = y - 2 - round(math.sqrt(r*r-(x-1)*(x-1)))
				result5 = x*x + y*y
				# or ((result2 <= 0.25) and (result2 > -0.5))):
				
				if ( ((x**2 + (y)**2 - r**2)**2 <= r**2)):
					if ((resultbelow < 0.5) and (resultbelow > -0.5)):
						if not (((resultbelowdiag1 < 0.5) and (resultbelowdiag1 > -0.5)) and ((resultbelowdiag2 < 0.5) and (resultbelowdiag2 > -0.5))):
							pix[x_orig,y_orig] = (0,pix[x_orig,y_orig][1],127)
				
				if ((result1 < 0.5) and (result1 > -0.5)):
					if not (((resultdiag1 < 0.5) and (resultdiag1 > -0.5)) and ((resultdiag2 < 0.5) and (resultdiag2 > -0.5))):
						if ( ((x**2 + (y+1)**2 - r**2)**2 <= r**2)):
							pix[x_orig,y_orig] = (0,0,0)
						else:
							pix[x_orig,y_orig] = (0,pix[x_orig,y_orig][1],127)
					else:
						pix[x_orig,y_orig] = (0,pix[x_orig,y_orig][1],127)
					#if not ((result1_2 <= 0.25) and (result1_2 > -0.5)):
					
				# elif (((result3 <= 0.25) and (result3 > -0.5)) or ((result4 <= 0.25) and (result4 > -0.5))):
					# pix[x_orig,y_orig] = (0,pix[x_orig,y_orig][1],127)
				# if (result5 == r*r):
					# pix[x_orig,y_orig] = (5,55,127)
			except:
				pass
			# if ( ((x**2 + y**2 - r**2)**2 <= r**2)):
				# p1 = [x+1,y]
				# p2 = [x-1,y]
				# p3 = [x,y+1]
				# p4 = [x,y-1]
				# sum = 0
				# grad_n = 0
				# #grad = y/x
				# if ( ((p1[0]**2 + p1[1]**2 - r**2)**2 <= r**2) and ((p3[0]**2 + p3[1]**2 - r**2)**2 <= r**2) ):
					# sum += 1

				# if ( ((p1[0]**2 + p1[1]**2 - r**2)**2 <= r**2) and ((p4[0]**2 + p4[1]**2 - r**2)**2 <= r**2) ):
					# sum += 1
				# if ( ((p2[0]**2 + p2[1]**2 - r**2)**2 <= r**2) and ((p3[0]**2 + p3[1]**2 - r**2)**2 <= r**2) ):
					# sum += 1
				# if ( ((p2[0]**2 + p2[1]**2 - r**2)**2 <= r**2) and ((p4[0]**2 + p4[1]**2 - r**2)**2 <= r**2) ):
					# sum += 1
					
					
				# if sum == 0:
					# pix[x_orig,y_orig] = (0,pix[x_orig,y_orig][1],127)
				# else:
					
					# pix[x_orig,y_orig] = (127,pix[x_orig,y_orig][1],127)
					
				# d = x**2 + y**2
				# if ((d >= (radius -1)**2) and (d < (radius +1)**2)):
					# pix[x_orig,y_orig] = (0,pix[x_orig,y_orig][1],127)


def count_error():
	perfect = 0
	missed = 0
	extra = 0
	decisions = []
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
			elif pix[x_orig,y_orig] == (127,127,127):
				temp = []
				temp.append([x,y])
				collisions = []
				try:
					if pix[x_orig+1,y_orig] == (127,0,127):
						collisions.append([x_orig+1-80,60 - y_orig])
					if pix[x_orig-1,y_orig] == (127,0,127):
						collisions.append([x_orig-1-80,60 - y_orig])
					if pix[x_orig,y_orig+1] == (127,0,127):
						collisions.append([x_orig-80,60 - y_orig+1])
					if pix[x_orig,y_orig-1] == (127,0,127):
						collisions.append([x_orig-80,60 - y_orig-1])
				except:
					pass
				temp.append(collisions)
				decisions.append(temp)
	return([perfect,missed,extra,decisions])


# def octant(x,y):
	


list = []
for radii in range(59):
	img = Image.new('RGB', (160, 120), color = 'black')
	pix = img.load()
	pix[80,60] = 127
	draw_circle(80,60,radii + 1)
	super_circle(0,0,radii + 1)
	ret = count_error()
	img.save("circ_"+str(radii+1)+"-missed-"+str(ret[1])+"-extra-"+str(ret[2])+".png")
	list.append(ret)


p = 0
e = 0
m = 0
r = 1
for item in list:
	p += item[0]
	m += item[1]
	e += item[2]
	r += 1

File_object2 = open("Perf-" + str(p) + "-Err-" + str(e) + "-Miss-"+ str(m) + ".txt","w")

i_l = []
j_l = []
for keep in list[58][3]:
	print("Point: " + str(keep[0]) + " collides with: " + str(keep[1]))
	if (len(keep[1]) == 1):
		i = keep[0][0]**2 + keep[0][1]**2 - r**2
		j = keep[1][0][0]**2 + keep[1][0][1]**2 - r**2
		i_l.append(i)
		j_l.append(j)
		print("val- Point: " + str(i) + " grad: " + str(keep[0][1]/keep[0][0])	+ " collides with: " + str(j) + " grad: " + str(keep[1][0][1]/keep[1][0][0]))
	elif (len(keep[1]) == 2):
		i = keep[0][0]**2 + keep[0][1]**2 - r**2
		j = [keep[1][0][0]**2 + keep[1][0][1]**2 - r**2, keep[1][1][0]**2 + keep[1][1][1]**2 - r**2]
		grads = [ keep[1][0][1]/keep[1][0][0], keep[1][1][1]/keep[1][1][0]]
		i_l.append(i)
		j_l.append(j)
		print("val -Point: " + str(i) + " grad: " + str(keep[0][1]/keep[0][0]) + " collides with: " + str(j[0]) + " and: " + str(j[1]) + " grads: " + str(grads))

for idx,item in enumerate(i_l):
	try:
		m = int(j_l[idx])
	except:
		print(str(abs(item)) + " - " + str(abs(j_l[idx][0])) + " = " + str(abs(item)- abs(j_l[idx][0])))
		print(str(abs(item)) + " - " + str(abs(j_l[idx][1])) + " = " + str(abs(item)- abs(j_l[idx][1])))
	else:
		print(str(abs(item)) + " - " + str(abs(j_l[idx])) + " = " + str(abs(item)- abs(j_l[idx])))




