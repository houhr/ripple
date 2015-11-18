#!/usr/bin/env python

# 0   1   2   3   4   5   6   7
# 8   9   10  11  12  13  14  15
# 16  17  18  19  20  21  22  23
# 24  25  26  27  28  29  30  31
# 32  33  34  35  36  37  38  39
# 40  41  42  43  44  45  46  47
# 48  49  50  51  52  53  54  55
# 56  57  58  59  60  61  62  63

import sys, re, nltk
import getopt, os, urllib, subprocess as sub
import urllib2
import json
import opc, time, random
from weathercom import get_weathercom
from google_api import get_google_asr
from tts import tts

numLEDs = 64
client = opc.Client('localhost:7890')
pixels = [ (0,0,0) ] * numLEDs

w = [[]] * 16

w[1] = [0]
w[2] = [1, 8]
w[3] = [2, 9, 16]
w[4] = [3, 10, 17, 24]
w[5] = [4, 11, 18, 25, 32]
w[6] = [5, 12, 19, 26, 33, 40]
w[7] = [6, 13, 20, 27, 34, 41, 48]
w[8] = [7, 14, 21, 28, 35, 42, 49, 56]
w[9] = [15, 22, 29, 36, 43, 50, 57]
w[10] = [23, 30, 37, 44, 51, 58]
w[11] = [31, 38, 45, 52, 59]
w[12] = [39, 46, 53, 60]
w[13] = [47, 54, 61]
w[14] = [55, 62]
w[15] = [63]

def turnOffAll():
    for i in range(numLEDs):
        pixels[i] = (0, 0, 0)
        client.put_pixels(pixels)

def showCentralDot(a, c):
    turnOffAll()
    for num in range(1, 11):
        for i in a:
            pixels[i] = (int(c[0] / 10 * num), int(c[1] / 10 * num), int(c[2] / 10 * num))
        client.put_pixels(pixels)
        time.sleep(0.1)

def generateRandomColor():
    i = int(random.randrange(0, 256))
    return (i*i%255, i*i*i%255, i*i*i*i%255)

if __name__=="__main__":

    #read command line arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:c:",
                                   ["help", "units=", "current_city="])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)


    # parse command line arguments
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-u", "--units"):
            default_unit = a
        elif o in ("-c", "--current_city"):
            default_city = a
        else:
            assert False, "unknown option"

    print "Hi, I'm WeatherBot built by Hongru Hou"   # modify this line to add the name of your bot.


    stopped = False
    is_first_question = True
    while not stopped:

        # Step 1: get the user input
        # user_input = raw_input(question)
        # user_input = get_google_asr()
        user_input = "application"

        print user_input
        user_input = user_input.lower()
        words = user_input.split()

        for word in words:
            if (len(word) <= 15):
                length = len(word)
            else:
                length = 15

            i = int(random.randrange(0, 256))
            # showCentralDot(w[length], (i*i%255, i*i*i%255, i*i*i*i%255))
            for index in range(1, (length + 1)):
                i = int(random.randrange(0, 256))
                showCentralDot(w[index], (i*i%255, i*i*i%255, i*i*i*i%255))
            time.sleep(0.5)
            for index in range(0, length):
                i = int(random.randrange(0, 256))
                showCentralDot(w[length - 1 - index], (i*i%255, i*i*i%255, i*i*i*i%255))


        # check if the user wants to quit
        if user_input == "quit":
            break # exit the loop right away

        #parse location
        # tokens = nltk.word_tokenize(user_input)
        # tagged = nltk.pos_tag(tokens)
        # chunk = nltk.chunk.ne_chunk(tagged)
        # chunk.draw()
