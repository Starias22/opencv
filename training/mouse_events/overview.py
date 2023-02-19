import cv2 as cv

#get the list of all the available mouse events in opencv

#mouse_events = [j for j in dir(cv) if 'EVENT' in j]
mouse_events=list()
#browse the directory of opencv: for each element inside,
for j in dir(cv):
    #ifthe object contains the word 'EVENT'
    if 'EVENT' in j:
    #add it to the list of mouse event
        mouse_events.append(j)

print("Opencv provides",len(mouse_events),"mouse events")
print('There are')
for evt in mouse_events:
    print(evt)