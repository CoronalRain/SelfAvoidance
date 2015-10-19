# Self-Avoiding Walks Visualizer

**by Troy P. Kling**

<img src="http://troykling.com/files/selfavoidance.png" alt="Self-Avoiding Walk" width="300" height="300">

## Description

Self-avoiding walks are random walks that never overlap.

## Installation

Start by ensuring that all dependencies are installed. The Mandelbrot Visualizer requires the numpy, matplotlib, and docopt packages.

Next, clone this repository.

> git clone https://gitlab.com/RedShift/SelfAvoidance.git

Once the repo is successfully cloned, navigate to the SelfAvoidance directory and install the package.

> python setup.py install

You're now ready to use the Self-Avoiding Walks Visualizer!

## How to Use

You can interface with the tool in two different ways: through Python and through the terminal/command prompt.

### Python

Self-Avoiding Paths Visualizer 1.0

### Terminal

The Self-Avoiding Walks Visualizer can also be used from the terminal/command prompt. In order to see the documentation for this, run the following command.

> python selfavoiding.py --help

    Usage:
      selfavoiding.py [options]
      selfavoiding.py (-h | --help)
      selfavoiding.py --version
    
    Options:
      -n --size <int>      Width/Height of the lattice containing the random walk.
                           [default: 51]
      -c --cmap <string>   Colormap to use.
                           [default: jet]
      -m --ms <int>        Milliseconds between frames in the animation.
                           [default: 50]
      -h --help            Show this screen.
      -v --verbose         Show runtime info.
      --version            Show version.