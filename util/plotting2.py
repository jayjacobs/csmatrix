# Copyright 2013 Philip N. Klein
"""
This file contains a simple plotting interface, which uses a browser with SVG to 
present a plot of points represented as either complex numbers or 2-vectors.

"""

from numbers import Number
# from IPython.display import HTML


def plot(L, scale=4, dot_size = 3, browser=None):
    """ plot takes a list of points, optionally a scale (relative to a 200x200 frame),
        optionally a dot size (diameter) in pixels, and optionally a browser name.
        It produces an html file with SVG representing the given plot,
        and opens the file in a web browser. It returns nothing.
    """
    scalar = 200./scale
    origin = (210, 210)
    svgout = ['<svg height="420" width=420 xmlns="http://www.w3.org/2000/svg">\n'
        ,'<line x1="0" y1="210" x2="420" y2="210"'
        ,'style="stroke:rgb(0,0,0);stroke-width:2"/>\n'
        ,'<line x1="210" y1="0" x2="210" y2="420"'
        ,'style="stroke:rgb(0,0,0);stroke-width:2"/>\n']
    for pt in L:
        if isinstance(pt, Number):
            x,y = pt.real, pt.imag
        else:
            if isinstance(pt, tuple) or isinstance(pt, list):
                x,y = pt
            else:
                raise ValueError
        svgout.append('<circle cx="%d" cy="%d" r="%d" fill="red"/>\n'
                      % (origin[0]+scalar*x,origin[1]-scalar*y,dot_size))
    svgout.append('</svg>')
    return ''.join(svgout)

