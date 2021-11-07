import cv2
import pytesseract
import re
import datefinder

#use pytesseract module
pytesseract.pytesseract.tesseract_cmd = "D:\\tesseract-OCR\\tesseract.exe"
#reed the image
#convert image to RGB based
#OCR the image and extract text and convert it to string
img = cv2.imread('pyproject.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
text = pytesseract.image_to_string(img)

#Open Text file to write all data
text_file = open("data.txt", "w")
#I. find all dates
print("Dates:")
text_file.write('\nDates:')
dates = datefinder.find_dates(text)
for i in dates:
    i = str(i)
    i = i.split(' ')[0]
    print(i)
    text_file.write('\n'+i)

#II. find all room names
print("\n\nRoom names:")
text_file.write('\n\nRoom names:')
Rnames = re.findall(r'Room: \w+', text)
for i in Rnames:
    i = i.replace('Room: ', '')
    print(i)
    text_file.write('\n'+i)

#III. find all room rates
print("\n\nRoom rates:")
text_file.write('\n\nRoom rates:')
rates = re.findall(r'\$+\d+', text)
for i in rates:
    print(i)
    text_file.write('\n'+i)

#IV. find all individual names
print("\n\nIndividual names:")
text_file.write('\n\nIndividual names:')
Inames = re.findall(r'[\w+]+[\s\w.+]+\, +[\w+]+', text)

for i in Inames:
    i = i.split(', ')
    i = i[::-1]
    if 'available' in i:
        del i
    else:
        new_str = ' '.join(i)
        print(new_str)
        text_file.write('\n'+new_str)

#V. find all emails
print("\n\nEmails:")
text_file.write('\n\nEmails:')
emails = re.findall(r'[\w.+-]+@[\s\w-]+\.[\w.-]+', text)
for i in emails:
    print(i)
    text_file.write('\n'+i)


# close file
text_file.close()

#show image
cv2.imshow('result', img)
cv2.waitKey(0)
