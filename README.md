# image to coordinates
A CLI tool for converting images to coordinate points. As shown below, some filtering is supported, specifically color, neighbour count and random. Points can be saved as json (shown in root/demo/data.json). Point format is
  
    {
      "0": {            # // key is an index 0...n
          "x": 132,     # // x is x coordinate
          "y": 90,      # // y is y coordinate
          "r": 1,       # // r is r in rgb
          "g": 1,       # // g is g in rgb
          "b": 1        # // b is gb in rgb
       },
      ...,
    }
      

#### Original:
![alt text](https://raw.githubusercontent.com/crunchypi/img2coordinates/master/demo/cat.png?raw=true)



#### After filtering (pink is substitute for nothing (points are black)):
![alt text](https://github.com/crunchypi/img2coordinates/blob/master/demo/screenshot.png?raw=true)


#### Another example, animation in p5js https://editor.p5js.org/crunchypi/sketches/bGcjFyEEa:
![alt text](https://raw.githubusercontent.com/crunchypi/img2coordinates/master/demo/doge.gif)


## CLI Usage (-help printout):

    Basic usage:
        Use each arg in the desired processing order
        For example, if '-size' is called before '-o'
        then the current progress is saved before a resize.

    Arguments:
        -i            specifies input (image) path
        -o            specifies output (point json) path
        -size         specifies new size with x,y
        -show         shows current progress (will exit)
        -filtercolor  filters by color with exactly 6 ints
                      rgb max
        -thinner      specifies random thinning where only
                      a percent of points remain.
    Examples:
        Load cat.png, filter out any colors which are not
        pure red and show.
            -i cat.png -filtercolor 0,0,0,255,0,0 -show
        Load cat.png, resize to 50,50 and show.
            -i cat.png -size 100,100 -show
        Load cat.png and thin out 90% pixels before showing.
            -i cat.png -thinner 10 -show
        Same as abovem but save instead of show
            -i cat.png -thinner 10 -o data.json
