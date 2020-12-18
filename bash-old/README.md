## Prerequsites
    - Linux (Or Windows Subsystem for Linux)
    - mkvtoolnix (Install from your linux repo)
    
## About

  As someone who is fairly picky about his subtitles, something about SubsPleases subtitle's style just bugged me. It was probably the thicker outlines, but I can't really be sure. Anyways, I noticed that all these fansub groups used more or less the same format. It was usually a .mkv with a single video, audio, and sub a .ssa track bundled together. There is usually an embeded font as well. Since they were all so similar, I decided to write a script to change modify the subtitle style of any video with the same format and this is it. This script will restyle any subtitles in a .mkv with the aformentioned format to match either HorribleSubs or Erai-raws sub style. I choose these two as they were the most unoffensive to me. Unfortunately this script will not be for everyone as it is a bash script. You will need to know how to use linux or WSL (Windows Subsystem for Linux) and a terminal.
    
## How to use

  1. Have either Linux or WSL (Windows Subsystem for Linux) installed
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

**Q:** What is the difference between the two font files?
\
**A:** No clue. I pulled these out of a HorribleSubs and Erai-raws video. Not sure why they are different sizes. All I know is that the font sizing will not be correct if you use the wrong file. 

**Q:** How would I do this manually?
\
**A:** See Below. 

## How would I do this manually.

  I applaud you for having the tenacity to even think about doing this manually. Although then again, I did too, so who am I to judge.
  
Below is a step by step of what this script does so you can do it by hand if you want to. Anything bolded will need to be modified by you to match your file locations:
1. `cd` to your video's folder
2. Copy the font that you want to use (OpenSans-Semibold-Horrible.ttf or OpenSans-Semibold-Erai.ttf) from your downloads folder to the folder your video is in
2. Extract the existing subtitle with this command. Remember to put in the path to your video file.
        <pre><code>mkvextract tracks <b>video_file.mkv</b> 2:subtitle.ssa</pre></code>
3. You should now see a file named subtitle.ssa in the folder. Open it with your favorite file editor (Notepad, Vim, Nano, Sublime, Atom, etc)
4. You will need to replace the 3 lines that start with `PlayResX:`, `PlayResY:`, and `Style: Default` with the following lines
        
        For HorribleSubs style subs:
        ```
        PlayResX: 848
        PlayResY: 480
        Style: Default,Open Sans Semibold,36,&H00FFFFFF,&H000000FF,&H00020713,&H00000000,-1,0,0,0,100,100,0,0,1,1.7,0,2,0,0,28,0
        ```
        
        For Erai-raws style subs:
        ```
        PlayResX: 1280
        PlayResY: 720
        Style: Default,Open Sans Semibold,45,&H00FFFFFF,&H000000FF,&H00020713,&H00000000,-1,0,0,0,100,100,0,0,1,1.7,0,2,10,10,25,1
        ```
        
If you try and play the video with this subtitle file you may find that the sizes are not quite right. This is because these sizes are tied to their specific font files. You may be able to adjust them in your video player settings.
       
5. Remove old subtitles and fonts from the video file and create a temporary video file. mkvtools does not like overwriting the origional.
        <pre><code>mkvmerge -o tmpMKV.mkv -M -S <b>video_file.mkv</b></pre></code>
6. Rebuild the video file with the following command:
        <pre><code>mkvmerge -o <b>video_file.mkv</b> tmpMKV.mkv --language 0:eng subtitle.ssa --attachment-mime-type application/x-truetype-font --attachment-name OpenSans-Semibold.ttf --attach-file <b>OpenSans-Semibold-XXXXXX.ttf</b></pre></code>
7. Delete any files created during this process

## Other
If you notice any issues with the script or the subtitle/video output please let me know. You can submit a bug report or something. 
