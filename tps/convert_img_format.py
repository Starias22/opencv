
import cv2 as cv
img_exts = ['bmp', 'jpg', 'jpeg', 'jpe', 'jp2', 'png',
                    'webp', 'pbm', 'pgm', 'ppm', 'sr', 'ras', 'tiff', 'tif']

def convert(inputPath,outputPath):
    #get the exetension of the output file
    ext=outputPath.split('.')[-1]
    #img reading
    try:
        #try to read the image
        img=cv.imread(inputPath )
        """,cv.IMREAD_GRAYSCALE"""
        if ext is( 'pgm' or 'pbm'):
            if len(img.shape)==3:
                print("You're using",ext,"file etension which doesnt support",
                        'bgr while the input file is bgr','Press O/o if you',
                        'want the output file be a brayscale image.',
                        'Press any key else to exit')
                key=cv.waitKey(0)
                #if O/o not pressed
                if key!=ord('O'):
                    print('Converting aborted!')
                    return
                #else(O/ key is pressed)
                #convert img to rayscale
                img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

        #if failure
        if img is None:
            print('File not found or wrong input file')
            #nothing else to do
            return
        #else
        cv.imshow('Image to convert',img)
        print('File converting: Press a key to continue')
        cv.waitKey()
        #assert the extension is in the exts list
        assert ext in img_exts
        cv.imwrite(outputPath,img)

    except cv.error as e:
        print('An cv error occured: ',e)
    except AssertionError as e:
        print('Output image extension',ext,' not recognized: ',e)
    except Exception as e:
        print('An unknown error occured: ',e)
    else:
        print('Image successfully converted to',ext)
inputPath='../images/apple.jpeg'
"""convert(inputPath,outputPath='')#wrong
convert(inputPath,outputPath='ke')#wrong
convert(inputPath,outputPath='out.org')#wrong"""

convert(inputPath,outputPath='out.png')#right
convert(inputPath,outputPath='out.bmp')#right
convert(inputPath,outputPath='out.jpeg')#right
convert(inputPath,outputPath='out.jpg')#right
convert(inputPath,outputPath='out.jpe')#right
convert(inputPath,outputPath='out.jp2')#right
convert(inputPath,outputPath='out.webp')#right
convert(inputPath,outputPath='out.ras')#right
convert(inputPath,outputPath='out.tiff')#right
convert(inputPath,outputPath='out.tif')#right
convert(inputPath,outputPath='out.sr')#right

convert(inputPath,outputPath='out.ppm')#right # doesn't support grayscale
convert(inputPath,outputPath='out.pgm')#right doesn't support bgr
convert(inputPath,outputPath='out.pbm')#right  doesn't support bgr
