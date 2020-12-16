## Prerequsites
    - Linux (Or Windows Subsystem for Linux)
    - mkvtoolnix (Install from your linux repo)
    
## About

  As someone who is fairly picky about his subtitles, something about SubsPleases subtitle's style just bugged me. It was probably the thicker outlines, but I can't really be sure. Anyways, I noticed that all these fansub groups used more or less the same format. It was usually a .mkv with a single video, audio, and sub a .ssa track bundled together. There is usually an embeded font as well. Since they were all so similar, I decided to write a script to change modify the subtitle style of any video with the same format and this is it. This script will restyle any subtitles in a .mkv with the aformentioned format to match either HorribleSubs or Erai-raws sub style. I choose these two as they were the most unoffensive to me. Unfortunately this script will not be for everyone as it is a bash script. You will need to know how to use linux or WSL and a terminal.
    
## How to use

  1. Have either Linux or WSL installed
  2. Have mkvtoolnix installed (Just use the package manager for your distro `yum/dnf/apt install mkvtoolnix`)
  3. Download the above script and font files and unzip it. (Use the green button)
  4. Navigate to it in a terminal and run it as follows:
  
          `./chgSubs /path/to/your/video/file.mkv`
          
          You can also add a -e if you wish to use Erai-raw style subs.
          
## FAQ
**Q:** Where do I find my video file on WSL?
\
**A:** Assuming you have it downloaded to your downloads folder or your desktop, you can find it at `/mnt/c/Users/username/Downloads/` or `/mnt/c/Users/username/Desktop/`. Remember to replace `username` with your own username


**Q:** How long will this conversion take?
\
**A:** No more than a few seconds (3 - 8 seconds for me). The script does not reencode the video. It just modifies the subtitle file and changes out the font files for ones that were extracted from HorribleSubs/Erai-raws videos.

**Q:** Will you ever make a more user friendly version of this for non techy people to use?
\
**A:** Probably not, I never learned how to make graphical user interfaces. Also I would probably have to rewrite everything since this is written in a scripting language that doesnt support it.

**Q:** Will there ever be a Mac version?
\
**A:** Not from me. I don't own any Macs so I have no way of testing it. If you know how to code a shell script for Mac, it should be very easy to convert this to something you can use.

## Other
If you notice any issues with the script or the subtitle/video output please let me know. You can submit a bug report or something. 
