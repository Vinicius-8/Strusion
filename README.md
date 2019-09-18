# Strusion
![Python](https://img.shields.io/badge/Python-3.7.4-yellow?style=flat-square)

This python tool provides a subtitle' handler, that allows you to fuse subtitles and change some features, like position, color and so on.
## Usage
- [Fuse two subtitles](#basic-fusion)
- [Fuse two subtitles and set position (above subtitle)](#basic-fusion-and-set-position)

### Basic fusion
The basic usage fuse two subtitles and shows them at the same time on screen, as the example below:


<p align="center">

<img src="https://user-images.githubusercontent.com/33498293/64730220-30898a00-d4b5-11e9-87c0-ef5eec47c1a8.png" width="720" alt="Portuguese and english subtitles">
</p>

<p align="center">
<i>Portuguese and english subtitles</i>
</p>

> The above subtitle positon are set by default 

For that use: 
```
$ python strusion.py -S portuguese_sub.srt english_sub.srt -o fused_sub.srt
```
### Basic fusion and set position
> Note that changes only the above subtitle

Just add -x -y in the command: 
```
$ python strusion.py -S portuguese_sub.srt english_sub.srt -o fused_sub.srt -x 200 -y 45
```

