from setuptools import setup

setup(name = "Self-Avoiding Walks Visualizer",
      version = "1.0",
      description = "Mathematical tool for visualizing self-avoiding walks.",
      author = "Troy P. Kling",
      author_email = "troykling1308@gmail.com",
      url = "https://gitlab.com/CoronalRain/SelfAvoidance",
	  py_modules = ["selfavoidance"],
	  install_requires=[
		"numpy",
		"matplotlib",
		"docopt"
	  ],
     )