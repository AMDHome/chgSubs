import argparse
import console
from ui import *

version = 1.1

# Compile using the following command:
# pyinstaller --onefile --noconsole -n chgSubs main.py


def validPlayRes(PlayRes):
    global parser

    try:
        val = int(PlayRes)
        if val < 1:  # if not a positive int print message and ask for input again
            parser.error("PlayRes values must be a positive integer.")
            return False
        return PlayRes
    except ValueError:
        parser.error("PlayRes values must be a positive integer.")
        return False 


def validFile(file):
    global currPath, parser

    if not os.path.isfile(file):
        if not os.path.isfile(currPath + file):
            parser.error("File not found.")
            return False

    return file


def validFolder(path):
    global currPath, parser

    if not os.path.isdir(path):
        parser.error("File not found.")
        return False

    return path


if __name__ == '__main__':
    if getattr(sys, 'frozen', False):
        currPath = os.path.dirname(sys.executable)
    elif __file__:
        currPath = os.path.dirname(__file__)

    parser = argparse.ArgumentParser(description = "chgSubs Subtitle Modifier v" + str(version))
    parser.add_argument("-C", "--console", dest = 'console', action = 'store_true', help = "Use console mode (No GUI)")
    parser.add_argument("-i", metavar = "<input_filename>", help = "Target video file", type = validFile)
    parser.add_argument("-f", metavar = "<font_location>", help = "Font file location", type = validFile)

    styleGroup = parser.add_mutually_exclusive_group(required = False)
    styleGroup.add_argument("-H", "--HorribleSubs", dest = 'style', action = 'store_const', const = "HorribleSubs", help = "Use HorribleSubs preset style")
    styleGroup.add_argument("-E", "--Erai-raws", dest = 'style', action = 'store_const', const = "Erai-raws", help = "Use Erai-raws preset style")

    parser.add_argument("-X", "--PlayResX", metavar = "<PlayResX>", help = "Custom PlayResX value", type = validPlayRes)
    parser.add_argument("-Y", "--PlayResY", metavar = "<PlayResY>", help = "Custom PlayResY value", type = validPlayRes)
    parser.add_argument("--Stylecode", metavar = "<Stylecode>", help = "Custom stylecode values")

    parser.add_argument("-m", "--MKVToolKit", metavar = "<mkvtoolkit_location>", help = "Path to MKVToolKit", type = validFolder)
    args = parser.parse_args()

    if args.console is not False:
        if args.i is None:
            parser.error("Console mode set. Input filename required")

        if args.style is None:
            if args.PlayResX is None or args.PlayResY is None or args.StyleCode is None:
                parser.error("You must specify a style and/or custom PlayRes and Stylecode values")            

    if args.console:
        console.start(path = currPath, MKVToolKit = args.MKVToolKit, PlayResX = args.PlayResX,
                      PlayResY = args.PlayResY, Stylecode = args.Stylecode, console = args.console,
                      f = args.f, i = args.i, style = args.style)

    else:
        root = Root(Tk(), version, currPath, MKVToolKit = args.MKVToolKit, PlayResX = args.PlayResX,
                    PlayResY = args.PlayResY, Stylecode = args.Stylecode, f = args.f, i = args.i,
                    style = args.style)
        root.mainloop()