from PIL import Image, ImageDraw, ImageFilter, ImageOps
import random
import time
class map_create:
    def __init__(self, length, width):
        self.length = length
        self.width = width
map = map_create(200, 200)
rand = random.randint(-2,2)
amountofblack = -1
evolutions = 100
savedland = 1000
map_image = Image.new("RGB", (map.length, map.width), color='blue')
data = []
biomedata = []
whatsaround = [0,0,0,0]
fordeep = 0
relativeheight = 0
relativesize = 0
seed = 114
random.seed(seed)
color1 = [62, 184, 62]
color2 = [219,217,269]
color3 = [190,205,205]
color4 = [220,205,100]
color5 = [126,195,134]
color6 = [141,195,81]
color7 = [0,180,220]
#water color that I like
color7 = [78,156,123]
color7 = [29, 196, 157]
colors = [color1,color2,color3,color4,color5,color6,color7]
for i in range(3):
    rand = random.randint(30,220)
    color1[i] = rand
for i in range(3):
    rand = random.randint(30,220)
    color3[i] = rand
for i in range(3):
    rand = random.randint(30,220)
    color4[i] = rand
for i in range(3):
    color5[i] = int((color3[i] + color1[i])/2)
for i in range(3):
    color6[i] = int((color4[i] + color1[i])/2)
for i in range(3):
    color2[i] = int((color3[i] + color4[i])/2)
for i in range(3):
    rand = random.randint(30,220)
    color7[i] = rand
t0 = time.time()
def oceancreate():
    global oceanaround
    oceanaround = 0
    if f > 0:
        if data[(i * map.length) + f - 1] == 0:
            oceanaround += 1
    elif data[map.length - i] == 0:
        oceanaround += 1
    if f < map.length - 1:
        if data[(i * map.length) + f + 1] == 0:
            oceanaround += 1
    elif data[((map.length-1)*map.length) + (map.length-i)] == 0:
        oceanaround += 1
    if i > 0:
        if data[((i - 1) * map.length) + f] == 0:
            oceanaround += 1
    elif data[f*map.length] == 0:
        oceanaround += 1
    if i < map.length - 1:
        if data[((i + 1) * map.length) + f] == 0:
            oceanaround += 1
    elif data[f*(map.length-1)+1] == 0:
        oceanaround += 1
for i in range (int(map.length*map.width*1.2)):
    data.append(0)
    biomedata.append(0)
rand = random.randint(0, (map.length*map.width)-1)
rand = int(map.length*map.length/1.75)
for i in range(rand):
    rand = random.randint(0, map.length-1)
    rand2 = random.randint(0, map.width-1)
    data[(rand*map.length)+rand2-1] = 1
numofevo = 0
for i in range(evolutions):
    for i in range(map.length):
        for f in range(map.width):
            rand = 0
            landaround = 0
            if f > 0:
                if data[(i * map.length) + f - 1] == 1:
                    landaround += 1
            elif data[map.length - i] == 1:
                landaround += 1
            if f < map.length - 1:
                if data[(i * map.length) + f + 1] == 1:
                    landaround += 1
            elif data[((map.length - 1) * map.length) + (map.length - i)] == 1:
                landaround += 1
            if i > 0:
                if data[((i - 1) * map.length) + f] == 1:
                    landaround += 1
            elif data[f * map.length] == 1:
                landaround += 1
            if i < map.length - 1:
                if data[((i + 1) * map.length) + f] == 1:
                    landaround += 1
            elif data[f * (map.length - 1) + 1] == 1:
                landaround += 1
            rand = random.randint(1,400)
            if rand <= landaround*100 + amountofblack:
                data[(i * map.length) + f] = 1
            bababooey = False
            if data[(i * map.length) + f] == 1:
                if landaround == 1:
                    #map_image.putpixel((i, f), (int((color1[0] + color7[0])/2), int((color1[1] + color7[1])/2), int((color1[2] + color7[2])/2)))
                    bababooey = True
                if landaround == 2:
                    #map_image.putpixel((i, f), (int((color1[0] + color7[0])/2), int((color1[1] + color7[1])/2), int((color1[2] + color7[2])/2)))
                    bababooey = True
                if landaround == 3:
                    #map_image.putpixel((i, f), (int((color1[0] + color7[0])/2), int((color1[1] + color7[1])/2), int((color1[2] + color7[2])/2)))
                    bababooey = True
                if landaround == 4:
                    rand3 = random.randint(-5, 5)
                    map_image.putpixel((i, f), (color1[0] + rand3, color1[1] + rand3, color1[2] + rand3))
                    bababooey = True
                savedland = (i * map.length) + f
            if numofevo >= evolutions - 28:
                if landaround == 4:
                    if bababooey == True:
                        if biomedata[(i * map.length) + f] == 0:
                            biomedata[(i * map.length) + f] = 1
                        rand3 = random.randint(1, 8000)
                        if rand3 == 1:
                            rand3 = random.randint(1,3)
                            if rand3 == 1:
                                biomedata[(i * map.length) + f] = 3
                            if rand3 == 2:
                                biomedata[(i * map.length) + f] = 4
                            if rand3 == 3:
                                biomedata[(i * map.length) + f] = 1
                        else:
                            if f > 0:
                                whatsaround[0] = biomedata[(i * map.length) + f - 1]
                            else:
                                whatsaround[0] = biomedata[map.length - i]
                            if f < map.length - 1:
                                whatsaround[1] = biomedata[(i * map.length) + f + 1]
                            else:
                                whatsaround[1] = biomedata[((map.length - 1) * map.length) + (map.length - i)]
                            if i > 0:
                                whatsaround[2] = biomedata[((i - 1) * map.length) + f]
                            else:
                                whatsaround[2] = biomedata[f * map.length]
                            if i < map.length - 1:
                                whatsaround[3] = biomedata[((i + 1) * map.length) + f]
                            else:
                                whatsaround[3] = biomedata[f * (map.length - 1) + 1]
                            if whatsaround.count(3) >= 1 and whatsaround.count(4) >= 1:
                                biomedata[(i * map.length) + f] = 2
                            elif whatsaround.count(3) >= 1:
                                rand3 = random.randint(1, 4)
                                if whatsaround.count(3) >= rand3:
                                    biomedata[(i * map.length) + f] = 3
                            elif whatsaround.count(4) >= 1:
                                rand3 = random.randint(1, 4)
                                if whatsaround.count(4) >= rand3:
                                    biomedata[(i * map.length) + f] = 4
                            elif whatsaround.count(2) >= 1:
                                rand3 = random.randint(1, 4)
                                if whatsaround.count(2) >= rand3:
                                    biomedata[(i * map.length) + f] = 2
                            if whatsaround.count(3) >= 1 and whatsaround.count(1) >= 1:
                                if numofevo == evolutions-1:
                                    biomedata[(i * map.length) + f] = 5
                            if whatsaround.count(1) >= 1 and whatsaround.count(4) >= 1:
                                if numofevo == evolutions-1:
                                    biomedata[(i * map.length) + f] = 6
                            #elif whatsaround.count(5) >= 1:
                                #rand3 = random.randint(1, 4)
                                #if whatsaround.count(5) >= rand3:
                                    #biomedata[(i * map.length) + f] = 5
                           # elif whatsaround.count(6) >= 1:
                                #rand3 = random.randint(1, 4)
                                #if whatsaround.count(6) >= rand3:
                                    #biomedata[(i * map.length) + f] = 6

    for i in range(map.length):
        for f in range(map.width):
            rand = 0
            oceancreate()
            rand = random.randint(1,400)
            if rand <= oceanaround*100 - amountofblack:
                data[(i * map.length) + f] = 0
            if data[(i * map.length) + f] == 0:
                if oceanaround == 1:
                    bababooey = True
                    map_image.putpixel((i, f), (int((color1[0] + color7[0])/2), int((color1[1] + color7[1])/2), int((color1[2] + color7[2])/2)))
                if oceanaround == 2:
                    bababooey = True
                    #map_image.putpixel((i, f), (int((color1[0] + color7[0])/2), int((color1[1] + color7[1])/2), int((color1[2] + color7[2])/2)))
                if oceanaround == 3:
                    bababooey = True
                    #map_image.putpixel((i, f), (int((color1[0] + color7[0])/2), int((color1[1] + color7[1])/2), int((color1[2] + color7[2])/2)))
                if oceanaround == 4:
                    if numofevo == evolutions -1:
                        size = 1
                        noland = True
                        cellschecked = []
                        for bogus in range(20):
                            size += 2
                            for a in range(size):
                                for b in range(size):
                                    if a == 0 or a == size-1:
                                    #if cellschecked.count(((i * map.length) + f) - (int((size-1)/2)*(map.length+1))) == 0:
                                        if data[(((i * map.length) + f) - (int((size-1)/2)*(map.length+1))) + b + (a*map.length)-1] == 1:
                                            noland = False
                                            break
                                    elif b == 0 or b == size-1:
                                        if data[(((i * map.length) + f) - (int((size-1)/2)*(map.length+1))) + b + (a*map.length)] == 1:
                                            noland = False
                                            break
                                        #else:
                                            #cellschecked.append((((i * map.length) + f) - (int((size-1)/2)*(map.length+1))) + b + (a*map.length))
                            if noland == False:
                                break
                        #mess with these for darkness of ocean
                        rand3 = random.randint(-8,8)
                        map_image.putpixel((i, f), (color7[0], int(color7[1]-(2.5*size)+rand3), color7[2]))
                    else:
                        map_image.putpixel((i, f), (color7[0], color7[1], color7[2]))
                savedland = (i * map.length) + f
    numofevo += 1
    print(numofevo)
    '''
    if numofevo < 10:
        map_image.save("00"+str(numofevo)+'map_image.png')
    elif numofevo < 100:
        map_image.save("0" + str(numofevo) + 'map_image.png')
    else:
        map_image.save("" + str(numofevo) + 'map_image.png')
    '''
    bumofbevo = numofevo
for i in range(map.length):
    for f in range(map.width):
        if data[(i*map.length) + f] == 1:
            if biomedata[(i * map.length) + f] == 5:
                rand3 = random.randint(-5, 5)
                map_image.putpixel((i, f), (color5[0] + rand3, color5[1] + rand3, color5[2] + rand3))
            if biomedata[(i * map.length) + f] == 6:
                rand3 = random.randint(-5, 5)
                map_image.putpixel((i, f), (color6[0] + rand3, color6[1] + rand3, color6[2] + rand3))
            if biomedata[(i * map.length) + f] == 2:
                rand3 = random.randint(-5, 5)
                map_image.putpixel((i, f), (color2[0] + rand3, color2[1] + rand3, color2[2] + rand3))
            if biomedata[(i * map.length) + f] == 3:
                rand3 = random.randint(-5, 5)
                map_image.putpixel((i, f), (color3[0] + rand3, color3[1] + rand3, color3[2] + rand3))
            if biomedata[(i * map.length) + f] == 4:
                rand3 = random.randint(-5, 5)
                map_image.putpixel((i, f), (color4[0] + rand3, color4[1] + rand3, color4[2] + rand3))
    bumofbevo += 1
#

for i in range(map.length):
    for f in range(map.width):
        #if i == 0 or  i == map.length-1:
            #map_image.putpixel((i, f), (0, 0, 0))
        #elif f == 0 or f == map.width-1:
            #map_image.putpixel((i, f), (0, 0, 0))
        landaround = 0
        if  f > 1:
            if data[(i * map.length) + f - 1] == 1:
                landaround += 1
        if f < map.length - 1:
            if data[(i * map.length) + f + 1] == 1:
                landaround += 1
        if i > 1:
            if data[((i - 1) * map.length) + f] == 1:
                landaround += 1
        if i < map.length - 1:
            if data[((i + 1) * map.length) + f] == 1:
                landaround += 1
        if data[(i * map.length) + f] == 1:
            if landaround == 4:
                #rand3 = random.randint(1, 10000)
                #if rand3 == 1:
                    #rand3 = random.randint(1, 5)
                    #tree = Image.open("D:/Sticks/Pythin/assets/tree" + str(rand3) + ".png")
                    #tree_mask_blur = tree.filter(ImageFilter.GaussianBlur(0.3))
                    #tree_mask = tree_mask_blur.convert("RGBA")
                    #map_image.paste(tree, (i, f-6),tree_mask_blur)
                bababooey = True
            savedland = (i * map.length) + f
map_image.save("map_small_"+str(seed)+".png")
print(map.length)
print(map.width)
print("This took"+ str(int(time.time()-t0)) + "seconds")
print("Which is"+ str((time.time()-t0)/evolutions) +"seconds per evolution")
#cube = Image.new("RGB", (map.length*3, map.length*4), color='black')
#im1 = Image.open("map_small_"+str(seed)+".png")
#cube.paste(im1, (map.length,0))
#im2 = ImageOps.mirror(im1)
#im2 = im2.rotate(180)
#cube.paste(im2, (0,map.length))
#im3 = im1.rotate(270)
#im3 = ImageOps.flip(im3)
#cube.paste(im3, (map.length,map.length))
#im4 = im1.rotate(180)
#cube.paste(im4, (map.length*2,map.length))
#im5 = im1.copy()
#cube.paste(im5, (map.length,map.length*2))
#im6 = im1.rotate(270)
#cube.paste(im6, (map.length,map.length*3))
#cube.save("willthiswork.png")