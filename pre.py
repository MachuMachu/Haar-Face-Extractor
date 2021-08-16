import cv2 as cv,numpy as num, os

haar_cascade = cv.CascadeClassifier("haar/haar_face_front.xml")

path="in/"
people = os.listdir(path)

def extractFaces(people):
    try:
        for person in people:
            if person.find('.')==-1: #if not a file
                folder = path+person+"/"
                
                directory = "./out/"+person+"/" #create out directory
                if not os.path.exists(directory):
                    if not os.path.exists("out"):
                        os.mkdir("out")
                    os.mkdir(directory)
                images=os.listdir(folder)
                for image in images:
                    imgpath=folder+image
                    print("opening: "+imgpath)
                    img = cv.imread(imgpath)
                    print("image size: "+str(img.shape[:2]))
                    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                    faces = haar_cascade.detectMultiScale(img, 1.1, 5)
                    maxx=0
                    maxy=0
                    larger=0
                    for index,(x,y,w,h) in enumerate(faces):
                            if(x+w>maxx and y+h>maxy):
                                maxx=img.shape[1]-(x+w)
                                maxy=img.shape[0]-(y+h)
                                larger = index
                            face=img[y:y+h, x:x+w]
                            if(face.shape[0]>100 and face.shape[1]>100):
                                try:
                                    if(larger):
                                        if cv.imwrite(directory+image+"_index-"+str(larger)+"_largest.png",face):
                                            print("Largest- Width: "+str(face.shape[0])+"Height: "+str(face.shape[1]))
                                            print("Image succesfully created.")
                                    else:
                                        if cv.imwrite(directory+image+"_index-"+str(index)+".png",face):
                                            print("Width: "+str(face.shape[0])+"Height: "+str(face.shape[1]))
                                            print("Image created.")
                                except Exception as e:
                                    print(e)
                            
                    print("#of faces: "+str(len(faces))+" largest face is index: "+str(larger)+"\n")
    except Exception as e:
        print(e)


extractFaces(people)
