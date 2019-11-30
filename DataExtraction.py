from PIL import Image
import pytesseract
import argparse
import cv2
import os
import parsedatetime
from dateutil.parser import parse
import nltk
import datefinder,glob

filenames = glob.glob("images/*.*")

images = [cv2.imread(img) for img in filenames]

output = open('output.txt','w')

for img in filenames:
    print(img)
    output.write(img+'\n')
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))

    try:
        matches = datefinder.find_dates(text)
        for match in matches:
            ans = match
            print(match)
            output.write(str(match)+'\n')
    except:
        ans = 'Error'
        output.write(ans + '\n')
    output.write('\n\n')
