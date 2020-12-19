## Prerequsites
	- Windows 10 or Linux computer
    - mkvtoolnix

## About
  As someone who is fairly picky about his subtitles, something about SubsPleases subtitle's style just bugged me. It was probably the thicker outlines, but I can't really be sure. Anyways, I noticed that all these fansub groups used more or less the same format. It was usually a .mkv with a single video, audio, and sub a .ssa track bundled together. There is usually an embeded font as well. Since they were all so similar, I decided to write a script to change modify the subtitle style of any video with the same format. Origionally it was just going to be a script that was only for people who knew how to use Linux/WSL, but then I realised that that was a very small population in this group. I felt bad so I created a regular program that is hopefully easy enough for everyone (on Windows 10) to use. This program will restyle any subtitles in a .mkv with the aformentioned format to match either HorribleSubs or Erai-raws sub style. I choose these two as they were the most unoffensive to me.

## How to use:

### Windows

  1. Download and install mkvtoolnix from the following link: (https://www.fosshub.com/MKVToolNix.html)[https://www.fosshub.com/MKVToolNix.html]
  2. Download and unzip the program from our releases tab
  3. Launch chgSubs.exe and select your video file.
  4. Select the style preset and the font you want to use and press go.

Please note: if you chose to install the portable version of mkvtoolnix, you will need to chose where you unzipped mkvtoolnix to

### Linux

Download the source code and run `python3 ./main.py` in the python folder for a GUI or run `sh ./chgSubs` for the bash command line version.
