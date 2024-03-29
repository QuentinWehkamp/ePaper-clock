import sys
sys.path.insert(1, "./lib")
from PIL import Image, ImageDraw, ImageFont
import epd2in7
import time
from spotify import Spotify
typeface = 'assets/fonts/FreeSansBold.otf'

epd = epd2in7.EPD() # get the display
epd.init()           # initialize the display

startTime = time.localtime()
startClock = [time.strftime("%Y", startTime), time.strftime("%b",startTime), time.strftime("%d",startTime), time.strftime("%a",startTime), time.strftime("%H",startTime), time.strftime("%M",startTime), time.strftime("%S",startTime)]
# 0 = year, 1 = month, 2 = calander day, 3 = weekday, 4 = hour, 5 = minute, 6 = seconds

epd.Clear(0xFF)      # clear the display
    
def printClock(clock):
    Show = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)
    
    draw = ImageDraw.Draw(Show) # Create draw object and pass in the image layer we want to work with (Show)
    font = ImageFont.truetype(typeface, 49) # Create our font, passing in the font file and font size
    dateFont = ImageFont.truetype(typeface, 43)
    
    draw.rectangle((0, 0, epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), fill=None, outline=None, width=4) #screen rectangle
    draw.rectangle((0, 0, 138, 50), fill=None, outline=None, width=3) #time rectangle
    draw.rectangle((135, 0, epd2in7.EPD_HEIGHT, 50), fill=None, outline=None, width=3) #day rectangle
    draw.rectangle((0, 47, epd2in7.EPD_HEIGHT, 91), fill=None, outline=None, width=3) #date rectangle
    draw.line((87, 92, epd2in7.EPD_HEIGHT, 92), fill=None, width=3)
    draw.text((7, -5), clock[4] + ":" + clock[5], font = font, fill = 0) #clock
    draw.text((143, -5), clock[3] , font = font, fill = 0) #day of the week
    draw.text((7, 43), clock[2] + " " + clock[1] + " " + clock[0], font = dateFont, fill = 0) #date
    
    #comment if you don't want to use spotify
    Spotify(Show, draw)
    
    epd.display(epd.getbuffer(Show))

# clock start
printClock(startClock)

while True:
    t = time.localtime()
    clock = [time.strftime("%Y", t), time.strftime("%b", t), time.strftime("%d", t), time.strftime("%a", t), time.strftime("%H", t), time.strftime("%M", t), time.strftime("%S", t)]
    if clock[6] == "00":
        printClock(clock)