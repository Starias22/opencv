import cv2 as cv
def save(rpath='../images/cat.jpeg',wpath='output.png'):
    try:
        img=cv.imread(rpath)
        if img is None:#image not read
            print('Unable to read: file not found or wrong input file')
            return
        else:
            cv.imshow('image to write',img)
            cv.waitKey()
            cv.imwrite(wpath,img)
    except cv.error as e:
        print('An cv error occured: ',e)
    except Exception as e:
        print('An unknown exception occured:',e)
    else :
        print('File written successfully')
"""save('wrong')
save('wrong.png')
save(wpath='out')
save(wpath='out.xj')
save(wpath='out.dfj')
save(wpath='out.png')#right
save('normal_cat_img')#right"""

"""build_info=cv.getBuildInformation()
print(build_info)
exit()
# Search for the line that contains "Media I/O" in
# the build information
media_io_start = build_info.find("Media I/O")
media_io_end = build_info.find("\n\n", media_io_start)
media_io_info = build_info[media_io_start:media_io_end]

# Split the "Media I/O" information into lines
# and search for the line that contains "Image codecs:"
media_io_lines = media_io_info.split("\n")
image_codecs_line = next((line for line in media_io_lines
                            if "Image codecs:" in line), None)

# Extract the image file extensions from the "Image codecs:" line
if image_codecs_line is not None:
    image_codecs = image_codecs_line.split(":")[1].strip().split()
    print("Supported image file extensions:", image_codecs)
else:
    print("Unable to find image codecs in build information")"""



img_extensions = ['bmp', 'jpg', 'jpeg', 'jpe', 'jp2', 'png',
                    'webp', 'pbm', 'pgm', 'ppm', 'sr', 'ras', 'tiff', 'tif']

print("Supported image file extensions:", img_extensions)
