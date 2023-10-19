
import cv2 as cv 
import numpy as num

# colors 
# values =(blue, green, red) open cv accepts BGR values not RGB
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (255,0,0)
RED = (0,0,255)
CYAN = (255,255,0)
YELLOW =(0,255,255)
MAGENTA = (255,0,255)
GRAY = (128,128,128)
GREEN = (0,255,0)
PURPLE = (128,0,128)
ORANGE = (0,165,255)
PINK = (147,20,255)
points_list =[(200, 300), (150, 150), (400, 200)]
def drawColor(pic, colors):
    x, y = 0,10
    w, h = 20, 30
    
    for color in colors:
        x += w+5 
        # y += 10 
        cv.rectangle(pic, (x-6, y-5 ), (x+w+5, y+h+5), (10, 50, 10), -1)
        cv.rectangle(pic, (x, y ), (x+w, y+h), color, -1)
    
def colorBackgroundText(pic, text, font, fontScale, textPos, textThickness=1,textColor=(0,255,0), bgColor=(0,0,0), pad_x=3, pad_y=3):
    """
    Draws text with background, with  control transparency
    @param pic:(mat) which you want to draw text
    @param text: (string) text you want draw
    @param font: fonts face, like FONT_HERSHEY_COMPLEX, FONT_HERSHEY_PLAIN etc.
    @param fontScale: (double) the size of text, how big it should be.
    @param textPos: tuple(x,y) position where you want to draw text
    @param textThickness:(int) fonts weight, how bold it should be
    @param textPos: tuple(x,y) position where you want to draw text
    @param textThickness:(int) fonts weight, how bold it should be.
    @param textColor: tuple(BGR), values -->0 to 255 each
    @param bgColor: tuple(BGR), values -->0 to 255 each
    @param pad_x: int(pixels)  padding of in x direction
    @param pad_y: int(pixels) 1 to 1.0 (), controls transparency of  text background 
    @return: pic(mat) with draw with background
    """
    (t_w, t_h), _= cv.getTextSize(text, font, fontScale, textThickness) # getting the text size
    x, y = textPos
    cv.rectangle(pic, (x-pad_x, y+ pad_y), (x+t_w+pad_x, y-t_h-pad_y), bgColor,-1) # draw rectangle 
    cv.putText(pic,text, textPos,font, fontScale, textColor,textThickness ) # draw in text
    
    return pic

def textWithBackground(pic, text, font, fontScale, textPos, textThickness=1,textColor=(0,255,0), bgColor=(0,0,0), pad_x=3, pad_y=3, bgOpacity=0.5):
    """
    Draws text with background, with  control transparency
    @param pic:(mat) which you want to draw text
    @param text: (string) text you want draw
    @param font: fonts face, like FONT_HERSHEY_COMPLEX, FONT_HERSHEY_PLAIN etc.
    @param fontScale: (double) the size of text, how big it should be.
    @param textPos: tuple(x,y) position where you want to draw text
    @param textThickness:(int) fonts weight, how bold it should be
    @param textPos: tuple(x,y) position where you want to draw text
    @param textThickness:(int) fonts weight, how bold it should be.
    @param textColor: tuple(BGR), values -->0 to 255 each
    @param bgColor: tuple(BGR), values -->0 to 255 each
    @param pad_x: int(pixels)  padding of in x direction
    @param pad_y: int(pixels) 1 to 1.0 (), controls transparency of  text background 
    @return: pic(mat) with draw with background
    """
    (t_w, t_h), _= cv.getTextSize(text, font, fontScale, textThickness) # getting the text size
    x, y = textPos
    overlay = pic.copy() # coping the image
    cv.rectangle(overlay, (x-pad_x, y+ pad_y), (x+t_w+pad_x, y-t_h-pad_y), bgColor,-1) # draw rectangle 
    new_pic = cv.addWeighted(overlay, bgOpacity, pic, 1 - bgOpacity, 0) # overlaying the rectangle on the image.
    cv.putText(new_pic,text, textPos,font, fontScale, textColor,textThickness ) # draw in text
    pic = new_pic

    return pic


def textBlurBackground(pic, text, font, fontScale, textPos, textThickness=1,textColor=(0,255,0),kneral=(33,33) , pad_x=3, pad_y=3):
    """    
    Draw text with background blurred,  control the blur value, with kernal(odd, odd)
    @param pic:(mat) which you want to draw text
    @param text: (string) text you want draw
    @param font: fonts face, like FONT_HERSHEY_COMPLEX, FONT_HERSHEY_PLAIN etc.
    @param fontScale: (double) the size of text, how big it should be.
    @param textPos: tuple(x,y) position where you want to draw text
    @param textThickness:(int) fonts weight, how bold it should be.
    @param textColor: tuple(BGR), values -->0 to 255 each
    @param kneral: tuple(3,3) int as odd number:  higher the value, more blurry background would be
    @param pad_x: int(pixels)  padding of in x direction
    @param pad_y: int(pixels)  padding of in y direction
    @return: pic mat, with text drawn, with background blurred
    
    call the function: 
     pic =textBlurBackground(pic, 'Blurred Background Text', cv2.FONT_HERSHEY_COMPLEX, 0.9, (20, 60),2, (0,255, 0), (49,49), 13, 13 )
    """
    
    (t_w, t_h), _= cv.getTextSize(text, font, fontScale, textThickness) # getting the text size
    x, y = textPos
    blur_roi = pic[y-pad_y-t_h: y+pad_y, x-pad_x:x+t_w+pad_x] # cropping Text Background
    pic[y-pad_y-t_h: y+pad_y, x-pad_x:x+t_w+pad_x]=cv.blur(blur_roi, kneral)  # merging the blurred background to pic
    cv.putText(pic,text, textPos,font, fontScale, textColor,textThickness )          
    # cv.imnsho('blur roi', blur_roi)
    # cv.imnsho('blurred', pic)

    return pic

def fillPolyTrans(pic, points, color, opacity):
    """
    @param pic: (mat) input image, where shape is drawn.
    @param points: list [tuples(int, int) these are the points custom shape,FillPoly
    @param color: (tuples (int, int, int)
    @param opacity:  it is transparency of image.
    @return: pic(mat) image with rectangle draw.

    """
    list_to_num_array = num.array(points, dtype=num.int32)
    overlay = pic.copy()  # coping the image
    cv.fillPoly(overlay,[list_to_num_array], color )
    new_pic = cv.addWeighted(overlay, opacity, pic, 1 - opacity, 0)
    # print(points_list)
    pic = new_pic
    cv.polylines(pic, [list_to_num_array], True, color,1, cv.LINE_AA)
    return pic

# def pollyLines(pic, points, color):
#     list_to_num_array = num.array(points, dtype=num.int32)
#     cv.polylines(pic, [list_to_num_array], True, color,1, cv.LINE_AA)
#     return pic

def rectTrans(pic, pt1, pt2, color, thickness, opacity):
    """

    @param pic: (mat) input image, where shape is drawn.
    @param pt1: tuple(int,int) it specifies the starting point(x,y) os rectangle
    @param pt2: tuple(int,int)  it nothing but width and height of rectangle
    @param color: (tuples (int, int, int), it tuples of BGR values
    @param thickness: it thickness of board line rectangle, if (-1) passed then rectangle will be fulled with color.
    @param opacity:  it is transparency of image.
    @return:
    """
    overlay = pic.copy()
    cv.rectangle(overlay, pt1, pt2, color, thickness)
    new_pic = cv.addWeighted(overlay, opacity, pic, 1 - opacity, 0) # overlaying the rectangle on the image.
    pic = new_pic

    return pic

def main():
    cap = cv.VideoCapture('Girl.mp4')
    counter =0
    while True:
        success, pic = cap.read()
        # pic = num.zeros((1000,1000, 3), dtype=num.uint8)
        pic=rectTrans(pic, pt1=(30, 320), pt2=(160, 260), color=(0,255,255),thickness=-1, opacity=0.6)
        pic =fillPolyTrans(pic=pic, points=points_list, color=(0,255,0), opacity=.5)
        drawColor(pic, [BLACK,WHITE ,BLUE,RED,CYAN,YELLOW,MAGENTA,GRAY ,GREEN,PURPLE,ORANGE,PINK])
        textBlurBackground(pic, 'Blurred Background Text', cv.FONT_HERSHEY_COMPLEX, 0.8, (60, 140),2, YELLOW, (71,71), 13, 13)
        pic=textWithBackground(pic, 'Colored Background Texts', cv.FONT_HERSHEY_SIMPLEX, 0.8, (60,80), textThickness=2, bgColor=GREEN, textColor=BLACK, bgOpacity=0.7, pad_x=6, pad_y=6)
        picGray = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)
        # cv.imwrite('color_image.png', pic)
        counter +=1
        cv.imnsho('pic', pic)
        cv.imwrite(f'image/image_{counter}.png', pic)
        if cv.waitKey(1) ==ord('q'):
            break

if __name__ == "__main__":
    main()
