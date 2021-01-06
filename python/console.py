import os, sys, platform
import chgSubs

def start(path = None, MKVToolKit = None, PlayResX = None, PlayResY = None, Stylecode = None, console = None, f = None, i = None, style = None):
    
    stylePresetOptions = [("848", "480", "Style: Default,Open Sans Semibold,36,&H00FFFFFF,&H000000FF,&H00020713,&H00000000,-1,0,0,0,100,100,0,0,1,1.7,0,2,0,0,28,0"),
                          ("1280", "720", "Style: Default,Open Sans Semibold,45,&H00FFFFFF,&H000000FF,&H00020713,&H00000000,-1,0,0,0,100,100,0,0,1,1.7,0,2,10,10,25,1")]
    
    # get video path
    video = i
    
    # get font path
    if not f:
        font = getDefaultFont(path, style)
    else:
        font = f
    
    # get toolkit path
    if not MKVToolKit:
        if platform.system() == "Windows":
            toolkit = getToolKitLocation()
        else:
            toolkit = ""
    else:
        toolkit = MKVToolKit

    # set default style options
    
    if style:
        if style == "HorribleSubs":
            entry = 0
        elif style == "Erai-raws":
            entry = 1

        x = stylePresetOptions[entry][0]
        y = stylePresetOptions[entry][1]
        stylecode = stylePresetOptions[entry][2]
    else:
        x = stylePresetOptions[0][0]
        y = stylePresetOptions[0][1]
        stylecode = stylePresetOptions[0][2]

    # set custom style options:
    if PlayResX:
        x = PlayResX

    if PlayResY:
        y = PlayResY

    if Stylecode:
        stylecode = Stylecode

    chgSubs.convert(video, font, x, y, stylecode, toolkit)



def getDefaultFont(path, style):
    if style == "Erai-raws":
        font = path + "/OpenSans-Semibold-Erai.ttf"
    elif style == "HorribleSubs":
        font = path + "/OpenSans-Semibold-Horrible.ttf"
    else:
        print("Warning: Font and Style not specified. Using default font.")
        font = path + "/OpenSans-Semibold-Horrible.ttf"

    if not os.path.isfile(font):
        print("Error: Font not specified. Default font not found.")
        sys.exit()

    return font


def getToolKitLocation():
    if os.path.isdir("C:\\Program Files\\MKVToolNix"):
        if checkFolderPrograms(os.listdir("C:\\Program Files\\MKVToolNix")):
            return "C:\\Program Files\\MKVToolNix\\"
    elif os.path.isdir("C:\\Program Files (x86)\\MKVToolNix"):
        if checkFolderPrograms(os.listdir("C:\\Program Files (x86)\\MKVToolNix")):
            return "C:\\Program Files (x86)\\MKVToolNix\\"
    else:
        print("Error: MKVToolNIX not found, please install the toolkit or provide custom path")
        sys.exit()


def checkFolderPrograms(files):
        sansExt = map(lambda x: os.path.splitext(x)[0], files)
        return set(['mkvextract', 'mkvmerge', 'mkvpropedit']).issubset(list(sansExt))