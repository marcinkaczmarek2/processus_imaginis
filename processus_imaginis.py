from PIL import Image
import numpy as np
import sys

###########################
#        FUNCTIONS        #
###########################

def doBrightness(factor, image):
    arr = np.array(image.getdata())
    try:
        factor = float(factor)
    except ValueError:
        print("Wrong factor value, image will remain unchanged.")
        return arr
    if arr.ndim == 1: #grayscale i binary
        numColorChannels = 1
        arr = arr.reshape(image.size[1], image.size[0])
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                arr[i][j]+=factor
                if arr[i][j] > 255:
                    arr[i][j] = 255
                elif arr[i][j] < 0:
                    arr[i][j] = 0
    else:
        numColorChannels = arr.shape[1] #RGB/RGBA
        arr = arr.reshape(image.size[1], image.size[0], numColorChannels)
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                for k in range(arr.shape[2]):
                    arr[i][j][k]+=factor
                    if arr[i][j][k] > 255:
                        arr[i][j][k] = 255
                    elif arr[i][j][k] < 0:
                        arr[i][j][k] = 0
    print("Function doBrightness invoked with factor: " + str(factor))
    return arr


def doContrast(factor):
    print("Function doContrast invoked with factor: " + factor)
    print("This is TO BE IMPLEMENTED...")

def doNegative(image):
    arr = np.array(image.getdata())
    if arr.ndim == 1: #grayscale i binary
        numColorChannels = 1
        arr = arr.reshape(image.size[1], image.size[0])
    else:
        numColorChannels = arr.shape[1] #RGB/RGBA
        arr = arr.reshape(image.size[1], image.size[0], numColorChannels)
    arr = 255 - arr
    print("Function doNegative invoked")
    return arr

def saveImage(arr):
    newIm = Image.fromarray(arr.astype(np.uint8))
    newIm.save("result.bmp")
def showHelp():
    print('---------------------------------')
    print('AVAILABLE COMMANDS:')
    print('---------------------------------\n')

    print('(B1) Image brightness modification (--brightness <factor>)')
    print('     Adjusts image brightness by a given factor.\n')

    print('(B2) Image contrast modification (--contrast <factor>)')
    print('     Adjusts image contrast by a given factor.\n')

    print('(B3) Negative (--negative)')
    print('     Inverts pixel intensity values to create a negative image.\n')

    print('(G1) Horizontal flip (--hflip)')
    print('     Flips the image horizontally (mirror along vertical axis).\n')

    print('(G2) Vertical flip (--vflip)')
    print('     Flips the image vertically (mirror along horizontal axis).\n')

    print('(G3) Diagonal flip (--dflip)')
    print('     Flips the image diagonally (transpose across main diagonal).\n')

    print('(G4) Image shrinking (--shrink <scale>)')
    print('     Reduces the image size by the given scale factor (>1).\n')

    print('(G5) Image enlargement (--enlarge <scale>)')
    print('     Enlarges the image by the given scale factor (>1)\n.')

    print('(N3a) Alpha-trimmed mean filter (--alpha <window_size> <alpha>)')
    print('     Reduces noise by trimming extreme pixel values in a neighborhood.')
    print('     <window_size>: int, e.g. 3 for a 3x3 window.')
    print('     <alpha>: int, number of pixels discarded from both ends.\n')

    print('(N3b) Contraharmonic mean filter (--cmean <window_size> <Q>)')
    print('     Removes salt or pepper noise using the contraharmonic mean.')
    print('     <window_size>: int, e.g. 3 for a 3x3 window.')
    print('     <Q>: float, >0 for pepper noise, <0 for salt noise.\n')

    print('(E1) Mean Square Error (--mse <image1> <image2>)')
    print('     Calculates the mean squared error between two images.\n')

    print('(E2) Peak Mean Square Error (--pmse <image1> <image2>)')
    print('     Computes the peak mean square error (emphasizes peak differences).\n')

    print('(E3) Signal to Noise Ratio (--snr <image1> <image2>)')
    print('     Computes the signal-to-noise ratio in decibels (dB).\n')

    print('(E4) Peak Signal to Noise Ratio (--psnr <image1> <image2>)')
    print('     Computes the peak signal-to-noise ratio (PSNR) in dB.\n')

    print('(E5) Maximum Difference (--md <image1> <image2>)')
    print('     Calculates the maximum absolute pixel difference between two images.\n')

    print('---------------------------------')
    print('Example usage:')
    print('  python processus_imaginis.py --contrast 1.5')
    print('  python processus_imaginis.py --alpha 3 2')
    print('  python processus_imaginis.py --psnr original.png processed.png')
    print('---------------------------------')




###########################
#           MAIN          #
###########################

if '--help' in sys.argv:
    showHelp()
    sys.exit()

if len(sys.argv) < 3:
    print("Too few command line parameters given.\n")
    print("Use '--help' to see available commands.")
    sys.exit()

photo = sys.argv[1]
command = sys.argv[2]

if (len(sys.argv)>3):
    factor = sys.argv[3]

try:
    image = Image.open("Images/" + photo)
except FileNotFoundError:
    print("Wrong image name. Finishing program...")
    sys.exit()

if command == '--brightness':
    arr = doBrightness(factor, image)
    saveImage(arr)
elif command == '--contrast':
    doContrast(factor)
elif command == '--negative':
    arr = doNegative(image)
    saveImage(arr)
else:
    print("Unknown command: " + command)
print("")

#NOISE FILTER CHOSEN : (N3) Alpha-trimmed mean filter (--alpha), contraharmonic mean filter (--cmean)