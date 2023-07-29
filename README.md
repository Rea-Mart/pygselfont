# pygselfont
A class that makes pixel art fonts easy to implement in pygame.
## How to implement
1. download / copy-paste pygselfont.py
2. put the .py file and the .png for the font in the same folder as your project
3. import pygselfont
4. create a font using the Pygselfont() class
5. call Pygselfont.render() and blit the returned Surface to the screen
## How to make your own fonts
You can use any image editor that supports .png files (microsoft paint, photoshop, you name it)
The font files use a color code to indicate the start and end of a letter, outline, etc.
Color         | Purpose
------------- | -------------
(255,0,0)/#ff0000/red | Text fill
(0,0,0)/#000000/black  | Text outline (pixel perfect)
(100,100,100)/#646464/grey  | Text outline (double)
(0,0,255)/0000ff/blue | Letter separator
(255,255,255)/ffffff/white | Transparent background

1. Draw the letters, leaving a 2-pixel wide gap after each letter
2. Add the pixel perfect and double outlines as you wish
3. Add 1 new row of pixels at the top of the image
4. Add blue dots in the top row representing the first pixel of a letter.
   Have a look at the example_font.png if you don't understand:
   ![image](https://github.com/Rea-Mart/pygselfont/assets/126715517/3e06f8e1-0625-494b-8920-1d1882f4f540)

