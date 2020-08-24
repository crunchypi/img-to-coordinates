from random import randint
from math import sqrt
from points import Point
from typing import List, Tuple


def wbounds(v:int, min:int, max:int) -> bool:
    'Checks whether value v is within bounds min,max'
    return v > min and v < max


def filter_color(points: List[Point], rgb_min: tuple, rgb_max: tuple) -> list:
    ''' Filters all p in points such that rgb in p is 
        within bounds rgb_min and rgb_max.
    '''
    assert len(rgb_min) == len(rgb_max) == 3, 'incorrect length'
    res: List[Point]  = []
    for p in points:
        r_ok = wbounds(p.rgb[0], rgb_min[0], rgb_max[0])
        g_ok = wbounds(p.rgb[1], rgb_min[1], rgb_max[1])
        b_ok = wbounds(p.rgb[2], rgb_min[2], rgb_max[2])
        if r_ok and g_ok and b_ok:
            res.append(p)
    return res
        

def thinner_random(points: List[Point], leavePercent:int) -> list:
    ''' Filters all p in points such that only a percent
        specified by leavePercent remain.
    '''
    result = []
    result_n:int = int(len(points) / 100 * leavePercent)
    # added_index = []
    for i in range(result_n):
        choice = randint(0, len(points)-1)
        result.append(points[choice])

    return result

        
def thinner_neightbour(points: List[Point], dist_min:int, dist_max:int) -> list:
    ''' Filters all p in points such that distance between
        them is within the bounds of dist_min and dist_max
    '''
    result = []
    for p in points:
        for q in points:
            if p == q: continue
            dx = abs(p.coord[0] - q.coord[0])
            dy = abs(p.coord[1] - q.coord[1])
            dst = sqrt(dx**2 + dy**2)
            if wbounds(dst, dist_min, dist_max) and q not in result:
                result.append(q)
    return result

