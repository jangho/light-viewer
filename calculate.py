import math
import time

class light(object):
	"""docstring for light"""
	def __init__(self, x, y, distance, orientation, percent):
		super(light, self).__init__()
		self.x = x
		self.y = y
		self.distance = distance
		self.orientation = orientation
		self.percent = percent
		
l1 = light(20,80,0,0,0)
l2 = light(80,80,0,0,0)
l3 = light(20,20,0,0,0)
l4 = light(80,20,0,0,0)
lights = [l1, l2, l3, l4]

# calculate takes in person and lights array to populate distance, orientation and percent
def calculate (human, lamp):
	for q in range(0,len(lamp)):
		deltaY = lamp[q].y - human.y
		deltaX = lamp[q].x - human.x
		lamp[q].distance = math.sqrt((float(deltaY))**2+(float(deltaX))**2)
		if human.x == lamp[q].x and human.y == lamp[q].y:
			lamp[q].orientation = 0
		elif lamp[q].x == human.x and lamp[q].y > human.y:
			lamp[q].orientation = 90
		elif lamp[q].x == human.x and lamp[q].y < human.y:
			lamp[q].orientation = 270
		elif lamp[q].x > human.x and lamp[q].y == human.y:
			lamp[q].orientation = 0
		elif lamp[q].x < human.x and lamp[q].y == human.y:
			lamp[q].orientation = 180
		elif lamp[q].x > human.x and lamp[q].y > human.y:
			lamp[q].orientation = math.atan(deltaY / float(deltaX)) * (180 / math.pi)
		elif lamp[q].x < human.x and lamp[q].y > human.y:
			lamp[q].orientation = math.atan(deltaY / float(deltaX)) * (180 / math.pi) + 180
		elif lamp[q].x < human.x and lamp[q].y < human.y:
			lamp[q].orientation = math.atan(deltaY / float(deltaX)) * (180 / math.pi) + 180
		elif lamp[q].x > human.x and lamp[q].y < human.y:
			lamp[q].orientation = math.atan(deltaY / float(deltaX)) * (180 / math.pi) + 360
		#print lamp[q].orientation
		#print lamp[q].distance
		q += 1
	minAngle = person.orientation - 30
	maxAngle = person.orientation + 30
	highestD = lamp[0].distance
	for q in range(0,len(lamp)-1):
		r = q+1
		check = lamp[r].distance
		if highestD < check:
			highestD = lamp[r].distance
	lampCount = 0
	for q in range(0,len(lamp)):
		if minAngle < lamp[q].orientation < maxAngle:
			lamp[q].percent = 20
			lampCount += 1
		else:
			lamp[q].percent = 50
			lampCount += 1
		if highestD == lamp[q].distance:
			backup = lamp[q].percent
			s = q
			lamp[q].percent = 0
			lampCount -= 1
	if lampCount < 3:
		lamp[s].percent = backup
	#for q in range(0,len(lamp)):
		#print lamp[q].percent
	#print highestD


def output (lamp, level, levelReal):
	mod = 1
	while levelReal < level:
		mod += 1
		for q in range(0,len(lamp)):
			print lamp[q].percent
			if lamp[q].percent != 0:
				lamp[q].percent = lamp[q].percent + 5
		if mod > 10:
			break
	while levelReal > level:
		mod += 1
		for q in range(0,len(lamp)):
			if lamp[q].percent != 0:
				print lamp[q].percent
				lamp[q].percent = lamp[q].percent - 5
		if mod > 10:
			break
	#print levelReal
while 1:
	with open('user.txt', 'r') as f:
		read_data = f.read()
 		f.close
	
	readCount=0
	lCount=0
	while len(read_data)>0:
		if (read_data[readCount]=="\n") or (readCount==len(read_data)-1):
			print "Found: "+read_data[0:readCount]
			if lCount==0:
				lx=int(read_data[0:readCount])
			elif lCount==1:
				ly=int(read_data[0:readCount])
			elif lCount==2:
				lo=int(read_data[0:readCount])
			read_data=read_data[readCount+1:]
			readCount=0
			lCount+=1
		else:
			readCount+=1
	person = light(50,50,0,200,0)
	lux = 80
	luxReal = 0


	calculate (person, lights)

	output (lights, lux, luxReal)
	
	strOut="A\n"+str(lights[0].percent)+"\n"+str(lights[1].percent)+"\n"+str(lights[2].percent)+"\n"+str(lights[3].percent)

	f = open('power.php', 'w')
	f.write(strOut)
	f.close()
	time.sleep(1)
	

# def push (data):
# 	#push data to web

# 	break

# push (lights)
