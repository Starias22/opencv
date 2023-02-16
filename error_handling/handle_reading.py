import cv2 as cv

def read(path='normal_cat_img'):#empty, 'jfk',:dosnt exist
    try:
        img=cv.imread(path)
        if img is None:
            print('File not found or wrong input file')
            return
        else:
            cv.imshow('Image',img)
            cv.waitKey(0)
    except cv.error as e:
        print("An cv error occured",e)
    except Exception as e:
        print("An unknown error occured",e)
        print(type(e))
    else :
        print('Any error occured')


read()