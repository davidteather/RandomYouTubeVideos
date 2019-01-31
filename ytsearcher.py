import random, string, time, json, requests, webbrowser, os, logging

# How long the generated video tag should be
vidtaglength = 11

# Delay after each if video exist to prevent timeouts
# I'm not responsible if you change this to DDOS levels
videocheckexistdelay = 10

# If Console Logging should be enabled
consolelogging = False

# Time Sleep after every video is found consolelogging must be on
sleepatend = 60

# Log file
logfile = "youtubefound.log"
filelogging = False

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


def usr_input():
    # Asks user for how many tabs they would like to open
    while True:
        try:
            tabs = int(input("How many random tabs would you like to open?" + os.linesep))
        except ValueError:
            print("That is not a valid integer." + os.linesep + "If you believe this is an error make a"
                                                                "n issue report on https://github.com/davidteath"
                                                                "er/Random-Youtube" + os.linesep)
            continue
        else:
            return tabs
            break


def check_vid(consolelogging, vidval):
    r = requests.post(
        'https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v=' + str(vidval))
    if consolelogging == True:
        print(vidval)
    if "Not Found" in r.text:
        if consolelogging == True:
            print("vid doesn't exist")
        time.sleep(videocheckexistdelay)


print("By using this program you are taking full responsibilities for your ow"
      "n actions with this program and in no way is the creator or contrib"
      "utors liable for your own actions." + os.linesep)
logging.basicConfig(filename=logfile, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
tabs1 = usr_input()
overallinittime = time.time()
while (tabs1 > 0):
    tabtime = time.time()
    vidnotfoundcounter = 0
    vidfound = False
    while (vidfound == False):
        #Random youtube value
        vidval = str(randomStringDigits(vidtaglength))
        # Checks if vid exists
        if check_vid(consolelogging, vidval) == True:
            vidfound == True
            tabs1 -= 1
        else:
            vidnotfoundcounter += 1
            continue
    #Sets url
    url = 'https://www.youtube.com/watch?v=' + str(vidval)

    # Opens the set url
    webbrowser.open_new(url)
    tabendtime = time.time()
    timefortab = (tabtime - tabendtime)
    if consolelogging == True:
        print("Video Found After " + str(vidnotfoundcounter) + " Attempts and " + timefortab + os.linesep + url)
    if filelogging == True:
        logging.info("Video Found After " + str(vidnotfoundcounter) + " Attempts and " + timefortab + os.linesep + url)

totalendtime = time.time()
totaltime = (overallinittime - totalendtime)
if consolelogging == True:
    print("All tabs found in " + totaltime)
if filelogging == True:
    logging.info("Video Found After " + str(vidnotfoundcounter) + " Attempts and " + timefortab + os.linesep + url)
time.sleep(sleepatend)