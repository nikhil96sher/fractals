from django.shortcuts import render,HttpResponse
from PIL import Image, ImageDraw 
import math
def bucket(value,low1,mean,low2):
	if value<low1:
		return 1
	if value<mean:
		return 2
	if value>low2:
		return 4
	return 3

def transform(c,loc):
	(x,y) = loc
	if c==1:
		return (x/2 , y/2)
	if c==2:
		return ((x+512)/2 , y/2)
	if c==3:
		return (x/2 , (y+512)/2)
	return ((x+512)/2 , (y+512)/2)

def index(request):
	if request.method == "GET":
		return render(request,'datavisualize/index.html')
	else:
		try:
			data = request.POST.get("input","")
			field = map(float,data.split('\n'))
			mean = sum(field)/len(field)
			diff = [ (x - mean*mean)*(x - mean*mean) for x in field ]
			devn = math.sqrt(sum(diff)/(len(diff)-1))
			print mean,devn
			low1 = mean - devn
			low2 = mean + devn
			buckets = [bucket(x,low1,mean,low2) for x in field]
			size = (512,512)
			image = Image.new('RGB', size)

			loc = (0,0)
			for i in xrange(0,9):
				loc = transform(buckets[i],loc)

			for i in xrange(9,len(field)):
				loc = transform(buckets[i],loc)
				image.putpixel(loc, (255,0,0))

			INC = 128
			GRID_COLOR = (0xd3,0xd3,0xd3)
			for x in xrange(0,512,INC):
				for y in xrange(0,512):
					image.putpixel((x,y),GRID_COLOR)

			for y in xrange(0,512,INC):
				for x in xrange(0,512):
					image.putpixel((x,y),GRID_COLOR)

			response = HttpResponse(content_type="image/png")
			image.save(response, 'PNG')
			return response
		except:
			return HttpResponse("Some Exception Occured")