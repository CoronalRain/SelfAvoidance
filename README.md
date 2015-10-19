# Self-Avoiding Walks Visualizer

**by Troy P. Kling**

<img src="http://troykling.com/files/selfavoidance.png" alt="Self-Avoiding Walk" width="239" height="239">

## Description

A self-avoiding walk (SAW) is a sequence a moves along a lattice path that does not visit the same point more than once. SAWs have many interesting properties and applications in computational physics and other areas of research.

## Installation

Start by ensuring that all dependencies are installed. The Mandelbrot Visualizer requires the numpy, matplotlib, and docopt packages.

Next, clone this repository.

    > git clone https://gitlab.com/RedShift/SelfAvoidance.git

Once the repo is successfully cloned, navigate to the SelfAvoidance directory and install the package.

    > python setup.py install

You're now ready to use the Self-Avoiding Walks Visualizer!

## How to Use

The Self-Avoiding Walks Visualizer should be used from the terminal/command prompt. In order to see the documentation for this, run the following command.

    > python selfavoiding.py --help

    Self-Avoiding Paths Visualizer 1.0
	
    Usage:
      selfavoiding.py [options]
      selfavoiding.py (-h | --help)
      selfavoiding.py --version
    
    Options:
	  -l --lower <int>     Sets a lower bound on the length of the random walk.
                           [default: 0]
      -n --size <int>      Width/Height of the lattice containing the random walk.
                           [default: 51]
      -m --ms <int>        Milliseconds between frames in the animation.
                           [default: 50]
      -c --cmap <string>   Colormap to use.
                           [default: jet]
      -h --help            Show this screen.
      -v --verbose         Show runtime info.
      --version            Show version.

The *l* argument allows the user to have some control over the length of the self-avoiding walk. If *l* is set, then the program will generate self-avoiding walks until one is found that has length greater than or equal to *l*. The default value for *l* is 0, which implies that the first walk will be accepted. However, this may result in very short walks (possibly as short as length 8), so setting the *l* parameter to 50 or 100 may be ideal. If *l* is set to be quite large, a suitable walk may never be found and the program may run indefinitely. This can be counteracted to a degree by setting *n* to be very large as well.

The *n* argument defines the size of the lattice over which the self-avoiding walk takes place. The default, *n=51*, is normally sufficient to contain any walk, assuming *l* is not very large.

The *m* argument defines the number of milliseconds between each frame of the animation. The default is 50, which is usually sufficient for all but the longest self-avoiding walks.

The *c* argument allows the user to change to colormap. The default is "jet", but users are encouraged to try out other colormaps, found [here](http://matplotlib.org/examples/color/colormaps_reference.html).

### Examples

    > python selfavoidance.py -l 500 -n 101 --cmap terrain -m 25 --verbose