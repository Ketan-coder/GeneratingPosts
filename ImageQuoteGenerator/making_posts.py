from itertools import count
import random
import cv2
import textwrap

def get_count():
    count = 0
    try:
        with open("count.txt", "r") as file:
            count = int(file.read())
    finally:
        return count

def write_count(count):
    with open("count.txt", "w") as file:
        file.write(count)

def reset_count():
    with open("count.txt", "w") as file:
        file.write(str('0'))

# reset_count()
count = get_count()
count += 1
write_count(str(count))

def draw_border(img, pt1, pt2, color, thickness, r, d):
    x1,y1 = pt1
    x2,y2 = pt2

    # Top left
    cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)

    # Top right
    cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)

    # Bottom left
    cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)

    # Bottom right
    cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)


# Variables
image = cv2.imread('Template.jpg')
quotes_list = ["I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best._-Marilyn Monroe"
                ,"So many books, so little time_-Marcus Tullius Cicero"
                ,"A room without books is like a body without a soul_-Oscar Wilde"]
fonts_list = [cv2.FONT_HERSHEY_SCRIPT_COMPLEX]
        #Blue,Green,Red
colors = [(238,190,121),(176,147,219),(180,191,247),(43,42,4),(241,241,241)]
num = [1,2,3,4,5,6,7,8,9,10]

# Main Execution
ran_quotes = random.choice(quotes_list)
ran_colors = random.choice(colors[0:2])

ran_num = random.choice(num)

quoter= ran_quotes.split("_")
ran_fonts = random.choice(fonts_list)
quotes = textwrap.wrap(f'Quotes #{count}',width=25)
wrapped_text = textwrap.wrap(quoter[0],width=25)
wrapped_text_quoter = textwrap.wrap(quoter[1],width=25)

rectangle = cv2.rectangle(image, (0, 0),(1080, 1080), ran_colors, -1)
rectangle = cv2.rectangle(image, (100, 100),(975, 975), colors[4], -1)
draw_border(image, (100, 100),(975, 975), ran_colors, 30, 25, 25)

for i, line in enumerate(quotes):
    textsize = cv2.getTextSize(line, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  , 1, 2)[0]
    print(textsize)

    gap = textsize[1] + 5

    y = int(((image.shape[0] + textsize[1]) / 2)/2.5) + i * gap
    x = int(((image.shape[1] - textsize[0]) / 2)/2.5)

    cv2.putText(image, line, (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  , 3, ran_colors, 5, lineType = cv2.LINE_AA)
    cv2.line(image, (200,260),(500,260), ran_colors, 5)

for i, line in enumerate(wrapped_text):
    textsize = cv2.getTextSize(line, ran_fonts, 1, 2)[0]
    print(textsize)

    gap = textsize[1] + 30

    y = int(((image.shape[0] + textsize[1]) / 2)/1.5) + i * gap
    x = int(((image.shape[1] - textsize[0]) / 2) /2)

    cv2.putText(image, line, (x, y), ran_fonts, 2, colors[3], 2, lineType = cv2.LINE_AA)

for i, line in enumerate(wrapped_text_quoter):
    textsize = cv2.getTextSize(line, ran_fonts, 1, 2)[0]
    print(textsize)

    gap = textsize[1] + 90

    x = int((image.shape[1] - textsize[0]) / 2) #width

    if ran_fonts == 7:
        y = (((int((image.shape[0] + textsize[1]) / 2) + i * gap) + i + gap) + i + gap)+ i + gap #height
    elif ran_fonts == 4:
        y = (((int((image.shape[0] + textsize[1]) / 2) + i * gap) + i + gap) + i + gap)+ i + gap #height
        
    cv2.putText(image, line, (x, y), ran_fonts, 1.5, colors[3], 1, lineType = cv2.LINE_AA)

for quotes in range(len(quotes_list)):
    cv2.imshow('Output', image)
    cv2.imwrite(f'Quotes#{count}.jpg', image)
cv2.destroyAllWindows()
quotes_list.remove(ran_quotes)