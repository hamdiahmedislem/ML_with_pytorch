from PIL import Image , ImageDraw
import random

num_img = 360000
img_size = (25,25)

def create(A:int,B:int):
    x1 = random.randint(A,B)
    x2 = random.randint(x1,B)
    y1 = random.randint(A,B)
    y2 = random.randint(y1,B)
    return [int(x1),int(y1),int(x2),int(y2)]

def create_tu(A:int,B:int,nV:int):
    tupl_return = ()
    for i in range(nV) :
        x = random.randint(A,B)
        tupl_return = tupl_return + (x,)
    return tupl_return

for i in range(num_img) :
    img = Image.new("L",img_size,"white")
    if i % 2 == 1 :
        img.save("empty/img"+str(i)+".png")
    else :
        draw = ImageDraw.Draw(img,"L")
        draw.rectangle(create(0,img_size[0]-1),0)
        img.save("notempty/img"+str(i)+".png")