import cv2 as cv
import os
img_exts = ['bmp', 'jpg', 'jpeg', 'jpe', 'jp2', 'png',
                    'webp', 'pbm', 'pgm', 'ppm', 'sr', 'ras', 'tiff', 'tif']

def iswritable(outputPath):

    #img reading
    try:
        #if the output path is not valid
        if outputPath =='' :
            raise OSError('Output filename is empty')
        if os.path.isdir(outputPath):
            raise OSError('The output file is a directory')
        if os.path.exists(outputPath):
            raise FileExistsError("The output file already exists")
        ext=outputPath.split('.')[-1]
        if '.' not in outputPath:
            raise AssertionError('Output file without extension')

        if ext not in img_exts:
            raise AssertionError('Output image extension '+ext+' not supported:')
        if '/' not in outputPath:
            dirname=os.getcwd()
        else:
            dirname=os.path.dirname(outputPath)
        #print(dirname)
        if not os.access(dirname, os.W_OK):
            raise PermissionError("You don't have writing permission to the specified output path")
        #try to read the image


    except OSError as e:
        print(e)
    except cv.error as e:
        print('An cv error occured:',e)
    except AssertionError as e:
        print(e)
    except PermissionError as e:
        print(e)

    except Exception as e:
        print('An error occured:')
    else:
        return True

if __name__=='__main__':
    iswritable('')
    iswritable('fkg')
    iswritable('flglg/')
    iswritable('')
    iswritable('file')
    iswritable('djj.cju')
    iswritable('./djj.png')
    iswritable('.')
    print("Test")
    val=iswritable('djj.png')
    print(val)