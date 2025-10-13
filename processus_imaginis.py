from PIL import Image
import numpy as np
import sys

###########################
#        FUNCTIONS        #
###########################

def doBrightness(param, arr):
    print("Function doBrightness invoked with param: " + param)
    if arr.ndim == 1: #grayscale
        numColorChannels = 1
        arr = arr.reshape(im.size[1], im.size[0])
    else:
        numColorChannels = arr.shape[1] #RGB/RGBA
        arr = arr.reshape(im.size[1], im.size[0], numColorChannels)
    param = float(param)
    arr = arr + param
    arr[arr > 255] = 255
    arr[arr < 0] = 0
    return arr


def doContrast(param):
    print("Function doContrast invoked with param: " + param)
    print("This is TO BE IMPLEMENTED...")

def saveImage(arr):
    newIm = Image.fromarray(arr.astype(np.uint8))
    newIm.save("result.bmp")



###########################
#           MAIN          #
###########################

if len(sys.argv) == 1:
    print("No command line parameters given.\n")
    sys.exit()

if len(sys.argv) == 2:
    print("Too few command line parameters given.\n")
    sys.exit()

command = sys.argv[1]
param = sys.argv[2]

im = Image.open("Images/Color/lenac.bmp")
arr = np.array(im.getdata())

if command == '--brightness':
    arr = doBrightness(param, arr)
    saveImage(arr)
elif command == '--contrast':
    doContrast(param)
else:
    print("Unknown command: " + command)
print("")

#NOISE FILTER CHOSEN : (N3) Alpha-trimmed mean filter (--alpha), contraharmonic mean filter (--cmean)