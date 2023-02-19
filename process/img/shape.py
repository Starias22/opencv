import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt
drawn=False
radius=10
color=[0,0,0]
thickness=-1
def getImgWithCircle(img,center,radius=radius,color=color,thickness=thickness):
    if img is None:
        return
    try:
        cv.circle(img,center,radius,color,thickness)
        return img
    except cv.error as e:
        print(e)

def drawCircle(inputPath,outputPath,center,radius=10,color=[0,0,0],thickness=-1):
    #img reading
    try:
        wrtable=wrt.iswritable(outputPath)
        if  wrtable is None:
            return
        #try to read the image
        img=reading.read(inputPath)
        #if failure
        if img is None:
            #nothing else to do
            return
        #else
        #get the exetension of the output and input files
        outext=outputPath.split('.')[-1]
        inext=inputPath.split('.')[-1]
        #assert the extension is in the exts list
        assert inext==outext
        img=getImgWithCircle(img,center,radius,color,thickness)
        if img is None:
            return
        if wt.imwrite(img,outputPath):
            print('Circle successfully drawn to',outputPath)

        return None
    except AssertionError as e:
        print(
            'The output image extension ('+outext+')','should be as same',
                'as the input one ('+inext+')'
            )
    except TypeError as e:
        print(e)
    except cv.error as e:
        print('An cv error occured:',e)
    except Exception as e:
        print('An unknown error occured:',e)

def circleDrawingEvent( event, x, y,img, radius=radius, color=color, thickness=thickness,
                    wname='xxx'):
    global drawn;
    drawn=False
    print("**/*/*/*/",img)
    print('Click to draw a circle(Exit in 60s)')
    print('Press Q/q to exit')
    key=cv.waitKey(60000)
    cv.imshow(wname, img)
    if key==ord('q'):
        print("Exit")
        drawn=False
        #cv.destroyWindow(wname)
        return
    #return
    if event == cv.EVENT_LBUTTONUP:
        drawn=True
        print('krfkghk',drawn)
        print('****************')
        cv.circle(img,(x,y),radius,color,thickness)
        if img is None:
            return
        print("Let's go")
        cv.imshow(wname, img)
        print('Your circle is drawn')
        cv.imshow(wname, img)
        cv.waitKey(0)
        return

def  pointDrawingEvent(event,x,y,img,radius,color=color,thickness=thickness):

    if event==cv.EVENT_LBUTTONDOWN:
        img=getImgWithCircle(img,(x,y))
        if img is None:
            return
        sh.show2('Circle drawing',img)
name='circle'

def drawing(inputPath,outputPath,shape='point',params=''):
    write=wrt.iswritable(outputPath)
    if write is None:
        return
    inext=inputPath.split('.')[-1]
    outext=outputPath.split('.')[-1]
    try:
        assert inext==outext
        img=reading.read(inputPath)
        if img is None:
            return
        wname='Image to draw '+shape+' on'
        sh.show2(wname,img)
        wname='Drawing '+shape+' on '+inputPath
        sh.show2(wname,img)

        if shape=='point':
            callback=pointDrawingEvent
        elif shape=='circle':
            callback=lambda event, x, y, flags,param: circleDrawingEvent(event,x, y, img, radius, color, thickness,wname)

        elif shape=='line':
            callback=lineDrawingEvent
        elif shape=='polylines':
            callback=polylinesDrawingEvent
        elif shape=='triangle':
            callback=triangleDrawingEvent
        elif shape=='rectangle':
            callback=rectangleDrawingEvent;
        elif shape=='square':
            callback=squareDrawingEvent
        elif shape=='ellipse':
            callback=ellipseDrawingEvent
        else:
            print('Unknown shape')
            return
        print('Fine***')
        print('calling------')
        print('img',img)
        cv.setMouseCallback(window_name=wname,on_mouse=callback);
        print(drawn)
        if drawn:
            print('Successfully drawn')
            return wts.imwrite(img,outputPath)
        cv.waitKey(0)
        print('called------')

    except AssertionError as e:
        print(
            'The output image extension ('+outext+')','should be as same',
                'as the input one ('+inext+')'
            )
    except RecursionError as e:
        print("reccc---",e)
        return


if __name__=='__main__':
    """drawing('../images/cat.jpeg','')
    drawing('../images/cat.jpeg','out.xml')
    drawing('../images/cat.jpeg','out.bmp')
    drawing('../images/cat.jpeg','out.jpeg')
    drawing('../images/cat.jpeg','draw.jpeg','circe')"""
    drawing('../images/cat.jpeg','draw.jpeg','circle')

if os.path.exists('out.jpeg'):
    os.remove('out.jpeg')
    print('file removed')

if os.path.exists('draw.jpeg'):
    os.remove('draw.jpeg')
    print('file removed')

pass
