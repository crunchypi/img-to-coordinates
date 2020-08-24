from PIL import Image
import json

class Point():
    def __init__(self, coord:tuple, rgb:tuple):
        self.coord = coord
        self.rgb = rgb

class PointImg():
    def __init__(self):
        self.points = []
        self.width = 0
        self.height = 0

    def from_pil_img(self, img):
        self.width = img.size[0]
        self.height = img.size[1]
        points = []
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                px = img.getpixel((i,j))
                points.append(Point(
                        coord=[i,j], 
                        rgb=px
                ))
        self.points = points

    def to_img(self):
        new = Image.new(mode='RGB', size=(self.width+1, self.height+1))
        for p in self.points:
            new.putpixel((p.coord[0], p.coord[1]),p.rgb)
        return new
        
    def to_dict(self):
        sub = lambda p: {
            'x':p.coord[0],
            'y':p.coord[1],
            'r':p.rgb[0],
            'g':p.rgb[1],
            'b':p.rgb[2],
        }
        return {
           i : sub(p) 
           for i,p in enumerate(self.points)
        }


    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def save_json(self, path):
        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=4)