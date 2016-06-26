## Installation

These installation options only work on OSX and Linux. If you're using a non-unix based operating system like Windows you should format your C:\ drive immediately and install Ubuntu. The sooner you make this important step in your development as a programmer/IT professional the better. Trust me.

### From binary

Download the binary from: https://github.com/thomashorrobin/welly-bus/releases/download/v1.0/metlink

The metlink file needs to be copied to your path folder. The most appropriate place for this is usually /usr/local/bin/

Run this command to copy the file:

    $ sudo cp ~/Downloads/metlink /usr/local/bin/

### From source

Clone the project from https://github.com/thomashorrobin/welly-bus.git

navigate to the projects root and run PyInstaller on the main.py file

    $ pyinstaller -F main.py

You should then be able to see something in the /dist directory that will have been created.

The file will be called main so you'll need to rename it to metlink and move it to /usr/local/bin/ to use the program as documented. 

However if you don't want to add the program to your path you can just run the main.py using python:

    $ python main.py <cmd> <bus stop number|search term>

## Usage

This program currently only does three things: 

- It can get bus departure times for any given bus stop. 
- It will list bus stops that you have previously searched.
- It can search avalible bus stops with a grep like feature.

### Bus Stop Search

To get bus timetable departure times simply run this command:

    $ metlink stop <your bus stop number>
or:

    $ metlink <your bus stop number>

For example if your stop number is 5500 you'd run:

    $ metlink 5500

### List previous searches

To get all previously searched bus stops just run:

    $ metlink list

### Grep avalible bus stops

The grep functionality is very basic, it just passes a search term in using the url. So no spaces, etc.

To grep the avilible bus stops on the server run this command:

    $ metlink grep <your search term>

For example if your stop number is on Lambton Quay you'd run:

    $ metlink grep Lambton

