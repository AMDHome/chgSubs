import tempfile
import os, stat
import sys, fileinput
import subprocess

def checkMKVTools():
    if subprocess.call(["mkvextract", "-V"]) == 0:
        return True
    return False

def convert(mkv_location, font_location, propX, propY, propStyle, toolkit_location, root = None):
    tempdir = tempfile.gettempdir()
    tempssa = tempdir + "/tempssa.ssa"
    tempmkv = tempdir + "/tempmkv.mkv"

    # extracting subtitles
    # eval mkvextract tracks MKV_LOCATION 2:"SUB_LOCATION"
    if root:
        root.updateProgress("Extracting Subtitles")

    cmd = [toolkit_location + "mkvextract", "tracks", mkv_location, "2:" + tempssa]

    subprocess.call(cmd)


    # modifying subtitles
    if root:
        root.updateProgress("Modifying Subtitles")

    for line in fileinput.input(tempssa, inplace=True):
        stripline = line.strip()

        if stripline.startswith('PlayResX:'):
            line = "PlayResX: " + propX + "\n"

        elif stripline.startswith('PlayResY:'):
            line = "PlayResY: " + propY + "\n"

        elif stripline.startswith('Style: Default'):
            line = propStyle + "\n"

        sys.stdout.write(line)


    # remove unnecessary fonts from mkv
    # mkvpropedit MKV_LOCATION --delete-attachment name:OpenSans-Semibold.ttf
    if root:
        root.updateProgress("Removing Unnecessary Fonts")

    cmd = [toolkit_location + "mkvpropedit", mkv_location , "--delete-attachment", "name:OpenSans-Semibold.ttf"]
    ret = subprocess.call(cmd)      # if this = 2 throw error

    # returned 2, try removing read only attribute and try again
    if ret == 2:
        os.chmod(mkv_location, stat.S_IWRITE)
        ret = subprocess.call(cmd)

        if ret != 0:
            if root:
                root.processError("Write Error: Video Input - Please check permissions")
            else:
                print("Write Error: Video Input - Please check permissions")
            return


    # remove old subtitles from mkv
    # mkvmerge -o /tmp/tmpMKV.mkv -S MKV_LOCATION
    if root:
        root.updateProgress("Removing Old Subtitles")
    
    cmd = [toolkit_location + "mkvmerge", "-o", tempmkv, "-S", mkv_location]
    subprocess.call(cmd)


    # rebuilding mkv file
    # mkvmerge -o MKV_LOCATION /tmp/tmpMKV.mkv --language 0:eng \"SUB_LOCATION\"\
    #          --attachment-mime-type application/x-truetype-font\
    #          --attachment-name OpenSans-Semibold.ttf\
    #          --attach-file FONT_LOCATION
    if root:
        root.updateProgress("Rebuilding MKV File")

    cmd = [toolkit_location + "mkvmerge", "-o", mkv_location, tempmkv, "--language", "0:eng", tempssa, "--attachment-mime-type", "application/x-truetype-font", "--attachment-name", "OpenSans-Semibold.ttf", "--attach-file", font_location]
    ret = subprocess.call(cmd)      # if this = 2 throw error

    # returned 2, try removing read only attribute and try again
    if ret == 2:
        os.chmod(mkv_location, stat.S_IWRITE)
        ret = subprocess.call(cmd)

        if ret != 0:
            if root:
                root.processError("Write Error: Video Input - Please check permissions")
            else:
                print("Write Error: Video Input - Please check permissions")
            return


    # Clean up temp files
    if root:
        root.updateProgress("Cleaning Up")
    
    os.unlink(tempssa)
    os.unlink(tempmkv)

    # Done
    if root:
        root.done()
    return