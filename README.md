# beamer2video

## Bash and python scripts for converting LaTex Beamer slides to video with text to speech voice over.

In this repository we present a bash script that makes use of two python scripts to 
turn Beamer slides to videos.

### Dependencies

* Python 3
* [pdfminer.six package](https://github.com/pdfminer/pdfminer.six) and its dependencies; e.g.: `pip3 install pdfminer.six`
* `ffmpeg` eg: `brew install ffmpeg`
* `pdflatex`

### Directories

* `bin` 
contains beam2vid bash script plus two python scripts

* `clips` 
for storing short narrator video clip

* `images` 
for storing images used in Beamer slides

* `frames` 
temporary directory for storing video frames

* `vids` 
temporary dirctory for storing videos


