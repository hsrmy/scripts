#!/bin/sh
LESSOPEN_SH=/usr/local/bin/lesspipe.sh
file=$1
case $file in
  *.gif|*.jpeg|*.jpg|*.pcd|*.png|*.tga|*.tiff|*.tif)
    mediainfo ${file};;
  *.mkv|*.ogg|*.avi|*.wav|*.mpeg|*.mpg|*.vob|*.mp4|*.m2v|*.mp2|*.mp3|*.asf|*.wma|*.wmv|*.mov|*.ifo|*.aac|*.ape|*.flac|*.aiff|*.mp4|*.iso|*.dmg|*.m4a)
    mediainfo ${file};;
  *)
    $LESSOPEN_SH $file;;
esac
