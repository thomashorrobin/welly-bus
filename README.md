## Usage

To run this program you need python and to know you stop number.

This program currently only does three things. Firstly it gets bus departure times for any given bus stop, secondly it will list recent bus stops that you have searched, and finally you can search avalible bus stops with a grep like feature.

### Bus Stop Search

To get bus timetable departure times simple run this command:

    $ python main.py stop <your bus stop number>

For example if your stop number is 5500 you'd run:

    $ python main.py stop 5500

### List previous searches

To get all previously searched bus stops just run:

    $ python main.py list

### Grep avalible bus stops

The grep functionality is very basic, it just passes a search term in the url. So no spaces, etc.

To grep the avilible bus stops on the server run this command:

    $ python main.py grep <your search term>

For example if your stop number is on Lampton Quay you'd run:

    $ python main.py grep Lampton

/grep is case sensitive/