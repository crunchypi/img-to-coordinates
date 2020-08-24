import sys
from PIL import Image

from points import PointImg
import point_filter 


def arg_map() -> dict:
    ''' Returns a dict where keys describe
        argument identifier and are lists
        describing actions. Second elements
        are functions while first dictate 
        how far away argument values are
        to said functions. 
        Example -i ./image.pgn expects that
        path is one position from '-i'
    '''
    return {
        "-i"            :[1, load], 
        "-o"            :[1, save],
        "-size"         :[1, resize],
        "-show"         :[0, show],
        "-filtercolor"  :[1, filtercolor],
        "-thinner"      :[1, thinner],
        
    }

def check_nonempty(pointImg:PointImg) -> None:
    if not pointImg.points:
        print("nothing is loaded into handler obj, quitting.")
        sys.exit(0)

def unpack_arg(arg:str, conversion_f, 
                expected_len:int, identifier:str) -> list:
    'Helper function to unpack arguments.'
    string_args = arg.split(',')
    if len(string_args) != expected_len:
        print(f'invalid value length for {identifier}, quitting.')
        sys.exit(1)

    fixed_type_args = []
    for item in string_args:
        try:
            fixed_type_args.append(conversion_f(item))
        except:
            print(f'invalid value in {identifier}, quitting')
            sys.exit(1)
    return fixed_type_args
   
def load(arg:str, pointImg:PointImg, _:str) -> PointImg:
    'Uses PIL to load image into PointIMG obj.'
    img = Image.open(arg)
    pointImg.from_pil_img(img)
    return pointImg

def save(arg:str, pointImg:PointImg, _:str) -> None:
    'Saves PointIMG obj values into a path as json.'
    check_nonempty(pointImg)
    pointImg.save_json(arg)
    os.exit(1)

def resize(arg:str, pointImg:PointImg, cmd:str) -> PointImg:
    'Uses PIL to resize image data in PointIMG obj.'
    check_nonempty(pointImg)

    # Expect arg of len 2 where each val is int.
    xy_int = unpack_arg(
        arg=arg, 
        conversion_f=int, 
        expected_len=2, 
        identifier=cmd
    )
    img = pointImg.to_img()
    img = img.resize((xy_int[0],xy_int[1]))
    pointImg.from_pil_img(img)
    return pointImg

def show(arg:str, pointImg:PointImg, _:str) -> None:
    'Uses PIL to show contents of PointImg obj.'
    check_nonempty(pointImg)
    pointImg.to_img().show()
    sys.exit(0)

def filtercolor(arg:str, pointImg:PointImg, cmd:str) -> PointImg:
    'Filters color values of points in PointImg obj.points'
    check_nonempty(pointImg)

    # Expect arg of length 6 where each val is int.
    minmax_int = unpack_arg(
        arg=arg, 
        conversion_f=int, 
        expected_len=6, 
        identifier=cmd
    )
    pointImg.points = point_filter.filter_color(
        points=pointImg.points,
        rgb_min=tuple(minmax_int[:3]),
        rgb_max=tuple(minmax_int[3:])
    )
    return pointImg

def thinner(arg:str, pointImg:PointImg, cmd:str) -> PointImg:
    'Reduces points in PointImg obj.points to arg percent.'
    check_nonempty(pointImg)
    # Percent must be int
    if not arg.isnumeric():
        print(f'invalid value in {cmd}, quitting')
        sys.exit(0)
    # Filter and return updated val
    pointImg.points = point_filter.thinner_random(
        points=pointImg.points,
        leavePercent=int(arg)
    )
    return pointImg

def start() -> None:
    'Point of entry of CLI'

    dct = arg_map()
    args = sys.argv[1:]
    # Keep track of state.
    pointImg = PointImg()

    # Always assume that arg comes right after command.
    for i  in range(0, len(args), 2):
        try:
            # Assumed to be keys in dct
            current_arg = args[i]
            # Unpack for readability.
            argjump, func = dct.get(current_arg)
            # Point of action.
            pointImg = func(
                args[i+argjump], 
                pointImg, 
                current_arg
            )
            
        except Exception as e:
            print(f'issue on {args[i]}: '+ 
                    f'\n\tException:{e}')

start()