# Strusion
![Python](https://img.shields.io/badge/Python-3.7.4-yellow?style=flat-square)

This python tool provides a subtitle' handler, that allows you to merge subtitles and change some features, like position, color and so on.
## Usage
- [Merge two subtitles](#basic-merging)
- [Merge two subtitles and set position](#basic-merging-and-set-position)
- [Change subtitle position](#set-subtitle-position)
- [Sync subtitles](#sync-subtitles)
### Basic merging
The basic usage merge two subtitles and shows them at the same time on screen, as the example below:


<p align="center">

<img src="https://user-images.githubusercontent.com/33498293/64730220-30898a00-d4b5-11e9-87c0-ef5eec47c1a8.png" width="720" alt="Portuguese and english subtitles">
</p>

<p align="center">
<i>Portuguese and english subtitles</i>
</p>

> The above subtitle position is set by default 

For that use: 
```
$ python strusion.py -S portuguese_sub.srt english_sub.srt -o merged_sub.srt
```
### Basic merging and set position
Add -x -y in the command: 
```
$ python strusion.py -S portuguese_sub.srt english_sub.srt -o merged_sub.srt -x 192 -y 48
```
> Note that changes only the above subtitle
### Set subtitle position
Add -x -y in the command: 
```
$ python strusion.py -s movie_sub.srt -o movie_sub.mod.srt -x 192 -y 48
```
> Note the use of -s for handling just one subtitle 
### Sync subtitles
Add -d in the command, then put the millisecs and subtitle: 
```
$ python strusion.py -d 2500 unsynchronized_sub.srt -o synchronized_sub.srt
```
