import urequests as requests
import pycom
import time

# define colours we want to show at certain bgl thresholds
# note I am using mmol/l
thresholds = [0,3,4.5,6,10,13]
colours = [(1,0,1), (0,0,1), (0,1,0), (0,1,0), (1,1,0), (1,0,0)]
# seconds to sleep between updates
delay = 1
# NightScout server API
url = "https://MY-NIGHTSCOUT-URL/api/v1/entries.json?count=1"

pycom.heartbeat(False)

def get_bgl(url):
    response = requests.get(url)
    # really ought to check that sgv is a key, if not check prev values or give up
    # I'm using mmol/L, so divide mg/dL by 18
    bgl = response.json()[0]['sgv']/18
    return bgl

def get_colour(bgl):
    # find bracketing colours and thresholds
    for i,threshold in enumerate(thresholds):
        if threshold > bgl:
            break
        # we are above max threshold
        i += 1
    if i==0:
        # we are below min
        colour = colours[i]
    elif i==len(colours):
        colour = colours[-1]
    else:
        upper = threshold
        lower = thresholds[i-1]
        proportion = (bgl-lower)/(upper-lower)
        # get colour as a list of 3 floats
        colour = (colours[i-1][j]*(1-proportion) + colours[i][j]*proportion for j in [0,1,2])
    colour_int = sum([int(0xff*v)*multiplier for (v,multiplier) in zip(colour,[0x10000,0x100,1])])
    return colour_int

while True:
    # need try block - how to do in micropython?
    bgl = get_bgl(url)
    #print(bgl)
    colour = get_colour(bgl)
    pycom.rgbled(colour)
    time.sleep(delay)
