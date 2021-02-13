import cv2
from matplotlib import pyplot as plt

print("1 - Horizontal Left / (y,x-1)")
print("2 - Horizontal Right / ((y,x+1)")
print("3 - Vertical Up / (y-1,x)")
print("4 - Vertical Down / (y+1,x)")
print("5 - Diagonal Top Left / (y-1,x-1)")
print("6 - Diagonal Top Right / (y-1,x+1)")
print("7 - Diagonal Bottom Left / (y+1,x-1)")
print("8 - Diagonal Bottom Right / (y+1,x+1)")
text = input("Type a number for the pixel neighbor relationship you'd like to select:") #User inputs numbers 1 - 8 for neighbor relationship

file = input("Type the path for the image you would like to use:") #User inputs image path
image = cv2.imread(file) #Saves the bgr image to image
greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converts image to greyscale and saves to greyImage

imageWidth = image.shape[1] #Saves the number of horizontal pixels to imageWidth
imageHeight = image.shape[0] #Saves the number of vertical pixels to imageHeight

#Initializing variables used in evaluating pixel - neighbor relationship
xPosition = 0
yPosition = 0

xNeighbor = 0
yNeighbor = 0

#Initializes lists used for tracking difference values obtained from each color format
greyList = []
bgrList = []
hsvList = []
labList = []

while(xPosition < imageWidth): #Loops through each row
    while (yPosition < imageHeight): #Loops through each column

        centerPixel = greyImage[yPosition, xPosition] #Sets centerPixel to the intensity value for the current x and y pixel position

        #The following functions initialize the Neighbor pixel based on the relationship selected by the user.
        #If the neighbor is valid, the squared of the difference is found between the pixel and its neighbor and append to the appropriate list.
        if(text == '1'):
            xNeighbor = xPosition - 1
            if(xNeighbor >= 0):
                Neighbor = greyImage[yPosition, xNeighbor]
                difference = abs(int(centerPixel) - int(Neighbor))
                greyList.append(difference)

        if(text == '2'):
            xNeighbor = xPosition + 1
            if(xNeighbor <= imageWidth - 1):
                Neighbor = greyImage[yPosition, xNeighbor]
                difference = abs(int(centerPixel) - int(Neighbor))
                greyList.append(difference)

        if(text == '3'):
            yNeighbor = yPosition - 1
            if(yNeighbor >= 0):
                Neighbor = greyImage[yNeighbor, xPosition]
                difference = abs(int(centerPixel) - int(Neighbor))
                greyList.append(difference)

        if(text == '4'):
            yNeighbor = yPosition + 1
            if(yNeighbor <= imageHeight - 1):
                Neighbor = greyImage[yNeighbor, xPosition]
                difference = abs(int(centerPixel) - int(Neighbor))
                greyList.append(difference)

        if(text == '5'):
            xNeighbor = xPosition - 1
            yNeighbor = yPosition - 1
            if(xNeighbor >= 0 and yNeighbor >= 0):
                Neighbor = greyImage[yNeighbor, xNeighbor]
                difference = abs(int(centerPixel) - int(Neighbor))
                greyList.append(difference)

        if(text == '6'):
            xNeighbor = xPosition + 1
            yNeighbor = yPosition - 1
            if(xNeighbor <= imageWidth - 1 and yNeighbor >= 0):
                Neighbor = greyImage[yNeighbor, xNeighbor]
                difference = abs(int(centerPixel) - int(Neighbor))
                greyList.append(difference)

        if(text == '7'):
            xNeighbor = xPosition - 1
            yNeighbor = yPosition + 1
            if(xNeighbor >= 0 and yNeighbor <= imageHeight - 1):
                Neighbor = greyImage[yNeighbor, xNeighbor]
                difference = abs(int(centerPixel) - int(Neighbor))
                greyList.append(difference)

        if(text == '8'):
            xNeighbor = xPosition + 1
            yNeighbor = yPosition + 1
            if(xNeighbor <= imageWidth - 1 and yNeighbor <= imageHeight - 1):
                Neighbor = greyImage[yNeighbor, xNeighbor]
                difference = abs(int(centerPixel) - int(Neighbor))
                greyList.append(difference)

        yPosition = yPosition + 1 #Increment Y position by 1

    yPosition = 0
    xPosition = xPosition + 1 #Increment X position by 1



plt.hist(greyList, 256) #The histogram evaluates the values contained in the list
plt.xlabel("Number difference between pixels")
plt.ylabel("Number of times difference is counted")
plt.title("Intensity Histogram")
plt.show()

#Initializing variables used in evaluating pixel - neighbor relationship
xPosition = 0
yPosition = 0

xNeighbor = 0
yNeighbor = 0

while(xPosition < imageWidth): #Loops through each row
    while(yPosition < imageHeight): #Loops through each column

        bCenterPixel = image[yPosition, xPosition,0] #Sets bCenterPixel to number for the blue intensity for the current x and y pixel position
        gCenterPixel = image[yPosition, xPosition,1] #Sets gCenterPixel to number for the green intensity for the current x and y pixel position
        rCenterPixel = image[yPosition, xPosition,2] #Sets rCenterPixel to number for the red intensity for the current x and y pixel position

        # The following functions initialize the Neighbor pixel based on the relationship selected by the user.
        # If the neighbor is valid, the squared of the difference is found between the pixel and its neighbor and append to the appropriate list.
        if(text == '1'):
            xNeighbor = xPosition - 1
            if(xNeighbor >= 0):
                bNeighbor = image[yPosition, xNeighbor,0]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                gNeighbor = image[yPosition, xNeighbor,1]
                gDifference = abs(int(gCenterPixel) - int(gNeighbor))
                rNeighbor = image[yPosition, xNeighbor,2]
                rDifference = abs(int(rCenterPixel) - int(rNeighbor))
                difference = bDifference + gDifference + rDifference
                bgrList.append(difference)

        if(text == '2'):
            xNeighbor = xPosition + 1
            if(xNeighbor <= imageWidth - 1):
                bNeighbor = image[yPosition, xNeighbor, 0]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                gNeighbor = image[yPosition, xNeighbor, 1]
                gDifference = abs(int(gCenterPixel) - int(gNeighbor))
                rNeighbor = image[yPosition, xNeighbor, 2]
                rDifference = abs(int(rCenterPixel) - int(rNeighbor))
                difference = bDifference + gDifference + rDifference
                bgrList.append(difference)

        if(text == '3'):
            yNeighbor = yPosition - 1
            if(yNeighbor >= 0):
                bNeighbor = image[yNeighbor, xPosition, 0]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                gNeighbor = image[yNeighbor, xPosition, 1]
                gDifference = abs(int(gCenterPixel) - int(gNeighbor))
                rNeighbor = image[yNeighbor, xPosition, 2]
                rDifference = abs(int(rCenterPixel) - int(rNeighbor))
                difference = bDifference + gDifference + rDifference
                bgrList.append(difference)

        if(text == '4'):
            yNeighbor = yPosition + 1
            if(yNeighbor <= imageHeight - 1):
                bNeighbor = image[yNeighbor, xPosition, 0]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                gNeighbor = image[yNeighbor, xPosition, 1]
                gDifference = abs(int(gCenterPixel) - int(gNeighbor))
                rNeighbor = image[yNeighbor, xPosition, 2]
                rDifference = abs(int(rCenterPixel) - int(rNeighbor))
                difference = bDifference + gDifference + rDifference
                bgrList.append(difference)

        if(text == '5'):
            xNeighbor = xPosition - 1
            yNeighbor = yPosition - 1
            if(xNeighbor >= 0 and yNeighbor >= 0):
                bNeighbor = image[yNeighbor, xNeighbor, 0]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                gNeighbor = image[yNeighbor, xNeighbor, 1]
                gDifference = abs(int(gCenterPixel) - int(gNeighbor))
                rNeighbor = image[yNeighbor, xNeighbor, 2]
                rDifference = abs(int(rCenterPixel) - int(rNeighbor))
                difference = bDifference + gDifference + rDifference
                bgrList.append(difference)

        if(text == '6'):
            xNeighbor = xPosition + 1
            yNeighbor = yPosition - 1
            if(xNeighbor <= imageWidth - 1 and yNeighbor >= 0):
                bNeighbor = image[yNeighbor, xNeighbor, 0]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                gNeighbor = image[yNeighbor, xNeighbor, 1]
                gDifference = abs(int(gCenterPixel) - int(gNeighbor))
                rNeighbor = image[yNeighbor, xNeighbor, 2]
                rDifference = abs(int(rCenterPixel) - int(rNeighbor))
                difference = bDifference + gDifference + rDifference
                bgrList.append(difference)

        if(text == '7'):
            xNeighbor = xPosition - 1
            yNeighbor = yPosition + 1
            if(xNeighbor >= 0 and yNeighbor <= imageHeight - 1):
                bNeighbor = image[yNeighbor, xNeighbor, 0]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                gNeighbor = image[yNeighbor, xNeighbor, 1]
                gDifference = abs(int(gCenterPixel) - int(gNeighbor))
                rNeighbor = image[yNeighbor, xNeighbor, 2]
                rDifference = abs(int(rCenterPixel) - int(rNeighbor))
                difference = bDifference + gDifference + rDifference
                bgrList.append(difference)

        if(text == '8'):
            xNeighbor = xPosition + 1
            yNeighbor = yPosition + 1
            if(xNeighbor <= imageWidth - 1 and yNeighbor <= imageHeight - 1):
                bNeighbor = image[yNeighbor, xNeighbor, 0]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                gNeighbor = image[yNeighbor, xNeighbor, 1]
                gDifference = abs(int(gCenterPixel) - int(gNeighbor))
                rNeighbor = image[yNeighbor, xNeighbor, 2]
                rDifference = abs(int(rCenterPixel) - int(rNeighbor))
                difference = bDifference + gDifference + rDifference
                bgrList.append(difference)

        yPosition = yPosition + 1 #Increment Y position by 1

    yPosition = 0
    xPosition = xPosition + 1 #Increment X position by 1

plt.hist(bgrList, 256) #The histogram evaluates the values contained in the list
plt.xlabel("Number difference between pixels")
plt.ylabel("Number of times difference is counted")
plt.title("RGB Histogram")
plt.show()


#Initializing variables used in evaluating pixel - neighbor relationship
xPosition = 0
yPosition = 0

xNeighbor = 0
yNeighbor = 0

hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #Converts image to hsv and saves the hsv image to hsvImage

while(xPosition < imageWidth): #Loops through each row
    while(yPosition < imageHeight): #Loops through each column

        hCenterPixel = hsvImage[yPosition, xPosition,0] #Sets hCenterPixel to number for the hue of the current x and y pixel position
        sCenterPixel = hsvImage[yPosition, xPosition,1] #Sets sCenterPixel to number for the saturation for the current x and y pixel position
        vCenterPixel = hsvImage[yPosition, xPosition,2] #Sets vCenterPixel to number for the intensity for the current x and y pixel position

        # The following functions initialize the Neighbor pixel based on the relationship selected by the user.
        # If the neighbor is valid, the squared of the difference is found between the pixel and its neighbor and append to the appropriate list.
        if(text == '1'):
            xNeighbor = xPosition - 1
            if(xNeighbor >= 0):
                hNeighbor = hsvImage[yPosition, xNeighbor,0]
                hDifference = abs(int(hCenterPixel) - int(hNeighbor))
                sNeighbor = hsvImage[yPosition, xNeighbor,1]
                sDifference = abs(int(sCenterPixel) - int(sNeighbor))
                vNeighbor = hsvImage[yPosition, xNeighbor, 2]
                vDifference = abs(int(vCenterPixel) - int(vNeighbor))
                difference = hDifference + sDifference + vDifference
                hsvList.append(difference)

        if(text == '2'):
            xNeighbor = xPosition + 1
            if(xNeighbor <= imageWidth - 1):
                hNeighbor = hsvImage[yPosition, xNeighbor, 0]
                hDifference = abs(int(hCenterPixel) - int(hNeighbor))
                sNeighbor = hsvImage[yPosition, xNeighbor, 1]
                sDifference = abs(int(sCenterPixel) - int(sNeighbor))
                vNeighbor = hsvImage[yPosition, xNeighbor, 2]
                vDifference = abs(int(vCenterPixel) - int(vNeighbor))
                difference = hDifference + sDifference + vDifference
                hsvList.append(difference)

        if(text == '3'):
            yNeighbor = yPosition - 1
            if(yNeighbor >= 0):
                hNeighbor = hsvImage[yNeighbor, xPosition, 0]
                hDifference = abs(int(hCenterPixel) - int(hNeighbor))
                sNeighbor = hsvImage[yNeighbor, xPosition, 1]
                sDifference = abs(int(sCenterPixel) - int(sNeighbor))
                vNeighbor = hsvImage[yNeighbor, xPosition, 2]
                vDifference = abs(int(vCenterPixel) - int(vNeighbor))
                difference = hDifference + sDifference + vDifference
                hsvList.append(difference)

        if(text == '4'):
            yNeighbor = yPosition + 1
            if(yNeighbor <= imageHeight - 1):
                hNeighbor = hsvImage[yNeighbor, xPosition, 0]
                hDifference = abs(int(hCenterPixel) - int(hNeighbor))
                sNeighbor = hsvImage[yNeighbor, xPosition, 1]
                sDifference = abs(int(sCenterPixel) - int(sNeighbor))
                vNeighbor = hsvImage[yNeighbor, xPosition, 2]
                vDifference = abs(int(vCenterPixel) - int(vNeighbor))
                difference = hDifference + sDifference + vDifference
                hsvList.append(difference)

        if(text == '5'):
            xNeighbor = xPosition - 1
            yNeighbor = yPosition - 1
            if(xNeighbor >= 0 and yNeighbor >= 0):
                hNeighbor = hsvImage[yNeighbor, xNeighbor, 0]
                hDifference = abs(int(hCenterPixel) - int(hNeighbor))
                sNeighbor = hsvImage[yNeighbor, xNeighbor, 1]
                sDifference = abs(int(sCenterPixel) - int(sNeighbor))
                vNeighbor = hsvImage[yNeighbor, xNeighbor, 2]
                vDifference = abs(int(vCenterPixel) - int(vNeighbor))
                difference = hDifference + sDifference + vDifference
                hsvList.append(difference)

        if(text == '6'):
            xNeighbor = xPosition + 1
            yNeighbor = yPosition - 1
            if(xNeighbor <= imageWidth - 1 and yNeighbor >= 0):
                hNeighbor = hsvImage[yNeighbor, xNeighbor, 0]
                hDifference = abs(int(hCenterPixel) - int(hNeighbor))
                sNeighbor = hsvImage[yNeighbor, xNeighbor, 1]
                sDifference = abs(int(sCenterPixel) - int(sNeighbor))
                vNeighbor = hsvImage[yNeighbor, xNeighbor, 2]
                vDifference = abs(int(vCenterPixel) - int(vNeighbor))
                difference = hDifference + sDifference + vDifference
                hsvList.append(difference)

        if(text == '7'):
            xNeighbor = xPosition - 1
            yNeighbor = yPosition + 1
            if(xNeighbor >= 0 and yNeighbor <= imageHeight - 1):
                hNeighbor = hsvImage[yNeighbor, xNeighbor, 0]
                hDifference = abs(int(hCenterPixel) - int(hNeighbor))
                sNeighbor = hsvImage[yNeighbor, xNeighbor, 1]
                sDifference = abs(int(sCenterPixel) - int(sNeighbor))
                vNeighbor = hsvImage[yNeighbor, xNeighbor, 2]
                vDifference = abs(int(vCenterPixel) - int(vNeighbor))
                difference = hDifference + sDifference + vDifference
                hsvList.append(difference)

        if(text == '8'):
            xNeighbor = xPosition + 1
            yNeighbor = yPosition + 1
            if(xNeighbor <= imageWidth - 1 and yNeighbor <= imageHeight - 1):
                hNeighbor = hsvImage[yNeighbor, xNeighbor, 0]
                hDifference = abs(int(hCenterPixel) - int(hNeighbor))
                sNeighbor = hsvImage[yNeighbor, xNeighbor, 1]
                sDifference = abs(int(sCenterPixel) - int(sNeighbor))
                vNeighbor = hsvImage[yNeighbor, xNeighbor, 2]
                vDifference = abs(int(vCenterPixel) - int(vNeighbor))
                difference = hDifference + sDifference + vDifference
                hsvList.append(difference)

        yPosition = yPosition + 1 #Increment Y position by 1

    yPosition = 0
    xPosition = xPosition + 1 #Increment X position by 1

plt.hist(hsvList, 256) #The histogram evaluates the values contained in the list
plt.xlabel("Number difference between pixels")
plt.ylabel("Number of times difference is counted")
plt.title("HSV Histogram")
plt.show()

#Initializing variables used in evaluating pixel - neighbor relationship
xPosition = 0
yPosition = 0

xNeighbor = 0
yNeighbor = 0

labImage = cv2.cvtColor(image, cv2.COLOR_BGR2LAB) #Converts image to Lab and saves the Lab image to labImage

while(xPosition < imageWidth): #Loops through each row
    while(yPosition < imageHeight): #Loops through each column

        lCenterPixel = labImage[yPosition, xPosition,0] #Sets lCenterPixel to number for the intensity for the current x and y pixel position
        aCenterPixel = labImage[yPosition, xPosition,1] #Sets aCenterPixel to number for the a color channel for the current x and y pixel position
        bCenterPixel = labImage[yPosition, xPosition,2] #Sets bCenterPixel to number for the b color channel for the current x and y pixel position

        # The following functions initialize the Neighbor pixel based on the relationship selected by the user.
        # If the neighbor is valid, the squared of the difference is found between the pixel and its neighbor and append to the appropriate list.
        if(text == '1'):
            xNeighbor = xPosition - 1
            if(xNeighbor >= 0):
                lNeighbor = labImage[yPosition, xNeighbor,0]
                lDifference = abs(int(lCenterPixel) - int(lNeighbor))
                aNeighbor = labImage[yPosition, xNeighbor,1]
                aDifference = abs(int(aCenterPixel) - int(aNeighbor))
                bNeighbor = labImage[yPosition, xNeighbor, 2]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                difference = lDifference + aDifference + bDifference
                labList.append(difference)

        if(text == '2'):
            xNeighbor = xPosition + 1
            if(xNeighbor <= imageWidth - 1):
                lNeighbor = labImage[yPosition, xNeighbor, 0]
                lDifference = abs(int(lCenterPixel) - int(lNeighbor))
                aNeighbor = labImage[yPosition, xNeighbor, 1]
                aDifference = abs(int(aCenterPixel) - int(aNeighbor))
                bNeighbor = labImage[yPosition, xNeighbor, 2]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                difference = lDifference + aDifference + bDifference
                labList.append(difference)

        if(text == '3'):
            yNeighbor = yPosition - 1
            if(yNeighbor >= 0):
                lNeighbor = labImage[yNeighbor, xPosition, 0]
                lDifference = abs(int(lCenterPixel) - int(lNeighbor))
                aNeighbor = labImage[yNeighbor, xPosition, 1]
                aDifference = abs(int(aCenterPixel) - int(aNeighbor))
                bNeighbor = labImage[yNeighbor, xPosition, 2]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                difference = lDifference + aDifference + bDifference
                labList.append(difference)

        if(text == '4'):
            yNeighbor = yPosition + 1
            if(yNeighbor <= imageHeight - 1):
                lNeighbor = labImage[yNeighbor, xPosition, 0]
                lDifference = abs(int(lCenterPixel) - int(lNeighbor))
                aNeighbor = labImage[yNeighbor, xPosition, 1]
                aDifference = abs(int(aCenterPixel) - int(aNeighbor))
                bNeighbor = labImage[yNeighbor, xPosition, 2]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                difference = lDifference + aDifference + bDifference
                labList.append(difference)

        if(text == '5'):
            xNeighbor = xPosition - 1
            yNeighbor = yPosition - 1
            if(xNeighbor >= 0 and yNeighbor >= 0):
                lNeighbor = labImage[yNeighbor, xNeighbor, 0]
                lDifference = abs(int(lCenterPixel) - int(lNeighbor))
                aNeighbor = labImage[yNeighbor, xNeighbor, 1]
                aDifference = abs(int(aCenterPixel) - int(aNeighbor))
                bNeighbor = labImage[yNeighbor, xNeighbor, 2]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                difference = lDifference + aDifference + bDifference
                labList.append(difference)

        if(text == '6'):
            xNeighbor = xPosition + 1
            yNeighbor = yPosition - 1
            if(xNeighbor <= imageWidth - 1 and yNeighbor >= 0):
                lNeighbor = labImage[yNeighbor, xNeighbor, 0]
                lDifference = abs(int(lCenterPixel) - int(lNeighbor))
                aNeighbor = labImage[yNeighbor, xNeighbor, 1]
                aDifference = abs(int(aCenterPixel) - int(aNeighbor))
                bNeighbor = labImage[yNeighbor, xNeighbor, 2]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                difference = lDifference + aDifference + bDifference
                labList.append(difference)

        if(text == '7'):
            xNeighbor = xPosition - 1
            yNeighbor = yPosition + 1
            if(xNeighbor >= 0 and yNeighbor <= imageHeight - 1):
                lNeighbor = labImage[yNeighbor, xNeighbor, 0]
                lDifference = abs(int(lCenterPixel) - int(lNeighbor))
                aNeighbor = labImage[yNeighbor, xNeighbor, 1]
                aDifference = abs(int(aCenterPixel) - int(aNeighbor))
                bNeighbor = labImage[yNeighbor, xNeighbor, 2]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                difference = lDifference + aDifference + bDifference
                labList.append(difference)

        if(text == '8'):
            xNeighbor = xPosition + 1
            yNeighbor = yPosition + 1
            if(xNeighbor <= imageWidth - 1 and yNeighbor <= imageHeight - 1):
                lNeighbor = labImage[yNeighbor, xNeighbor, 0]
                lDifference = abs(int(lCenterPixel) - int(lNeighbor))
                aNeighbor = labImage[yNeighbor, xNeighbor, 1]
                aDifference = abs(int(aCenterPixel) - int(aNeighbor))
                bNeighbor = labImage[yNeighbor, xNeighbor, 2]
                bDifference = abs(int(bCenterPixel) - int(bNeighbor))
                difference = lDifference + aDifference + bDifference
                labList.append(difference)

        yPosition = yPosition + 1 #Increment Y position by 1

    yPosition = 0
    xPosition = xPosition + 1 #Increment X position by 1

plt.hist(labList, 256) #The histogram evaluates the values contained in the list
plt.xlabel("Number difference between pixels")
plt.ylabel("Number of times difference is counted")
plt.title("Lab Histogram")
plt.show()
